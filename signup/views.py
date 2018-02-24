from django.shortcuts import render, redirect

from django.contrib.auth.models import User

def signup(request):
    if request.method =="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        new_user = User.objects.create(
            username = email
        )

        new_user.set_password(password)
        new_user.save()

        return redirect('/')

    return render(request, 'signup.html' )
