
class DatabaseConnection:

    def __init__(self, db_name, host="localhost", port = 5432):
        self.db_name = db_name
        self.host = host
        self.port = port
        self.is_connected = False

        self._connect()


    def _connect(self):
        self.is_connected = True

        print(f"Success Connected to {self.db_name} at {self.host}:{self.port}")


    def get_status(self):
        return f"Database: {self.db_name} | Active: {self.is_connected}"



db1 = DatabaseConnection("production_db")
db2 = DatabaseConnection("analytics_db", host="192.168.1.50", port=5433)

print(db1.get_status())
print(db2.get_status())
        

