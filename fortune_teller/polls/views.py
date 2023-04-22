from django.shortcuts import render


def fortune_form(request):
    return render(request, "fortune_form.html")


def fortune(request):
    return render(request, "fortune.html")
