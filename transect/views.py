# transect/views.py
import os
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, Http404
import aiohttp
from .forms import ImageForm
from .custom_storage import MediaStorage
from json import loads, JSONDecodeError, dumps

api_link = 'https://thegreatleapforward.pythonanywhere.com/'
formats = (
    'apng', 'avif', 'gif', 'jpeg', 'png', 'svg', 'webp'
)


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
    return render(request, 'transect/upload.html', context={'domain': request.get_host()})


async def api(request):
    if request.method != "POST":
        raise Http404
    '''
    try:
        body = loads(request.body.decode())
        nodes = body['markers']
        obvs = body['observations']
        date = body['date']
    except JSONDecodeError | KeyError as e:
        return HttpResponse(str(e), status=400)

    print(f'{nodes=}, {obvs=}, {date=}')
    body = {
        "name": "Unnamed",
        "user": 1,
        "date": date,
        "nodes": [{"latitude": node['lat'], "longitude": node['lng'], "index": i}
                  for i, node in enumerate(nodes)],
        "observations": [{"latitude": obv['lat'], "longitude": obv['lng'], "species": None, "date_offset": 0, "images": [{"url": obv['url']}]}
                         for obv in obvs]
    }
'''
    async with aiohttp.ClientSession(api_link) as session:
        async with session.post('/transects', json=request.body.decode(), headers={'Content-Type': 'application/json'}) as response:
            pass#data = await response.json()
    #print(data)

    return HttpResponse(status=200)


async def transect(request, transect_id):
    data = await get(f'transects/{transect_id}')

    return render(request, 'transect/transect.html', context={'data': data})


def test(request):
    return render(request, 'transect/test.html', context={"gaming": "six"})


async def observations(request):
    data = await get('observations')

    return render(request, 'transect/observations.html', context={'data': data})


def upload_popup(request, lat, lng):
    url = error = ''
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            file_obj = form.files.get('img', None)
            if not file_obj.name.endswith(formats):  # Incorrect filetype
                error = f'{file_obj.name} is invalid filetype'
            else:
                path = 'images/'
                full = os.path.join(path, file_obj.name)
                media = MediaStorage()

                if media.exists(full):  # Image already exists
                    error = f'image {file_obj.name} already exists'
                else:
                    media.save(full, file_obj)
                url = media.url(full).split('?')[0]  # remove api key
        else:  # Form not valid
            error = f'no file'

    print(f'{request.method} = {url}')

    try:
        lat = float(lat)
        lng = float(lng)
    except ValueError:
        raise Http404("Value Error")

    return render(request, 'transect/upload_popup.html',
                  context={'latitude': lat, 'longitude': lng, 'form': ImageForm(), 'preview': url, 'error': error})
