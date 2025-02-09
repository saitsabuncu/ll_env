from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Yeni kullanıcı kaydı"""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)  # Kullanıcıyı otomatik giriş yaptır
            return redirect('logs:index')

    context = {'form': form}
    return render(request, 'users/register.html', context)
