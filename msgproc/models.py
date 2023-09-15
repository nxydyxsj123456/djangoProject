from django.db import models

# Create your models here.
class gjzpCookie(models.Model):
    phone=models.CharField(max_length=200,primary_key=True)
    content = models.CharField(max_length=200)
    TimeStamp = models.DateTimeField(auto_now=True, verbose_name='时间戳')

    def __str__(self):
        return self.phone+" "+self.content+" "+str(self.TimeStamp)