from django.db import models

# Create your models here.
class UserInfo(models.Model):
    id=models.AutoField(max_length=11, db_column="UID", primary_key=True)
    user=models.CharField(max_length=12, blank=False)
    pwd=models.CharField(max_length=32, blank=False)
    email=models.CharField(max_length=32, blank=False)

class DouBanMovie(models.Model):
        title = models.CharField(max_length=32)
        score = models.CharField(max_length=32)
        content = models.TextField()
        info = models.TextField()

