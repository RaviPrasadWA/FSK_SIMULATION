import numpy as np


def oscillator(A, N, Fbit, Fc, Fs, Fdev, data_in):
    t = np.arange(0, float(N) / float(Fbit), 1 / float(Fs), dtype=np.float)
    m = np.zeros(0).astype(float)
    for bit in data_in:
        if bit == 0:
            m = np.hstack((m, np.multiply(np.ones(Fs / Fbit), Fc + Fdev)))
        else:
            m = np.hstack((m, np.multiply(np.ones(Fs / Fbit), Fc - Fdev)))
    y = np.zeros(0)
    y = A * np.cos(2 * np.pi * np.multiply(m, t))
    return y
