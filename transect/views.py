# transect/views.py
import json
from datetime import datetime
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
import aiohttp

api_link = 'https://thegreatleapforward.pythonanywhere.com/'


async def get(uri):
    async with aiohttp.ClientSession() as session:
        async with session.get(api_link + uri) as response:
            data = await response.json()

    return data


def index(request):
    now = datetime.now()
    return render(request, 'transect/index.html', context={'now': now})


async def observation(request, obvs_id):
    data = await get(f'observations/{obvs_id}/')
    return render(request, 'transect/observation.html', context={**data})


def upload(request):
    return render(request, 'transect/upload.html')


def api(request):
    return render(request, 'transect/api.html')


async def transect(request, transect_id):
    data = await get(f'transects/{transect_id}')

    return render(request, 'transect/transect.html', context={'data': data})


def test(request):
    return render(request, 'transect/test.html', context={"gaming": "six"})


async def observations(request):
    data = await get('observations')

    return render(request, 'transect/observations.html', context={'data': data})
