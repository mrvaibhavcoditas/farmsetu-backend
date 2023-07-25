from rest_framework.permissions import AllowAny
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from django.db.models import F

from farmsetu.models import Weather
from farmsetu.serializers import WeatherSerializer
from farmsetu.api.filters import WeatherFilter


class WeatherAPIView(ListModelMixin, GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = WeatherSerializer
    queryset = Weather.objects.all()
    filterset_class = WeatherFilter

    def get_queryset(self):
        queryset = self.queryset.all()
        queryset = queryset.annotate(
            q1=(F('jan') + F('feb') + F('mar')) / 3,
            q2=(F('apr') + F('may') + F('jun')) / 3,
            q3=(F('jul') + F('aug') + F('sep')) / 3,
            q4=(F('oct') + F('nov') + F('dec')) / 3
        )
        return queryset
