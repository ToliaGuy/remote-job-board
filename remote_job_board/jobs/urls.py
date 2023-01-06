from django.urls import path
from django.urls.conf import include
from jobs.views import JobAPI
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('', views.listing, name='home'),
    path('api/', csrf_exempt(JobAPI.as_view())),
    path('<slug:pk>/', views.JobPostDetail.as_view(), name='job_post_detail'),
]