# database_connection.py

import uuid
import random
from datetime import datetime
from exception import ConnectionFailedError, QueryTimeoutError

class DatabaseConnection:
    
    def __init__(self):
        self.connection_id = str(uuid.uuid4())[:8]   # short unique ID like "a3f9b1c2"
        self.status = "idle"                          # starts as idle
        self.created_at = datetime.now()              # timestamp of creation

    def connect(self):
        # simulate 20% chance of connection failure
        if random.random() < 0.2:
            raise ConnectionFailedError(f"Connection {self.connection_id} failed to connect!")
        
        self.status = "active"
        print(f"[+] Connection {self.connection_id} is now ACTIVE")

    def disconnect(self):
        self.status = "idle"
        print(f"[-] Connection {self.connection_id} is now IDLE")

    def execute_query(self, query):
        # can only run query if connection is active
        if self.status != "active":
            raise ConnectionFailedError(f"Connection {self.connection_id} is not active!")
        
        # simulate 15% chance of timeout
        if random.random() < 0.15:
            raise QueryTimeoutError(f"Query timed out on connection {self.connection_id}")
        
        print(f"[Q] [{self.connection_id}] Executing: {query}")
        return f"Result of: {query}"

    def is_alive(self):
        return self.status == "active"





