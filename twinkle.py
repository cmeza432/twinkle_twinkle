"""
Name:   Carlo Meza
ID:     1001170229
Date:   02/04/05
"""

import numpy as np
from math import pi
from math import cos
import soundfile as sf

# Constant piano keys
a = 49
b = 51
c = 52
d = 54
e = 56
f = 57
g = 59
a5 = 61
b5 = 63

# Constant values used to play rythm
step_rate = 1/8000
t = 0.5
sample_rate = 8000
time = np.arange(0, t, step_rate)

# Function to output frequency when key is given
def freq(key):
    fr = 440*(2**((key-49)/12))
    return np.cos(2*pi*fr*time)

# Arrange an array of the 24 notes of the song to pass to write function
final = np.array([freq(c), freq(c), freq(g), freq(g), freq(a5), freq(a5), freq(g), freq(g), freq(f), freq(f), freq(e), freq(e),
                  freq(d), freq(d), freq(e), freq(c), freq(g), freq(g), freq(f), freq(f), freq(e), freq(e), freq(d), freq(d)])
final = np.concatenate(final, axis = None)
    
# Create a wav sound file of the arranged values above
sf.write('twinkle.wav', final, sample_rate)
