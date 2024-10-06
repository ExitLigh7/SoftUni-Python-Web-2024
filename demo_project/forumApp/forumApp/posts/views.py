from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        "current_time": datetime.now(),
        "person":{
            "age": 20,
            "height": 190,
        },
        "ids": ["564", "758", "926"],
        "some_text": "Hello my name is Dimitar, and I want to be developer",
        "users": [
            "Pesho",
            "Ivan",
            "Stamat",
            "Maria",
            "Gosho"
        ]
    }

    return render(request, 'base.html', context)

def dashboard(request):
    context = {
        "posts":[
            {
                "title" : "How to create django project",
                "author" : "Dimitar Georgiev",
                "content" : "I am **learning** Django",
                "created_at" : datetime.now (),
            },

            {
                "title" : "How to create django project1",
                "author" : "",
                "content" : "I am learning Django",
                "created_at" : datetime.now (),
            },

            {
                "title" : "How to create django project2",
                "author" : "Dimitar Georgiev",
                "content" : "",
                "created_at" : datetime.now (),
            }
        ]
    }

    return render(request, "posts/dashboard.html", context)