# capital_guess/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.guess_capital, name='guess_capital'),
    path('guess_capital_result',views.guess_capital_result,name='guess_capital_result')
]
