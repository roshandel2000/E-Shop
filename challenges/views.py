from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

days_week = {
    "saturday": "Today is Saturday",
    "sunday": "Today is Sunday",
    "monday": "Today is Monday",
    "tuesday": "Today is Tuesday",
    "wednesday": "Today is Wednesday",
    "thursday": "Today is Thursday",
    "friday": "Today is Friday",
    "holiday": None
}


def index(request):
    return HttpResponse(render_to_string('challenges/index.html'))


def days(request, day):
    if days_week.get(day) is not None:
        context = {
            "data": days_week.get(day)
        }
    else:
        # response = render_to_string('404.html')
        # return HttpResponseNotFound(response)
        raise Http404()
    return render(request, "challenges/days.html", context)


def fun(request, string):
    if string == "404":
        return HttpResponseNotFound("It's not valid.")
    return HttpResponse(f'<h1> wow {string} </h1>')


def fun_by_number(request, num):
    return HttpResponseRedirect(reverse("fun", args=[f'{num}redirect']))


def days_of_week(request):
    days_name = list(days_week.keys())

    addresses = [reverse("days_of_the_week", args=[day_name]) for day_name in days_name]
    addresses.reverse()
    context = {
        'days': days_name,
        'addresses': addresses
    }
    print(addresses)
    return render(request, "challenges/listDays.html", context)