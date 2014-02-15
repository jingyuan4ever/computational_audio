# Example of creating a mono WAV file using the Python wave library

from struct import pack           # This creates the binary data structure for frames
from math import sin, pi
import wave                       # The main library for manipulating wave files

# Significant parameters
fileName = 'sinusoid.wav'
numberChannels = 1     # mono
sampleWidth = 2        # in bytes, so this is a 16-bit int (a short in C)
sampleRate = 44100
lengthSeconds = 6      # how long the file is in seconds


def calculateFrame(amplitude, frequency, i):
    return amplitude * sin(2 * pi * frequency * i / sampleRate)

# dependent variables

#maximum amplitude is 2**15 - 1  = 0111 1111 1111 1111 = 32767
maxAmplitude = 2 ** (8 * sampleWidth - 1) - 1.0      # keep this a float

# open wave file for writing
waveFile = wave.open(fileName, 'w')

#    setparams(nchannels, sampleWidth (in bytes), sampleRate, numFrames, compressionType, nameOfCompressionType)
#      last two parameters not supported, leave as shown
#      numFrames is 0 for now and will be updated later
waveFile.setparams((numberChannels, sampleWidth, sampleRate, 0, 'NONE', 'not compressed'))

waveData = ""       # this holds the data to be written to file in binary form

# now we write 3 seconds worth of frames

for i in range(0, sampleRate * lengthSeconds):
# for i in range( 0, 10 ):

    #  2 * pi * frequency is the angular velocity in radians/sec
    #  multiplying this by i / sampleRate incrementally creates angle at each sample
    #  and then sin ( angle ) => amplitude at this sample
    frame = calculateFrame(maxAmplitude / 2, 440, i) + calculateFrame(maxAmplitude / 4, 880, i) + calculateFrame(
        maxAmplitude / 8, 1760, i) + calculateFrame(maxAmplitude / 8, 3520, i)

    # pack frame into short int (format 'h') in binary
    waveData += pack('h', frame)

    # if want to see samples, uncomment this
    # print( frame )

# write the frames; this will automatically update the number of frames in numFrames
waveFile.writeframes(waveData)
waveFile.close()

