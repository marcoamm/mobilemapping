import pyaudio
from scipy.io import wavfile
import numpy as np
from datetime import datetime

p = pyaudio.PyAudio()

fs = 44100       # sampling rate, Hz, must be integer
duration = 0.5   # in seconds, may be float
f = 2500        # sine frequency, Hz, may be float

# generate samples, note conversion to float32 array
samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)

frames = []

frames.append((samples))
frames.append((0.0*samples))
frames.append((samples))
frames.append((samples))
frames.append((0.0*samples))
frames.append((samples))
frames.append((samples))
frames.append((0.0*samples))
frames.append((0.0*samples))
frames.append((samples))
frames.append((0.0*samples))
frames.append((samples))
frames.append((samples))
frames.append((samples))
frames.append((0.0*samples))
frames.append((0.0*samples))
frames.append((samples))
frames.append((0.0*samples))
frames.append((samples))
frames.append((samples))
frames.append((0.0*samples))
frames.append((samples))
frames.append((0.0*samples))
frames.append((samples))

stack = np.hstack(frames)

#Save audio to disk
wavfile.write('beep.wav', fs, stack)

p.terminate()
