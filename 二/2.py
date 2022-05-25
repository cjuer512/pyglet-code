import pyglet

window = pyglet.window.Window()
@window.event
def on_key_press(symbol,modifiers):
    if symbol == pyglet.window.key.A:
        print("A")
    elif symbol == pyglet.window.key.B:
        print("B")
    else:
        print("try 'a' or 'b'")
pyglet.app.run()