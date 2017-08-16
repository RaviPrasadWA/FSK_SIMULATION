from vco import oscillator
from plotter import plot
from input_ import unmodulated_input
from differentiator import differentiator
from slicer import slicer

input_,m = oscillator(unmodulated_input)
input_ = differentiator(input_)
input_ = slicer(input_,unmodulated_input)
input_,m = oscillator(input_)
plot(input_,m)