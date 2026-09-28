class ConnectionFailedError(Exception):
    """Raised when a database connection cannot be established"""
    pass

class QueryTimeoutError(Exception):
    """Raised when a query takes too long to execute"""
    pass

class MaxRetriesExceededError(Exception):
    """Raised when maximum retry attempts have been exceeded"""
    pass


