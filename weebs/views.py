from django.shortcuts import render
import requests
# Create your views here.
import json
from django.http import JsonResponse

def home(request):

    return render(request,'home.html')


def by_character(request,word):
    url = "https://animechan.vercel.app/api/quotes/character?name={character}".format(character=word)
    response = requests.get(url)
    print("Status Code", response.status_code)
    print(word)
    print("JSON Response ", response.json())
    return JsonResponse(response.json(),safe=False)

def by_anime(request,anime):
    url = "https://animechan.vercel.app/api/quotes/anime?title={title}".format(title=anime)
    response = requests.get(url)
    print("Status Code", response.status_code)
    print(anime)
    print("JSON Response ", response.json())
    return JsonResponse(response.json(),safe=False)

