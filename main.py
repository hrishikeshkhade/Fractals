import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z**2 + c
        n += 1
    if n == max_iter:
        return max_iter
    return n + 1 - np.log(np.log2(abs(z)))

def generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter):
    x, y = np.meshgrid(np.linspace(x_min, x_max, width), np.linspace(y_min, y_max, height))
    z = x + 1j * y
    fractal = np.zeros_like(z, dtype=np.float32)

    for i in range(width):
        for j in range(height):
            fractal[i, j] = mandelbrot(z[i, j], max_iter)

    return fractal

def display_fractal(fractal):
    plt.imshow(fractal, cmap='viridis', extent=(x_min, x_max, y_min, y_max))
    plt.colorbar()
    plt.title('Mandelbrot Fractal')
    plt.show()

# Set the parameters for the Mandelbrot set
width, height = 800, 800
x_min, x_max = -2, 2
y_min, y_max = -2, 2
max_iter = 100

# Generate and display the Mandelbrot set
fractal = generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter)
display_fractal(fractal)
