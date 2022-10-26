import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open(BUS_STATION_CSV) as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    paginator = Paginator(data, 8)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': data,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
