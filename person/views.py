from django.shortcuts import render_to_response

from person.models import *

def index( r ):
    persons = Person.objects.all()
    return render_to_response('person/index.html', {'users': persons } )
