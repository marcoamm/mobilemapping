import pyaudio
import numpy as np
from datetime import datetime

p = pyaudio.PyAudio()

fs = 44100       # sampling rate, Hz, must be integer
duration = 2   # in seconds, may be float
f = 2500        # sine frequency, Hz, may be float

# generate samples, note conversion to float32 array
samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)

# for paFloat32 sample values must be in range [-1.0, 1.0]
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)

# play. May repeat with different volume values (if done interactively)
print("Sync beeping starting at: ")
print(datetime.now().time())
stream.write(samples)
stream.write(0.0*samples)
stream.write(samples)
stream.write(samples)
stream.write(0.0*samples)
stream.write(samples)
stream.write(samples)
stream.write(0.0*samples)
stream.write(0.0*samples)
stream.write(samples)
stream.write(0.0*samples)
stream.write(samples)
stream.write(samples)
stream.write(samples)
stream.write(0.0*samples)
stream.write(0.0*samples)
stream.write(samples)
stream.write(0.0*samples)
stream.write(samples)
stream.write(samples)
stream.write(0.0*samples)
stream.write(samples)
stream.write(0.0*samples)
stream.write(samples)

stream.stop_stream()
stream.close()

p.terminate()
