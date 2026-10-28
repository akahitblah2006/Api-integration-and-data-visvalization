
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Add your valid OpenWeatherMap API key here.
API_KEY = "5f64a9246d78152ca6311739d180a00f"

cities = [
    "Delhi",
    "Mumbai",
    "Kolkata",
    "Chennai",
    "Bengaluru",
    "Hyderabad",
    "Ahmedabad"
]

weather_data = []

for city in cities:
    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url, timeout=15)

    if response.status_code == 200:
        data = response.json()

        weather_data.append({
            "City": city,
            "Temperature": data["main"]["temp"],
            "Humidity": data["main"]["humidity"]
        })

        print(f"{city}: Weather data received")

    else:
        print(f"{city}: Unable to fetch weather data")
        print(response.text)

if weather_data:
    df = pd.DataFrame(weather_data)
    print("\nWeather Data:")
    print(df)

    # Temperature graph
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x="City", y="Temperature")
    plt.title("Temperature Comparison Across Cities")
    plt.xlabel("City")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig("temperature_chart.png")
    plt.show()

    # Humidity graph
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x="City", y="Humidity")
    plt.title("Humidity Comparison Across Cities")
    plt.xlabel("City")
    plt.ylabel("Humidity (%)")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig("humidity_chart.png")
    plt.show()

else:
    print("No weather data received. Check your API key.")

