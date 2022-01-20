from scipy.fftpack import rfft
import json
import h5py
from scipy.fftpack import irfft
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

from obspy.io.segy.core import _read_segy
from obspy.core.util import get_example_file
import numpy as np
import os

print(os.getcwd())
filename = get_example_file(r"/C:/Users/Владимир/OneDrive/Документы/makeSGY/043rfff.SGY")

segyfile= _read_segy(filename, unpack_trace_headers=True)

x_coord=[]
y_coord=[]
z_coord=[]
Traces=[]
corr=[]

for tr in range (0, len(segyfile)-4120):
    x_coord.append(segyfile[tr].stats.segy.trace_header.source_coordinate_x)
    y_coord.append(segyfile[tr].stats.segy.trace_header.source_coordinate_y)
    Traces.append (segyfile[tr].data)

provyf=rfft(Traces[0])
UsTraces=Traces[:-1]
print(len(UsTraces))
with h5py.File('/C:/Users/Владимир/OneDrive/Документы/makeSGY/data/random.hdf5', 'w') as f:
    for i in range(len(Traces[0])-11995):
        Z = np.array([], dtype=float)
        syf=[]
        for j in range(len(UsTraces)):
            yf=(rfft(UsTraces[j]))
            syf.append(yf[10:1300])
            Z = np.concatenate([Z,UsTraces[j]])
        f.create_dataset("default"+str(i), data=syf)
        Z = np.delete(Z,0)
        Z = np.append(Z,Traces[-1][i])
        UsTraces = Z.reshape((len(UsTraces), -1))

with h5py.File('/C:/Users/Владимир/OneDrive/Документы/makeSGY/data/random.hdf5', 'r') as f:
    data = f["default2"]
    print(data)

a = input()
print(a)