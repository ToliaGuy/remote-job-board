from django.urls import path
from django.urls.conf import include
from jobs.views import JobAPI
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('api/', csrf_exempt(JobAPI.as_view()))
]