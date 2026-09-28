from datetime import datetime
from database_connection import DatabaseConnection
from exception import ConnectionFailedError, QueryTimeoutError 

class Logger:
    """A simple base class that handles timestamped console logging."""
    def log(self, message):
        # Format the current time to match the prompt requirement: [2026-09-28 11:46]
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        print(f"[{current_time}] {message}")


class QueryLogger(DatabaseConnection, Logger):
    """
    Inherits from BOTH DatabaseConnection and Logger.
    Logs successful executions and captures/logs specific database exceptions.
    """
    def execute_query(self, query):
        try:
            # 1. Try to run the query work using the parent class logic
            result = super().execute_query(query)
            
            # 2. If it succeeds, log the success
            self.log(f"[SUCCESS] [{self.connection_id}] Executed: {query}")
            return result
            
        except QueryTimeoutError as e:
            # 3. Log the query timeout exception cleanly
            self.log(f"[EXCEPTION] [{self.connection_id}] Query Timed Out! Details: {e}")
            raise  # Re-raise the exception so the main application knows it failed
            
        except ConnectionFailedError as e:
            # 4. Log the inactive connection exception cleanly
            self.log(f"[EXCEPTION] [{self.connection_id}] Connection State Error! Details: {e}")
            raise  # Re-raise the exception
