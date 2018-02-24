from django.shortcuts import render
from reserve.models import reservation
from django.contrib.auth.models import User

def mypage(request):
    context = {}
    context["hotel_list"] = reservation.objects.filter(
        user = User.objects.get(username=request.session["email"])
    )

    return render(request, 'mypage.html', context)
