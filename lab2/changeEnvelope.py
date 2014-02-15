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

def writewav(fname, data, params):
    with contextlib.closing(wave.open(fname, "w")) as f:
        f.setparams(params)
        f.writeframes(data.tostring())
    print(fname + " written.")

def main():

    infileName = raw_input("Enter the name of the input .wav file: ")
    enfileName = raw_input("Enter the name of the envelope .env.txt file: ")
    outfileName = raw_input("Enter the name of the output .wav file: ")

# Next, get all the samples as an array of short, and the parameters as a 
# tuple (numChannels, sampleWidth, sampleRate, numFrames, not-used, not-used)

    data, params = readwav(infileName)

    envFile = open(enfileName,"r")

    maxEnv = envFile.readline()
    windowSize = 882
    i = 0
    
    while ('' != maxEnv) and (i < len(data)):
        maxValue = 0
        for j in range(0,windowSize):
            if i+j < len(data):
                if abs(data[i+j]) > maxValue:
                    maxValue = abs(data[i+j])
        maxEnv = float(maxEnv)
        for j in range(0,windowSize):
            if i+j < len(data):
                print '1:maxEnv:%f, maxValue:%d, data:%d'%(maxEnv, maxValue, data[i+j])
                data[i+j] = int(maxEnv / maxValue * data[i+j])
                print '2:maxEnv:%f, maxValue:%d, data:%d'%(maxEnv, maxValue, data[i+j])


        maxEnv = envFile.readline()
        i +=windowSize

    writewav(outfileName, data, params)
    envFile.close()

main()