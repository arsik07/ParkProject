from django.db import models
from django.shortcuts import render
from googleplaces import GooglePlaces, types, lang
from .models import Photo, Park, Review
from itertools import islice
from django.http import JsonResponse
import time

google_api_key = 'AIzaSyCxXyUAfR3gpbBowNNUlBb0CCaxqz5aU2c'
max_height = 1200
max_width = 1000
number_of_photos=7
number_of_reviews=100

def start_page(request):
    queries = ['парк развлечений казань', 'кинотеатр казань', 'парк казань', 'аттракционы казань', 'аквапарк казань']
    google_places = GooglePlaces(google_api_key)
    '''Park.objects.all().delete()
    Photo.objects.all().delete()
    Review.objects.all().delete()
    for q in queries:
        try:
            query_result = google_places.text_search(query=q, radius=10000, language=lang.RUSSIAN)
            time.sleep(1)
            for place in query_result.places:
                place.get_details()
                time.sleep(1)
                park = Park(title=place.name, rating=place.rating, website=place.website, formatted_address=place.formatted_address)
                park.save()
                try:
                    iterator = islice(place.photos, number_of_photos)
                    for p in iterator:
                        p.get(maxheight=max_height, maxwidth=max_width)
                        if Photo.objects.filter(photourl=p.url).exists():
                            continue
                        else:
                            ph = Photo.objects.create(photourl=p.url)
                            ph.save()
                            park.photos.add(ph) #here
                        park.save()
                except Exception as e:
                    print('Photos exception', e)
                    pass
                try:
                    iterator = islice(place._details['reviews'], number_of_reviews)
                    for r in iterator:
                        if Review.objects.filter(review_text=r['text']):
                            continue
                        else:
                            rev = Review.objects.create(review_text=r['text'])
                            rev.save()
                            park.reviews.add(rev)
                        park.save()
                except Exception as e:
                    print('Review exception: ', e)

                park.save()
                print('Details: ')
                print(place._details)
                print()
        except Exception as e:
            print(e)
            print('Произошла ошибка!')'''
    all_parks = Park.objects.all()
    return render(request, 'park/park_list.html', {'all_parks':all_parks})

def places(request):
    all_parks = Park.objects.all()
    return render(request, 'park/places.html', {'all_parks':all_parks})


def place_details(request, park_id):
    park = Park.objects.get(id=park_id)
    return render(request, 'park/place_details.html', {'park': park})

def get_review_marks(request):
    reviews = Review.objects.all()
    for rev in reviews:
        print(rev.review_text)
        try:
            blob = TextBlob(rev.review_text)
            blob = blob.translate(to='en')
            if blob.sentiment.polarity > 0:
                rev.mark = True
                print(blob.sentiment.polarity)
                print('yes')
            else:
                rev.mark = False
                print(blob.sentiment.polarity)
                print('no')
            rev.save()
        except:
            continue
    return JsonResponse({})


