import numpy as np
from bokeh.plotting import figure
from bokeh.embed import components


def plot_sine(amplitude, frequency, upper=0, lower=1, **kwargs):

    t = np.linspace(upper, lower, 250)
    plot = figure(width=600, height=400)
    plot.line(
        x=t,
        y=amplitude * np.sin(2 * np.pi * frequency * t),
        **kwargs,
    )

    return components(plot)
