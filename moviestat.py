#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import urllib2
import getopt
from Movie import Movie
from DirectoryManager import DirectoryManager
from sys import argv, exit


def main(argv):
    moviepath = ''

    try:
        opts, args = getopt.getopt(argv, 'hp:', ['-path'])
    except getopt.GetoptError:
        print 'test.py -p <inputfile>'
        exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -p <moviePath>'
            exit()

        elif opt in ("-p", "--path"):
            moviepath = arg

    if moviepath is '':
        print 'test.py -p <moviepath> : -p parameter is must!'
        exit(2)


    print '\n'
    dm = DirectoryManager(moviepath)
    movie_list = dm.get_movie_directories()

    for movie_name in movie_list:
        movie_info = urllib2.urlopen(dm.getApiUrlFor(movie_name))
        
        decoded_data = json.loads(movie_info.read())
        
        if not "Error" in decoded_data: 
            movie = Movie(**decoded_data)
            dm.rename_directory(movie_name, movie)
            
            print "           Info: {{ %s }} - movie information has been found and replacing directory name" % (movie_name)
        else:
            print  "          Error: {{ %s }} - could not found!" % (movie_name)

    print "           --------------------------------------------------------------------------------------------------------"
    print "         /"
    print "(\__/)  /"
    print "(='.'=)"
    print "('')('')"

if __name__ == "__main__":
    main(argv[1:])