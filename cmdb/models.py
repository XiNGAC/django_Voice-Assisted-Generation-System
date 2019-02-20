from django.db import models
# Create your models here.


class Audio(models.Model):
    temp_audio = models.FileField('录音', upload_to='./upload')



