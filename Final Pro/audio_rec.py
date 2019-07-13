from scipy.io import wavfile
#from matplotlib import pyplot as plt
#import numpy as np

# Load the data and calculate the time of each sample
samplerate, data = wavfile.read('/home/pi/FTP/test.wav')
#times = np.arange(len(data))/float(samplerate)
#data = data - 100
# Make the plot
# You can tweak the figsize (width, height) in inches
#plt.figure(figsize=(30, 4))
#plt.fill_between(times, data)
#plt.xlim(times[0], times[-1])
#plt.xlabel('time (s)')
#plt.ylabel('amplitude')
print(max(data))
# You can set the format by changing the extension
# like .pdf, .svg, .eps
#plt.savefig('plot.png', dpi=100)
#plt.show()

if(max(data) > 133):
	print("Emergency")
else:
	print("Normal")