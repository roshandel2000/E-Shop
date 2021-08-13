from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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
    "friday": "Today is Friday"
}


def index(request):
    # return HttpResponse("It's an index page!")
    return HttpResponse(render_to_string('challenges/challenge.html'))


def days(request, day):
    # return HttpResponse(days_week.get(day))
    context = {
        "data": days_week.get(day)
    }
    return render(request, "challenges/days.html", context)


def fun(request, string):
    if string == "404":
        return HttpResponseNotFound("It's not valid.")
    return HttpResponse(f'<h1> wow {string} </h1>')


def fun_by_number(request, num):
    return HttpResponseRedirect(reverse("fun", args=[f'{num}redirect']))
    # return HttpResponseRedirect(f'/challenges/{num}redirect')
    # return HttpResponse(f'It\'s a number: {num}')


def days_of_week(request):
    days_name = list(days_week.keys())
    items_list = ""
    for day in days_name:
        path_url = reverse("days_of_the_week", args=[day])
        items_list += f'<li> <a href={path_url}> {day} </a> </li>'
    content = """
        <ul>
            <li>
                <a href='/challenges/saturday'> saturday </a>
                <a href='/challenges/sunday'> sunday </a>
                <a href='/challenges/monday'> monday </a>
                <a href='/challenges/tuesday'> tuesday </a>
                <a href='/challenges/wednesday'> wednesday </a>
                <a href='/challenges/thursday'> thursday </a>
                <a href='/challenges/friday'> friday </a>
            </li> 
        </ul>
    """

    return HttpResponse(items_list)