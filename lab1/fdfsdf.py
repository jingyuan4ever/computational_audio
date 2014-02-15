# Example of reading a WAV file using the Python wave library

import array
import wave                       # The main library for manipulating wave files

# Significant parameters
fileName = 'mono.wav'

# open wave file for reading
waveFile = wave.open(fileName, 'r')

# get the parameters
(numChannels, sampleWidth, sampleRate, numFrames, compressionType, nameOfCompression) = waveFile.getparams()

# how many frames to read each loop iteration?
numFramesToRead = 1

for i in range(0, numFrames):
    # in mono, frame will have one sample, in stereo, two
    frame = waveFile.readframes(numFramesToRead)

    # unpack binary string into array of ints
    data = array.array('h', frame)

    print(data[0])          #  for mono
    # print(data[0], data[1])   # for stereo, left then right

waveFile.close()

    