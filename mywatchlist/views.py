from django.shortcuts import render
from mywatchlist.models import mywatchlistItem
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data_mywatchlist_item = mywatchlistItem.objects.all()
    nonton = 0
    belom = 0

    for i in data_mywatchlist_item:
        if i.watched == True:
            nonton += 1
        else:
            belom += 1
            
    context ={
        'list_item' : data_mywatchlist_item,
        'name': 'Moza Adirafi Satria Jaka',
        'NPM' : '2106657292',
        'nonton' : nonton,
        'belom' : belom,
    }
    
    return render(request,"mywatchlist.html", context)


def show_xml(request):
    data = mywatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request):
    data = mywatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request,id):
    data = mywatchlistItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
   

def show_xml_by_id(request,id):
    data = mywatchlistItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")




