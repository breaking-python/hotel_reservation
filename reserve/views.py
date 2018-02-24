from django.shortcuts import render,redirect
from .models import hotel, reservation
from django.contrib.auth.models import User
from datetime import date
def reserve(request, id):

    is_hotel = hotel.objects.get(id=id)

    if request.method == "POST":
        party = request.POST.get('party')
        startday = request.POST.get('startday') #YYYY/MM/DD
        rd = startday.split('/')
        days = request.POST.get('days')

        reservation.objects.create(
            user=User.objects.get(username=request.session["email"]),
            hotel=is_hotel,
            party=party,
            days=days,
            startday=date(int(rd[0]),int(rd[1]),int(rd[2]))

        )
        return redirect('/')

    return render(request, 'reserve.html')
