import pyglet
import time

window = pyglet.window.Window()
x,y = window.get_location()
time.sleep(3)
window.set_location(x=x + 100,y=y + 100)
pyglet.app.run()