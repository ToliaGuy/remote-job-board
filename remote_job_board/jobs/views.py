from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from .models import JobPost
import json
from django.core import serializers


class JobAPI(TemplateView):
    def get(self, request, *args, **kwargs):
        SomeModel_json = serializers.serialize("json", JobPost.objects.all()[:10])
        data = {"jobs": SomeModel_json}
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        job = json.loads(request.body)
        JobPost.objects.create(title=job["title"], company=job["company"], url=job["link"], description=job["description"], source=job["source"])
        print(request.body)
        return HttpResponse("ok")

    # delete data from source
    def delete(self, request, *args, **kwargs):
        data = json.loads(request.body)
        source = data["source"]
        JobPost.objects.filter(source=source).delete()
        return HttpResponse("ok")


def listing(request):
    jobs = JobPost.objects.all()[:10]
    context = {"object_list": jobs}
    return render(request, "index.html", context)


class JobPostDetail(generic.DetailView):
    model = JobPost
    template_name = 'job_post_detail.html'