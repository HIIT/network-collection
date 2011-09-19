from django.db import models

class Person(models.Model):
    name = models.CharField()
    image = models.CharField()

class Connection(moderls.Model):
    initial = models.ForeignKey( Person )
    target = models.ForeignKey( Person )
    weight = models.IntegerField()
