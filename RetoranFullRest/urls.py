from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from api_apps.views import CategoryViewSet, MenuViewSet, ReservationViewSet, TestimonialsViewSet, EventsViewSet,\
                 RoleViewSet, ChefsViewSet, GalleryViewSet, ContactViewSet

router = routers.DefaultRouter()


router.register(r'Category', CategoryViewSet)
router.register(r'Menu', MenuViewSet)
router.register(r'Reservation', ReservationViewSet)
router.register(r'testimonials', TestimonialsViewSet)
router.register(r'events', EventsViewSet)
router.register(r'role', RoleViewSet)
router.register(r'chefs', ChefsViewSet)
router.register(r'gallery', GalleryViewSet)
router.register(r'contact', ContactViewSet)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('food.urls')),
    path('api/', include(router.urls))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)