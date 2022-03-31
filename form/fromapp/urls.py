from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('thankyou', views.ThankYouView.as_view(), name='thank_you'),
]