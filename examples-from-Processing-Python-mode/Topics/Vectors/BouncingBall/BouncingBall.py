"""
Bouncing Ball with Vectors
by Daniel Shiffman.

Demonstration of using vectors to control motion of body.
This example is not object-oriented.
See AccelerationWithVectors for an example of how to simulate motion using
vectors in an object.
"""

location = Py5Vector(100, 100)  # Location of shape
velocity = Py5Vector(1.5, 2.1)  # Velocity of shape
gravity = Py5Vector(0, 0.2)  # Gravity acts at the shape's acceleration.


def setup():
    size(640, 360)
    smooth()


def draw():
    background(0)
    # Add velocity to the location.
    location += velocity
    # Add gravity to velocity.
    velocity += gravity
    # Bounce off edges.
    if location.x < 0 or location.x > width:
        velocity.x = velocity.x * -1
    if location.y > height:
        # We're reducing velocity ever so slightly
        # when it hits the bottom of the window.
        velocity.y = velocity.y * -0.95
        location.y = height
    # Display circle at location vector.
    stroke(255)
    stroke_weight(2)
    fill(127)
    ellipse(location.x, location.y, 48, 48)
