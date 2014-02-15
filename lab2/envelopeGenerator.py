import array
import contextlib
import wave
import math


def maxAbsolute(a):
    return max(map(abs, a))

# Read a wave file and return the entire file as an array, and the parameters
# Parameters are:  (numChannels, sampleWidth, sampleRate, numFrames, not-used, not-used)

def readwav(fname):
    with contextlib.closing(wave.open(fname)) as f:
        params = f.getparams()
        frames = f.readframes(params[3])
    return array.array("h", frames), params


def main():
    infileName = raw_input("Enter the name of the input .wav file: ")
    outfileName = infileName.split('.', 1)[0] + '.env.txt'
    k = n = input("Enter the window size: ")

    f = open(outfileName, 'w')
    f.write("%d\n" % n)
    data, params = readwav(infileName)

    i = 0
    while True:
        window = data[i * k: i * k + n]
        f.write("%d\n" % maxAbsolute(window))
        i += 1
        if len(window) < n:
            break
    f.close()


main()