# WEEKLY ASSIGNMENT 02

Moza Adirafi Satria Jaka - 2106657292

[Press this to open the link](https://weeklyassignment02.herokuapp.com/katalog/)

## Client Request to the Django Web Application

![Django Diagram drawio](https://user-images.githubusercontent.com/112457836/190058400-f84f3733-38f8-41e2-8f40-1d53b3370db2.png)


In conclusion, this application will receive request from the client that will be directed to URL.  After receiving a request, Django searches if there is any corresponding response for the request and will direct it into Views. Views will then fetch data from Models.py which will render a Template (contains the static HTML output of a webpage) that will be showcased to the client.



## Why do we use virtual environments?

Python has a variety of modules and packages for various applications. During our project, we may need to install a third-party library. Another project, which does not require any third-party packages, also uses the same directory for retrieval and storage. As a result, the virtual environment can be used to create a separate isolated environment for both projects, and each project can store and retrieve packages from its own environment. 

## Can we still create a django web application without virtual environment?
Without a virtual environment, web application development is still possible, but it is very not recommended because let’s say you want to work with two different projects in python, if we install all those libraries in the same default environment, then errors might come up and the default environment will become messy. So, it’s very recommended to use a virtual environment



## IMPLEMENTING STEP 1-4

### ```Step 1 (views.py)```
On this step, I filled this file with a function called show_catalog that returns the render function which has a function of showing the “Katalog.html”(filled with the data on the variable “context”).

```shell
 def show_catalog(request):
   return render(request,"katalog.html", context)

data_katalog_item = CatalogItem.objects.all()
context ={
    'list_item' : data_katalog_item,
    'name': 'Moza Adirafi Satria Jaka',
    'NPM' : '2106657292'
}
```
   
### ```Step 2 (urls.py)```
This step is used to route the views function so that the HTML page can be displayed within the browser. The variable url patterns is added to call the show_catalog function.

```shell
urlpatterns = [
   path('', show_catalog, name='show_catalog'),
]
```
Also, katalog/ is registered in urls.py that is located on project_django with this following code
```shell
path('', include('example_app.urls')),
```

### ```Step 3 (katalog.html)```
On this step, to display the list of items in a table, make a loop of list_item to take the data that is already stored inside the models.py.

```shell
{% for item in list_item %}
   <tr>
     <th>{{item.item_name}}</th>
     <th>{{item.item_price}}</th>
     <th>{{item.item_stock}}</th>
     <th>{{item.rating}}</th>
     <th>{{item.description}}</th>
     <th>{{item.item_url}}</th>
   </tr>
```
### ```Step 4 (Deploy)```
After we finish editing all the codes, we use the 3 git commands which are git add, git commit and git push. Then, all the updated codes will be displayed on the repository. To deploy it on Heroku, add a secret repository filled with the API key and the APP name (created on Heroku).


## Soruces

- https://python.plainenglish.io/the-mvt-design-pattern-of-django-8fd47c61f582  
- https://towardsdatascience.com/why-you-should-use-a-virtual-environment-for-every-python-project-c17dab3b0fd0
