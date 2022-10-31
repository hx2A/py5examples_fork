"""
Noise2D
by Daniel Shiffman.

Using 2D noise to create simple texture.
"""

increment = 0.02


def setup():
    size(640, 360)


def draw():
    load_pixels()
    xoff = 0.0  # Start xoff at 0
    detail = remap(mouse_x, 0, width, 0.1, 0.6)
    noise_detail(8, detail)

    # For every x,y coordinate in a 2D space, calculate a noise value and
    # produce a brightness value
    for x in range(width):
        xoff += increment     # Increment xoff
        yoff = 0.0     # For every xoff, start yoff at 0
        for y in range(height):
            yoff += increment  # Increment yoff

            # Calculate noise and scale by 255
            bright = noise(xoff, yoff) * 255
            # Try using this line instead
            # float bright = random(0,255)

            # Set each pixel onscreen to a grayscale value
            pixels[x + y * width] = color(bright)
    update_pixels()
