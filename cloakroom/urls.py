from django.urls import path
from cloakroom.views import IndexView


app_name = "cloakroom"


urlpatterns = [
    path("", IndexView.as_view(), name="index")
]