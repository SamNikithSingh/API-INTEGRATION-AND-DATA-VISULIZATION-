!pip install -q requests pandas matplotlib seaborn

import requests, pandas as pd, matplotlib.pyplot as plt, seaborn as sns
print("welcome to api integration using python")
print("we will be working with weather data")
print("choose your city & the data will be shown")
print("our public api is meteo forcast")
print("we will find the weather details in the city Madurai")
def geocode_location(place="Madurai"):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    r = requests.get(url, params={"name": place, "count": 1, "language": "en"})
    r.raise_for_status()
    match = r.json()["results"][0]
    return match["latitude"], match["longitude"], match["name"]

def fetch_forecast(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m,relativehumidity_2m,precipitation_probability",
        "timezone": "auto",
    }
    r = requests.get(url, params=params); r.raise_for_status()
    df = pd.DataFrame(r.json()["hourly"]).assign(time=lambda d: pd.to_datetime(d["time"])).set_index("time")
    return df
lat, lon, city = geocode_location("Madurai")
df = fetch_forecast(lat, lon)


sns.set_style("whitegrid")

plt.figure(figsize=(12,6))
sns.lineplot(data=df, y="temperature_2m", x=df.index)
plt.title(f"Hourly Temperature — {city} (next 7 days)")
plt.ylabel("°C"); plt.xlabel("Date/Time"); plt.tight_layout(); plt.show()

plt.figure(figsize=(12,4))
sns.lineplot(data=df, y="relativehumidity_2m", x=df.index, color="tab:green")
plt.title(f"Hourly Relative Humidity — {city}"); plt.ylabel("%"); plt.tight_layout(); plt.show()

plt.figure(figsize=(8,4))
sns.histplot(df["precipitation_probability"], bins=20, kde=True)
plt.title(f"Distribution of Precip-Probability — {city}")
plt.xlabel("% chance"); plt.tight_layout(); plt.show()


df_heat = df.copy()
df_heat["date"] = df_heat.index.date
df_heat["hour"] = df_heat.index.hour

pivot_temp = df_heat.pivot_table(index="hour", columns="date", values="temperature_2m")

plt.figure(figsize=(12, 6))
sns.heatmap(pivot_temp, cmap="coolwarm", annot=True, fmt=".1f", linewidths=0.5, linecolor="gray", cbar_kws={'label': '°C'})
plt.title(f"Hourly Temperature Heatmap — {city}")
plt.xlabel("Date")
plt.ylabel("Hour of Day")
plt.tight_layout()
plt.show()
