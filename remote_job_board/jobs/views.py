from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q
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
    context = {}
    page = request.GET.get('page')
    search = request.GET.get('search')
    if page:
        page = request.GET["page"]
    else:
        page = 1
    
    if search:
        job_posts = JobPost.objects.filter(
              Q(title__icontains=search) | Q(description__icontains=search) | Q(company__icontains=search)
        )
    else:
        job_posts = JobPost.objects.all()
    paginator = Paginator(job_posts, per_page=10)
    page_object = paginator.get_page(page)
    context = {"object_list": page_object}
    if search:
        context["search"] = search
    return render(request, "index.html", context)

def contact(request):
    return render(request, "contact.html")

def policies(request):
    return render(request, "policies.html")


class JobPostDetail(generic.DetailView):
    model = JobPost
    template_name = 'job_post_detail.html'