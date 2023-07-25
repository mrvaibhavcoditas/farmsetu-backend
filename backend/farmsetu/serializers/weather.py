from rest_framework import serializers

from farmsetu.models import Weather


class WeatherSerializer(serializers.ModelSerializer):
    year = serializers.ReadOnlyField(source='year.name')
    q1 = serializers.SerializerMethodField()
    q2 = serializers.SerializerMethodField()
    q3 = serializers.SerializerMethodField()
    q4 = serializers.SerializerMethodField()

    class Meta:
        model = Weather
        fields = '__all__'

    def get_q1(self, obj):
        return round(obj.q1, 2)

    def get_q2(self, obj):
        return round(obj.q2, 2)

    def get_q3(self, obj):
        return round(obj.q3, 2)

    def get_q4(self, obj):
        return round(obj.q4, 2)