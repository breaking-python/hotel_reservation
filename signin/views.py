from django.shortcuts import render,redirect

from django.contrib.auth import authenticate, login, logout

def signin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=email, password=password)

        if user:
            login(request, user=user)
            request.session["email"] = user.username

            return redirect('/')
        else:
            context = {}
            context["error"] = "아이디가 없거나 비밀번호가 틀렸습니다."
            return render(request, 'signin.html', context)

    return render(request, 'signin.html')



def signout(request):
    logout(request)
    return redirect('/')

