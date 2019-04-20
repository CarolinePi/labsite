from django.shortcuts import render, HttpResponse, redirect
from .forms import TvForm, FridgeForm
from .models import TvModel, FridgeModel
from django.views.decorators.csrf import csrf_exempt
from .db import update_fridge_clicks, update_tv_clicks


# Create your views here.
def home(request):
    return render(request, 'appliances/home.html')

# use_required_attribute=False


def add_new(request):
    form_fridge = FridgeForm(request.POST, request.FILES, prefix='fridge_form')
    form_tv = TvForm(request.POST, request.FILES, prefix='tv_form')
    if form_fridge.is_valid() and request.method == 'POST':
        print('tv' + str(form_fridge.data))
        form_fridge.save()
        return redirect('new')
    elif form_tv.is_valid() and request.method == 'POST':
        print('fr' + str(form_tv.data))
        form_tv.save()
        return redirect('new')

    return render(request, 'appliances/add_new.html', {'form_tv': form_tv,
                                                       'form_fridge': form_fridge})


def tv(request):
    tv_posts = TvModel.objects.all()
    return render(request, 'appliances/tv.html', {'tv_posts': tv_posts})


def fridge(request):
    fridge_posts = FridgeModel.objects.all()
    return render(request, 'appliances/fridge.html', {'fridge_posts': fridge_posts})


@csrf_exempt
def receiver(request):
    if request.method == 'POST' and request.is_ajax():
        json_string = dict(request.POST)
        if json_string['db'][0] == 'appliances_fridgemodel':
            update_fridge_clicks(*json_string['id'], *json_string['clicks'])
        elif json_string['db'][0] == 'appliances_tvmodel':
            update_tv_clicks(*json_string['id'], *json_string['clicks'])
    return redirect('fridge')
