#  Python Weather Tool

A professional CLI-based application that fetches real-time weather data using the **OpenWeatherMap API**. This tool handles data parsing, unit conversions, and custom error handling to provide a smooth user experience.

##  Features
- **Real-time Weather:** Fetches temperature, humidity, and weather conditions.
- **Smart Conversions:**
  - Converts Wind Speed from **m/s** to **km/h**.
  - Converts Unix Timestamps to **Readable 24-hour Time**.
- **Timezone Intelligence:**
  - Calculates the city's offset relative to **London (UTC)**.
  - Detects if a city is "Forward" or "Backward" in time.
- **Robust Logic:**
  - **Exception Handling:** Uses a custom `MyCustomError` class to handle invalid city names.
  - **Interactive Loop:** Allows users to check multiple cities without restarting the script.
  - **Loading Animation:** Includes a sleek CLI progress bar for better UX.

## 🛠️Tech Stack
- **Language:** Python 3
- **Libraries:** `requests`, `datetime`, `time`
- **API:** OpenWeatherMap API

##  How to Use
1. **Clone the project:**
   ```bash
   git clone https://github.com
   ```
2. **Install dependencies:**
   ```bash
   pip install requests
   ```
3. **Run the application:**
   ```bash
   python weather.py
   ```

##  Project Structure
- `get_weather(city)`: Handles the API request.
- `tm(tm)`: Formats timestamps into human-readable strings.
- `spd(spp)`: Mathematical conversion for wind speed.
- `country(tzone)`: Logical calculation for timezone offsets.
- `inputr()`: Manages user input and exception handling.


