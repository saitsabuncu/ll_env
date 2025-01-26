""" learnin_logs için URL örüntülerini tanımlar."""
from django.urls import path
from . import views

app_name='learning_logs'
urlpatterns = [
    #Ana sayfa.
    path('', views.index, name='index'),
    #Bütün konuları gösteren sayfa.
    path('topics/', views.topics, name='topics'),
    #tek bir konu için ayrıntı sayfası.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #Yeni Konu eklemek için olan sayfa
    path('new_topic/', views.new_topic, name='new_topic'),  # Bu satırı ekle
    #Yeni bir girdi eklemek için olan sayfa.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    
]