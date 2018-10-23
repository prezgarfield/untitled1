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

def createKML(list, raw):
    geolocator = Nominatim()

    kml = simplekml.Kml()
    #inputfile = csv.reader(open('ontheroad.csv', 'r'))

    for entry in list:
        location = geolocator.geocode(entry)
        if location:
            wordloc = raw.find(entry)
            point = kml.newpoint(name=entry, coords=[(location.longitude, location.latitude)])
            #needs out of bounds error check for character number
            if wordloc > -1:
                description = raw[wordloc - 300: wordloc + 300]
                point.description = "..." + description + "..."
            else:
                point.description = "Error retrieving text"

    kml.save("ontheroad.kml")

def makePlaces(list, raw):
    createKML(list, raw)
    return list

def pullStuff(file):
    t = open(file, encoding='utf8')
    raw = t.read()
    words = nltk.word_tokenize(raw)
    sents = nltk.sent_tokenize(raw)
    sents = [nltk.word_tokenize(sent) for sent in sents]
    sents = [nltk.pos_tag(sent) for sent in sents]
    places = GeoText(raw)
    listn = list(set(places.cities))
    return makePlaces(listn, raw)



if __name__ == '__main__':
    hello()
    print(pullStuff('ontheroad.txt'))
    exit()