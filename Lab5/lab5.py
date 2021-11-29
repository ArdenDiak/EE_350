def resp_bode_plt(a_coeffs, b_coeffs, window_type, win_size, axs):
    num_samples= 64

    #filter freq. and impulse responses
    w, H = signal.freqz(b_coeffs, a_coeffs, num_samples)
    (t_out, hd) = signal.dimpulse((b_coeffs, a_coeffs, 1))
    hd = np.squeeze(hd)

    #freq. response of windowed h_d[n]
    window = signal.get_window(window_type, win_size)
    hd_w = hd[:win_size] * window
    Hd = np.fft.fft(hd_w)

    print(Hd.shape)
    print(H.shape)

    H_phase = np.unwrap(np.angle(H))
    Hd_phase= np.unwrap(np.angle(Hd))


    axs[0].set_xlabel('Frequency [rad/samples]')
    axs[0].set_ylabel('Amplitude [dB]', color='b')
    axs[0].set_title('Bode plot de les réponses fréquentielles')
    axs[0].plot(w, dB(H), color='b', label='$|H(\omega)|$')
    axs[0].plot(w[:len(Hd)], dB(Hd), color='r', label='$|H_d(\omega)|$')
    axs[0].legend()

    axs[1].plot(w, H_phase, color='g', label='$\\angle{H(\omega)}$')
    axs[1].set_ylabel('Angle (radians)', color='g')
    axs[1].set_title('Phase de la $H(\omega)$ fenêtrée et non-fenêtrée')
    axs[1].plot(w[:len(Hd_phase)], Hd_phase, color='g', label='$\\angle{H_d(\omega)}$')
    axs[1].legend()

