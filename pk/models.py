from django.db import models

class Cricket(models.Model):
    runs=models.IntegerField(max_length=100)
    avg=models.SmallIntegerField(max_length=100)




