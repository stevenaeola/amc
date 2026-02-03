import time
import digitalio
import board
import keypad
import adafruit_midi
import usb_midi
from adafruit_midi.control_change  import ControlChange
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn

print ("starting organ")

button_pins = (board.GP6, board.GP7, board.GP8, board.GP9,
               board.GP10, board.GP11, board.GP12, board.GP13, board.GP14)
buttons = keypad.Keys(button_pins, value_when_pressed=False, pull=True)

currently_pressed = []

midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1])

midi_channel = 1  # count from 0 not 1

scale_offset = {"major": [0,2,4,5,7,9,11,12],
    "minor": [0,2,3,5,7,8,10,12]
    }

def midi_scale(key, root, scale="major"):
    global midi_channel
    if key>= len(scale_offset[scale]):
        return
    while(len(currently_pressed) >0):
        old_midi_note = currently_pressed.pop()
        midi.send(NoteOff(old_midi_note, 0), midi_channel)
    offset = scale_offset[scale][key]
    print("offset" , offset)
    new_midi_note = root + offset
    print("new_midi_note", new_midi_note)
    currently_pressed.append(new_midi_note)
    midi.send(NoteOn(new_midi_note, 127), midi_channel)



root = 24 # C1

while True:
    button = buttons.events.get()  # see if there are any key events
    if button:                      # there are events!
      if button.pressed:
        key = button.key_number
        midi_scale(key, root)
