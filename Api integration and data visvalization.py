# Weather Data API Integration and Visualization using Python


import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

API_KEY = "your_api_key_here"  
cities = ["Delhi", "Mumbai", "Kolkata", "Chennai", "Bengaluru", "Hyderabad", "Ahmedabad"]


weather_data = []

for city in cities:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        weather_data.append({
            "City": city,
            "Temperature (°C)": data['main']['temp'],
            "Humidity (%)": data['main']['humidity'],
            "Pressure (hPa)": data['main']['pressure']
        })
    else:
        print(f"Failed to fetch data for {city}")


df = pd.DataFrame(weather_data)
print("\nLive Weather Data:\n")
print(df)


plt.figure(figsize=(10, 6))
sns.barplot(x='City', y='Temperature (°C)', data=df, palette='coolwarm')
plt.title("Current Temperature in Indian Cities")
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.tight_layout()
plt.savefig("temperature_chart.png")
plt.show()


plt.figure(figsize=(10, 6))
sns.lineplot(x='City', y='Humidity (%)', data=df, marker='o', color='blue')
plt.title("Humidity Levels in Indian Cities")
plt.xlabel("City")
plt.ylabel("Humidity (%)")
plt.grid(True)
plt.tight_layout()
plt.savefig("humidity_chart.png")
plt.show()
 
