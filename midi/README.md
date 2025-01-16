# Advanced Music Computation

## Interfacing and MIDI


## Coming up

- What Electronic Music is Made of
- Music Protocols
- MIDI note messages, setup and demo
- MIDI Control Change (CC) and other messages
- Limitations and extensions
- Alternatives
- Controllers
- MIDI and Tidal
- Other fun things to do with MIDI


## What Electronic Music is Made of

- Not all Electronic Music is Computational
- Not all Computational Music is Electronic
- But there is a big overlap
- How do you specify what notes to play when?
- How do you play specified notes e.g. a score?
- How do humans get involved?


## Music Protocols

- For communication
- But also for storage e.g. MIDI files (c.f. JSON) 
- Musical Instrument Digital Interface (MIDI)
  - And MIDI Polyphonic Expression (MPE)
- Open Sound Control (OSC)


## [MIDI](https://en.wikipedia.org/wiki/MIDI)

- Interchange standard from 1983 (1.0)
- Originally over serial 5-pin DIN (in, out and thru)
- MIDI over USB now common
- TRS jacks for serial sometimes used
- Also via bluetooth, ethernet


## MIDI messages

- One status byte followed by one or two data bytes
- Channel number is encoded in bottom nybble of status: 16 channels
- Channel voice messages e.g. note on and off
- Channel mode messages e.g. all notes off
- System messages e.g. timing clock


## MIDI basics

- "Note on" and "note off"
- Sent by a controller
- Played by an instrument
- Channel per instrument (with daisy-chaining for serial)
- First data byte for note value
- Second data byte for velocity
- Each in 7 bits i.e. 0-127
- If a "note off" is missed then note is "stuck on"


## MIDI setup

- Use DAW e.g. [Reaper](https://www.reaper.fm/) for routing
- A MIDI track has a source of data
  - MIDI piano roll or
  - MIDI controller (physical or virtual)
- MIDI controller e.g. sequencer sends a series of messages
- MIDI instrument can be virtual (VST) or physical (hardware synth)


## Demo


## MIDI Control Change (CC)

- Often sourced from external hardware (buttons/knobs)
- Used for performance expression/control
  - Piano sustain pedal
  - Overall volume
  - Modulation of filters
- [Official list](https://midi.org/midi-1-0-control-change-messages)


## Other MIDI messages

- Program control: select synth presets
- Aftertouch and pitch bend
- Time codes
- SysEx (vendor specific)


## MIDI limitations

- Resolution: 7 bits
  - Some controls can be "high resolution" i.e. 2 bytes
- 12 tone equal temperament
  - Can use pitch bend
- Serial: one note at a time
  - With fast serial like USB this is not audible


## MIDI 1.0 Extensions

- MIDI Polyphonic Expression (MPE) 2018
  - Per-note control of expression (not per-channel)
- MIDI 2.0 (2020/2023)
  - Increased resolution
  - Bidirectional
  - Profiles
  - Compatible with 1.0


## MIDI Alternatives

- Open Sound Control (OSC) 2002
  - Notes can be played in bundles
  - Time tags can be relative or absolute
  - High-resolution data
  - Symbolic naming
  - Used by SuperCollider (and hence Tidal)
- Control Voltage (CV) 1995 (Eurorack)
  - Continuous time and voltage range: analogue
  - Gates and triggers to turn things on and off
  - Used in (semi-)modular synthesisers


## Some MIDI controllers I have

- Arturia Keystep 37
Often used in [loopop review videos](https://youtu.be/I3iaHNIJFsg?si=hpDtUAKiLqwwQoyy)
- KORG SQ-1. Often used by [Hainbach](https://youtu.be/iyykGgOKj_Y?si=YpQKu-nq1MlqFnPk)
- Roli Seabord. One fan is [Andrew Huang](https://youtu.be/pSPJTMcpG98?si=6VKEU9r-_KV_QSGm)


## Tidal with MIDI

- SuperCollider can send and receive MIDI messages
- It converts these to and from OSC
- So [Tidal can work with MIDI](https://tidalcycles.org/docs/configuration/MIDIOSC/midi)
- Need to update your SuperCollider startup
- Send MIDI note on/off and CC values
- Read CC values e.g. for volume, filter control
- No easy way to read note on/off


## Other fun things to do with MIDI

- [Control acoustic instruments](https://youtu.be/oHUl6R8jRJ0?si=3m0PinoPjkrrwZaJ)
- [Adapt](https://discord.com/channels/778912359888060437/1072013045863301131) [hydra](https://hydra.ojack.xyz/) sketches
and other [WebMIDI](https://developer.mozilla.org/en-US/docs/Web/API/Web_MIDI_API) things