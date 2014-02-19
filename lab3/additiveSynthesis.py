import array
import contextlib
import wave
from math import sin, pi

# Global parameters

numChannels = 1                      # mono
sampleWidth = 2                      # in bytes, a 16-bit short
sampleRate = 44100
#MAX_AMP = 2**(8*sampleWidth - 1) - 1 #maximum amplitude is 2**15 - 1  = 32767 

# Take an array of shorts and write it out to a mono wave file

def writewav(fname, data, params):
    with contextlib.closing(wave.open(fname, "w")) as f:
        f.setparams(params)
        f.writeframes(data.tostring())
    print(fname + " written.")
    

def main():

    # parameters for this file

    timFileName = raw_input("Enter the name of the timbre .tim.txt file: ")
    envFileName = raw_input("Enter the name of the envelope .env.txt file: ")
    #outfileName = raw_input("Enter the name of the output .wav file: ")


    data = array.array("h")

    # read the timbre file to get the frequency and relative factor about amuplitude
    timFile = open(timFileName,"r")
    item = timFile.readline()

    i = 0
    freq =[]
    fact =[]
    while('' != item):
        (freq[i],fact[i]) = item.rstrip().split('\t')
        item = timFile.readline()
        i += 1
    timFile.close()

    for j in range(0,i-1):
        print(freq[j]+"\t"+fact[j]+"\n")

    envFile = open(envFileName,"r")
    ampLeft = envFile.readline()
    ampRight = envFile.readline()
    windowSize = int(sampleRate * ampRight)
    print(str(windowSize))
    i = 0
    #while ('' != ampRight)
    #   for j in range(0,windowSize):
    #       
    #       sample = MAX_AMP * sin( 2 * pi * 440.0 * i / sampleRate ) 

    #    data.append( int( sample ) )


    #params = [numChannels, sampleWidth, sampleRate , len(data), "NONE", None]
    #writewav(outfileName, data, params)
    envFile.close()

main()