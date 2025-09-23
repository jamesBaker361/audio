#!/usr/bin/env python3
import soundfile as sf
import numpy as np
import os

# Directory containing WAV files
wav_dir = "clips"
output_file = "combined.wav"

# Get all WAV files in sorted order
wav_files = sorted([os.path.join(wav_dir, f) for f in os.listdir(wav_dir) if f.endswith(".wav")],key=lambda x: int(x.split("_")[0].split("/")[1]))
print(wav_files)
exit()

if not wav_files:
    raise ValueError("No WAV files found in directory.")

# Read first file to get sample rate and number of channels
first_data, sr = sf.read(wav_files[0])
num_channels = 1 if first_data.ndim == 1 else first_data.shape[1]

# Open output file in write mode
with sf.SoundFile(output_file, mode='w', samplerate=sr, channels=num_channels, subtype='PCM_16') as out_f:
    for f in wav_files:
        data, sr_f = sf.read(f)
        if sr_f != sr:
            raise ValueError(f"Sample rate mismatch in {f}: {sr_f} != {sr}")
        # If mono vs stereo mismatch, convert
        if data.ndim != first_data.ndim:
            if data.ndim == 1 and num_channels == 2:
                data = np.stack([data, data], axis=1)
            elif data.ndim == 2 and num_channels == 1:
                data = data.mean(axis=1)
        out_f.write(data)

print(f"Combined {len(wav_files)} files into {output_file}")
