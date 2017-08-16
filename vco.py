import numpy as np
from constants import A, N, BITRATE, F_CARRIER, F_SAMPLING, DEVIATION


def oscillator(data_in):
    t = np.arange(0, float(N) / float(BITRATE), 1 / float(F_SAMPLING), dtype=np.float)
    m = np.zeros(0).astype(float)
    for bit in data_in:
        if bit == 0:
            m = np.hstack((m, np.multiply(np.ones(F_SAMPLING / BITRATE), F_CARRIER + DEVIATION)))
        else:
            m = np.hstack((m, np.multiply(np.ones(F_SAMPLING / BITRATE), F_CARRIER - DEVIATION)))
    y = np.zeros(0)
    y = A * np.cos(2 * np.pi * np.multiply(m, t))
    return y,m
