from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30,blank=False,null=False)
    def __str__(self):
        return self.username

class Mood(models.Model):
    MOOD_CHOICES = [
        ('happy', 'Счастлив'),
        ('sad', 'Грусть'),
        ('angry', 'Злость'),
        ('anxious', 'Тревога'),
        ('calm', 'Спокойствие'),
    ]
    users_mood = models.CharField(choices=MOOD_CHOICES,max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='mood')
    def __str__(self):
        return f'created at {self.created_at} : mood {self.users_mood}'

    