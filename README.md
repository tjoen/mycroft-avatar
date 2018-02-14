# mycroft-avatar
Adds a virtual character in an X session. WIP

# screenshot
![alt text](https://github.com/tjoen/mycroft-avatar/blob/master/example.jpg "Screenshot")

# installation
* copy the script and chars dir to /home/pi/
* install pyglet first with: pip install pyglet
* then in an X session run this script: python avatar.py

Mycroft has the following mouthshapes:

- 0 = shape for sounds like 'y' or 'aa'
- 1 = shape for sounds like 'aw'
- 2 = shape for sounds like 'uh' or 'r'
- 3 = shape for sounds like 'th' or 'sh'
- 4 = neutral shape for no sound
- 5 = shape for sounds like 'f' or 'v'
- 6 = shape for sounds like 'oy' or 'ao'

Blinking is not yet handled correctly by this script.


