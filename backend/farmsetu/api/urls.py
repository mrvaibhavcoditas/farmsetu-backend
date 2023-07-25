from rest_framework.routers import DefaultRouter

from farmsetu.api.views import WeatherAPIView

router = DefaultRouter()
router.register('weather', WeatherAPIView, basename='weather')
