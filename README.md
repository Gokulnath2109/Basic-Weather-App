# Weather App using Python

## Overview

This project is a simple command-line Weather Application built using Python and the OpenWeatherMap API. Users can enter a city name and receive real-time weather information, including temperature, humidity, and weather conditions.

## Features

* Search weather by city name
* Real-time weather data using API
* Temperature displayed in Celsius
* Humidity information
* Weather condition description
* Error handling for invalid cities and network issues
* Simple and user-friendly interface

## Technologies Used

* Python 3
* Requests Library
* OpenWeatherMap API

## Project Structure

```text
Weather-App/
│
├── weather_app.py
└── README.md
```

## Installation

### 1. Install Python

Download and install Python from:
https://www.python.org/downloads/

### 2. Install Required Package

```bash
pip install requests
```

### 3. Get an API Key

1. Create an account on OpenWeatherMap.
2. Generate an API key.
3. Replace the API key in the code:

```python
API_KEY = "YOUR_API_KEY"
```

## Running the Application

Run the program using:

```bash
python weather_app.py
```

Example:

```text
=== Weather App ===
Enter city name: Chennai

--- Weather Report ---
City: Chennai
Temperature: 32°C
Humidity: 68%
Condition: Clear Sky
```

## How It Works

1. User enters a city name.
2. The application sends a request to the OpenWeatherMap API.
3. Weather data is received in JSON format.
4. The program extracts:

   * Temperature
   * Humidity
   * Weather Condition
5. Results are displayed to the user.

## Key Concepts Used

* API Integration
* JSON Data Parsing
* HTTP Requests
* User Input Handling
* Exception Handling
* Real-Time Data Retrieval

## Error Handling

The application handles:

* Invalid city names
* Network connection issues
* API request failures

## Future Enhancements

* Graphical User Interface (GUI)
* Multiple city weather comparison
* 5-day weather forecast
* Weather icons and animations
* Temperature unit conversion (°C / °F)
* Automatic location detection

## Learning Outcomes

Through this project, I learned:

* How APIs work
* How to send HTTP requests in Python
* How to process JSON responses
* How to handle exceptions effectively
* How real-time data applications are developed

## Author

Gokulnath S

Python Programming Internship Project
