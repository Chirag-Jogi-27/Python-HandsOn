import hashlib
import time

def get_current_timestamp():

    return time.time()

def generate_cache_key(endpoint, params):

    raw_string = f"{endpoint}_{params}"

    cache_key = hashlib.md5(raw_string.encode()).hexdigest()

    return cache_key



