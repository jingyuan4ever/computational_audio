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

    #timFileName = raw_input("Enter the name of the timbre .tim.txt file: ")
    #envFileName = raw_input("Enter the name of the envelope .env.txt file: ")
    outfileName = raw_input("Enter the name of the output .wav file: ")
    
    timFileName = 'timbre.tim.txt'
    envFileName = 'sinusoid.env.txt'


    data = array.array("h")

    # read the timbre file to get the frequency and relative factor about amuplitude
    timFile = open(timFileName,"r")
    item = timFile.readline()

    i = 0
    freq =[]
    fact =[]
    while('' != item):
        (freq0,fact0) = item.rstrip().split('\t')
        freq.append(freq0)
        fact.append(fact0)
        item = timFile.readline()
        i += 1
    timFile.close()

    envFile = open(envFileName,"r")
    ampLeft = envFile.readline().rstrip().split('\t')[1]
    line = envFile.readline()
    windowTime,ampRight = line.rstrip().split('\t')
    windowSize = int(sampleRate * float(windowTime))

    i = 0
    while (line):
        ampRight = line.rstrip().split('\t')[1]
        for j in range(0,windowSize):
            amp = (float(j) / windowSize) * int(ampRight) + (1 - (float(j) / windowSize)) * int(ampLeft)
            sample = 0
            for k in range(0,len(freq)):
                sample += float(fact[k]) * amp * sin( 2 * pi * float(freq[k]) * (i+j) / sampleRate ) 
            data.append( int( sample ) )
        
        i += windowSize
        ampLeft = ampRight
        line = envFile.readline()


    params = [numChannels, sampleWidth, sampleRate , len(data), "NONE", None]
    writewav(outfileName, data, params)
    envFile.close()

main()