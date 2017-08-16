import numpy as np
from constants import F_SAMPLING, BITRATE, N

def slicer(signal_filtered, unmodulated_input):
	mean = np.mean(signal_filtered)
	#if the mean of the bit period is higher than the mean, the data is a 0
	rx_data = []
	sampled_signal = signal_filtered[F_SAMPLING/BITRATE/2:len(signal_filtered):F_SAMPLING/BITRATE]
	for bit in sampled_signal:
	    if bit > mean:
	        rx_data.append(0)
	    else:
	        rx_data.append(1)

	bit_error=0
	for i in range(0,len(unmodulated_input)):
	    if rx_data[i] != unmodulated_input[i]:
	        bit_error+=1
	return np.asarray(rx_data)
