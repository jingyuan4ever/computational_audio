from struct import pack           # This creates the binary data structure for frames
from math import sin, pi
import wave


# Example of creating a mono WAV file using the Python wave library
                   # The main library for manipulating wave files

# Significant parameters
fileName = raw_input('Please input file name:')
waveType = raw_input('Please input wave type[mono or stereo]:')
numberChannels = 1
if waveType == 'stereo':
    numberChannels = 2     # mono
sampleWidth = 2        # in bytes, so this is a 16-bit int (a short in C)
sampleRate = 44100
frequency = 440.0     # keep this a float so calculation below is floating-point
lengthSeconds = 3      # how long the file is in seconds
lengthSeconds = input('Please input length of file (seconds)')

# dependent variables

#maximum amplitude is 2**15 - 1  = 0111 1111 1111 1111 = 32767
maxAmplitude = 2**(8*sampleWidth - 1) - 1.0      # keep this a float

# open wave file for writing
waveFile = wave.open(fileName, 'w')

#    setparams(nchannels, sampleWidth (in bytes), sampleRate, numFrames, compressionType, nameOfCompressionType)
#      last two parameters not supported, leave as shown
#      numFrames is 0 for now and will be updated later
waveFile.setparams((numberChannels, sampleWidth, sampleRate, 0, 'NONE', 'not compressed'))

waveData=""       # this holds the data to be written to file in binary form

# now we write 3 seconds worth of frames

for i in range( 0, sampleRate * lengthSeconds ):

        # pack frame into short int (format 'h') in binary
        if numberChannels == 1:
            waveData += pack( 'h', maxAmplitude )

        else:
            waveData += pack('h', maxAmplitude)
            waveData += pack('h', maxAmplitude)

# write the frames; this will automatically update the number of frames in numFrames
waveFile.writeframes(waveData)
waveFile.close()

