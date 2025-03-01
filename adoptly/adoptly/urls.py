from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from adoptions.views import AnimalViewSet
from adoptions.views import animals_list, home
from django.conf import settings
from django.conf.urls.static import static
from adoptions.views import adoption_request, success_page

router = DefaultRouter()
router.register(r'animals', AnimalViewSet)  # /api/animals/


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Add this line
    path('', home, name='home'),  # New home page
    path('animals_list/', animals_list, name='animals_list'),  # Move animals list
    path('adopt/<int:animal_id>/', adoption_request, name='adoption_request'),
    path('success/', success_page, name='success_page'),
]

# Add this line to serve media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)