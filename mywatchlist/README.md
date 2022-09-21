# WEEKLY ASSIGNMENT 03
- Main(https://weeklyassignment02.herokuapp.com/)
- Katalog(https://weeklyassignment02.herokuapp.com/katalog/)
- mywachlist(https://weeklyassignment02.herokuapp.com/mywatchlist/)
<br>
## Difference between JSON, XML, and HTML!
HTML (Hyper Text Markup Language) is a programming language used to generate web pages and web applications. It is a type of markup language. We can create our own static page using HTML. It is used to display data rather than convey data.

XML (Extensible Markup Language) is also used to develop web pages and web applications. It is dynamic because it is used to transfer data rather than to display data. XML's design goals are focused on simplicity, universality, and Internet usability.

JSON (JavaScript Object Notation) is a language-independent lightweight data-exchange format. It is simple to understand and generate because it is built on the JavaScript programming language.
<br>
## Why do we need data delivery when implementing on a platform?
Data delivery come in a variety of formats such as HTML, XML, JSON, and others. If we want to make a platform in which we transfer data, it is required so that the process can be executed successfully.
<br>
## STEPS OF IMLEMENTATION

1. Make a new application by doing the python "manage.py startapp mywatchlist" in the terminal (on your project directory)
2. Put mywatchlist app inside the INSTALLED_APPS on "settings.py"
3. Add this following code inside urlpatterns on "settings.py"
``` shell
path('mywatchlist/',include('mywatchlist.urls'))
```
4. Make a route inside the urls.py on mywatchlist app with these following code:
``` shell
urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
    path('html/', show_mywatchlist, name='show_mywatchlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    
]
```

5. Make a model data inside "models.py" on mywatchlist app with 5 attributes:
``` shell
class mywatchlistItem(models.Model):
    watched = models.BooleanField()
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.TextField()
    review = models.TextField()
```
6. On the Json file, write 10 data's with the attributes on models.py with this following format:
``` shell
{
        "model": "mywatchlist.mywatchlistitem",
        "pk": 1,
        "fields": {
            "watched": true,
            "title": "All or Nothing (Arsenal)",
            "rating": 7,
            "release_date": "August 4, 2022",
            "review": "Entertaining Scenes!"
        }
}
```
7. Write functions on views.py with these following code:
``` shell
def show_mywatchlist(request):
    data_mywatchlist_item = mywatchlistItem.objects.all()
    context ={
        'list_item' : data_mywatchlist_item,
        'name': 'Moza Adirafi Satria Jaka',
        'NPM' : '2106657292',
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
```
9. Lastly, make a html file so that it can be rendered to the client:
<br>

## POSTMAN

### HTML
![image](https://user-images.githubusercontent.com/112457836/191538971-5a01d06d-1117-459a-b916-b98ac52710cf.png)

### JSON
![image](https://user-images.githubusercontent.com/112457836/191539131-6da5eae4-ab1f-449d-95a7-c3d6d7a83310.png)

### XML
![image](https://user-images.githubusercontent.com/112457836/191539190-a685aa4e-8b73-4e5c-828d-5a1140c5a0a2.png)





