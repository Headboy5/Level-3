"""
Weather Application for LeedsNews
Developer: Stephen Clark
Date: December 2025

This application provides real-time weather information for cities worldwide
using the Open-Meteo API and GeoCoding API.

AI Usage Statement:
This assignment used generative AI in the following ways for the purposes of 
completing the assignment: brainstorming, research, planning, feedback, editing.
"""

import sys
import requests
from datetime import datetime
from PySide6 import QtCore, QtWidgets, QtGui


class WeatherApp(QtWidgets.QWidget):
    """
    Main Weather Application Widget
    
    This class creates a GUI application that fetches and displays weather data
    for a user-specified city using the Open-Meteo API.
    
    Attributes:
        city_input (QLineEdit): Input field for city name
        search_button (QPushButton): Button to trigger weather search
        result_area (QTextEdit): Display area for weather information
        status_label (QLabel): Status indicator for API requests
    """
    
    def __init__(self):
        """Initialize the weather application with all UI components"""
        super().__init__()
        
        # Set window properties
        self.setWindowTitle("LeedsNews Weather Application")
        self.setMinimumSize(600, 700)
        
        # Dark mode state
        self.dark_mode = False
        
        # Initialize UI components
        self.init_ui()
        
        # Apply styling
        self.apply_styles()
    
    def init_ui(self):
        """
        Initialize and layout all UI components
        
        Creates the main layout with title, input field, search button,
        and results display area.
        """
        # Main layout
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        # Title label and dark mode toggle in horizontal layout
        title_layout = QtWidgets.QHBoxLayout()
        
        title_label = QtWidgets.QLabel("🌤️ LeedsNews Weather Forecast")
        title_label.setAlignment(QtCore.Qt.AlignCenter)
        title_label.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
            color: #2c3e50;
            padding: 15px;
            background-color: #ecf0f1;
            border-radius: 10px;
        """)
        
        # Dark mode toggle button
        self.dark_mode_button = QtWidgets.QPushButton("🌙 Dark Mode")
        self.dark_mode_button.setStyleSheet("""
            QPushButton {
                background-color: #34495e;
                color: white;
                font-size: 14px;
                font-weight: bold;
                padding: 10px 20px;
                border: none;
                border-radius: 8px;
                min-width: 120px;
            }
            QPushButton:hover {
                background-color: #2c3e50;
            }
            QPushButton:pressed {
                background-color: #1a252f;
            }
        """)
        self.dark_mode_button.clicked.connect(self.toggle_dark_mode)
        self.dark_mode_button.setFixedWidth(150)
        
        title_layout.addWidget(title_label, 1)
        title_layout.addWidget(self.dark_mode_button)
        main_layout.addLayout(title_layout)
        
        # Input section
        input_layout = QtWidgets.QHBoxLayout()
        
        # City input label
        city_label = QtWidgets.QLabel("Enter City:")
        city_label.setStyleSheet("font-size: 16px; color: #34495e; font-weight: bold;")
        input_layout.addWidget(city_label)
        
        # City input field
        self.city_input = QtWidgets.QLineEdit()
        self.city_input.setPlaceholderText("e.g., London, Paris, New York...")
        self.city_input.setStyleSheet("""
            background-color: #ffffff;
            color: #2c3e50;
            font-size: 16px;
            padding: 12px;
            border: 2px solid #3498db;
            border-radius: 8px;
        """)
        # Connect Enter key press to search
        self.city_input.returnPressed.connect(self.search_weather)
        input_layout.addWidget(self.city_input)
        
        # Search button
        self.search_button = QtWidgets.QPushButton("🔍 Search Weather")
        self.search_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 12px 25px;
                border: none;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #21618c;
            }
        """)
        self.search_button.clicked.connect(self.search_weather)
        input_layout.addWidget(self.search_button)
        
        main_layout.addLayout(input_layout)
        
        # Status label
        self.status_label = QtWidgets.QLabel("")
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label.setStyleSheet("""
            font-size: 14px;
            padding: 8px;
            border-radius: 5px;
        """)
        main_layout.addWidget(self.status_label)
        
        # Results display area
        results_label = QtWidgets.QLabel("Weather Information:")
        results_label.setStyleSheet("font-size: 16px; color: #34495e; font-weight: bold;")
        main_layout.addWidget(results_label)
        
        self.result_area = QtWidgets.QTextEdit()
        self.result_area.setReadOnly(True)
        self.result_area.setStyleSheet("""
            QTextEdit {
                background-color: #ffffff;
                color: #2c3e50;
                font-size: 14px;
                font-family: 'Consolas', 'Courier New', monospace;
                padding: 15px;
                border: 2px solid #bdc3c7;
                border-radius: 8px;
            }
            QScrollBar:vertical {
                border: none;
                background: #f0f0f0;
                width: 12px;
                border-radius: 6px;
            }
            QScrollBar::handle:vertical {
                background: #3498db;
                border-radius: 6px;
                min-height: 20px;
            }
            QScrollBar::handle:vertical:hover {
                background: #2980b9;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                border: none;
                background: none;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
        """)
        self.result_area.setPlaceholderText("Weather information will appear here after searching...")
        self.result_area.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        main_layout.addWidget(self.result_area)
        
        # Footer with instructions
        footer_label = QtWidgets.QLabel(
            "💡 Tip: Enter a city name and press Enter or click Search Weather"
        )
        footer_label.setAlignment(QtCore.Qt.AlignCenter)
        footer_label.setStyleSheet("""
            font-size: 12px;
            color: #7f8c8d;
            padding: 10px;
        """)
        main_layout.addWidget(footer_label)
    
    def apply_styles(self):
        """Apply global styles to the main window"""
        if self.dark_mode:
            self.apply_dark_mode()
        else:
            self.apply_light_mode()
    
    def apply_light_mode(self):
        """Apply light mode color scheme"""
        self.setStyleSheet("""
            QWidget {
                background-color: #f5f6fa;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
        """)
        
        # Update title
        self.findChild(QtWidgets.QLabel, "").setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
            color: #2c3e50;
            padding: 15px;
            background-color: #ecf0f1;
            border-radius: 10px;
        """)
        
        # Update input label
        for label in self.findChildren(QtWidgets.QLabel):
            if label.text() == "Enter City:":
                label.setStyleSheet("font-size: 16px; color: #34495e; font-weight: bold;")
            elif label.text() == "Weather Information:":
                label.setStyleSheet("font-size: 16px; color: #34495e; font-weight: bold;")
            elif "💡" in label.text():
                label.setStyleSheet("""
                    font-size: 12px;
                    color: #7f8c8d;
                    padding: 10px;
                """)
        
        # Update input field
        self.city_input.setStyleSheet("""
            background-color: #ffffff;
            color: #2c3e50;
            font-size: 16px;
            padding: 12px;
            border: 2px solid #3498db;
            border-radius: 8px;
        """)
        
        # Update search button
        self.search_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 12px 25px;
                border: none;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #21618c;
            }
        """)
        
        # Update result area
        self.result_area.setStyleSheet("""
            QTextEdit {
                background-color: #ffffff;
                color: #2c3e50;
                font-size: 14px;
                font-family: 'Consolas', 'Courier New', monospace;
                padding: 15px;
                border: 2px solid #bdc3c7;
                border-radius: 8px;
            }
            QScrollBar:vertical {
                border: none;
                background: #f0f0f0;
                width: 12px;
                border-radius: 6px;
            }
            QScrollBar::handle:vertical {
                background: #3498db;
                border-radius: 6px;
                min-height: 20px;
            }
            QScrollBar::handle:vertical:hover {
                background: #2980b9;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                border: none;
                background: none;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
        """)
        
        # Update dark mode button
        self.dark_mode_button.setText("🌙 Dark Mode")
        self.dark_mode_button.setStyleSheet("""
            QPushButton {
                background-color: #34495e;
                color: white;
                font-size: 14px;
                font-weight: bold;
                padding: 10px 20px;
                border: none;
                border-radius: 8px;
                min-width: 120px;
            }
            QPushButton:hover {
                background-color: #2c3e50;
            }
            QPushButton:pressed {
                background-color: #1a252f;
            }
        """)
    
    def apply_dark_mode(self):
        """Apply dark mode color scheme"""
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
        """)
        
        # Update title
        for label in self.findChildren(QtWidgets.QLabel):
            if "LeedsNews" in label.text():
                label.setStyleSheet("""
                    font-size: 28px;
                    font-weight: bold;
                    color: #e0e0e0;
                    padding: 15px;
                    background-color: #2b2b2b;
                    border-radius: 10px;
                """)
            elif label.text() == "Enter City:":
                label.setStyleSheet("font-size: 16px; color: #b0b0b0; font-weight: bold;")
            elif label.text() == "Weather Information:":
                label.setStyleSheet("font-size: 16px; color: #b0b0b0; font-weight: bold;")
            elif "💡" in label.text():
                label.setStyleSheet("""
                    font-size: 12px;
                    color: #808080;
                    padding: 10px;
                """)
        
        # Update input field
        self.city_input.setStyleSheet("""
            background-color: #2b2b2b;
            color: #e0e0e0;
            font-size: 16px;
            padding: 12px;
            border: 2px solid #3498db;
            border-radius: 8px;
        """)
        
        # Update search button
        self.search_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 12px 25px;
                border: none;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #21618c;
            }
        """)
        # Update result area
        self.result_area.setStyleSheet("""
            QTextEdit {
                background-color: #2b2b2b;
                color: #e0e0e0;
                font-size: 14px;
                font-family: 'Consolas', 'Courier New', monospace;
                padding: 15px;
                border: 2px solid #444444;
                border-radius: 8px;
            }
            QScrollBar:vertical {
                border: none;
                background: #1a1a1a;
                width: 12px;
                border-radius: 6px;
            }
            QScrollBar::handle:vertical {
                background: #3498db;
                border-radius: 6px;
                min-height: 20px;
            }
            QScrollBar::handle:vertical:hover {
                background: #2980b9;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                border: none;
                background: none;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
        """)
        
        # Update dark mode button
        self.dark_mode_button.setText("☀️ Light Mode")
        self.dark_mode_button.setStyleSheet("""
            QPushButton {
                background-color: #f39c12;
                color: white;
                font-size: 14px;
                font-weight: bold;
                padding: 10px 20px;
                border: none;
                border-radius: 8px;
                min-width: 120px;
            }
            QPushButton:hover {
                background-color: #e67e22;
            }
            QPushButton:pressed {
                background-color: #d35400;
            }
        """)
    
    @QtCore.Slot()
    def toggle_dark_mode(self):
        """Toggle between light and dark mode"""
        self.dark_mode = not self.dark_mode
        self.apply_styles()
    
    @QtCore.Slot()
    def search_weather(self):
        """
        Handle weather search request
        
        This method is triggered when the user clicks the search button or
        presses Enter in the city input field. It validates input, fetches
        weather data, and displays results.
        """
        city_name = self.city_input.text().strip()
        
        # Validate input
        if not city_name:
            self.show_error("Please enter a city name")
            return
        
        # Update status
        self.update_status("Searching...", "info")
        self.search_button.setEnabled(False)
        
        # Fetch weather data
        try:
            weather_data = self.fetch_weather_data(city_name)
            self.display_weather(weather_data, city_name)
            self.update_status("✓ Weather data loaded successfully", "success")
        except Exception as e:
            self.show_error(str(e))
        finally:
            self.search_button.setEnabled(True)
    
    def fetch_weather_data(self, city_name):
        """
        Fetch weather data from Open-Meteo API
        
        This method performs two API calls:
        1. GeoCoding API to get coordinates from city name
        2. Weather API to get current weather data using coordinates
        
        Args:
            city_name (str): Name of the city to search for
            
        Returns:
            dict: Weather data including temperature, wind speed, humidity, etc.
            
        Raises:
            Exception: If city is not found or API request fails
        """
        # Step 1: Get coordinates from city name using GeoCoding API
        geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"
        geocoding_params = {
            "name": city_name,
            "count": 1,
            "language": "en",
            "format": "json"
        }
        
        try:
            geo_response = requests.get(geocoding_url, params=geocoding_params, timeout=10)
            geo_response.raise_for_status()
            geo_data = geo_response.json()
            
            # Check if city was found
            if "results" not in geo_data or len(geo_data["results"]) == 0:
                raise Exception(f"City '{city_name}' not found. Please check the spelling and try again.")
            
            # Extract coordinates and location info
            location = geo_data["results"][0]
            latitude = location["latitude"]
            longitude = location["longitude"]
            city_display_name = location.get("name", city_name)
            country = location.get("country", "")
            
        except requests.exceptions.Timeout:
            raise Exception("Request timed out. Please check your internet connection and try again.")
        except requests.exceptions.ConnectionError:
            raise Exception("Connection error. Please check your internet connection.")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to find city: {str(e)}")
        
        # Step 2: Get weather data using coordinates
        weather_url = "https://api.open-meteo.com/v1/forecast"
        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,weather_code,wind_speed_10m,wind_direction_10m",
            "daily": "temperature_2m_max,temperature_2m_min",
            "timezone": "auto"
        }
        
        try:
            weather_response = requests.get(weather_url, params=weather_params, timeout=10)
            weather_response.raise_for_status()
            weather_data = weather_response.json()
            
            # Add location information to weather data
            weather_data["location"] = {
                "name": city_display_name,
                "country": country,
                "latitude": latitude,
                "longitude": longitude
            }
            
            return weather_data
            
        except requests.exceptions.Timeout:
            raise Exception("Weather request timed out. Please try again.")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch weather data: {str(e)}")
    
    def display_weather(self, weather_data, city_name):
        """
        Display weather data in the results area
        
        Formats and presents weather information in a user-friendly format
        with appropriate units and descriptions.
        
        Args:
            weather_data (dict): Weather data from API
            city_name (str): Name of the city searched
        """
        try:
            # Extract location information
            location = weather_data.get("location", {})
            city_display = location.get("name", city_name)
            country = location.get("country", "")
            
            # Extract current weather data
            current = weather_data.get("current", {})
            temperature = current.get("temperature_2m", "N/A")
            feels_like = current.get("apparent_temperature", "N/A")
            humidity = current.get("relative_humidity_2m", "N/A")
            wind_speed = current.get("wind_speed_10m", "N/A")
            wind_direction = current.get("wind_direction_10m", "N/A")
            precipitation = current.get("precipitation", "N/A")
            weather_code = current.get("weather_code", 0)
            
            # Extract daily data (min/max temperatures)
            daily = weather_data.get("daily", {})
            temp_max = daily.get("temperature_2m_max", [None])[0]
            temp_min = daily.get("temperature_2m_min", [None])[0]
            
            # Get weather description from code
            weather_description = self.get_weather_description(weather_code)
            weather_emoji = self.get_weather_emoji(weather_code)
            
            # Get current time
            current_time = datetime.now().strftime("%A, %B %d, %Y at %I:%M %p")
            
            # Create HTML formatted display with proper styling
            html_content = f"""
            <div style='font-family: "Segoe UI", Arial, sans-serif; color: {"#e0e0e0" if self.dark_mode else "#2c3e50"};'>
                <div style='background: {"#2b2b2b" if self.dark_mode else "#ecf0f1"}; 
                            padding: 20px; 
                            border-radius: 10px; 
                            margin-bottom: 20px;
                            text-align: center;
                            border: 2px solid {"#444" if self.dark_mode else "#bdc3c7"};'>
                    <h2 style='margin: 0; color: {"#e0e0e0" if self.dark_mode else "#2c3e50"};'>
                        🌍 CURRENT WEATHER INFORMATION 🌍
                    </h2>
                </div>
                
                <div style='margin-bottom: 15px; font-size: 16px;'>
                    <p style='margin: 5px 0;'><strong>📍 Location:</strong> {city_display}, {country}</p>
                    <p style='margin: 5px 0;'><strong>🕒 Time:</strong> {current_time}</p>
                </div>
                
                <div style='background: {"#2b2b2b" if self.dark_mode else "#e8f4f8"}; 
                            padding: 15px; 
                            border-radius: 8px; 
                            margin-bottom: 15px;
                            border-left: 4px solid #3498db;'>
                    <h3 style='margin: 0 0 10px 0; color: {"#e0e0e0" if self.dark_mode else "#2c3e50"};'>
                        {weather_emoji} Current Conditions: {weather_description}
                    </h3>
                </div>
                
                <div style='background: {"#2b2b2b" if self.dark_mode else "#fff"}; 
                            padding: 20px; 
                            border-radius: 8px; 
                            margin-bottom: 15px;
                            border: 1px solid {"#444" if self.dark_mode else "#ddd"};'>
                    <p style='margin: 10px 0; font-size: 18px; color: {"#e0e0e0" if self.dark_mode else "#2c3e50"};'>
                        <strong>🌡️ Temperature:</strong> {temperature}°C
                    </p>
                    <p style='margin: 10px 0; padding-left: 30px; color: {"#e0e0e0" if self.dark_mode else "#2c3e50"};'>
                        Feels like: {feels_like}°C
                    </p>
                    
                    <p style='margin: 15px 0 5px 0; color: {"#e0e0e0" if self.dark_mode else "#2c3e50"};'><strong>📊 Today's Range:</strong></p>
                    <p style='margin: 5px 0; padding-left: 30px; color: {"#e0e0e0" if self.dark_mode else "#2c3e50"};'>
                        ▸ Maximum: {temp_max if temp_max is not None else 'N/A'}°C
                    </p>
                    <p style='margin: 5px 0; padding-left: 30px; color: {"#e0e0e0" if self.dark_mode else "#2c3e50"};'>
                        ▸ Minimum: {temp_min if temp_min is not None else 'N/A'}°C
                    </p>
                    
                    <p style='margin: 15px 0; color: {"#e0e0e0" if self.dark_mode else "#2c3e50"};'><strong>💧 Humidity:</strong> {humidity}%</p>
                    
                    <p style='margin: 15px 0 5px 0; color: {"#e0e0e0" if self.dark_mode else "#2c3e50"};'><strong>🌬️ Wind:</strong></p>
                    <p style='margin: 5px 0; padding-left: 30px; color: {"#e0e0e0" if self.dark_mode else "#2c3e50"};'>
                        ▸ Speed: {wind_speed} km/h
                    </p>
                    <p style='margin: 5px 0; padding-left: 30px; color: {"#e0e0e0" if self.dark_mode else "#2c3e50"};'>
                        ▸ Direction: {self.get_wind_direction(wind_direction)}
                    </p>
                    
                    <p style='margin: 15px 0; color: {"#e0e0e0" if self.dark_mode else "#2c3e50"};'><strong>🌧️ Precipitation:</strong> {precipitation} mm</p>
                </div>
                
                <div style='background: {"#1a1a1a" if self.dark_mode else "#fff3cd"}; 
                            padding: 15px; 
                            border-radius: 8px;
                            border-left: 4px solid #f39c12;'>
                    <h3 style='margin: 0 0 10px 0; color: {"#e0e0e0" if self.dark_mode else "#856404"};'>
                        💡 Weather Summary
                    </h3>
                    <p style='margin: 5px 0; line-height: 1.6; color: {"#e0e0e0" if self.dark_mode else "#856404"};'>
                        {self.get_weather_summary(temperature, humidity, wind_speed, weather_description).replace(chr(10), '<br>')}
                    </p>
                </div>
            </div>
            """
            
            self.result_area.setHtml(html_content)
            
        except Exception as e:
            self.show_error(f"Error displaying weather data: {str(e)}")
    
    def get_weather_description(self, code):
        """
        Convert WMO weather code to human-readable description
        
        Args:
            code (int): WMO weather code from API
            
        Returns:
            str: Weather description
        """
        weather_codes = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            45: "Foggy",
            48: "Depositing rime fog",
            51: "Light drizzle",
            53: "Moderate drizzle",
            55: "Dense drizzle",
            61: "Slight rain",
            63: "Moderate rain",
            65: "Heavy rain",
            71: "Slight snow",
            73: "Moderate snow",
            75: "Heavy snow",
            77: "Snow grains",
            80: "Slight rain showers",
            81: "Moderate rain showers",
            82: "Violent rain showers",
            85: "Slight snow showers",
            86: "Heavy snow showers",
            95: "Thunderstorm",
            96: "Thunderstorm with slight hail",
            99: "Thunderstorm with heavy hail"
        }
        return weather_codes.get(code, "Unknown")
    
    def get_weather_emoji(self, code):
        """
        Get appropriate emoji for weather code
        
        Args:
            code (int): WMO weather code
            
        Returns:
            str: Weather emoji
        """
        if code == 0 or code == 1:
            return "☀️"
        elif code == 2 or code == 3:
            return "⛅"
        elif code in [45, 48]:
            return "🌫️"
        elif code in [51, 53, 55, 61, 63, 80, 81]:
            return "🌧️"
        elif code in [65, 82]:
            return "⛈️"
        elif code in [71, 73, 75, 77, 85, 86]:
            return "🌨️"
        elif code in [95, 96, 99]:
            return "⚡"
        else:
            return "🌤️"
    
    def get_wind_direction(self, degrees):
        """
        Convert wind direction in degrees to compass direction
        
        Args:
            degrees: Wind direction in degrees (0-360)
            
        Returns:
            str: Compass direction (e.g., "N", "NE", "E")
        """
        if degrees == "N/A" or degrees is None:
            return "N/A"
        
        directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                     "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
        index = int((degrees + 11.25) / 22.5) % 16
        return f"{directions[index]} ({degrees}°)"
    
    def get_weather_summary(self, temperature, humidity, wind_speed, description):
        """
        Generate a weather summary with recommendations
        
        Args:
            temperature: Current temperature
            humidity: Current humidity
            wind_speed: Current wind speed
            description: Weather description
            
        Returns:
            str: Weather summary text
        """
        summary = []
        
        # Temperature advice
        if isinstance(temperature, (int, float)):
            if temperature < 0:
                summary.append("🥶 It's freezing! Bundle up with warm layers.")
            elif temperature < 10:
                summary.append("🧥 It's cold. A warm jacket is recommended.")
            elif temperature < 20:
                summary.append("👕 Mild weather. A light jacket might be comfortable.")
            elif temperature < 30:
                summary.append("😊 Pleasant temperature. Enjoy the weather!")
            else:
                summary.append("🥵 It's hot! Stay hydrated and seek shade.")
        
        # Humidity advice
        if isinstance(humidity, (int, float)):
            if humidity > 70:
                summary.append("💧 High humidity may make it feel warmer than it is.")
            elif humidity < 30:
                summary.append("🌵 Low humidity. Stay hydrated.")
        
        # Wind advice
        if isinstance(wind_speed, (int, float)):
            if wind_speed > 30:
                summary.append("💨 Strong winds. Be cautious outdoors.")
            elif wind_speed > 20:
                summary.append("🍃 Moderate winds expected.")
        
        # Weather condition advice
        if "rain" in description.lower() or "drizzle" in description.lower():
            summary.append("☔ Don't forget your umbrella!")
        elif "snow" in description.lower():
            summary.append("⛄ Snow conditions. Drive carefully.")
        elif "thunder" in description.lower():
            summary.append("⚠️ Thunderstorm alert. Stay indoors if possible.")
        
        return "\n".join(summary) if summary else "Have a great day!"
    
    def update_status(self, message, status_type):
        """
        Update the status label with a message
        
        Args:
            message (str): Status message to display
            status_type (str): Type of status ('info', 'success', 'error')
        """
        colors = {
            "info": "#3498db",
            "success": "#27ae60",
            "error": "#e74c3c"
        }
        
        self.status_label.setText(message)
        self.status_label.setStyleSheet(f"""
            font-size: 14px;
            padding: 8px;
            border-radius: 5px;
            background-color: {colors.get(status_type, '#95a5a6')};
            color: white;
            font-weight: bold;
        """)
    
    def show_error(self, error_message):
        """
        Display error message to user
        
        Args:
            error_message (str): Error message to display
        """
        self.update_status(f"❌ Error: {error_message}", "error")
        
        html_content = f"""
        <div style='font-family: "Segoe UI", Arial, sans-serif; color: {"#e0e0e0" if self.dark_mode else "#2c3e50"};'>
            <div style='background: #e74c3c; 
                        padding: 20px; 
                        border-radius: 10px; 
                        margin-bottom: 20px;
                        text-align: center;'>
                <h2 style='margin: 0; color: white;'>⚠️ ERROR ⚠️</h2>
            </div>
            
            <div style='background: {"#2b2b2b" if self.dark_mode else "#fff"}; 
                        padding: 20px; 
                        border-radius: 8px; 
                        margin-bottom: 20px;
                        border: 2px solid #e74c3c;'>
                <p style='color: #e74c3c; font-size: 16px; font-weight: bold;'>
                    ❌ {error_message}
                </p>
            </div>
            
            <div style='background: {"#1a1a1a" if self.dark_mode else "#e8f4f8"}; 
                        padding: 20px; 
                        border-radius: 8px; 
                        margin-bottom: 15px;
                        border-left: 4px solid #3498db;'>
                <h3 style='margin: 0 0 10px 0; color: {"#e0e0e0" if self.dark_mode else "#2c3e50"};'>💡 Troubleshooting Tips</h3>
                <ul style='margin: 5px 0; padding-left: 30px; color: {"#e0e0e0" if self.dark_mode else "#2c3e50"};'>
                    <li>Check your spelling</li>
                    <li>Try a major city first (e.g., London, Paris)</li>
                    <li>Verify your internet connection</li>
                    <li>Make sure the city name is in English</li>
                </ul>
            </div>
            
            <div style='background: {"#1a1a1a" if self.dark_mode else "#fff3cd"}; 
                        padding: 20px; 
                        border-radius: 8px;
                        border-left: 4px solid #f39c12;'>
                <h3 style='margin: 0 0 10px 0; color: {"#e0e0e0" if self.dark_mode else "#856404"};'>📝 Valid City Examples</h3>
                <ul style='margin: 5px 0; padding-left: 30px; color: {"#e0e0e0" if self.dark_mode else "#856404"};'>
                    <li>London (UK)</li>
                    <li>Paris (France)</li>
                    <li>New York (USA)</li>
                    <li>Tokyo (Japan)</li>
                    <li>Leeds (UK)</li>
                    <li>Manchester (UK)</li>
                </ul>
            </div>
        </div>
        """
        
        self.result_area.setHtml(html_content)


def main():
    """
    Main function to run the Weather Application
    
    Creates the application instance, displays the main window,
    and starts the event loop.
    """
    app = QtWidgets.QApplication(sys.argv)
    
    # Set application metadata
    app.setApplicationName("LeedsNews Weather App")
    app.setOrganizationName("LeedsNews")
    
    # Create and show the main window
    weather_window = WeatherApp()
    weather_window.show()
    
    # Start the event loop
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
