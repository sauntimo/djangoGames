# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.core import serializers
from django.http import Http404
import urllib
import models

def index(request):
   entries = models.Entry.objects.all() 
   return render(request, 'index',{'entries': entries} )

def index_json(request):
   entries = models.Entry.objects.all() 
   return HttpResponse(serializers.serialize('json', entries))

#   html = '<html><body><h1> Posts </h1><ul>'
#   for entry in entries:
#       html += '<li><a href="/blog/posts/%s/">%s</li>' % ( entry.id, entry.title )
#   html += '</ul></body></html>'
#   return HttpResponse(html)


def display_post(request,id):
    entry = models.Entry.objects.get(pk=id)
    return render(request, 'display_post', {'entry': entry} )
#    html = '<html><head><title>%s</title></head><body><h1>%s</h1>%s</body></html>' % (
#        entry.title, 
#        entry.title,
#        entry.body
#    )
#    return HttpResponse(html)

def display_tag(request,name):
    try:
        decoded_tag_name = urllib.unquote(name)
        tag = models.Tag.objects.filter(name=decoded_tag_name)[0]
        return render(request, 'display_tag', {'tag': tag} )
    except IndexError:
        raise Http404('Tag "%s" not found' % decoded_tag_name)
