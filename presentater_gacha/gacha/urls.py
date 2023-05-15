from django.urls import path
from .views import TopView


urlpatterns = [
    path('', TopView.as_view(), name="top")
]
