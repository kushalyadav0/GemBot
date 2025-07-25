from django.urls import path
from . import views

urlpatterns = [
    path('', views.gembot_view),

]