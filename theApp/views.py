from django.http import JsonResponse
from .models import Links


# Create your views here.
def index(request):
    links = []

    urls = Links.objects.all()

    for url in urls:
        links.append(url.the_url)

    json_dict = {'URLs': links}

    return JsonResponse(json_dict)
