# Advanced Music Computation
## Scales and harmony in Strudel 


Duplicate some rhythms with bd sd cp hh

- [sample 1](./sample1.mp3)
- [sample 2](./sample2.mp3)
- [sample 3](./sample3.mp3)


## Simple sound design

Design two sounds: one for bass, one for tune

- in strudel sidebar, choose sounds:synths and search for 'bass'
- try playing with some low notes e.g. `note("c2 g2").sound("gm_acoustic_bass")`
- tune sound, search for 'lead' and 'piano'. Play `note("c4 f4 bf4 ef4")`



## Audio effects

See <https://strudel.cc/learn/effects>
- change volume with `.postgain()` (1 is default)
- add reverb with `.room()` 0-1
- filter with `.lpf()` or `.hpf()` in Hz
- raise pitch by octave with `.add(12)`
- play parallel fifths with `.add("[0,7]")`


## Tune and bass

Happy birthday on piano fingers (counting from 0)

```
let melody = "[2 2 2 [1 2] 4 4 5 [4 2] 0 [2 1] 0 -1 0@4]/4"

let bass = "[0 _ _ 3 0 4 0 _]/4"
```

Play tune with

```
$: note(melody.scale("major")).sound("piano")
```

Add bass in another voice


## Chords and arpeggios

Add arpeggiated chords to bass notes (in separate voice) with

```
note("[0 4 7 4]*4".add(bass).scale("major")).sound("gm_acoustic_guitar_nylon")
```

What happens if you add the arp to the bass instead? Try `add.out()`

Try adding other notes into chord: replacement or extra

Move voices in the stereo field with `.pan()` default 0.5


## Make it sadder

In a major key The chords "ii" "iii" and "vi" are minor chords 

Try changing the bass line to use these notes

In functional harmony "vi" have the same function as "I"

"ii" has the same function as "IV"

"iii" can be function "I" or sometimes "V"


## Make it creepy

Try some [scalar mapping](https://youtu.be/raYkJq2eIlE?si=24LGSmMXhtxk9GSB)

See all the [available scales](https://github.com/tonaljs/tonal/blob/main/packages/scale-type/data.ts): care with spaces 

We will always be in the scale if we apply `scale` to a sequence

If we apply changes like `.add("[0,7,14]")` after scale we get [chromatic harmonic planing](https://youtu.be/tDPLt9u7gQ8?si=6hYjAKz_vHXcrwrx)


## Make it more complex

- Add non-integer speed-scaled versions of melody
- Add a polymetric sequence
- Add a drum sequence: with variations every n bars
- Drop parts with `_$:`
- Plan a structure for "performance"