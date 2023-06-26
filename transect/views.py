# transect/views.py
import json
from datetime import datetime
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
import aiohttp


def index(request):
    now = datetime.now()
    return render(request, 'transect/index.html', context={'now': now})


async def observation(request, obvs_id):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://thegreatleapforward.pythonanywhere.com/observations/{obvs_id}/?format=json') as response:
            data = await response.json()

    return render(request, 'transect/observation.html', context={**data})


def upload(request):
    return render(request, 'transect/upload.html')


def api(request):
    return render(request, 'transect/api.html')


async def transect(request, transect_id):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://thegreatleapforward.pythonanywhere.com/transects/{transect_id}') as response:
            data = await response.json()

    return render(request, 'transect/transect.html', context={'data': data})

def test(request):
    return render(request, 'transect/test.html', context={"gaming": "six"})


def browse(request):
    return render(request, 'transect/browse.html')
