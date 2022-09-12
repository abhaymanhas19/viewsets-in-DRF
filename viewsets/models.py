from django.db import models

class songs(models.Model):
    id=models.AutoField(primary_key=True)
    songtitle=models.CharField(max_length=100)
    singer=models.CharField(max_length=100)
    dateandtime=models.DateTimeField(auto_now=True)