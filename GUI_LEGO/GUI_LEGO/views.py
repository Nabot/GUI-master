def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'login.html', c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username = username, password = password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpRespo
        nseRedirect('/accounts/invalid')