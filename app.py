from dotenv import load_dotenv
import requests
import os
import pandas as pd

load_dotenv()

def get_weather_data(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")  # Använd din API-nyckel här eller spara den som en miljövariabel
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Kontrollera om API-anropet lyckades
        data = response.json()

        # Omvandla temperaturen från Kelvin till Celsius
        temperature_celsius = data["main"]["temp"] - 273.15

        # Skapa ett objekt med den bearbetade datan
        weather_info = {
            "city": data["name"],
            "temperature": round(temperature_celsius, 1),
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        }

        return weather_info

    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)
        return None
    
def save_to_excel(data, filename="weather_data.xlsx"):
    # Skapa en DataFrame från datan
    df = pd.DataFrame([data])  # Skapa en lista med ett objekt för att kunna skapa en DataFrame
    df.to_excel(filename, index=False)  # Spara till en Excel-fil

# Testa funktionen
city = "Stockholm"
weather_data = get_weather_data(city)
if weather_data:
    weather_data["temperature"] = f"{weather_data['temperature']} °C"
    print(weather_data)
    save_to_excel(weather_data)
    print(f"Weather data saved!")
