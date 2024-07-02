import time
import sys

songname = "\033[38;2;255;165;0m-- ตามใจ | fellow fellow --\033[0m"

lyrics = (
    ("ใช่ฉัน ใช่ฉันบ้างหรือเปล่า", 4.1),
    ("คล้ายคนที่รอบ้างหรือเปล่า", 3),
    ("คนที่เธออยากใช้คำว่าเรา", 3.9),
    ("คนที่เธออธิษฐานให้ได้เจอ", 3.5),
    ("ถ้าใจของเธอมีคำตอบ", 3.4),
    ("ใช้ใจนำทางก็พอ", 3.3),
    ("ถ้าฉันคือคนที่เธอเฝ้ารอ", 3.3),
    ("รู้ไว้เลย ฉันก็รอแค่เธอเหมือนกัน", 5.8),
)

for line, delay in lyrics:
    dpl = delay / len(line)
    for char in line:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(dpl)
    print('\n')

print(songname + '\n\n< Khian Code Gun />')
