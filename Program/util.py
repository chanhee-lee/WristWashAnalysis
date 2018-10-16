from scipy.signal import butter, lfilter
import numpy

def vector_magnitude(data):
    """ function to calculate the magnitude of a vector

    Calculate the magnitude of the vector superposition of data (for
    example, acceleration) on x, y, and z axis

    Arguments:
        data: array of (x, y, z) tuples for a vector

    Returns:
        array of the magnitude of a vector

    """
    array = []
    for x,y,z in data:
        magnitude = (x**2 + y**2 + z**2)**.5
        array.append(magnitude)
    return array

    raise NotImplementedError


def moving_average(data, window_size):
    """ moving average filter

    Implement a simple moving average filter to use as a low pass
    filter

    Arguments:
        data: data be filtered
        window_size: window_size chosen for the data

    Returns:
        The filtered data.

    TODO:
        Finish this function. Think about how you want to handle
        the size difference between your input array and output array.
        You can write it yourself or consider using numpy.convole for
        it:
        https://docs.scipy.org/doc/numpy/reference/generated/numpy.convolve.html

    """

    mag = vector_magnitude(data)
    weights = numpy.repeat(1.0, window_size)/window_size
    return numpy.convolve(mag, weights, mode = 'full')

    raise NotImplementedError


def moving_average2(dataXYZ, window_size):
    """ moving average filter

    Implement a simple moving average filter to use as a low pass
    filter

    Arguments:
        data: data be filtered
        window_size: window_size chosen for the data

    Returns:
        The filtered data.

    TODO:
        Finish this function. Think about how you want to handle
        the size difference between your input array and output array.
        You can write it yourself or consider using numpy.convole for
        it:
        https://docs.scipy.org/doc/numpy/reference/generated/numpy.convolve.html

    """

    #mag = vector_magnitude(data)
    weights = numpy.repeat(1.0, window_size) / window_size
    return numpy.convolve(dataXYZ, weights, mode='full')

    raise NotImplementedError


def butter_lowpass_filter(data, cutoff, fs, order=5):
    """ butter lowpass filter

    See this link for more information:
    https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.signal.butter.html

    Arguments:
        data: data be filtered
        curoff: cutoff freqency of the filter
        fs: sample rate of data
        order: order of the lowpass filter

    Returns:
        The filtered data.

    TODO:
        Figure out the parameter when you call this function

    """
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

