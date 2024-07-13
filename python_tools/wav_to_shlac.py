# This fast-made shitty code allows you to convert ".wav" and several other audioformats into ".shlac".
# Input your file names down here.
# Used libraries aren't made by me and the rights to the libraries belong to their respectful owners.
import numpy as np
import librosa


def audio_to_shlac(file_path, output_file):
    y, sr = librosa.load(file_path, mono=False)

    # Get amount of channels
    num_channels = 1 if len(y.shape) == 1 else y.shape[0]

    # Creating and writing data into .shlac file
    with open(output_file, 'wb') as f:
        # Writing headers
        f.write(np.array(sr, dtype='int32').tobytes())
        f.write(np.array(num_channels, dtype='int8').tobytes())

        # Writing audiodata into .shlac file
        f.write(np.array(y, dtype='float32').tobytes())
        return sr, num_channels


file = 'input.wav'
output = 'audiofile.shlac'
sr_out, num_channels_out = audio_to_shlac(file, output)
print(f"Sample rate: {sr_out}")
print(f"Channels amount: {num_channels_out}")
print(f"Converted into {output}")
