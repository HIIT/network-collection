from django.db import models

class Person(models.Model):
    name = models.CharField( max_length = 200 )
    image = models.CharField( max_length = 200 )

class Connection(models.Model):
    fromPerson = models.ForeignKey( Person , related_name = 'from' )
    toPerson = models.ForeignKey( Person ,  related_name = 'to' )
    weight = models.IntegerField()
