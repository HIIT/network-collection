from django.shortcuts import render_to_response

from django.template import RequestContext

from person.models import *

import json

def index( r ):
    persons = Person.objects.all()
    persons = persons.exclude( done = 1 )
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
            if weight > 0:
                c = Connection( fromPerson = person, toPerson = target, weight = weight )
                c.save()
    person.done = 1
    person.save()
    return render_to_response('person/message.html', { 'message' : 'Data stored succesfully' } )

def statistics(r):
    js = []
    persons = Person.objects.all()

    colors = [ None, '#eee' , '#eee', 'green', 'orange', 'red']

    for p in persons:
         friends = []
         for c in p.from_set.all():
             q = { 'nodeTo' : 'person_' + str( c.toPerson.id ) , 'data' : { '$lineWidth' : c.weight * 2 , '$color' : colors[ c.weight ] } }
             friends.append( q )
         p = { 'id' : 'person_' + str( p.id ) ,
               'name' : p.name ,
               'adjacencies' : friends }
         js.append( p )
    return render_to_response('person/graph.html', { 'json' : json.dumps( js ) } )

def ucinet(r):
    persons = Person.objects
    out = ''
    out += 'DL n=' + str( persons.count() ) + '<br/>'
    temp = []
    for p in persons.all():
       temp.append( p.display() )
    out += ', '.join( temp ) + '<br/>'
    out += 'format = edgelist1 <br/>'
    out += 'labels embedded:<br/>'
    out += 'data:<br/>'
    for c in Connection.objects.all():
        out += c.fromPerson.display() + ' ' + c.toPerson.display() + ' ' + str( float( c.weight ) ) + '<br/>'
    return render_to_response('person/export.file', { 'data' : out } )

def csv(r):
     persons = Person.objects.all()
     persons2 = Person.objects.all()
     connections = COnnection.objects.all()
     out = ''
     for p in persons:
         array = []
         array.append( p.display() )
         contacts = map( lambda c : c.toPerson, p.from_set.all() )
         for p2 in persons2:
             if p2 in contacts:
                 array.append( str( 'x' ) )
             else:
                 array.append( '0' )
         out += ','.join( array ) + '<br/>'
     return render_to_response('person/export.file', { 'data' : out } )
