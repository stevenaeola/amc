# Advanced Music Computation
## Introduction to Live Coding with Tidal {data-background-color=#7E317B}

---

`performing arts form and a creativity technique centred upon the writing of source code and the use of interactive programming in an improvised way`

[https://en.wikipedia.org/wiki/Live_coding](wikipedia)

---


![Anna Xambó live coding at the Noiselets microfestival in Barcelona](https://upload.wikimedia.org/wikipedia/commons/0/07/Anna_Xamb%C3%B3_live_coding_at_the_Noiselets_microfestival_in_Barcelona.jpg)

Photo by Helena Coll, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons

---

## Summary

- What is Live Coding?
- Live Coding Languages for Music
- Starting with strudel
- (Slightly) Under the Hood
- Sequencing sounds
- Functions on Patterns
- Mini-notation and Combining Patterns
- Other stuff

---

## What is Live Coding?

::: incremental

- Live i.e. performed
- Coding i.e. programming
- Usually music
- Typically performed with a PA and projected code
- Sometimes solo, sometimes ensemble
- Sometimes with live-coded graphics
- Perhaps niche/nerdy but definite [community](https://blog.toplap.org/)

:::

---

## Live Coding Languages for Music

- [ChucK (C-ish)](http://chuck.cs.princeton.edu/)
- [Supercollider (smalltalk)](https://supercollider.github.io/)
- [SonicPi (ruby)](https://sonic-pi.net/)
- [Orca (???)](https://100r.co/site/orca.html)
- [Tidal Cycles (haskell)](https://tidalcycles.org/)
- [Strudel (JS)](https://strudel.cc/)
- [Foxdot/Renaldo (python)](https://github.com/e-lie/renardo)

---

## Starting with Strudel

- Simpler than "older brother" tidal (still quite new)
- Go to <https://strudel.cc> (can install locally)
- Hit play (top right) and then stop
- Use keyboard shortcuts crtl+enter and ctrl+. to start/update and stop

```sound ("bd")```

- See [workshop](https://strudel.cc/workshop/getting-started/) and [discord](https://discord.com/invite/HGEdXmRkzT)

---

## (Slightly) Under the Hood

- Strudel uses [WebAudio](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API) by default
- Samples loaded on demand, not always instantaneous
- Can also use OSC (for SuperCollider) or MIDI 
- Sounds are created by samples or synthesisers
- Effects such as reverb, delay, filter, bitcrush can be included

---

## Sequencing sounds

- Nearly all strings are sequencable
- Sounds are spaced evenly over a cycle
- Some samples have more than one variant, select with colon e.g. `sound("agogo:2 agogo:3")`
- Set cycles per second with e.g. `setcps(0.6)`

---

## Functions on Patterns

- A pattern is a function from time to value
- Patterns can be transformed with functions

```sound("balafon").fast(3)```

- Pattern transformation functions include: [slow](https://strudel.cc/learn/time-modifiers/#slow); [euclid](https://strudel.cc/learn/time-modifiers/#euclid); [degrade](https://strudel.cc/learn/random-modifiers/#degrade); [rev](https://strudel.cc/learn/time-modifiers/#rev)
- See [Strudel reference](https://strudel.cc/functions/intro/) for many more
- Pattern transformations can be applied selectively: [firstOf](https://strudel.cc/learn/conditional-modifiers/#firstof); [sometimes](https://strudel.cc/learn/random-modifiers/#sometimes)
- Transformations can be applied in parallel: [jux](https://strudel.cc/learn/effects/#jux); [off](https://strudel.cc/learn/accumulation/#off)


---

## Mini-notation and Combining Patterns

- Some pattern functions have shorthand in [mini-notation](https://strudel.cc/learn/mini-notation/)
- Interesting ones include Euclidean and polymetric patterns
- Add multiple simultaneous "tracks" by using `$:` and silence with `$_:`


---

## Other stuff

- [Visual feedback](https://strudel.cc/learn/visual-feedback/)
- [Synthesisers](https://strudel.cc/learn/synths/)
- [Audio effects](https://tidalcycles.org/docs/reference/audio_effects)
- [Notes, scales and chords](https://strudel.cc/learn/tonal/)
- [Scales](https://tidalcycles.org/docs/reference/harmony_melody)
- [Signals (LFO)](https://strudel.cc/learn/signals/)
- [MIDI](https://strudel.cc/learn/input-output/)
- jux rev
