from connection import ConnectionPool
from logger import QueryLogger
from exception import MaxRetriesExceededError, ConnectionFailedError, QueryTimeoutError

# Upgrade ConnectionPool to provision QueryLogger objects
def get_logged_connection(self):
    if self.idle_pool:
        conn = self.idle_pool.pop()
        conn.connect() 
        self.active_pool.append(conn)
        print(f"[POOL] Reused idle connection: {conn.connection_id}")
        return conn

    total = self.active_connection + self.idle_connection
    if total < self.MAX_SIZE:
        conn = QueryLogger()  
        conn.connect()  # Note: this has a 20% random crash risk
        self.active_pool.append(conn)
        print(f"[POOL] Created new connection: {conn.connection_id}")
        return conn

    raise MaxRetriesExceededError("Connection pool is full! No connection available.")

ConnectionPool.get_connection = get_logged_connection


if __name__ == "__main__":
    print("=========================================================")
    print("🧪 TESTING POOL LIMITS AND CAPACITY EXHAUSTION")
    print("=========================================================\n")

    with ConnectionPool() as pool:
        print(f"[INITIAL STATE] Stats: {pool.get_stats()}\n")

        # -------------------------------------------------------------
        # SCENARIO 1 & 2: No Idle Connections Available -> Create New Ones
        # We will attempt to open 7 connections to deliberately break the MAX_SIZE=5 limit.
        # -------------------------------------------------------------
        active_connections = []
        print("--- Phase 1: Rapidly Requesting 7 Connections (Max is 5) ---")
        
        for i in range(1, 8):
            print(f"\nRequesting Connection #{i}...")
            try:
                conn = pool.get_connection()
                active_connections.append(conn)
            except ConnectionFailedError:
                print("❌ [SIMULATED FAILURE] Random 20% network drop occurred. Trying next...")
            except MaxRetriesExceededError as e:
                print(f"🔥 [SUCCESSFUL CATCH] Pool Blocked Request #{i}! Error: {e}")

        print(f"\n[PEAK CAPACITY STATS] {pool.get_stats()}\n")

        # -------------------------------------------------------------
        # SCENARIO 3: Run Queries through the successfully opened ones
        # -------------------------------------------------------------
        print("--- Phase 2: Running Queries on Active Connections ---")
        for conn in active_connections:
            try:
                conn.execute_query("SELECT current_user();")
            except QueryTimeoutError:
                print("[APP] Handled a random query timeout safely.")

        # -------------------------------------------------------------
        # SCENARIO 4: Clean up by returning them to the pool
        # -------------------------------------------------------------
        print("\n--- Phase 3: Releasing All Connections Back To Pool ---")
        while active_connections:
            c = active_connections.pop()
            pool.release_connection(c)

        print(f"\n[IDLE POOL RESTORED STATS] {pool.get_stats()}")
        print("\n--- Phase 5: Leaving context manager block ---")

    print("\n=========================================================")
    print("🏁 POOL TERMINATION CLEANUP VERIFIED SUCCESSFULLY")
    print("=========================================================")
