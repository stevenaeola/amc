import pwmio
import board
import time
import random

# Construct PWM object, with first servo on GP0

pwm_pins = {0: board.GP0, 2: board.GP2, 4: board.GP4, 6: board.GP6, 8:board.GP8, 10:board.GP10}


pwm_freqs = {0: 220, 2:330, 4: 434, 6:392, 8: 438, 10: 440}
pwms = {}

for key in pwm_pins.keys():
    pwms[key] = pwmio.PWMOut(pwm_pins[key],frequency=pwm_freqs[key], variable_frequency=True)
    pwms[key].duty_cycle = 2 ** 15

# while True:
#     for i in range(20):
#         f = 438 + i/10.0
#         print ("f ", f)
#         pwms[0].frequency = f
#         time.sleep(0.5)




input("Hit enter to stop")
# Write your code here :-)
