from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


class JobAPI(TemplateView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("get request")

    def post(self, request, *args, **kwargs):
        return HttpResponse("post request")
