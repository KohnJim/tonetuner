# by Jooyoung (John) Kim

import sounddevice                                      # for accessing microphone
import os                                               # for clearing console
import numpy as np                                      # for sampling audio
from scipy import fftpack                               # for fft (fast fourier transform)

winSamp=[]                                              # create list for sampling audio waveform from microphone
for i in range(44100): 
    winSamp.append(0)

def run(val, f, t, s):                                  # main method
    global winSamp 
    for i in val[:,0].tolist():                         # updates list (winSamp) sampled audio real-time
        winSamp.append(i) 
    winSamp = winSamp[len(val[:, 0]):] 
    magSpec = fftpack.fft(winSamp)[:int(len(winSamp)/2)]                                        
    magSpec[: 62] = [0] * 62
    maxFreq = np.argmax(abs(magSpec))                   # find the frequency detected with the maximum amplitude
    temp = findClosestNote(maxFreq) 
    result(temp[0], maxFreq, temp[1])

def findClosestNote(pitch):                             # method that returns the closest pitch to the frquency detected with the highest magnitude
    i = np.log2(pitch/440)*12                           # how many notes the frequecy detected is appart from A4 (440 Hz)
    return ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"][round(i)%12] + str(int(4+ (i + 9) /12)), str(int((i%12-round(i%12))*100))

def result(cNote,maxFreq,corr):
    os.system('cls')                                    # clears console with each printout to keep console clean 
    print("note: {} ({} Hz) {} cents away".format(cNote, maxFreq, corr))                        # printout
    
   
with sounddevice.InputStream(channels=2, callback = run, blocksize=22050, samplerate=44100):    # access microphone and "run" the code
    try:
        while True:
            pass
            
    except KeyboardInterrupt:                           # ctrl + c to terminate the program and prevent KeyboardInterrupt error
        pass
