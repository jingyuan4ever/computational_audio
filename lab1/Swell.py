from struct import pack           # This creates the binary data structure for frames
import wave

import array

fileNameToRead = raw_input('Please input file name to read:')
waveFileToRead = wave.open(fileNameToRead, 'r')

(numChannels, sampleWidth, sampleRate, numFrames, compressionType, nameOfCompression) = waveFileToRead.getparams()

halfNumFrame = numFrames/2

frames = waveFileToRead.readframes(halfNumFrame)
data = array.array('h', frames)
maxAmplitude = data[-1]
print maxAmplitude
waveFileToRead.close()

fileNameToWrite = 'swell.wav'
waveFileToWrite = wave.open(fileNameToWrite, 'w')
waveFileToWrite.setparams((2, sampleWidth, sampleRate, 0, 'NONE', 'not compressed'))
waveData=""       # this holds the data to be written to file in binary form
for i in range(0, halfNumFrame):
    frame = (float(i)/halfNumFrame)*maxAmplitude
    waveData += pack('h', frame)
    waveData += pack('h', frame)
for i in range(halfNumFrame, numFrames):
    frame = (float(numFrames - i)/halfNumFrame)*maxAmplitude
    waveData += pack('h', frame)
    waveData += pack('h', frame)

waveFileToWrite.writeframes(waveData)

waveFileToWrite.close()



