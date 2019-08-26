import matplotlib.pyplot as plt
import numpy as np

def julia_set(w, h, c = -0.7+ 0.27j, zoom=1, niter=256):
    """ A julia set of geometry (width x height) and iterations 'niter' """

    # Why (hxw) ? Because numpy creates a matrix as row x column
    # and height represents the y co-ordinate or rows and
    # width represents the x co-ordinate or columns.
    pixels = np.arange(w*h,dtype=np.uint16).reshape(h, w)
    
    c_imag = c.imag
    c_real = c.real

    for x in range(w): 
        for y in range(h):
            # calculate the initial real and imaginary part of z,
            # based on the pixel location and zoom and position values
            zx = 1.5*(x - w/2)/(0.5*zoom*w) 
            zy = 1.0*(y - h/2)/(0.5*zoom*h)

            for i in range(niter):
                radius_sqr = zx*zx + zy*zy
                # Iterate till the point is outside
                # the circle with radius 2.
                if radius_sqr > 4: break
                # Calculate new positions
                zy,zx = 2.0*zx*zy + c_imag, zx*zx - zy*zy + c_real

            color = (i >> 22) + (i >> 10)  + i*8
            pixels[y,x] = color
    
    return pixels


def display_fractal(pixels):
    # display the created fractal 
    plt.imshow(pixels)
    plt.show()
