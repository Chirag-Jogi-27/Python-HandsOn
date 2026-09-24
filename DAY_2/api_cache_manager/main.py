import time
from cache_manager import cached

# Let's pretend this is a slow, expensive API call
@cached(endpoint="weather_api")
def get_weather(city):
    
    
    # time.sleep(3) simulates the 3 seconds it takes to fetch from the internet
    time.sleep(3) 
    
    # Fake data we pretend we got from the internet
    weather_database = {
        "london": {"temp": "15°C", "condition": "Rainy"},
        "newyork": {"temp": "22°C", "condition": "Sunny"},
        "tokyo": {"temp": "25°C", "condition": "Cloudy"}
    }
    
    return weather_database.get(city.lower(), "City not found")


# --- Testing the Cache ---
if __name__ == "__main__":
    print("--- FIRST CALL (Should take 3 seconds) ---")
    print(get_weather("London"))
    
    print("\n--- SECOND CALL (Should be instant!) ---")
    print(get_weather("London"))
    
    print("\n--- THIRD CALL (Different city, should take 3 seconds) ---")
    print(get_weather("Tokyo"))
    
    print("\n--- FOURTH CALL (Should be instant!) ---")
    print(get_weather("Tokyo"))
