import requests

# OpenWeatherMap API configuration
API_KEY = "your_api_key"  # Replace with your OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """
    Fetch the weather information for a given city.

    Args:
        city (str): Name of the city.

    Returns:
        str: Weather information or an error message.
    """
    # Build the query parameters
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # For temperature in Celsius
    }

    try:
        # Make the API request
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            # Extract weather details
            city_name = data["name"]
            temp = data["main"]["temp"]
            weather = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            return (
                f"Weather in {city_name}:\n"
                f"- Temperature: {temp}°C\n"
                f"- Description: {weather}\n"
                f"- Humidity: {humidity}%\n"
                f"- Wind Speed: {wind_speed} m/s"
            )
        elif data["cod"] == "404":
            return "City not found. Please check the name and try again."
        else:
            return "Error: Unable to fetch weather data."
    except Exception as e:
        return f"An error occurred: {e}"

def weather_bot():
    """
    Simple weather bot interface.
    """
    print("Weather Bot: Hello! I can provide current weather information.")
    print("Type 'exit' to stop the conversation.")

    while True:
        city = input("Enter the city name: ").strip()

        if city.lower() == "exit":
            print("Weather Bot: Goodbye!")
            break

        # Get weather details
        weather_info = get_weather(city)
        print(f"Weather Bot: {weather_info}\n")

# Run the weather bot
if __name__ == "__main__":
    weather_bot()
