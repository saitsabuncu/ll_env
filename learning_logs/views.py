from django.shortcuts import render, get_object_or_404
from .models import Topic

# Create your views here.
def index(request):
    """Learning Log için ana sayfa"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Belirli bir konuyu ve ilişkili girdileri göster."""
    topic = get_object_or_404(Topic, id=topic_id)
    entries = topic.entry_set.order_by('-date_added')  # İlgili girdileri sıralama
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)



