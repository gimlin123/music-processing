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

kTRT = 2 ** (1 / 12.0)

def pitch_to_freq(p):
    """Convert midi pitch value to frequency assuming A 440 = 69"""
    return 440 * kTRT ** (p - 69.0)


def freq_to_pitch(f):
    """Convert frequency to (floating point) midi pitch assuming A 440 = 69"""
    return 12 * np.log2(f / 440.0) + 69

# returns a matrix of frequencies to test for
#   will be a matrix with dimensions 88 * num_overtones
def get_test_freqs(num_overtone):
    test_freqs = np.arange(21, 109)
    test_freqs = pitch_to_freq(test_freqs)
    test_freqs = np.expand_dims(test_freqs, 1)

    concat = [test_freqs]
    for i in range(2, num_overtone + 2):
        concat.append(test_freqs * i)

    return np.concatenate(concat, 1)
