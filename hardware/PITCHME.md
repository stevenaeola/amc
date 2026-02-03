# Music Hardware with RPi Pico

---

## Pico

- Cheap as (cheaper than) chips
- Based on RP2040 microcontroller 32 bit dual core ARM 256GB RAM
- Connect via USB micro for PC and/or power connection
- GPIO ([GPIO numbers are not pin numbers](https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf))
- Analog-digital conversion
- SPI and I2C parallel/serial
- Pulse-width modulation
- PIO state machines

---

## Electricity and ways to break it

- Avoid short circuit: low resistance between positive and ground
- Low-resistance devices include wires, switches and diodes (inc LEDs)
- Make sure you know how breadboard connections work
- But in the end, if it fries it fries

---

## Python and ways to program it

- CircuitPython not MicroPython (Similar but different)
- MIDI support better in CircuitPython
- Tutorial at [adafruit](https://learn.adafruit.com/welcome-to-circuitpython) or [youtube](https://www.youtube.com/@BuildWithProfG)
- [Mu editor](https://codewith.mu/) (archived) or Visual Studio Code with [extension](https://learn.adafruit.com/using-the-circuitpython-extension-for-visual-studio-code/overview) 
- [Download](https://circuitpython.org/downloads?q=pico) and [install](https://learn.adafruit.com/pico-w-wifi-with-circuitpython/installing-circuitpython) firmware (.UF2) for Pico W

---

## Wire up an LED

- Light emitting diodes are directional valves (orientation)
- Need a resistor in series to limit current
- Connect Pico Power 3V3 out to +ve rail (usually red) on breadboard
- Connect Pico GND to -ve rail (usually black or blue)
- Try adding a button to turn it on or off
- Try programming [traffic lights](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/traffic-light-and-pedestrian-crossing)

---

## Inputs/Output

- Connect a button with a pull-up resistor to ground and a GPIO input
- Use a potentiometer (variable resistor) as a voltage divider
- Connect the wiper (centre pin) to an ADC input
- MIDI! Install the [adafruit library](https://circuitpython.org/libraries)
- Look at some of the MIDI [examples](./examples/)
