import array
import contextlib
import wave
from math import sin, pi

def createWave(n,a,f,p):
	sinWave = []
	for i in range (0,n):
		t = a * sin( 2 * pi * f * (i / (n * f) + p)
		sinWave.append(float(t))
	return sinWave

def DFT(x):

def addWaves(a,b):

def printRawSpectrum(X):

def printFullSpectrum(X):

def printSpectrum(X):

def main():

	test = createWave(10,1.0,1.0,0.0)
	for i in range(len(test)):
		print(str(test[i])+"\n")

main()