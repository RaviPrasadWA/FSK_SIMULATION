from vco import oscillator
from plotter import plot
from input_ import unmodulated_input

input_,m = oscillator(unmodulated_input)
plot(input_,m)