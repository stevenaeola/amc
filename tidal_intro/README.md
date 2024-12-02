# Advanced Music Computation
## Introduction to Live Coding with Tidal 


`performing arts form and a creativity technique centred upon the writing of source code and the use of interactive programming in an improvised way`

[https://en.wikipedia.org/wiki/Live_coding](wikipedia)



![Anna Xambó live coding at the Noiselets microfestival in Barcelona](https://upload.wikimedia.org/wikipedia/commons/0/07/Anna_Xamb%C3%B3_live_coding_at_the_Noiselets_microfestival_in_Barcelona.jpg)

Photo by Helena Coll, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons


## Summary

- What is Live Coding?
- Live Coding Languages for Music
- Starting with Tidal
- (Slightly) Under the Hood
- Sequencing sounds
- Functions on Patterns
- Mini-notation


## What is Live Coding?


- Live i.e. performed
- Coding i.e. programming
- Usually music
- Typically performed with a PA and projected code
- Sometimes solo, sometimes ensemble
- Sometimes with live-coded graphics
- Perhaps niche/nerdy but definite [https://blog.toplap.org/](community)



## Live Coding Languages for Music

- [http://chuck.cs.princeton.edu/](ChucK (C-ish))
- [https://supercollider.github.io/](Supercollider (smalltalk))
- [https://sonic-pi.net/](SonicPi (ruby))
- [https://100r.co/site/orca.html](Orca (???))
- [https://tidalcycles.org/](Tidal Cycles (haskell))
- [https://strudel.cc/](Strudel (JS))
- [https://github.com/e-lie/renardo](Foxdot/Renaldo (python))


## Starting with Tidal

- Install
- Start SuperCollider
- Environment: VSC .tidal extension
- First sound: execute with ctrl-enter

``` d1 $ sound "bd"```

- Stop with ctrl-h or 

```hush```


## (Slightly) Under the Hood

- Tidal sends OSC messages to SuperCollider
- Ask SuperCollider to show OSC messages

```s.dumpOSC(1)```

- See what happens when you ask for a non-existent sound
- List of samples in [https://tidalcycles.org/docs/configuration/AudioSamples/default_library/](Default library)
- `d1` is the first of 16 numbered functions which send the parameter to audio
- `$` is for function application with brackets


## Sequencing sounds

- Nearly all strings are sequencable
- Sounds are spaced evenly over a cycle
- Some samples have more than one variant, select with colon e.g.

``` d1 $ sound "bd 808:3"```

- Set cycles per second with e.g. 

```setcps 0.6```


## Functions on Patterns

- A pattern is a function from time to value
- Patterns can be transformed with (higher-order) functions

```d2 $ fast 3 $ sound "blip"```

- Pattern transformation functions include: [https://tidalcycles.org/docs/reference/time/#speeding-up-slowing-down](slow); [https://tidalcycles.org/docs/reference/concatenation/#brak](brak); [https://tidalcycles.org/docs/reference/alteration/#degrade](degrade)
- See [https://tidalcycles.org/docs/reference/cycles](Tidal reference) for many more
- Pattern transformations can be applied selectively: [https://tidalcycles.org/docs/reference/conditions/#every](every); [https://tidalcycles.org/docs/reference/randomness/#the-sometimes-family](sometimes)


## Mini-notation and Combining Patterns

- Some pattern functions have shorthand in [https://tidalcycles.org/docs/reference/mini_notation](mini-notation)
- Interesting ones include Euclidean and polymetric patternms
- Add multiple simultaneous "tracks" by having d1, d2 etc
- Sequence more than one property at once e.g. sample number

```d1 $ s "808" # n "[1 2 3 4 5]/6"```

- `#` is shorthand for `|>` taking structure from left
- [https://tidalcycles.org/docs/reference/pattern_structure](Other ways of combining structure)


## Other stuff

- [https://tidalcycles.org/docs/reference/oscillators](Low-frequency oscillators)
- [https://tidalcycles.org/docs/reference/synthesizers](Synthesisers)
- [https://tidalcycles.org/docs/reference/audio_effects](Audio effects)
- [https://tidalcycles.org/docs/reference/transitions](Transitions)
- [https://tidalcycles.org/docs/reference/state_values](State)
- [https://tidalcycles.org/docs/reference/harmony_melody](Scales)
- [https://tidalcycles.org/docs/reference/samplers](Samplers) and [https://tidalcycles.org/docs/reference/sampling](Sampling)
- [https://tidalcycles.org/docs/configuration/MIDIOSC/midi/](MIDI)
- jux rev
