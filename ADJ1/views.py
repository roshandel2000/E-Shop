from django.http import HttpResponse


def index(Request):
    return HttpResponse("index page")

