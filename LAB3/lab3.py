def gkernel(N, sigma):

    res= np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            res[i,j]= (1/(2*np.pi*(sigma**2)))*np.exp(-((i**2 + j**2)/(sigma**2)))

    delta= spsig.unit_impulse((N,N),'mid')
    h= spsig.convolve2d(delta, res)
    return h
