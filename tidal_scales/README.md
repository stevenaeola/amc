# Advanced Music Computation
## Scales and harmony in Tidal 


Duplicate some rhythms with bd sd cp hh

- [sample 1](./sample1.mp3)
- [sample 2](./sample2.mp3)
- [sample 3](./sample3.mp3)


## Simple sound design

Design two sounds: one for tune, one for bass

- bass sound from superhammond, moog, bass1:0 (or select from 29 others)
- tune sound from supercomparator, blip, supermandolin,  superpwm, gtr:0
- change volume with `# gain x` default 1.0


- add reverb with `# room y` (careful with volume)
- filter with `# djf x` default 0.5, low-pass lower, high-pass higher
- separate/smooth with `# legato x` default 1.0
- lower by octave with `|- note 12`



## Tune and bass

Jingle bells on piano fingers (counting from 0)

`setcps (80/(60*4))`

`melody = "[2 2 2 _ 2 2 2 _ 2 4 0 1 2 _ _ _ 3 3 3 3 3 2 2 2 2 1 1 2 1 _ 4 _]/4"`

`bass = "[0 _ 0 _ 3 0 4 _]/4"`

Play tune with

```
d1 $ note (scale "major" $ melody) 
   # sound "supercomparator"
```
Add bass in another voice


## Chords and arpeggios

Add arpeggiated chords to bass notes (in separate voice) with

```
d3 $ note (scale "major" "[0 4 7 4]*4") 
|+ note (scale "major" bass)
# sound "gtr:0"
```

Try adding other notes into chord: replacement or extra

Move voices in the stereo field with `# pan x` default 0.5


## Make it sadder

In a major key The chords "ii" "iii" and "vi" are minor chords 

Try changing the bass line to use these notes

In functional harmony "vi" have the same function as "I"

"ii" has the same function as "IV"

"iii" can be function "I" or sometimes "V"


## Change multiple things at once

Use `let ... in do ` for simultaneous changes


## Make it creepy

Try some [scalar mapping](https://youtu.be/raYkJq2eIlE?si=24LGSmMXhtxk9GSB)

See all the available scales in Tidal with `scaleList`

We will always be in the scale if we apply `scale` to a sequence

If we apply changes like `|+ note "[0,7,14]"` outside of scale we get [chromatic harmonic planing](https://youtu.be/tDPLt9u7gQ8?si=6hYjAKz_vHXcrwrx)


## Make it more complex

- Add non-integer speed-scaled versions of melody
- Add a polymetric sequence
- Add a drum sequence: with variations every n bars
- Drop parts with `mute n`/`unmute n` or solo with `solo`/`unsolo`
- Plan a structure for "performance"