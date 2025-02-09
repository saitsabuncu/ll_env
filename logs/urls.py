from django.urls import path
from . import views

app_name = 'logs'  # Namespace ekledik

urlpatterns = [
    path('', views.index, name='index'),  # Ana sayfa
    path('topics/', views.topics, name='topics'),  # Tüm konuları listeleyen sayfa
    path('topics/<int:topic_id>/', views.topic, name='topic'),  # Bir konuya ait girişler
    path('new_topic/', views.new_topic, name='new_topic'),  # Yeni konu ekleme
    path('topics/<int:topic_id>/new_entry/', views.new_entry, name='new_entry'),  # Yeni giriş ekleme
]
