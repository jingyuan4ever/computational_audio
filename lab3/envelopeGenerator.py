import array
import contextlib
import wave
import math

# Read a wave file and return the entire file as an array, and the parameters
# Parameters are:  (numChannels, sampleWidth, sampleRate, numFrames, not-used, not-used)

def readwav(fname):
    with contextlib.closing(wave.open(fname)) as f:
        params = f.getparams()
        frames = f.readframes(params[3])
    return array.array("h", frames), params

def main():

    infileName = raw_input("Enter the name of the input .wav file: ")
    windowSize = raw_input("Enter the size of the window: ")

# Next, get all the samples as an array of short, and the parameters as a 
# tuple (numChannels, sampleWidth, sampleRate, numFrames, not-used, not-used)

    data, params = readwav(infileName)

    outfileName = infileName.split('.',1)[0]+'.env.txt'
    outFile = open(outfileName,"w")

    outFile.write("%f\t%d\n"%(0.0,0))

    i = 0
    windowSize = int(windowSize)
    n = windowSize
    numWindow = len(data)/windowSize
    for i in range(1, numWindow):
        timeStamp = n/float(params[2])
        outFile.write("%f\t%d\n"%(timeStamp,data[n]))
        n += windowSize
    outFile.close()

main()