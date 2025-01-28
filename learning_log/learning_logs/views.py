from django.shortcuts import render, redirect, get_object_or_404
from .models import Entry, Topic
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    """Learning Log için ana sayfa"""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Bütün konuları göster."""
    topics = Topic.objects.order_by('date_add')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Belirli bir konuyu ve ilişkili girdileri göster."""
    topic = get_object_or_404(Topic, id=topic_id)
    entries = topic.entry_set.order_by('-date_added')  # İlgili girdileri sıralama
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Yeni bir konu oluştur."""
    if request.method != 'POST':
        # Boş bir form oluştur
        form = TopicForm()
    else:
        # POST verilerini işle
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    topic=Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form=EntryForm
    else:
        form=EntryForm(data=request.POST)
        if form.is_valid():
            new_entry=form.save(commit=False)
            new_entry.topic=topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    context={'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

def edit_entry(request, entry_id):
    """Var olan bir girdiyi düzenle."""
    entry = get_object_or_404(Entry, id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # Mevcut girdiyi form ile doldur
        form = EntryForm(instance=entry)
    else:
        # POST verilerini işle
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)