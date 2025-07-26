import requests
import tkinter as tk
from tkinter import messagebox

# Function to get weather data from OpenWeatherMap
def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    api_key = 'be14e4ef6cb7306228ab4af5e93218ea'  # <-- Replace with your actual API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    url = f"{base_url}?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()

            city_name = data["name"]
            country = data["sys"]["country"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            weather = data["weather"][0]["description"]
            wind_speed = data["wind"]["speed"]

            result = (
                f"📍 {city_name}, {country}\n"
                f"🌤️ Weather: {weather.capitalize()}\n"
                f"🌡️ Temperature: {temperature} °C\n"
                f"💧 Humidity: {humidity}%\n"
                f"💨 Wind Speed: {wind_speed} m/s"
            )

            output_label.config(text=result)
        else:
            output_label.config(text="")
            messagebox.showerror("Error", f"City not found: {city}")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Network error:\n{e}")

# GUI setup
root = tk.Tk()
root.title("Weather App")
root.geometry("350x300")
root.configure(bg="lightblue")

# Title Label
title_label = tk.Label(root, text="Weather App", font=("Arial", 16, "bold"), bg="lightblue")
title_label.pack(pady=10)

# City Entry
tk.Label(root, text="Enter City Name:", font=("Arial", 12), bg="lightblue").pack()
city_entry = tk.Entry(root, font=("Arial", 12), justify="center")
city_entry.pack(pady=5)

# Get Weather Button
get_button = tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather, bg="white")
get_button.pack(pady=10)

# Output Label
output_label = tk.Label(root, text="", font=("Arial", 11), bg="lightblue", justify="left")
output_label.pack(pady=10)

# Run the GUI loop
root.mainloop()
