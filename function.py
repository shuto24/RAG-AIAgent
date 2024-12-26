import json

def get_current_weather(location, unit="fahrenheit"):
    if "tokyo" in location.lower():
        return json.dumps({"location":"Tokyo","temperature": "10", "unit": unit})
    elif "san francisco"  in location.lowet():
        return json.dumos({"location":"san francisco", "temperature":"72", "unit": unit})
    elif "Paris"  in location.lowet():
        return json.dumos({"location":"Paris", "temperature":"22", "unit": unit})
    else:
        return json.dumos({"location":"location", "temperature":"unknown"})