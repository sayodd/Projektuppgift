from dotenv import load_dotenv
import requests
import os

load_dotenv()

def get_weather_data(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")  
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Kollar API funkar
        data = response.json()

        temperature_celsius = data["main"]["temp"] - 273.15

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


def generate_html(weather_data):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Weather Data</title>
    </head>
    <body>
        <h1>Weather Information for {weather_data['city']}</h1>
        <table border="1">
            <tr>
                <th>City</th>
                <th>Temperature (C)</th>
                <th>Humidity (%)</th>
                <th>Description</th>
            </tr>
            <tr>
                <td>{weather_data['city']}</td>
                <td>{weather_data['temperature']}</td>
                <td>{weather_data['humidity']}</td>
                <td>{weather_data['description']}</td>
            </tr>
        </table>
    </body>
    </html>
    """
    # Spara innehållet i HTML-filen
    with open("webb_app.html", "w") as file:
        file.write(html_content)
    print("HTML-fil genererad med väderdata.")



# Testa funktionen
city = "Stockholm"
weather_data = get_weather_data(city)
if weather_data:
    weather_data["temperature"] = f"{weather_data['temperature']}"
    generate_html(weather_data)

    