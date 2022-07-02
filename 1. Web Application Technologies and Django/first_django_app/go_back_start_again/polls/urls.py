from django.urls import path
from .views import index


urlpatterns = [
    # Wired an index or anything view into the URLconf
    path('', index, name='index'),
]