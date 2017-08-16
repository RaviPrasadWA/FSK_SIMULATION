from constants import BITRATE, F_SAMPLING
import scipy.signal.signaltools as sigtool
import numpy as np
import scipy.signal as sgn

def differentiator(signal):
	y_diff = np.diff(signal,1)
	y_env = np.abs(sigtool.hilbert(y_diff)) # Envelope detector
	h = sgn.firwin( numtaps=100, cutoff=BITRATE*2, nyq=F_SAMPLING/2)
	return sgn.lfilter( h, 1.0, y_env) #Low-Pass filter
