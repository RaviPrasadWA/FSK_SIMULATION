#Plotter to plot data in F(t) -> time domain
#                        F(x) -> frequency domain( Fourier )

from constants import F_SAMPLING, BITRATE, N_PRINTBITS, N, F_CARRIER, DEVIATION
import numpy as np
import pylab as pl


def plot(signal,m):
    #view the data in time and frequency domain
    #calculate the frequency domain for viewing purposes
    N_FFT = float(len(signal))
    f = np.arange(0,F_SAMPLING/2,F_SAMPLING/N_FFT)

    w = np.hanning(len(signal))
    y_f = np.fft.fft(np.multiply(signal,w))
    y_f = 10*np.log10(np.abs(y_f[0:N_FFT/2]/N_FFT))
    t = np.arange(0,float(N)/float(BITRATE),1/float(F_SAMPLING), dtype=np.float)
    pl.subplot(3,1,1)
    pl.plot(t[0:F_SAMPLING*N_PRINTBITS/BITRATE],m[0:F_SAMPLING*N_PRINTBITS/BITRATE])
    pl.xlabel('Time (s)')
    pl.ylabel('Frequency (Hz)')
    pl.title('Original VCO output versus time')
    pl.grid(True)
    pl.subplot(3,1,2)
    pl.plot(t[0:F_SAMPLING*N_PRINTBITS/BITRATE],signal[0:F_SAMPLING*N_PRINTBITS/BITRATE])
    pl.xlabel('Time (s)')
    pl.ylabel('Amplitude (V)')
    pl.title('Amplitude of carrier versus time')
    pl.grid(True)
    pl.subplot(3,1,3)
    pl.plot(f[0:(F_CARRIER+DEVIATION*2)*N_FFT/F_SAMPLING],y_f[0:(F_CARRIER+DEVIATION*2)*N_FFT/F_SAMPLING])
    pl.xlabel('Frequency (Hz)')
    pl.ylabel('Amplitude (dB)')
    pl.title('Spectrum')
    pl.grid(True)
    pl.tight_layout()
    pl.show()

