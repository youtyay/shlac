# This fast-made shitty code allows you to convert ".shlac" into ".wav".
# Input your file names down here.
# Used libraries aren't made by me and the rights to the libraries belong to their respectful owners.
import numpy as np
import soundfile as sf


def shlac_to_wav(input_file):
    with open(input_file, 'rb') as f:
        sr = np.frombuffer(f.read(4), dtype='int32')[0]
        num_channels = np.frombuffer(f.read(1), dtype='int8')[0]
        audio_data = np.frombuffer(f.read(), dtype='float32')

    if num_channels == 2:
        audio_data = audio_data.reshape(-1, 2)
        audio_data_parts = np.array_split(audio_data, 2, axis=0)

        max_length = max(len(part) for part in audio_data_parts)
        audio_data_parts = [np.pad(part, ((0, max_length - len(part)), (0, 0))) for part in audio_data_parts]

        audio_data = np.vstack([part.flatten() for part in audio_data_parts]).T

        return sr, num_channels, audio_data

    return sr, num_channels, audio_data


file = 'audiofile.shlac'
sr_out, num_channels_out, audio_data_out = shlac_to_wav(file)

output = 'output.wav'
sf.write(output, audio_data_out, sr_out)

print(f"Sample rate: {sr_out}")
print(f"Channels amount: {num_channels_out}")
print(f"Converted into {output}")
