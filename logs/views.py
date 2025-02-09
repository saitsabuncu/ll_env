from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request):
    """Ana sayfa"""
    return render(request, 'logs/index.html')

def topics(request):
    """Tüm konuları listeleyen sayfa"""
    topics = Topic.objects.order_by('-date_added')  # Konuları tarihe göre sırala
    context = {'topics': topics}
    return render(request, 'logs/topics.html', context)

def topic(request, topic_id):
    """Belirli bir konunun girişlerini listeleyen sayfa"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'logs/topic.html', context)

def new_topic(request):
    """Yeni bir konu ekleme"""
    if request.method != 'POST':
        form = TopicForm()  # Boş form göster
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('logs:topics')  # Konular listesine yönlendir

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
