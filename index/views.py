from django.shortcuts import render
from reserve.models import hotel


def index(request):
    context = {}
    context["hotel_list"] = hotel.objects.all()

    return render(request, 'index.html', context)