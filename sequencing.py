from pydub import AudioSegment
import wave
import os
filename = 'StereoMadness.wav'
sound = AudioSegment.from_file(filename, format="mp3")
outfile = "output.wav"

# https://en.wikipedia.org/wiki/Sequence_(music)
# tonal sequence in this case

shift = 1
for i in range(shift, 100, shift):
    new_sample_rate = int(sound.frame_rate * (2.0 ** (i/12)))
    hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
    hipitch_sound = hipitch_sound.set_frame_rate(44100)
    hipitch_sound.export(f"{i}.wav", format="wav")
    if i % 12 == 0:
        break

infiles = [filename] + [str(i)+".wav" for i in range(1,13)]
data = []
for infile in infiles:
    w = wave.open(infile, 'rb')
    data.append( [w.getparams(), w.readframes(w.getnframes())] )
    w.close()
output = wave.open(outfile, 'wb')
output.setparams(data[0][0])
for i in range(len(infiles)):
    output.writeframes(data[i][1])
output.close()
for f in infiles[1:]:
    os.remove(f)