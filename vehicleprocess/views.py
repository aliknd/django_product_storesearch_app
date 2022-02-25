import json
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.shortcuts import redirect

from vehicleprocess.models import Car

class Home(TemplateView):
    template_name = 'home.html'

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        # save json file in media folder
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        # reading data from json file
        with open(f"./jsons/{uploaded_file.name}", encoding="utf-8") as file:
            data = json.load(file)

        for item in data:
            c, new = Car.objects.get_or_create(**item)
            # check if there is any equivalent instance in DB:
            if not new:
                print("Entry already in the DB:")
                print(c)
    fresponse = redirect('/search-carsmodel')
    return fresponse

def search_carsmodel(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        # split the data based on white space and turn them into an array
        search_str_array = search_str.split()
        for x in search_str_array:
            # filtering the data based on the received array
            carsmodel = Car.objects.filter(
                make__istartswith=x) | Car.objects.filter(model__istartswith=x)
        data = carsmodel.values()
        return JsonResponse(list(data), safe=False)

    # Doing pagination
    cars_queryset  = Car.objects.all()
    p = Paginator(cars_queryset, 50)
    page = request.GET.get('page')
    cars_list = p.get_page(page)

    content = {
        'object_list' : cars_list,
    }

    return render(request, 'upload.html', content)