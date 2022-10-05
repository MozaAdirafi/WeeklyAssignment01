# WEEKLY ASSIGNMENT 04
- [Main](https://weeklyassignment02.herokuapp.com/)
- [Katalog](https://weeklyassignment02.herokuapp.com/katalog/)
- [mywachlist](https://weeklyassignment02.herokuapp.com/mywatchlist/)
- [todolist](https://weeklyassignment02.herokuapp.com/todolist)

## What does {% csrf_token %} do in the element? What happens if there is no such "code snippet"?
A CSRF token is a string that's associated with a user's session but isn't automatically submitted. 
A website only functions when it receives a valid CSRF token along with the cookies; as an attacker there is no way for them to know a user-specific token,
the attacker is unable to act on behalf of the user.

If we do not use the csrf token, our website will continue to function normally, but some sensitive route links may be viewed by others. Hence, it is dangerous if we
didn't put the csrf_token in.
<br>
<br>
## Can we create the form element manually (without using a generator like {{ form.as_table }})? Explain generally how to create form manually.
Yes, we can. Even i created the form element without a generator like {{form.as_table}} on "create.html". The steps are almost the same, all you need to do 
is to put ``<form method="POST">`` and write ``{% csrf_token %}`` to insert the token. Lastly, just put the input code like below without creating any table and 
specify each line.

```shell
<input type="text" name="title" placeholder="Name your Title!"required >
```
<br>
<br>

## Data Flow.
After the user pressed the submit button inside the html, the data that is inputted by the user will be processed
into the function inside views.py. The inputted data will be accessed by the code ``request.POST.get("input name")``. Then we can save the database with save(). This is the
example of the code,

```shell
title = request.POST.get("title")
        description = request.POST.get("description")
        create = TaskItem(user = user,date = datetime.datetime.now(), title = title, description = description )
        create.save()
```

## IMPLEMENTATION
1. Make a new application by doing the python "manage.py startapp todolist" in the terminal (on your project directory)
2. Put todolist app inside the INSTALLED_APPS on "settings.py"
3. Add this following code inside urlpatterns on "settings.py"
``` shell
path('todolist/',include('mywatchlist.urls'))
```
4. Make a route inside the "urls.py" on todolist app with these following code:
``` shell
urlpatterns = [
    path('',todolist, name='todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-text/', create_task, name='create_task'),
    path('change-status/<int:id>', change_status, name='change_status'),
    path('delete/<int:id>', delete_task, name='delete_task'),
]

```

5. Make a model data inside "models.py" on todolist app with 5 attributes:
``` shell
class TaskItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)
```
6. Make a login,logout, register function on "views.py" and also the template (html) for the login and register page:
7. Write a function to show the todolist on "views.py" also with the html page on templates :
``` shell
def todolist(request):
    data = TaskItem.objects.filter(user = request.user)
    context = {
        'todolist' : data,
        'username' : request.user.username,
        'lastlogin' : request.COOKIES['last_login']       
    }
    return render(request,"todolist.html", context)

```

8. Put the "login_required" on top of the todolist function.
 ``` shell
@login_required(login_url='/todolist/login/')
def todolist(request):
......
 ```
9. Make a function so that when a button is pressed on the todolist page, it will open another page and create a task for you.
```
def create_task(request):
    if request.method == "POST":
        user = request.user
        title = request.POST.get("title")
        description = request.POST.get("description")
        create = TaskItem(user = user,date = datetime.datetime.now(), title = title, description = description )
        create.save()
        return redirect('todolist:todolist')
    return render(request, 'create.html')
```
10. Lastly, deploy your app on the heroku page.




# WEEKLY ASSIGNMENT 05
- [Main](https://weeklyassignment02.herokuapp.com/)
- [Katalog](https://weeklyassignment02.herokuapp.com/katalog/)
- [mywachlist](https://weeklyassignment02.herokuapp.com/mywatchlist/)
- [todolist](https://weeklyassignment02.herokuapp.com/todolist)


## What is the difference between Inline, Internal, and External CSS? What are the advantages and disadvantages of each style?
<br>
 - For Inline,it is used to style a specific HTML element. To apply this CSS style, simply add the style attribute to each HTML tag 
without using selectors. The example is like this:

```shell
<div class="card" style="background-color: #15a83a91;">
```
- For Internal, it is required to add style tag in the head section of your HTML document.
  This CSS style is an effective method of styling a single page. However, if you do need to style multipage it will consume a lot of time.
  Example of an Internal style. 

```shell
<style>
    body {
        font-family: sans-serif;
        display: grid;
        justify-content: center;
        align-items: center;
        color: #586e75;
    }
</style>
```
- For External, you’ll link your web pages to an external .css file. It will be more efficient, especially for styling a large website. You can change
the entire site with a single file of css. Example:
Add these on top of the html page.

```shell
<link rel="stylesheet" href="styles.css">
```
Then, you can style it with an external css file.


## Describe the HTML5 tags that you know
- h1 to h6 : Defines HTML headings
- p        : Defines a paragraph.
- body     : Defines the document's body.
- br       : Produces a single line break.
- footer   : Represents the footer of a document or a section.
- head     : Defines the head portion of the document that contains information about the document such as title.
- script   : Places script in the document for client-side processing.
- title    : Defines a title for the document.
- ul       : Defines an unordered list.
- button   : Creates a clickable button.
And many more...

## Describe the types of CSS selectors you know
- id selector        : uses the id attribute of an HTML element to select a specific element.
- class selector     : selects elements with a specific class attribute.
- Element Selector   : selects HTML elements based on the element name.
- Universal Selector : universal selector selects all HTML elements on the page.
- Grouping Selector  : selects all the HTML elements with the same style definitions.


## IMPLEMENTATION

1. Import the Bootsrap framework inside the HTML
```shell
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js"></script>
```
2. Customize the Login, Register and create task page as attractive as possible using the css styling.
```shell
<style>
Insert your styling here......
</style>
```
3.  Customize the main page todo list using cards.
For this page, we can use the for loop on top of the card div and ends at the bottom of the card div. Just put in the mdoels and the card will be added automatically
by the for loop 
```shell
<div class="wrapper">
{% for task in todolist %}
	<section>
		<div class="container">
            {% if task.is_finished %} 
            <div class="card" style="background-color: #15a83a91;">
                <div class="content">
                <div class="imgBx">
                    <img src="https://www.pngall.com/wp-content/uploads/5/Green-Checklist.png">
                </div>
                     {% else %} 
                     <div class="card" style="background-color: #b1050591;">
                        <div class="content">
                            <div class="imgBx">
                                <img src="https://gra.gov.gh/wp-content/uploads/2021/10/GRA-Not-Recruiting.png">
                            </div>           
                     {% endif %}
 					<div class="contentBx">
						<h3>{{task.title}}<br><span>{{task.description}}</span><br><span>{{task.date}}</span></h3>
					</div>
				</div>
                <button class ="status"><a href="{% url 'todolist:change_status' id=task.id%}">Change Status</a></button>
                <button class ="status"><a href="{% url 'todolist:delete_task' id=task.id%}">Delete</a></button>
                
        </div>
    </div>
  </section>
  {% endfor %}
</div>
```

4. Make all the page responsive by using pseudo code like ::focus or ::hover to make it look attractive.
