# WEEKLY ASSIGNMENT 03
- [Main](https://weeklyassignment02.herokuapp.com/)
- [Katalog](https://weeklyassignment02.herokuapp.com/katalog/)
- [mywachlist](https://weeklyassignment02.herokuapp.com/mywatchlist/)
- [todolist](https://weeklyassignment02.herokuapp.com/todolist)
- 
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
## Describe the data flow process from the submission made by the user through the HTML form, data storage in the database, until the appearance of the data that has been stored in the HTML template.
After the user pressed the submit button inside the html, the data that is inputed by the user will be processed
into the function inside views.py. The inputted data will be accessed by the code ``request.POST.get("input name")``. Then we can save the database with save(). This is the
example of the code,
```shell
title = request.POST.get("title")
        description = request.POST.get("description")
        create = TaskItem(user = user,date = datetime.datetime.now(), title = title, description = description )
        create.save()
```

## IMPLEMENTATION
