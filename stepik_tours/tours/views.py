import random

from django.http import HttpResponseNotFound
from django.shortcuts import render

from .data import tours, departures, title, subtitle, description


def main_view(request):
    random_tours = dict(random.sample(tours.items(), k=6))
    return render(request, 'index.html', context={'departures': departures,
                                                  'tours': random_tours,
                                                  'title': title,
                                                  'subtitle': subtitle,
                                                  'description': description})


def departure_view(request, departure):
    if departure not in departures:
        return HttpResponseNotFound('<h1>Страница не найдена</h1>')
    else:
        departure_tours = {}
        tours_id = []
        for tour_id, tour in tours.items():
            if tour['departure'] == departure:
                tours_id.append(tour_id)

        for tour_id, tour in tours.items():
            if tour_id in tours_id:
                departure_tours.update({tour_id: tour})

        dep = departures[departure]
        amount = len(departure_tours)

        price = []
        nights = []
        for tour in departure_tours.values():
            price.append(tour['price'])
            nights.append(tour['nights'])

        min_price, min_nights = min(price), min(nights)
        max_price, max_nights = max(price), max(nights)

        return render(request, 'departure.html', context={'tours': departure_tours,
                                                          'departures': departures,
                                                          'dep': dep,
                                                          'amount': amount,
                                                          'min_price': min_price,
                                                          'max_price': max_price,
                                                          'min_nights': min_nights,
                                                          'max_nights': max_nights})


def tour_view(request, tour_id):
    if tour_id in tours:
        tour = tours.get(tour_id)
        dep = departures[tour['departure']]
        return render(request, 'tour.html', context={'tour': tour,
                                                     'departure': dep,
                                                     'departures': departures,
                                                     'tour_id': tour_id})
    else:
        return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
