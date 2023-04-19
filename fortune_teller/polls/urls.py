from django.urls import path

from . import views


urlpatterns = [
    # first parameter originates in the fortune_teller/urls
    # second parameter points to the specified view function. here it is the form for the fortune-teller
    path('fortune_form/', views.fortune_form),
    path('fortune/', views.fortune)
]
