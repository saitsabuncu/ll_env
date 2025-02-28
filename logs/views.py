from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required  # Kullanıcı girişini zorunlu kılar
from django.http import Http404

def index(request):
    """Ana sayfa"""
    return render(request, 'logs/index.html')

@login_required
def topics(request):
    """Sadece giriş yapan kullanıcının konularını listele"""
    topics = Topic.objects.filter(owner=request.user).order_by('-date_added')
    context = {'topics': topics}
    return render(request, 'logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Belirli bir konunun girişlerini listeleyen sayfa"""
    topic = Topic.objects.get(id=topic_id)
    
    # Eğer konu başkasına aitse, 404 hatası döndür
    if topic.owner != request.user:
        raise Http404
    
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'logs/topic.html', context)

@login_required
def new_topic(request):
    """Yeni bir konu ekleme"""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user  # Owner olarak giriş yapan kullanıcıyı ata
            new_topic.save()
            return redirect('logs:topics')

    context = {'form': form}
    return render(request, 'logs/new_topic.html', context)

def new_entry(request, topic_id):
    """Belirli bir konuya yeni giriş ekleme"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()  # Boş form göster
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic  # Konuyu belirle
            new_entry.save()
            return redirect('logs:topic', topic_id=topic_id)  # Konu sayfasına yönlendir

    context = {'topic': topic, 'form': form}
    return render(request, 'logs/new_entry.html', context)
