from database_connection import DatabaseConnection
from exception import ConnectionFailedError, MaxRetriesExceededError


class ConnectionPool:

    MAX_SIZE = 5

    def __init__(self):
        self.idle_pool = []

        self.active_pool = []


    @property
    def active_connection(self):
        return len(self.active_pool)

    @property
    def idle_connection(self):
        return len(self.idle_pool)

    def get_connection(self):
        if self.idle_pool:
            conn = self.idle_pool.pop()
            conn.connect()
            self.active_pool.append(conn)
            print(f"[POOL] Reused idle connection: {conn.connection_id}")
            return conn

        total = self.active_connection + self.idle_connection
        if total < self.MAX_SIZE:
            conn = DatabaseConnection()
            conn.connect()
            self.active_pool.append(conn)
            print(f"[POOL] Created new connection: {conn.connection_id}")
            return conn

        ## if pool is fool raise error    
        raise MaxRetriesExceededError("Connection pool is full No connection available")

    ## relase connection from active to idle pool
    def release_connection(self, conn):
        if conn in self.active_pool:
            self.active_pool.remove(conn)
            conn.disconnect()
            self.idle_pool.append(conn)
            print(f"[POOL] Released connection: {conn.connection_id} returned to pool")

    def close_all(self):
        print("\n[POOL] Closing all connections...")
        for conn in self.active_pool + self.idle_pool:
            conn.status = "idle"
            print(f" Closed connection: {conn.connection_id}")
        self.active_pool.clear()
        self.idle_pool.clear()
        print("[POOL] All connections closed.\n")

    def get_stats(self):
        return {
            "total": self.active_connection + self.idle_connection,
            "active": self.active_connection,
            "idle": self.idle_connection,
            "max_size": self.MAX_SIZE
        }

    # Context Manager 
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_all()  
        print("[POOL] Pool closed (context manager)")
        return False      

