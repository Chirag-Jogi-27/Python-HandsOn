import json
import os
from utils import get_current_timestamp, generate_cache_key

CACHE_DIR = "cache_files"
TTL_SECONDS = 300 

if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

def save_to_cache(endpoint, params, response_data):
    """Saves the API response to a JSON file along with a timestamp."""
    
    
    key = generate_cache_key(endpoint, params)
    file_path = os.path.join(CACHE_DIR, f"{key}.json")
    
    cache_content = {
        "timestamp": get_current_timestamp(),
        "data": response_data
    }
    
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(cache_content, file)
            print(f"[CACHE SAVED] -> {file_path}")
    except Exception as e:
        print(f"Failed to save cache: {e}")

def load_from_cache(endpoint, params):

    
    key = generate_cache_key(endpoint, params)
    file_path = os.path.join(CACHE_DIR, f"{key}.json")
    
    if not os.path.exists(file_path):
        return None
        
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            cache_content = json.load(file)
            
            # Check the math: (Time Right Now) - (Time Saved)
            time_saved = cache_content["timestamp"]
            time_elapsed = get_current_timestamp() - time_saved
            
            if time_elapsed <= TTL_SECONDS:
                print(f"[CACHE HIT] Loaded from {file_path}")
                return cache_content["data"]
            else:
                print("[CACHE EXPIRED]")
                return None 
                
    except Exception as e:
        print(f"Failed to load cache: {e}")
        return None



def cached(endpoint):
    
    def decorator(func):
        def wrapper(params):

            cached_data = load_from_cache(endpoint, params)
            
            if cached_data is not None:
                return cached_data
                
            print(f"[FETCHING] Getting fresh data for {endpoint}?{params}...")
            fresh_data = func(params)
            
            save_to_cache(endpoint, params, fresh_data)
            
            return fresh_data
        return wrapper
    return decorator
