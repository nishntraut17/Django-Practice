# myapp/views.py
from django.shortcuts import render

# Correct import statement based on your provided models.py file
from myapp.models import Student

# Now you can use the Student class in your code


from django.http import HttpResponse


def home(request):
    peoples = [
        {"name": "Nishant Raut", "age": 13},
        {"name": "Deep Patel", "age": 33},
    ]
    return render(request, "index.html", context={"peoples": peoples})


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


def success_page(request):
    return HttpResponse("This is a success page")
