from django.shortcuts import render_to_response

from person.models import *

def index( r ):
    persons = Person.objects.all()
    return render_to_response('person/index.html', {'users': persons } )

def show( r , id ):
    print id
    person = Person.objects.get( pk = id )
    print person.name
    return render_to_response('person/show.html', {'user': person } )

