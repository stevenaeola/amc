# Advanced Music Computation

## Sound design 2

---

## Previously

- Subtractive synthesis
- Modular synthesisers

---

## Coming up

- FM synthesis
- Sampling (inc granular, wavetable)
- Options for sound design
- Summary/Tips

---

## Sound Synthesis Techniques

- Additive - uncommon. Sine waves in electronics are hard
- Subtractive from 1970s e.g. [Minimoog](https://en.wikipedia.org/wiki/Minimoog) on [Pink Floyd](https://youtu.be/cWGE9Gi0bB0?si=5gvQkYuXl9wAKySN)
- Frequency Modulation from 1980s e.g. [DX7](https://en.wikipedia.org/wiki/Yamaha_DX7) on [Band Aid](https://youtu.be/bmj7KlIut1w?si=iGlbCDPS_-oKRAtp)
- Sampling from 1980s e.g. [Fairlight](https://en.wikipedia.org/wiki/Fairlight_CMI) on [Kate Bush](https://youtu.be/wp43OdtAAkM?si=bsbmOVkhrkL96T_w)
- Physical modelling from 1990s e.g. recently [Pianoteq](https://www.modartt.com/pianoteq_overview)

---

## Subtractive Synthesis (recap)

- Start with a "rich" oscillator: saw; square; triangle; noise
- Filter it with
  - Low pass filter (LPF)
  - High pass filter (HPF)
- Simple filters have
  - Cutoff frequency (Hz) usually variable
  - Attenuation/roll-off (dB per octave) often fixed
- Band pass filter (BPF) is a LPF/HPF combination
- Filters can have resonance: boost at cutoff

---

## Adding movement a constant sound

- On a modular synth you twiddle knobs 
- Filter sweeps (changes to cutoff) sound good
- Pulse Width Modulation (PWM) of square waves
- Change volume (tremolo)
- Change pitch (vibrato)
- Slightly de-tuned second (and third ...) oscillator
  - Interference patterns create beating

---

## Modulation

- Change things automatically
- Low Frequency Oscillator (LFO)
  - Typically below audio frequency
- Envelope generator
- In modular synth these are controlled with voltage (CV)
  - VCO Voltage Controlled Oscillator (V/oct, Hz/V)
  - VCF Voltage Controlled Filter
  - VCA Voltage Controlled Amplifier

---

## FM Synthesis

- Analogue synths can do frequency modulation (vibrato, [ring modulation](https://en.wikipedia.org/wiki/Ring_modulation))
- Introducing feedback into modulation becomes chaotic
- As modulation rates increase analogue circuits break down
- Digital implementation is more stable
- [Maths is more complex](https://www.soundonsound.com/techniques/introduction-frequency-modulation) than for AM

--- 

- Multiple sine-wave operators can be combined as carrier and modulator
- Up to six operators is fairly common
- Plenty of VSTs available inc free [dexed](https://www.kvraudio.com/product/dexed-by-digital-suburban)
- Closer to acoustic instrument sounds than subtractive: "brassy"; "bright"; "cliched"
- Very difficult to predict/program

---

## Sampling etc

- Record a sound and play it back when asked
- [Mellotron](https://en.wikipedia.org/wiki/Mellotron) used by [Beatles](https://en.wikipedia.org/wiki/Strawberry_Fields_Forever)
- Steve Reich did early work with tape including [It's Gonna Rain](https://youtu.be/Jsd50gJo5q4?si=XAcp0kQZlZWggAMN)

---

- Digital versions can replay changing pitch through changing speed [Fairlight](https://en.wikipedia.org/wiki/Fairlight_CMI)
- This also changes the length of sample sound
- [Granular](https://en.wikipedia.org/wiki/Granular_synthesis) handles this by changing speed of smaller grains
- [Wavetable](https://en.wikipedia.org/wiki/Wavetable_synthesis) synthesis generates waveform (one period) which evolve over time e.g. [vital](https://vital.audio/)
- Sample > grain > waveform

---

## Sampling exercise

- Choose three samples that sound interesting from [freesound](https://freesound.org/)
  - A short unpitched sound
  - A pitched note
  - A longer "soundscape"
- If necessary use [Audacity](https://www.audacityteam.org/) to trim, normalise, export in WAV
- Install it for use by [Strudel](https://strudel.cc/learn/samples/)
- Play the sample in Strudel
- Try manipulating the sample by changing the speed, start time and length

---

## Effects (FX)

- Delay (digital simple, analogue hard)
  - Flanger
  - Chorus
- Reverb (analogue/physical simpler, digital hard)
- Pitch-shifting (and other granular effects)
- Formants/vowels and vocoders
- Everybody likes [Valhalla Supermassive](https://valhalladsp.com/shop/reverb/valhalla-supermassive/)

---

## Options for sound design

- Analogue and digital standalone inc modular, guitar pedals
- Inside DAW with FX like delay and EQ modulated by LFO
- With VSTs from simple one-knob FX to beasts like [vital](https://vital.audio/) (free)
- Code your own high-level with [faust](https://faust.grame.fr/)
- Code your own low-level with [SuperCollider](https://supercollider.github.io/) (see [example](./bassdrone.scd)) or [WebAudio](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API)
- Build your own (cheap) hardware with [Hackaday Logic Noise](https://hackaday.com/tag/logic-noise/)

---

## Summary/Tips

- Lots of ways to do it: hardware/software; low-level/high-level; cheap/expensive
- Think about how to control it (or not: drone)
- Limit yourself: less is more
- Think about sounds together
  - distinct instruments in their own frequency range
  - stereo separation
- Keep sound design time separate from composition