import numpy as np
import numpy.matlib

def rectangleFilter(iWidth, iHeight, fWidth, fHeight):
    array = np.zeros((iHeight, iWidth))
    centerX = int(iWidth / 2)
    centerY = int(iHeight / 2)
    filterX = int(fWidth / 2)
    filterY = int(fHeight / 2)
    array[centerY - filterY : centerY + filterY + (fHeight % 2),
        centerX - filterX : centerX + filterX + (fWidth % 2)] = 1
    return array

def circleFilter(iWidth, iHeight, fRadius):
    array = np.zeros((iHeight, iWidth))
    centerX = int(iWidth / 2)
    centerY = int(iHeight / 2)
    for i in range(iHeight):
        for j in range(iWidth):
            array[i][j] = round(i - centerY) ** 2 + round(j - centerX) ** 2 <= fRadius ** 2
    return array


def frequencyFourierFilter(image, filterFunction, **kwargs):
    M, N = image.shape
    P, Q = 2 * M, 2 * N

    f_p = np.zeros((P, Q))
    f_p[0:M, 0:N] = np.array(image, copy=True) / 255.
    a0 = np.array(list(range(0, P)))
    b0 = np.array(list(range(0, Q)))
    a = np.transpose(np.matlib.repmat(a0, Q, 1)) + np.matlib.repmat(b0, P, 1)
    a = (-1) ** a
    f_p = f_p * a

    F = np.fft.fft2(f_p)

    H = filterFunction(Q, P, **kwargs)
    G = H * F
    gp = np.real(np.fft.ifft2(G)) * a
    g_p = gp[0:M, 0:N]

    # border fix
    g_p[1: -1, 0] = (g_p[1: -1, 0] + g_p[1: -1, 1]) * 1.15 / 2
    g_p[1: -1, N - 1] = (g_p[1: -1, N - 1] + g_p[1: -1, N - 2]) * 1.15 / 2
    g_p[0][:] = (g_p[0][:] + g_p[1][:] * 1.15) / 2
    g_p[M - 1][:] = (g_p[M - 1][:] + g_p[M - 2][:] * 1.15) / 2
    g_p = np.where(g_p > 1, 1, g_p)

    return (g_p * 255.).astype(np.uint8), G, F