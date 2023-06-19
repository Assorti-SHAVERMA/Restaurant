from django.shortcuts import render
from .models import Category, Menu, Events

# Create your views here.


def IndexView(request, id):
    foods = Menu.objects.filter(category_id=id)
    print(foods)
    categories = Category.objects.all()
    events = Events.objects.all()

    contex = {
        'foods': foods,
        'categories': categories,
        'events': events,
    }

    return render(request, 'index.html', context=contex)