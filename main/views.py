from django.shortcuts import render
from .info import *

cli = {
    "name": "Command line tools",
    "list": cli_projects
}

web = {
    "name": "Web Apps",
    "list": web_projects
}

games = {
    "name": "2D Games",
    "list": game_projects
}

all_projects = [web, cli, games]

awards = [award1, award2]


def index(request):
    return render(request, "main/index.html", {
        "info": info,
        "about": about,
        "likes": likes,
        "skills": skills,
        "tools": tools,
        "all_projects": all_projects,
        "awards": awards,
        "social": social,
        "github": github
    })
