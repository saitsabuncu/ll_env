from django.urls import path, include

app_name = 'users'

urlpatterns = [
    # Varsayılan Django kimlik doğrulama URL'leri
    path('', include('django.contrib.auth.urls')),
]
