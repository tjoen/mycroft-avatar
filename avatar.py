# 1> copy the script and chars dir to /home/pi/
# 2> install pyglet first with: pip install pyglet
# 3> then in an X session run this script: python avatar.py

import websocket
import time
import threading
import json
import pyglet

# Create and open a window
window = pyglet.window.Window(257, 257)

# choose character, available are 
# chars/minion, chars/dogfront, chars/putin
# chars/satan, chars/dog, chars/trump, 
# and chars/pokegirl
char = 'chars/minion'

# Reindex your character images
pyglet.resource.path = [char]
pyglet.resource.reindex()


# Load sprites
s0 = pyglet.resource.image('0.gif')
s1 = pyglet.resource.image('1.gif')
s2 = pyglet.resource.image('2.gif')
s3 = pyglet.resource.image('3.gif')
s4 = pyglet.resource.image('4.gif')
s5 = pyglet.resource.image('5.gif')
s6 = pyglet.resource.image('6.gif')
blink = pyglet.resource.image('7.gif')
sprites = [s0, s1, s2, s3, s4, s5, s6, blink]

# Animation
#sprite = pyglet.sprite.Sprite(s1) #anim

frame_index = 4
current_frame = sprites[frame_index]

def update(dt):
    global current_frame
    current_frame = sprites[frame_index]

@window.event
def on_draw():
    window.clear()
    current_frame.blit(0, 0)
 
class ThreadingPyg(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, interval=0.2):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def on_message(self, ws, message):
        mes = json.loads( message )
        global frame_index
        if mes['type'] == 'enclosure.mouth.viseme':
            frame_index = int(mes['data']['code'])
#        if mes['type'] == 'enclosure.eyes.blink':
#            frame_index = 7
#            time.sleep(1)
#            frame_index = 4

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws):
        print("### closed ###")

    def run(self):
        """ Method that runs forever """
        while True:
            # Do something
            print('Starting websocket')
            websocket.enableTrace(True)
            ws = websocket.WebSocketApp("ws://localhost:8181/core",
                                      on_message = self.on_message,
                                      on_error = self.on_error,
                                      on_close = self.on_close)
            ws.run_forever()


if __name__ == '__main__':
    sockit = ThreadingPyg()
    pyglet.clock.schedule_interval(update, 1/30.0) 
    pyglet.app.run()
