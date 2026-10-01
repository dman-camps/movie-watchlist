from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("<h1>hello world</h1>")
