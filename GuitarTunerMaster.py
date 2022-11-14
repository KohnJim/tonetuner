import sounddevice                      # access microphone
import os 
import numpy as np                      # for sampling audio
from scipy import fftpack as fp         # for fft (fast fourier transform)

winSamp=[]                              # create list for sampling audio 
for i in range(44100): 
    winSamp.append(0)

def run(val, f, t, s):                  # main method
    global winSamp 
    for i in val[:,0].tolist(): 
        winSamp.append(i) 
    winSamp = winSamp[len(val[:, 0]):] 
    magSpec = fp.fft(winSamp)[:int(len(winSamp)/2)]
    magSpec[: 62] = [0] * 62
    maxFreq = np.argmax(abs(magSpec))
    temp = findClosestNote(maxFreq)
    result(temp[0], maxFreq, temp[1])

def findClosestNote(pitch):             # method that returns the closest pitch to the frquency detected with the highest amplitude 
    i = np.log2(pitch/440)*12           # how many notes the frequecy detected is appart from A4 (440 Hz)
    return ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"][round(i)%12] + str(int(4+ (i + 9) /12)), str(int((i%12-round(i%12))*100))

def result(cNote,maxFreq,corr):
    os.system('cls')                    # clears console with each printout to keep console clean 
    print("note: {} ({} Hz) {} cents away".format(cNote, maxFreq, corr))                        # printout
    

with sounddevice.InputStream(channels=2, callback=run, blocksize=22050, samplerate=44100):      # access microphone
    try:
        while True:
            pass
            
    except KeyboardInterrupt:           # ctrl + c to terminate the program
        pass
  

