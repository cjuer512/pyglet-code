import pyglet
import time

window = pyglet.window.Window(resizable=True)
window.set_size(1280,720)
time.sleep(3)
window.set_size(333,333)
pyglet.app.run()