# django_test/urls.py (my app)
from django.urls import path
from . import views  # Import the views module from the current app

urlpatterns = [
    path('', views.index, name='index'),  # Root URL for the app
    path('add_students/', views.add_students, name='add_students'),  # Map the URL to the view function
]
