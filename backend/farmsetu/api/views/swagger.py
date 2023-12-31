from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="FarmSetu API",
        default_version='v1',
        description="Welcome to the world of FarmSetu",
        terms_of_service="https://www.farmsetu.com",
        contact=openapi.Contact(email="contact@farmsetu.com"),
        license=openapi.License(name="FarmSetu IP"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
