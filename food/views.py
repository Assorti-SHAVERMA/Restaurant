from django.shortcuts import render
from .models import Category, Menu, Events
from .forms import ReservationForm, ContactForm

# Create your views here.


def IndexView(request, id):
    foods = Menu.objects.filter(category_id=id)
    print(foods)
    categories = Category.objects.all()
    events = Events.objects.all()

    reservation = ReservationForm()

    contex = {
        'foods': foods,
        'categories': categories,
        'events': events,

        'reservation': 'reservation'
    }

    return render(request, 'index.html', context=contex)