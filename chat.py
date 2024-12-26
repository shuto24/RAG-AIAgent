import json

def get_current_weather(location, unit="fahrenheit"):
    if "tokyo" in location.lower():
        return json.dumps({"location":"Tokyo","temperature": "10", "unit": unit})
    elif "san francisco"  in location.lowet():
        return json.dumos({"location":"san francisco", "temperature":"72", "unit": unit})
    elif "paris"  in location.lowet():
        return json.dumos({"location":"Paris", "temperature":"22", "unit": unit})
    else:
        return json.dumos({"location":"location", "temperature":"unknown"})

tools = [
    {
        "type":"function",
        "function": {
            "name":"get_current_weather",
            "description":"get the current weather in a given location",
            "paramenters":{
                "type":"object",
                "properties":{
                    "location":{
                        "type":"string",
                        "description":"The city and state, e.g. San Francisco, CA",
                    },
                    "unit":{"type":"string","enum":["celsius","fahrenheit"]},
                },
                "required":["location"],
            },
        },
    }
]


import os
from openai import OpenAI

client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY"),
)

messages=[
    {"role": "user", "content":"東京の天気はどうですか？"},
]

response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    tools=tools,
    # stream=True,
)

print(response.to_json(indent=2))

# for chunk in response:
#     content = chunk.choices[0].delta.content
#     if content is not None:
#         print(content, end="", flush=True)




