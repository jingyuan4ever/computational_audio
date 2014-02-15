# File: readWave.py
# Author: Wayne Snyder
# Date: 1/5/14
# Description: This is a prototypical Python 3 program for reading and processing
#   a wave file. It reads in the entire input file into an array of shorts, which can then be
#   analyzed or processed as needed.
#   If you want to use this with Python 2.7, just change the input to raw_input in main().
# Citation: This is a modified version of a program from A Concise Introduction
#    to Programming in Python.


import array
import contextlib
import wave
import math


def maxAbsolute(a):
    return max(map(abs, a))


def average(a):
    return float(sum(a))/len(a)


def stdDeviation(a):
    l = len(a)
    m = sum(a) / float(l)
    d = 0.0
    for i in a:
        d += (i - m) ** 2
    return (d / l) ** 0.5


# Read a wave file and return the entire file as an array, and the parameters
# Parameters are:  (numChannels, sampleWidth, sampleRate, numFrames, not-used, not-used)

def readwav(fname):
    with contextlib.closing(wave.open(fname)) as f:
        params = f.getparams()
        frames = f.readframes(params[3])
    return array.array("h", frames), params


def main():
    n = 882
    k = 441

    infileName = raw_input("Enter the name of the input .wav file: ")

    # Next, get all the samples as an array of short, and the parameters as a
    # tuple (numChannels, sampleWidth, sampleRate, numFrames, not-used, not-used)

    data, params = readwav(infileName)

    #  Example: find the maximum value in the samples

    i = 0
    while True:
        window = data[i * k: i * k + n]
        print "maxAbsoluteValue\t:%d" % maxAbsolute(window)
        print "average\t:%f" % average(window)
        print "stdDeviation:\t%f" % stdDeviation(window)
        i += 1
        if len(window) < n:
            break



main()