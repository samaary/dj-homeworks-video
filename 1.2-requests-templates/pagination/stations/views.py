from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv
from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))

CONTENT = []
with open(BUS_STATION_CSV, encoding='utf-8', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        CONTENT.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})

def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    page_number = int(request.GET.get('page', 1))
    # также передайте в контекст список станций на странице
    paginator = Paginator(CONTENT, 50)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
