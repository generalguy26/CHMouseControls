# CHTabletControls
Implementation of Mouse/Tablet Controls for Clone Hero


Run either in a Python IDE or with "python controller.py" in cmd, with python added to your system PATH variable.
pynput, pyvjoy, PIL, and numpy are all dependencies
vjoy must also be installed to your system for emulating the gamepad.

The image denotes which areas of the screen coorespond to which buttons being pressed. This is configurable by making your own image and setting rgb values to input combinations. I didn't bother with figuring out chords, but it should be possible.
Mouse button must be clicked for buttons to be pressed.
Script will terminate when input is sent to the python terminal. Do not close out of the terminal to close the program, as there is a bug with pyvjoy that causes the thread to continue running even when the terminal is closed.
