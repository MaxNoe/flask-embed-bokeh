from flask import Flask
from flask import request
from flask import render_template

from .plots import plot_sine

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Welcome'


@app.route('/sine')
def sine():
    frequency = float(request.args.get('frequency', 1))
    amplitude = float(request.args.get('amplitude', 1))
    lower = float(request.args.get('lower', 0))
    upper = float(request.args.get('upper', 1))

    script, div = plot_sine(
        frequency=frequency,
        amplitude=amplitude,
        lower=lower,
        upper=upper,
    )
    title = 'Sine Wave A={}, f={}'.format(amplitude, frequency)
    return render_template(
        'bokeh_plot.html',
        script=script, div=div, title=title, frequency=frequency, amplitude=amplitude
    )
