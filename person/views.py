from django.shortcuts import render_to_response

from django.template import RequestContext

from person.models import *

def index( r ):
    persons = Person.objects.all()
    return render_to_response('person/index.html', {'users': persons } )

def show( r , id ):
    person = Person.objects.get( pk = id )
    persons = Person.objects.all().exclude( pk = id )
    return render_to_response('person/show.html', {'user': person, 'others' : persons }, context_instance=RequestContext (r ) )

def data( r , id ):
    person = Person.objects.get( pk = id )
    for i in r.POST.items():
        if i[0].startswith('connection_to_'):
	    target = int( i[0][14:] )
            target = Person.objects.get( pk = target )
	    weight = int( i[1] )
            c = Connection( fromPerson = person, toPerson = target, weight = weight )
            c.save()
    return ''
