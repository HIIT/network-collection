from django.db import models

class Person(models.Model):
    name = models.CharField( max_length = 200 )
    done = models.BooleanField(default=0)

    def __unicode__(self):
      return self.name

    def display(self):
        return self.name.replace(' ', '')[:18]

class Connection(models.Model):
    fromPerson = models.ForeignKey( Person , related_name = 'from_set' )
    toPerson = models.ForeignKey( Person ,  related_name = 'toPerson' )
    weight = models.IntegerField()
    
    def __str__(self):
      return str( self.fromPerson.id ) + '->' + str( self.toPerson.id )
