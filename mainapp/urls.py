from django.urls import path
from .views import * 
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('gallery', GalleryView.as_view(), name="gallery"),
]
