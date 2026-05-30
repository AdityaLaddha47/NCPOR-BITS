import requests
import pandas as pd

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 15.2993,
    "longitude": 74.1240,
    "hourly": "temperature_2m",
    "past_days": 30,
    "forecast_days": 1
}

response = requests.get(url, params=params)
data = response.json()

df = pd.DataFrame({
    "time": data["hourly"]["time"],
    "temperature": data["hourly"]["temperature_2m"]
})

df["time"] = pd.to_datetime(df["time"])
df.to_csv("goa_temperature.csv", index=False)

print(f"Saved {len(df)} rows")
print(df.tail())