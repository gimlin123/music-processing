import numpy as np

######################
# Assume real signal x
######################

# find the discrete fourier transform for signal x with a cosine function
# with frequency freq
def dft_cos_coeff(x, freq, sampling_rate):
    cos_vals = np.arange(len(x)) * 1. / sampling_rate
    cos_vals = np.cos(cos_vals)

    return np.dot(x, cos_vals)

# find the discrete fourier transform for signal x with sine function
# with frequency freq
def dft_sin_coeff(x, freq, sampling_rate):
    cos_vals = np.arange(len(x)) * 1. / sampling_rate
    cos_vals = np.cos(cos_vals)

    return np.dot(x, cos_vals)
