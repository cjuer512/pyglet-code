import pyglet

window = pyglet.window.Window()
@window.event
def on_mouse_press(x,y,button,modifiers):
    if button == pyglet.window.mouse.LEFT:
        print('LEFT')
    elif button == pyglet.window.mouse.RIGHT:
        print('RIGHT')
pyglet.app.run()