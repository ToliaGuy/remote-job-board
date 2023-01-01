from django.urls import path
from django.urls.conf import include
from jobs.views import JobAPI

urlpatterns = [
    path('api/', JobAPI.as_view())
]