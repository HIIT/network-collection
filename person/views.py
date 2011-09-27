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
    print r
    return HttpResponse("You're voting on poll %s." % id)
