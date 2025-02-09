from django.db import models
from django.contrib.auth.models import User  # Kullanıcı modelini dahil et

class Topic(models.Model):
    """Kullanıcının öğrenmek istediği konu"""
    title = models.CharField(max_length=200)  # Konu başlığı
    date_added = models.DateTimeField(auto_now_add=True)  # Otomatik tarih ekleme
    owner = models.ForeignKey(User, on_delete=models.CASCADE) # Artık null olamaz

    
    def __str__(self):
        return self.title

class Entry(models.Model):
    """Konu hakkındaki günlük girişleri"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)  # Hangi konuya ait olduğu
    text = models.TextField()  # Kullanıcının girdiği not
    date_added = models.DateTimeField(auto_now_add=True)  # Otomatik tarih ekleme

    class Meta:
        verbose_name_plural = 'entries'  # Django admin için düzgün isimlendirme

    def __str__(self):
        return f"{self.text[:50]}..."  # İlk 50 karakteri göster
