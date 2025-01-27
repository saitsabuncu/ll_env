from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    """Kullanıcıyı kaydet ve oturum aç"""
    if request.method != 'POST':
        # Boş bir kayıt formu oluştur
        form = UserCreationForm()
    else:
        # Doldurulmuş form verilerini işle
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            # Yeni kullanıcıyla oturum aç
            login(request, user)
            return redirect('learning_logs:index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)

