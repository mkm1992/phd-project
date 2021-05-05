import matplotlib.pyplot as plt
from matplotlib.pyplot import setp
import os
import numpy as np

fig = plt.figure(1)
ax = plt.axes([0.1, 0.1, 0.8, 0.8])
setp(ax, 'frame_on', False)
# Plot here
degree = np.arange(4, 20)
python_time = degree # replace with f(degree)
c_time = degree + 1 # replace with f(degree)
ax.plot(degree, python_time, label='Python', marker='o')
ax.plot(degree, c_time, label='C++', marker='o')
# End Plot
ax.text(1, 1, r'$\int_0^1\frac{x^3}{x+1}cos(x^2)$', fontsize=20,
	    horizontalalignment='right', verticalalignment='top',
	    transform=ax.transAxes)
ax.set_xlabel(r'Degree (n)')
ax.set_ylabel(r'Time (ms)')
handle, label = ax.get_legend_handles_labels()
ax.legend(handle, label, loc='upper left', bbox_to_anchor=(.01, .99), 
	      ncol=1, labelspacing=0.3, fancybox=True, shadow=True, 
	      columnspacing=1, borderpad=0.2, title='', handletextpad=0.1, 
	      numpoints=1, handlelength=1.5, markerscale=1)
plt.savefig(os.path.join(os.getcwd(), 'result.pdf'))