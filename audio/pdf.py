
from transformers import pipeline
from datasets import load_dataset
import soundfile as sf
import torch
import os

synthesiser = pipeline("text-to-speech", "microsoft/speecht5_tts")

embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
speaker_embedding = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)



text_arr=[]
with open("sailor.txt", "r", encoding="utf-8") as f:
    for line in f:
        line=line.strip()
        if line not in ["Summer","Fall","Autumn","Spring","Part One","Part Two"]:
            if line.strip().isdigit() is False:
                if len(line)>0:
                    text_arr.append(line)

# Join all strings into a single text

os.makedirs("clips")
for i,text in enumerate(text_arr):
    speech = synthesiser("Hello, my dog is cooler than you!", forward_params={"speaker_embeddings": speaker_embedding})

    path=os.path.join("clips",f"{i}_speech.wav")
    sf.write(path, speech["audio"], samplerate=speech["sampling_rate"])
    if i %100==0:
        print(f"{i}/{len(text_arr)}")