# WEEKLY ASSIGNMENT 06
- [Main](https://weeklyassignment02.herokuapp.com/)
- [Katalog](https://weeklyassignment02.herokuapp.com/katalog/)
- [mywachlist](https://weeklyassignment02.herokuapp.com/mywatchlist/)
- [todolist](https://weeklyassignment02.herokuapp.com/todolist/login/)

## Describe the difference between asynchronous programming with synchronous programming ?
Synchronous: In Synchronous Transmission,Frames or blocks of data are sent. Full-duplex transmission is being used here. Synchronization between the sender and receiver is necessary.
There is no lag in synchronous transmission when it comes to data.

Asynchronous: In Asynchronous Transmission, Data is transmitted as either bytes or characters. Half-duplex transmission is the type used in this. Start bits and stop bits are combined with the data in this transmission.
It doesn't need to be synchronized.
<br>
<br>
##  Explain Event-Driven Programming ?
The goal of event-driven programming is to keep the program as straightforward as possible while synchronizing the occurrence of numerous events. 
These are the fundamental elements of an event-driven program:
- When an event is triggered, a callback function (also known as an event handler) is invoked.
- an event loop that calls the appropriate event handler for each event as it is triggered.
<br>
<br>

## Describe the implementation of asynchronous programming in AJAX
Asynchronous Javascript & XML (AJAX) is a set of web technologies that execute without interfering with or reloading the website's current state and send and receive data from a client end server asynchronously.
AJAX is not a programming language, framework, or library.




## IMPLEMENTATION
1. Make a function on "views.py" to show the json
```shell
@login_required(login_url='/todolist/login/')
def todolist_json(request):
    data_task = TaskItem.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data_task), content_type="application/json")
```
2. Make a routing on "urls.py" for the json
```shell
path('json/', todolist_json, name='todolist_json'),
```
4. Import the jquery inside the html inside the todolist html file
```shell
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
```
5. Add the get and post function inside the script tag, example:
```shell
function create() {
        const form = $(".create_task");
        $.ajax({
            type: "POST",
            url: "/todolist/create_task/",
            data: form.serialize(),
        }).done(function (data) {
            form.trigger("reset");
            get_task();
        });
        $("#staticBackdrop").modal("hide");
    }
```
6. Add the url inside the function to call the function on "views.py"
```shell
url: "/todolist/create_task/", 
```
7. Create a modal inside the html file
