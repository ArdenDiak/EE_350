N_points= 10000
freq= 10

n= np.linspace(0, freq, N_points)
x_n= np.cos(0.2*np.pi*n) + np.cos(0.8*np.pi*n)
(w_x, h_x)= freqz(x_n, 1, 1000)

# Plotting the Magnitude and Phase
fig, ax1 = plt.subplots(1)
ax1.set_xlabel('Frequency [rad/samples]')
ax1.set_ylabel('Amplitude [dB]', color='b')
ax1.set_title('Réponse Fréquentiel')
ax1.plot(w_x, dB(h_x), color='b')

ax2 = ax1.twinx()
angles_rad = np.unwrap(np.angle(h_x))
ax2.plot(w_x, angles_rad, 'g')
ax2.set_ylabel('Angle (radians)', color='g')
ax2.plot(w_x, angles_rad, color='g')
ax2.grid()


(tout, yout)= dlsim((b, a, 1),x_n)
fig, ax1 = plt.subplots(1)
ax1.plot(tout, yout)

# fig, ax1 = plt.subplots(1)
# #ax1.plot(w_x, dB(h.real[:1000] * h_x.real) )
# t= np.linspace(0,50,100)
# ax1.plot(t, np.cos(0.1*np.pi*t))
# plt.show()

'''
n= np.linspace(0, 10, 1000)
x_n= np.cos(0.2*np.pi*n) + np.cos(0.8*np.pi*n)


b= np.array([0.2066, 0.4132, 0.2066])
a= np.array([1, -0.3695, 0.1958])

tout, yout= dimpulse((b,a,1), n=1000)
yout= np.squeeze(yout)

out= convolve(yout, x_n)
print(np.shape(out))

fig, ax1 = plt.subplots(1)
ax1.plot(tout, out[:1000])

plt.show()
'''
