from django.shortcuts import render
from .models import Menu, Category, Events, Testimonials, \
                    Gallery, Role, Chefs
from .forms import ReservationForm, ContactForm



def IndexView(request):
    foods = Menu.objects.all()
    categories = Category.objects.all()
    events = Events.objects.all()
    testimonials = Testimonials.objects.all()
    gallery = Gallery.objects.all()
    role = Role.objects.all()
    chefs = Chefs.objects.all()

    reservation = ReservationForm()
    contact = ContactForm()
    context = {
        'foods': foods,
        'categories': categories,
        'events': events,
        'reservation': reservation,
        'testimonials': testimonials,
        'gallery': gallery,
        'role': role,
        'chefs': chefs,
        'contact': contact,
    }
    return render(request, 'index.html', context=context)