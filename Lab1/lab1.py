import matplotlib.pyplot as plt
import numpy as np

freq= 10.0 #Hz
sampFreq= 100.0 #Hz
numCycles= 4.0

t= np.arange(0, numCycles * (1/freq), 1/sampFreq )
f= np.linspace(-sampFreq/2, sampFreq/2, len(t))

x= np.cos(2*np.pi*freq*t)
noise= np.random.randn(len(t))

fig, axs = plt.subplots(1,3)

X0_f= np.fft.fft(x + 0.5*noise);
X0_f_shifted= np.fft.fftshift(X0_f)

X1_f= np.fft.fft(x + noise);
X1_f_shifted= np.fft.fftshift(X1_f)

X2_f= np.fft.fft(x + 2*noise);
X2_f_shifted= np.fft.fftshift(X2_f)

axs[0].stem(f, abs(X0_f_shifted.real))
axs[1].stem(f, abs(X1_f_shifted.real))
axs[2].stem(f, abs(X2_f_shifted.real))

plt.show()
