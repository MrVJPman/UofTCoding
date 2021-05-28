# UPDATED: GUI display
from gui import GuiWorld as World
# from world import World

# Comment some of these out if you haven't implemented them yet:
from stone import Stone
from mouse import Mouse
from ant import Ant
from turtle import Turtle
from bird import Bird
from parrot import Parrot
from wolf import Wolf

# By default, the simulator requires you to press ENTER
# to go to the next time steps. (great for debugging!)
#
# To watch the animation, set DEBUG to False. You can also change
# the value passed to sleep() to speed up or slow down the
# animation (the value is the number of seconds between steps).
DEBUG = True

if __name__ == '__main__':
    # If your terminal displays funny things, like ESC[1, instead of nice,
    # colored strings, it probably doesn't support color. That sucks, but
    # until you get into CDF to test out the coloring, you can turn it off
    # by changing use_color to False in the folowing line:
    world = World(65, 35, use_color=True)
    world.generate(Stone, 250)
    world.generate(Mouse, 250)
    world.generate(Ant, 250)
    world.generate(Turtle, 250)
    world.generate(Bird, 250)
    world.generate(Parrot, 250)
    world.generate(Wolf, 16)

    world.run(prompt=DEBUG, delay=0.1, n=1000)
