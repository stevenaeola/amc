import time
import digitalio
import board
import keypad
import adafruit_midi
import usb_midi
from adafruit_midi.control_change  import ControlChange
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn

button_pins = (board.GP6, board.GP7, board.GP8, board.GP9,
               board.GP10, board.GP11, board.GP12, board.GP13, board.GP14)
buttons = keypad.Keys(button_pins, value_when_pressed=False, pull=True)


midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1])

midi_channel = 4  # count from 0 not 1. Usually have piano on channel 4 (really 5)

# circuitpython uses old version of python (3.4!) so dictionary merging is not provided

def merge_two_dicts(x, y):
    z = x.copy()   # start with keys and values of x
    z.update(y)    # modifies z with keys and values of y
    return z

latched_notes = []
max_latched_notes = 1

def do_action(action):
  to_send = action.get("send", "")
  print ("action", to_send)
  channel = action.get("channel", midi_channel)

  if to_send == "cc":
    ccn = action.get("ccn", 0)
    ccv = action.get("ccv", 0)
    midi.send( ControlChange(ccn, ccv), channel=channel)
    print ("sent cc ", ccn, ccv, channel)
  elif (to_send == "noteon" or to_send == "noteoff"):
    midi_note = action.get("midi_note", 0)
    velocity = action.get("velocity", 127)
    if to_send == "noteon":
      midi.send(NoteOn(midi_note, velocity), channel)
    else:
      midi.send(NoteOff(midi_note, 0), channel)
    print ("sent ", to_send, midi_note, channel)
  elif (to_send == "notelatch"):
    midi_note = action.get("midi_note", 0)
    velocity = action.get("velocity", 127)
    if(midi_note in latched_notes):
      midi.send(NoteOff(midi_note, 0), channel)
      print("removing ", midi_note)
      latched_notes.remove(midi_note)
      print ("latched_notes", latched_notes)

    else:
      midi.send(NoteOn(midi_note, velocity), channel)
      print ("adding latched note", midi_note)
      latched_notes.append(midi_note)
      print ("latched_notes", latched_notes)

    while(len(latched_notes) > max_latched_notes):
      print ("removing latched note ", latched_notes[0])
      midi.send(NoteOff(latched_notes[0], 0), channel)
      latched_notes.pop(0)
      print ("latched_notes", latched_notes)


scale_offset = {"major": [0,2,4,5,7,9,11,12],
    "minor": [0,2,3,5,7,8,10,12]
    }

def midi_note_actions (root, scale, offset, what="onoff", channel=midi_channel):
    midi_note = root + scale_offset[scale][offset]
    if what == "onoff":
        actions = {"press": {"send": "noteon", "midi_note": midi_note, "channel": channel},
               "release": {"send": "noteoff", "midi_note": midi_note, "channel": channel}}
    elif what == "latch":
        actions = {"press": {"send": "notelatch", "midi_note": midi_note, "channel": channel}}
    else:
        print ("unrecognised midi_note_action ", what)
        actions = {}
    return actions

# "what" can be "press": send ccv on press, then 0 on release; "release": send ccv on press; "pressrelease": send ccv on release
def cc_actions (ccn, what="pressrelease", ccv=127, channel=midi_channel):
    send_ccv = {"send": "cc", "ccn": ccn, "ccv": ccv, "channel": channel}
    send_0 = {"send": "cc", "ccn": ccn, "ccv": 0, "channel": channel}

    if what == "pressrelease":
        return {"press": send_ccv, "release": send_0}
    elif what == "press":
        return {"press": send_ccv}
    elif what == "release":
        return {"release": send_ccv}
    else:
        print ("unrecognised cc_action ", what)
        return {}

# stop_button is used in a python range: first one not to be used
def midi_scale_button_actions (root, scale, start_button, stop_button, what="onoff", channel=midi_channel, start_scale_offset=0 ):
    button_actions = {}
    for but_num in range(start_button, stop_button):
        button_actions[str(but_num)] = midi_note_actions(root, scale, but_num - start_button + start_scale_offset, what, channel)
    return button_actions

def ccn_range_button_actions (ccn, start_button, stop_button, what="pressrelease", ccv=127, channel=midi_channel):
    button_actions = {}
    for but_num in range(start_button, stop_button):
        button_actions[str(but_num)] = cc_actions(ccn, what, ccv, channel)
    return button_actions

pedal_down = {"send": "cc", "ccn": 64, "ccv": 127, "channel": 4}
pedal_up = {"send": "cc", "ccn": 64, "ccv": 0, "channel": 4}
pedal_actions = {"7": {"press": pedal_down, "release": pedal_up}}

fx_toggle_actions = {"6": cc_actions(91, "press", channel=1)}

sound_actions = {"4": midi_note_actions(22, "major", 0, what = "onoff", channel=0),
                "5": midi_note_actions(22, "major", 3, what = "onoff", channel=0)}


# scale D minor on real channel 6
scale_actions = midi_scale_button_actions(38, "minor", 0, 4, what="latch", channel=5)

all_actions = merge_two_dicts(merge_two_dicts(pedal_actions, scale_actions),  sound_actions)

print ("all actions", all_actions)

currently_pressed = []

while True:
    button = buttons.events.get()  # see if there are any key events
    if button:                      # there are events!
      key = str(button.key_number)
      action = all_actions.get(key, {})
      if button.pressed:
        currently_pressed.append(key)
        do_action(action.get("press", {}))
      if button.released:
        currently_pressed.remove(key)
        do_action(action.get("release", {}))



# Write your code here :-)
