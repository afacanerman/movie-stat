#!/usr/bin/python

import getopt
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
        print 'option is' + opt
        if opt == '-h':
            print 'test.py -p <moviePath>'
            exit()

        elif opt in ("-p", "--path"):
            moviepath = arg

    print moviepath
    if moviepath is '':
        print 'test.py -p <moviepath> : -p parameter is must!'
        exit(2)

    dm = DirectoryManager(moviepath)
    print dm.get_movie_directories()


if __name__ == "__main__":
    main(argv[1:])