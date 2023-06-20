from django.shortcuts import render
from .models import Category, Chefs, Gallery, Menu, Events, Role, Testimonials
from .forms import ReservationForm, ContactForm

# Create your views here.


def IndexView(request):
    foods = Menu.objects.all()
    print(foods)
    categories = Category.objects.all()
    events = Events.objects.all()

    reservation = ReservationForm()
    
    testimonials = Testimonials.objects.all()
    callery = Gallery.objects.all()
    role = Role.objects.all()
    chefs = Chefs.objects.all()

    contact = ContactForm()

    contex = {
        'foods': foods,
        'categories': categories,
        'events': events,

        'reservation': reservation,

        'testimonial':testimonials,        
        'callery':callery,
        'role':role,
        'chefs':chefs,

        'contact': contact,
    }

    return render(request, 'index.html', context=contex)