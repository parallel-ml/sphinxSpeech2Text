import sys
from datetime import datetime

def log_speech_input(speech_input):
    with open("./output/log.txt", 'a') as f:
        line = speech_input
        time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        line = time + ': ' + line
        line = line.strip()
        f.write(line + '\n')

def process_speech_input(speech_input):
    print(speech_input)
    log_speech_input(speech_input)

if __name__ == "__main__":
    speech_input = sys.stdin.read()
    process_speech_input(speech_input)
