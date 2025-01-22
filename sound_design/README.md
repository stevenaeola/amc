# Advanced Music Computation

## Sound design


## Previously

- Live coding with tidal
- Scales
- MIDI

## Coming up

- Fundamentals
- Subtractive synthesis
- FM synthesis
- Sampling (inc granular, wavetable)
- Options for sound design


## Fundamentals

- Sound is variation in air pressure audible 20Hz-20kHz
- Periodic/regular variation can be written as a sum of sines (Fourier)
- Frequency spectrum of a sound represents the amplitudes at different frequencies
- Spectrum distribution affects timbre
- Harmonics are integer multiples of fundamental frequency e.g. piano, violin, flute
- Inharmonic sounds have non-rational overtones e.g. drums, bells
- Electronic sound synthesis drives sound through voltage change


## Sound Synthesis Techniques

- Additive - uncommon. Sine waves in electronics are hard
- Subtractive from 1970s e.g. [Minimoog](https://en.wikipedia.org/wiki/Minimoog) 
- Frequency Modulation from 1980s e.g. [DX7](https://en.wikipedia.org/wiki/Yamaha_DX7) 
- Sampling from 1980s e.g. [Fairlight](https://en.wikipedia.org/wiki/Fairlight_CMI)
- Physical modelling from 1990s e.g. Karplus Strong, recently [Pianoteq](https://www.modartt.com/pianoteq_overview)


## Subtractive Synthesis

- Start with a "rich" oscillator: saw; square; triangle; noise
- Filter it with
  - Low pass filter (LPF)
  - High pass filter (HPF)
  - Band pass filter (BPF)
- Simple filters have
  - Cutoff frequency (Hz)
  - Attenuation/roll-off (dB per octave) 
- BPF is a LPF/HPF combination
- Filters can have resonance: boost at cutoff


## Adding movement a constant sound

- On a modular synth you twiddle knobs 
- Filter sweeps (changes to cutoff) sound good
- Pulse Width Modulation (PWM) of square waves
- Change volume (tremolo)
- Change pitch (vibrato)
- Slightly de-tuned second (and third ...) oscillator is good
  - Interference patterns create beating


## Modulation

- Change things automatically
- Low Frequency Oscillator (LFO)
  - Typically below audio frequency
- In modular synth these are controlled with voltage (CV)
  - VCO Voltage Controlled Oscillator (V/oct, Hz/V)
  - VCF Voltage Controlled Filter
  - VCA Voltage Controlled Amplifier


## Gates, Triggers, Envelopes

- MIDI has note on/off
- When note is on the gate is open/high
- Triggers detect change in gate
- [Envelope](https://en.wikipedia.org/wiki/Envelope_(music)) is a continuous change (attack; decay; sustain; release)
  - Often mapped to volume
  - Also used with filter cutoff
  - Can trigger two different envelopes at once


## Modular analogue synths - pros

- "Warm"?
- Playable/hands-on
- Configurable
- [Eurorack](https://en.wikipedia.org/wiki/Eurorack) standard for power and physical housing
- "Cool"? Especially flashing lights


## Modular analogue synths - cons

- Expensive (try [VCV rack](https://vcvrack.com/) for emulation)
- Low polyphony
- No presets
- Tuning issues: warming up
- "Hot": high-ish voltage compared with other audio gear
- Need to generate CV for playing tunes

Lots can be done in software


## FM Synthesis

- Analogue synths can do frequency modulation (vibrato, [ring modulation](https://en.wikipedia.org/wiki/Ring_modulation))
- Introducing feedback into modulation becomes chaotic
- As modulation rates increase analogue circuits break down
- Digital implementation is more stable
- Multiple sine-wave operators can be combined as carrier and modulator
- Up to six operators is fairly common
- Plenty of VSTs available inc free [dexed](https://www.kvraudio.com/product/dexed-by-digital-suburban)
- Closer to acoustic instrument sounds than subtractive: "brassy" "bright" "cliched"


## Sampling etc

- Record a sound and play it back when asked
- [Mellotron](https://en.wikipedia.org/wiki/Mellotron) used by [Beatles](https://en.wikipedia.org/wiki/Strawberry_Fields_Forever)
- Digital versions can replay changing pitch through changing speed [Fairlight](https://en.wikipedia.org/wiki/Fairlight_CMI)
- This also changes the length of sample sound
- [Granular](https://en.wikipedia.org/wiki/Granular_synthesis) handles this by changing speed of smaller grains
- [Wavetable](https://en.wikipedia.org/wiki/Wavetable_synthesis) synthesis generates waveform (one period) which evolve over time
- Sample > grain > waveform


# Effects (FX)

- Delay (digital simple, analogue hard)
  - Flanger
  - Chorus
- Reverb (analogue simpler, digital hard)
- Pitch-shifting
- Formants/vowels and vocoders
- Everybody likes [Valhalla Supermassive](https://valhalladsp.com/shop/reverb/valhalla-supermassive/)


## Options for sound design

- Analogue and digital standalone inc modular, guitar pedals
- Inside DAW with FX like delay and EQ modulated by LFO
- With VSTs from simple one-knob FX to beasts like [vital](https://vital.audio/) (free)
- Code your own high-level with [faust](https://faust.grame.fr/)
- Code your own low-level with [SuperCollider](https://supercollider.github.io/) or [WebAudio](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API)
- Build your own (cheap) hardware with [Hackaday Logic Noise](https://hackaday.com/tag/logic-noise/)


## Summary/Tips

- Lots of ways to do it: hardware/software; low-level/high-level; cheap/expensive
- Think about how to control it (or not: drone)
- Limit yourself: less is more
- Think about sounds together
  - distinct instruments in their own frequency range
  - stereo separation
- Keep sound design time separate from composition