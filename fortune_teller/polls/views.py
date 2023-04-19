from django.shortcuts import render


def fortune_form(request):
    name = request.POST.get("user", "")
    return render(request, "fortune_form.html", {"name": name})


def fortune(request):
    return render(request, "fortune.html")
