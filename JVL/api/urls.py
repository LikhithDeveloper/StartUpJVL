from django.urls import path , include
from users.views import profile

urlpatterns = [
    path('profile/',profile,name='profile'),
]
