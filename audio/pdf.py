from gtts import gTTS
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)  # speed
engine.setProperty('volume', 1.0)

text_arr=[]
with open("sailor.txt", "r", encoding="utf-8") as f:
    for line in f:
        line=line.strip()
        if line not in ["Summer","Fall","Autumn","Spring","Part One","Part Two"]:
            if line.strip().isdigit() is False:
                if len(line)>0:
                    text_arr.append(line)

# Join all strings into a single text
for i,text in enumerate(text_arr):
    print(text)

    engine.save_to_file(text,f"output_{f}.mp3")
    engine.runAndWait()
    if i ==5:
        break