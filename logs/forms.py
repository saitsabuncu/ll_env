from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """Yeni bir konu ekleme formu"""
    class Meta:
        model = Topic
        fields = ['title']
        labels = {'title': 'Konu Başlığı'}

class EntryForm(forms.ModelForm):
    """Belirli bir konuya yeni giriş ekleme formu"""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Günlük Girişi'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
