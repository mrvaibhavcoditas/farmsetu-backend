from rest_framework.test import APITestCase
from rest_framework import status


class WeatherAPITest(APITestCase):
    def test_get_all_weather_data(self):
        response = self.client.get(f'/api/weather/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_weather_api_not_found(self):
        response = self.client.get(f'/weather/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
