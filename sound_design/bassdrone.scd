(
SynthDef("s1",
	{ |out = 0, freq = 110, mod = 0.0, pan=0, vibfreq = 10, vibdepth = 0, amp = 1 |
		var mul, z, panned, vib, depth, f;
		depth = Lag.kr(vibdepth, 10, 0.5);
		vib = 1 + SinOsc.kr(Lag.kr(vibfreq, 10), 0, depth, depth);
		mul = 0.2*Lag.kr(mod*vib,10.0)/3;
		f = freq; // * vib
		z =  amp*RLPF.ar(Mix.new([ LFTri.ar(f, mul:mul), LFTri.ar(f*1.005, mul:mul), LFTri.ar(f*0.997, mul:mul), Resonz.ar(WhiteNoise.ar(mul*64.0), f*2, 0.002)
		]) , vib*100);
		//z = Blip.ar(freq,harms,0.1);
		panned = Pan2.ar(z,pan);
		Out.ar(out, panned);
	}
).store
)



(
var amp, out, note_names, note_freqs, synths, sliders, slider1;
out = 28;
amp = 5;
note_names = ["E","C", "D", "Eb", "E", "F", "G", "A", "B","C", "D", "Eb", "E", "F",  "Fs", "G", "A", "Bb", "B", "C", "Cs", "D", "E", "F", "Fs", "G", "A", "Bb", "B", "C"];
note_freqs = [16, 24, 26, 27, 28, 29, 31, 33, 35, 36,  38, 39, 40, 41, 42,   43,  45,  46,  47,  48,  49,  50,   52,  53,  54,   55,  57, 58,  59, 60];
synths = Array.fill(note_freqs.size, {arg i; var s; s = Synth("s1"); s.set("freq", midicps(note_freqs[i])); s.set("out", out); s.set("amp", amp); s});

w=Window("Bass synth", Rect(100, 400, 400, 500));
w.view.decorator = FlowLayout(w.view.bounds);


sliders = Array.fill(note_freqs.size, {|j| var slider; slider = EZSlider(w, 300@30, note_names[j]++note_freqs[j], ControlSpec(0, 2),
	{|ez|  synths[j].set("mod", ez.value)});
	w.view.decorator.nextLine;
	slider;});

		//	ControlSpec(0, 2), {|ez|  synths[j].set("mod", ez.value);w.view.decorator.nextLine; slider ;
//sliders = Array.fill(note_freqs.size, {arg j; var slider; slider = EZSlider(w, 300@20, note_names[i],
//	ControlSpec(0, 2), {|ez|  synths[j].set("mod", ez.value);w.view.decorator.nextLine; slider})});

w.front;
)

