# rotary encoder sample code https://learn.adafruit.com/adafruit-i2c-qt-rotary-encoder/python-circuitpython
# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2022 Neradoc
#
# SPDX-License-Identifier: Unlicense

# LCD sample code  https://www.waveshare.com/wiki/Raspberry_Pi_Pico
# SPDX-FileCopyrightText: 2021 John Furcean
# SPDX-License-Identifier: MIT

# neopixel sample code https://learn.adafruit.com/circuitpython-essentials/circuitpython-neopixel
# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time
import board
from rainbowio import colorwheel
import waveshare_LCD1602
from adafruit_seesaw import seesaw, rotaryio, digitalio
import neopixel
import keypad
import analogio

import adafruit_midi
import usb_midi
from adafruit_midi.control_change  import ControlChange
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn

import busio



encoder_i2c = busio.I2C(board.GP5, board.GP4)    # Pi Pico RP2040

seesaw = seesaw.Seesaw(encoder_i2c, 0x36)

seesaw_product = (seesaw.get_version() >> 16) & 0xFFFF
print("Found product {}".format(seesaw_product))
if seesaw_product != 4991:
    print("Wrong firmware loaded?  Expected 4991")

# Configure seesaw pin used to read knob enc_button presses
# The internal pull up is enabled to prevent floating input
seesaw.pin_mode(24, seesaw.INPUT_PULLUP)
enc_button = digitalio.DigitalIO(seesaw, 24)

enc_button_held = False

encoder = rotaryio.IncrementalEncoder(seesaw)
last_position = None

pixel_pin = board.GP15
num_pixels = 5

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

button_pins = (board.GP16, board.GP17, board.GP18, board.GP19, board.GP20)
buttons = keypad.Keys(button_pins, value_when_pressed=False, pull=True)

potentiometer = analogio.AnalogIn(board.GP26)

state_colours = [
    {"r": 0, "g": 0, "b": 0},
    {"r": 255, "g": 255, "b": 255},
    {"r": 255, "g": 0, "b": 0},
    {"r": 0, "g": 255, "b": 0},
    {"r": 0, "g": 0, "b": 255},
    {"r": 255, "g": 150, "b": 0},
    {"r": 180, "g": 0, "b": 255},
    {"r": 0, "g": 255, "b": 255}
]

colour_state = 0

max_colour_state = len(state_colours)

midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1])

enc_button_msg = ""
position_msg = ""

button_handlers = {}

def clamp(n, minn, maxn):
    return min(max(n, minn), maxn)

class LCD:
    def __init__(self, line_1, line_2):
        lcd_i2c = busio.I2C(board.GP11, board.GP10)    # Pi Pico RP2040
        self.controller = waveshare_LCD1602.LCD1602(lcd_i2c, 16, 2)
        self.line_1 = line_1
        self.line_2 = line_2
        self.setRGB(255,255,255)
        self.show_text()

    def setRGB(self, r, g, b):
        self.controller.setRGB(r, g, b)

    def show_text(self):
        self.controller.clear()
        self.controller.setCursor(0, 0)
        self.controller.printout(self.line_1)
        self.controller.setCursor(0, 1)
        self.controller.printout(self.line_2)

    def cls(self):
        self.line_1 = ""
        self.line_2 = ""
        self.show_text()

    def set_line_1(self, line_1):
        self.line_1 = line_1
        self.show_text()

    def set_line_2(self, line_2):
        self.line_2 = line_2
        self.show_text()


lcd = LCD("Welcome", "Louise <3")

class Parameter:
    def __init__(self, num, config):
        self.num = num
        self.name = config["name"]
        self.min = 0
        self.max = 127
        if config["range"] == "bipolar":
            self.value = 64
        elif config["range"] == "unipolar":
            self.value = 0
        elif config["range"] == "boolean":
            self.value = 0

    def __str__(self):
        return self.name + ": " + str(self.value)

    def set(self, val):
        self.value = clamp(val, self.min, self.max)

    def get(self):
        return self.value



class Device:
    devices = []
    _active_device_num = None # the device number which expression pedal currently controls

    def active_device_num():
        return Device._active_device_num

    def active_device():
        device_num = Device.active_device_num()
        if device_num is None:
            return None
        return Device.devices[device_num]

    def expression_handler(expression_val):
        if Device.active_device() is None:
            return None
        return Device.active_device().expression_handler_sub(expression_val)

    def active_next_parameter():
        device = Device.active_device()
        if device:
            device.next_parameter()
        else:
            print ("No active device, cannot do next")

    def __init__(self, num, name, params=None, param_cc_base=None):
        self.num = num
        self.name = name
        self.pixel_num = num_pixels - num - 1
        self.state = 0
    # _active_parameter is the number of the parameter to be adjusted
        self._active_parameter = None
        button_handlers[num] = {"short": self.toggle_state_short, "long": self.toggle_state_long}
        if params:
            self._active_parameter = 0
            self.params = []
            param_num = 0
            for param in params:
                self.params.append(Parameter(param_num, param))
                self.send_param(param_num)
                param_num += 1
        if param_cc_base:
            self.param_cc_base = param_cc_base
        self.show_state()
        self.send_state()

    def active_parameter_num(self):
        return self._active_parameter

    def active_parameter(self):
        if self.active_parameter_num() is None:
            return None
        return self.params[self.active_parameter_num()]

    def next_parameter(self):
        if self.active_parameter_num() is None:
            return None
        self._active_parameter += 1
        if self._active_parameter >= len(self.params):
            self._active_parameter = 0
        self.show_state()

    def expression_handler_sub(self, val):
        if self.active_parameter() is None:
            return None
        param = self.active_parameter()
        if abs(val - param.get()) >=2:
            param.set(val)
            self.send_param(self.active_parameter_num())
#            midi.send(ControlChange(self.cc_param(self.active_parameter_num()), param.get()))
            self.show_state()

    def delta_handler(self, delta):
        if self.active_parameter() is None:
            print ("no active parameter for delta_handler")
            return None
        param = self.active_parameter()
        old_val = param.get()
        new_val = old_val + delta
        param.set(new_val)
        if param.get() != old_val:
            self.send_param(self.active_parameter_num())
#            midi.send(ControlChange(self.cc_param(self.active_parameter_num()), param.get()))
            self.show_state()

# states are: 0 (off); 1 (on with expression control)
    def show_state(self):
        colour_num = self.state
        device_num = Device.active_device_num()
        if device_num == self.num:
            device = Device.active_device()
            parameter_num = device.active_parameter_num() + 1
            colour_num += parameter_num
        state_colour = state_colours[colour_num]
        pixels[self.pixel_num] = ((state_colour['g'], state_colour['r'], state_colour['b']))
        pixels.show()
        if device_num == self.num:
            lcd.set_line_1(self.name)
            if not(self.active_parameter_num() is None):
                lcd.set_line_2(str(self.params[self.active_parameter_num()]))
# change LCD/LED colour to match parameter number

    def send_state(self):
        if self.state > 0:
            new_ccv = 0 # turn off bypass
            self.send_all_params()
        else:
            new_ccv = 127 # turn on bypass
        midi.send( ControlChange(self.cc_onoff(), new_ccv))
#        print ("Sent ", new_ccv , " to " , self.cc_onoff())

    def send_param(self, param_num):
        param = self.params[param_num]
        midi.send(ControlChange(self.cc_param(param_num), param.get()))

    def send_all_params(self):
        for param_num in range(len(self.params)):
            self.send_param(param_num)


    def toggle_state_short(self):
        if self.state == 0:
            self.state = 1
            self.add_expression()
        else:
            self.state = 0
            self.remove_expression()
        self.send_state()
        self.show_state()

    def toggle_state_long(self):
        if self.state == 0:
            self.state = 1
        if Device._active_device_num == self.num:
            self.remove_expression()
        else:
            self.add_expression()
        self.send_state()
        self.show_state()

    def remove_expression(self):
        Device._active_device_num = None
        for device in Device.devices:
            device.show_state()

# auto_select_expression used to be called by default during remove_expression. Maybe remove?
    def auto_select_expression(self):
        for other_device in Device.devices:
            if ((other_device != self) and (Device._active_device_num is None) and (other_device.state == 1)):
                Device._active_device_num = other_device.num



    def add_expression(self):
       Device._active_device_num = self.num
       for other_device in Device.devices:
           other_device.show_state()

    def cc_onoff(self):
        return 80 + self.num

# param_num starts at 0
    def cc_param(self, param_num):
        base = getattr(self, 'param_cc_base', 102 + self.num*4)
        return base + param_num


Device.devices.append(Device(0, "Pitch Shift", [{"name": "-8va", "range": "bipolar"},{"name": "+5th", "range": "unipolar"},{"name": "+10th", "range": "unipolar"}]))

Device.devices.append(Device(1, "Freeze", [{"name": "freeze", "range": "boolean"},{"name": "mix", "range": "bipolar"}]))

# for some unfathmoable reason CC 110 does not work when mapping to VST controls

Device.devices.append(Device(2, "DJF", [{"name": "cutoff", "range": "bipolar"},{"name": "resonance", "range": "bipolar"},], param_cc_base=111))

Device.devices.append(Device(3, "Valhalla", [{"name": "feedback", "range": "bipolar"},{"name": "mix", "range": "bipolar"},{"name": "delay", "range": "bipolar"}]))

Device.devices.append(Device(4, "Volume", [{"name": "level", "range": "bipolar"}]))


def update_lcd_colour(state):
    if state >= len(state_colours):
        print ("colour too big: " + str(state))
        return
    state_colour = state_colours[state]
    lcd.setRGB(state_colour['r'], state_colour['g'], state_colour['b'])
#    print("colour_state", str(state))
#    print(state_colour['r'], state_colour['g'], state_colour['b'])



def get_expression():
    return int(potentiometer.value*127/65535)

currently_pressed = []
last_pressed = {}

last_expression_pedal = get_expression()

print ("button handlers ", button_handlers)

while True:
    # negate the position to make clockwise rotation positive
    position = -encoder.position
    if position != last_position:
        position_msg = "Position: {}".format(position)
        if Device.active_device():
            Device.active_device().delta_handler(position-last_position)
        else:
            print ("No active device", Device.active_device())
        last_position = position
        #lcd.set_line_1(position_msg)

    if not enc_button.value and not enc_button_held:
        enc_button_held = True
#        print("Encoder Button pressed")

    if enc_button.value and enc_button_held:
        enc_button_held = False
#        print("Encoder button released")
        Device.active_next_parameter()

    expression_pedal = get_expression()
    if abs(expression_pedal - last_expression_pedal)>=2:
        last_expression_pedal = expression_pedal
#        print("Expression pedal changed to ", expression_pedal)
        Device.expression_handler(expression_pedal)

    button = buttons.events.get()  # see if there are any key events
    if button:        # there are events!
      key = button.key_number
      key_str = str(button.key_number)
      if button.pressed:
        currently_pressed.append(key)
        last_pressed[key] = time.monotonic_ns()
#        print ("pressed ", key_str)
      if button.released:
        currently_pressed.remove(key)
#        print ("last pressed ",  (time.monotonic_ns() - last_pressed[key])/1000000000)
        release_time = (time.monotonic_ns() - last_pressed[key])/1000000000
        if key in button_handlers.keys():
            if release_time > 2 and "long" in button_handlers[key].keys():
#                print ("Calling long button handler")
                button_handlers[key]["long"]()
            else:
#                print ("Calling button handler")
                button_handlers[key]["short"]()
        else:
            print ("No handler for " , key)
            print ("type " , type(key))
            print (button_handlers.keys())
#        print ("released ", key)
