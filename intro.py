import nltk
from nltk import tokenize
from nltk import sent_tokenize

import geotext
from geotext import GeoText

import geopy
from geopy import Nominatim

import simplekml
import csv


def hello():
    print("Working on it...")

def createKML(list):
    geolocator = Nominatim()

    kml = simplekml.Kml()
    #inputfile = csv.reader(open('ontheroad.csv', 'r'))

    for entry in list:
        location = geolocator.geocode(entry)
        if location:
            point = kml.newpoint(name=entry, coords=[(location.longitude, location.latitude)])
            point.description = "point description is a go!"

    kml.save("ontheroad.kml")

def makePlaces(list):
    createKML(list)
    return list

def pullStuff(file):
    t = open(file, encoding='utf8')
    raw = t.read()
    words = nltk.word_tokenize(raw)
    sents = nltk.sent_tokenize(raw)
    sents = [nltk.word_tokenize(sent) for sent in sents]
    sents = [nltk.pos_tag(sent) for sent in sents]
    places = GeoText(raw)
    return makePlaces(list(set(places.cities)))



if __name__ == '__main__':
    hello()
    print(pullStuff('ontheroad.txt'))
    exit()