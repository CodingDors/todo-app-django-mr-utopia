from django.shortcuts import render

tasks = []

# Create your views here.
def index(request):
    # TODO: GET method - improve this function to send the tasks list to the HTML file
    return render(request, "tasks/index.html")

    # TODO: POST method - handle the submission of new tasks and redirect to index function
