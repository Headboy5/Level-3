"""
Unit tests for Weather Application

This module contains comprehensive unit tests for the WeatherApp class,
testing all major functionality including API calls, data processing,
and UI interactions.
"""

import unittest
from unittest.mock import Mock, patch, MagicMock
from PySide6 import QtWidgets
import sys

# Import the WeatherApp class
from WeatherApp import WeatherApp


class TestWeatherApp(unittest.TestCase):
    """
    Test suite for WeatherApp class
    
    Tests all major functionality including initialization, API calls,
    data processing, and error handling.
    """
    
    @classmethod
    def setUpClass(cls):
        """Set up the Qt Application once for all tests"""
        cls.app = QtWidgets.QApplication.instance()
        if cls.app is None:
            cls.app = QtWidgets.QApplication(sys.argv)
    
    def setUp(self):
        """Set up test fixtures before each test method"""
        self.weather_app = WeatherApp()
    
    def tearDown(self):
        """Clean up after each test method"""
        self.weather_app.close()
    
    def test_initialization(self):
        """Test that the WeatherApp initializes correctly"""
        # Check that the window title is set correctly
        self.assertEqual(self.weather_app.windowTitle(), "LeedsNews Weather Application")
        
        # Check that UI components exist
        self.assertIsNotNone(self.weather_app.city_input)
        self.assertIsNotNone(self.weather_app.search_button)
        self.assertIsNotNone(self.weather_app.result_area)
        self.assertIsNotNone(self.weather_app.status_label)
        
        # Check that result area is read-only
        self.assertTrue(self.weather_app.result_area.isReadOnly())
    
    def test_get_weather_description(self):
        """Test weather code to description conversion"""
        # Test various weather codes
        self.assertEqual(self.weather_app.get_weather_description(0), "Clear sky")
        self.assertEqual(self.weather_app.get_weather_description(3), "Overcast")
        self.assertEqual(self.weather_app.get_weather_description(61), "Slight rain")
        self.assertEqual(self.weather_app.get_weather_description(95), "Thunderstorm")
        self.assertEqual(self.weather_app.get_weather_description(999), "Unknown")
    
    def test_get_weather_emoji(self):
        """Test weather code to emoji conversion"""
        # Test that emojis are returned for different weather codes
        self.assertIn(self.weather_app.get_weather_emoji(0), ["☀️", "⛅", "🌤️"])
        self.assertEqual(self.weather_app.get_weather_emoji(61), "🌧️")
        self.assertEqual(self.weather_app.get_weather_emoji(71), "🌨️")
        self.assertEqual(self.weather_app.get_weather_emoji(95), "⚡")
    
    def test_get_wind_direction(self):
        """Test wind direction conversion from degrees to compass direction"""
        # Test cardinal directions
        self.assertIn("N", self.weather_app.get_wind_direction(0))
        self.assertIn("E", self.weather_app.get_wind_direction(90))
        self.assertIn("S", self.weather_app.get_wind_direction(180))
        self.assertIn("W", self.weather_app.get_wind_direction(270))
        
        # Test N/A handling
        self.assertEqual(self.weather_app.get_wind_direction("N/A"), "N/A")
        self.assertEqual(self.weather_app.get_wind_direction(None), "N/A")
    
    def test_get_weather_summary(self):
        """Test weather summary generation"""
        # Test cold weather
        summary = self.weather_app.get_weather_summary(-5, 50, 10, "Clear sky")
        self.assertIn("freezing", summary.lower())
        
        # Test hot weather
        summary = self.weather_app.get_weather_summary(35, 50, 10, "Clear sky")
        self.assertIn("hot", summary.lower())
        
        # Test rainy conditions
        summary = self.weather_app.get_weather_summary(20, 80, 15, "Moderate rain")
        self.assertIn("umbrella", summary.lower())
        
        # Test high humidity
        summary = self.weather_app.get_weather_summary(25, 85, 5, "Clear sky")
        self.assertIn("humidity", summary.lower())
    
    def test_empty_city_input(self):
        """Test that empty city input shows error"""
        # Set empty city name
        self.weather_app.city_input.setText("")
        
        # Trigger search
        self.weather_app.search_weather()
        
        # Check that status shows error
        self.assertIn("Error", self.weather_app.status_label.text())
    
    def test_update_status(self):
        """Test status label updates correctly"""
        # Test info status
        self.weather_app.update_status("Test info", "info")
        self.assertEqual(self.weather_app.status_label.text(), "Test info")
        
        # Test success status
        self.weather_app.update_status("Test success", "success")
        self.assertEqual(self.weather_app.status_label.text(), "Test success")
        
        # Test error status
        self.weather_app.update_status("Test error", "error")
        self.assertEqual(self.weather_app.status_label.text(), "Test error")
    
    @patch('WeatherApp.requests.get')
    def test_fetch_weather_data_success(self, mock_get):
        """Test successful weather data fetch"""
        # Mock geocoding response
        mock_geo_response = Mock()
        mock_geo_response.json.return_value = {
            "results": [{
                "name": "London",
                "country": "United Kingdom",
                "latitude": 51.5074,
                "longitude": -0.1278
            }]
        }
        
        # Mock weather response
        mock_weather_response = Mock()
        mock_weather_response.json.return_value = {
            "current": {
                "temperature_2m": 15.5,
                "relative_humidity_2m": 65,
                "wind_speed_10m": 12.5,
                "weather_code": 2
            },
            "daily": {
                "temperature_2m_max": [18.0],
                "temperature_2m_min": [10.0]
            }
        }
        
        # Set up mock to return different responses for different calls
        mock_get.side_effect = [mock_geo_response, mock_weather_response]
        
        # Fetch weather data
        result = self.weather_app.fetch_weather_data("London")
        
        # Verify the result contains expected data
        self.assertIn("location", result)
        self.assertEqual(result["location"]["name"], "London")
        self.assertIn("current", result)
        self.assertEqual(result["current"]["temperature_2m"], 15.5)
    
    @patch('WeatherApp.requests.get')
    def test_fetch_weather_data_city_not_found(self, mock_get):
        """Test handling of city not found"""
        # Mock geocoding response with no results
        mock_response = Mock()
        mock_response.json.return_value = {"results": []}
        mock_get.return_value = mock_response
        
        # Attempt to fetch weather data
        with self.assertRaises(Exception) as context:
            self.weather_app.fetch_weather_data("InvalidCityName123")
        
        # Check error message
        self.assertIn("not found", str(context.exception))
    
    @patch('WeatherApp.requests.get')
    def test_fetch_weather_data_timeout(self, mock_get):
        """Test handling of API timeout"""
        # Mock timeout exception
        import requests
        mock_get.side_effect = requests.exceptions.Timeout()
        
        # Attempt to fetch weather data
        with self.assertRaises(Exception) as context:
            self.weather_app.fetch_weather_data("London")
        
        # Check error message contains timeout reference
        error_msg = str(context.exception).lower()
        self.assertTrue("timeout" in error_msg or "timed out" in error_msg)
    
    @patch('WeatherApp.requests.get')
    def test_fetch_weather_data_connection_error(self, mock_get):
        """Test handling of connection error"""
        # Mock connection error
        import requests
        mock_get.side_effect = requests.exceptions.ConnectionError()
        
        # Attempt to fetch weather data
        with self.assertRaises(Exception) as context:
            self.weather_app.fetch_weather_data("London")
        
        # Check error message
        self.assertIn("connection", str(context.exception).lower())
    
    def test_show_error(self):
        """Test error display functionality"""
        error_message = "Test error message"
        self.weather_app.show_error(error_message)
        
        # Check that status label shows error
        self.assertIn("Error", self.weather_app.status_label.text())
        self.assertIn(error_message, self.weather_app.status_label.text())
        
        # Check that result area shows error message
        self.assertIn(error_message, self.weather_app.result_area.toPlainText())
    
    @patch('WeatherApp.requests.get')
    def test_display_weather(self, mock_get):
        """Test weather data display"""
        # Create sample weather data
        weather_data = {
            "location": {
                "name": "London",
                "country": "United Kingdom",
                "latitude": 51.5074,
                "longitude": -0.1278
            },
            "current": {
                "temperature_2m": 15.5,
                "apparent_temperature": 14.0,
                "relative_humidity_2m": 65,
                "wind_speed_10m": 12.5,
                "wind_direction_10m": 180,
                "precipitation": 0.0,
                "weather_code": 2
            },
            "daily": {
                "temperature_2m_max": [18.0],
                "temperature_2m_min": [10.0]
            }
        }
        
        # Display weather data
        self.weather_app.display_weather(weather_data, "London")
        
        # Check that result area contains key information
        result_text = self.weather_app.result_area.toPlainText()
        self.assertIn("London", result_text)
        self.assertIn("15.5", result_text)
        self.assertIn("65", result_text)
        self.assertIn("12.5", result_text)
    
    def test_input_validation(self):
        """Test input validation for various city names"""
        # Test valid city name
        self.weather_app.city_input.setText("London")
        city_name = self.weather_app.city_input.text().strip()
        self.assertTrue(len(city_name) > 0)
        
        # Test city name with spaces
        self.weather_app.city_input.setText("  New York  ")
        city_name = self.weather_app.city_input.text().strip()
        self.assertEqual(city_name, "New York")


class TestWeatherAppIntegration(unittest.TestCase):
    """
    Integration tests for WeatherApp
    
    These tests check the integration between different components
    of the application.
    """
    
    @classmethod
    def setUpClass(cls):
        """Set up the Qt Application once for all tests"""
        cls.app = QtWidgets.QApplication.instance()
        if cls.app is None:
            cls.app = QtWidgets.QApplication(sys.argv)
    
    def setUp(self):
        """Set up test fixtures before each test method"""
        self.weather_app = WeatherApp()
    
    def tearDown(self):
        """Clean up after each test method"""
        self.weather_app.close()
    
    def test_button_click_triggers_search(self):
        """Test that clicking the search button triggers search"""
        # Set city name
        self.weather_app.city_input.setText("London")
        
        # Mock the fetch_weather_data method
        with patch.object(self.weather_app, 'fetch_weather_data') as mock_fetch:
            mock_fetch.return_value = {
                "location": {"name": "London", "country": "UK"},
                "current": {
                    "temperature_2m": 15,
                    "relative_humidity_2m": 60,
                    "wind_speed_10m": 10,
                    "weather_code": 0
                },
                "daily": {
                    "temperature_2m_max": [20],
                    "temperature_2m_min": [10]
                }
            }
            
            # Click the button
            self.weather_app.search_button.click()
            
            # Verify fetch was called
            mock_fetch.assert_called_once_with("London")
    
    def test_enter_key_triggers_search(self):
        """Test that pressing Enter in input field triggers search"""
        # Set city name
        self.weather_app.city_input.setText("Paris")
        
        # Mock the fetch_weather_data method
        with patch.object(self.weather_app, 'fetch_weather_data') as mock_fetch:
            mock_fetch.return_value = {
                "location": {"name": "Paris", "country": "France"},
                "current": {
                    "temperature_2m": 18,
                    "relative_humidity_2m": 55,
                    "wind_speed_10m": 8,
                    "weather_code": 1
                },
                "daily": {
                    "temperature_2m_max": [22],
                    "temperature_2m_min": [12]
                }
            }
            
            # Simulate Enter key press
            self.weather_app.city_input.returnPressed.emit()
            
            # Verify fetch was called
            mock_fetch.assert_called_once_with("Paris")


def run_tests():
    """
    Run all tests and generate a report
    
    Returns:
        unittest.TestResult: Test results
    """
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test cases
    suite.addTests(loader.loadTestsFromTestCase(TestWeatherApp))
    suite.addTests(loader.loadTestsFromTestCase(TestWeatherAppIntegration))
    
    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result


if __name__ == "__main__":
    # Run the tests
    result = run_tests()
    
    # Print summary
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("="*70)
