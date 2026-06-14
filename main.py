import requests

print("=== Weather App ===")

city = input("Enter city name: ").strip()

API_KEY = "7cd9ef17068a43d688a7b300f06ce9ed"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url, timeout=5)
    data = response.json()

    if data.get("cod") != 200:
        print("Error:", data.get("message"))
    else:
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        desc = data["weather"][0]["description"]

        print("\n--- Weather Report ---")
        print("City:", city)
        print("Temperature:", temp, "°C")
        print("Humidity:", humidity, "%")
        print("Condition:", desc)

except requests.exceptions.RequestException:
    print("Network error. Please try again.")