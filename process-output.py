import sys

def process_speech_input(speech_input):
    print(speech_input)

if __name__ == "__main__":
    speech_input = sys.stdin.read()
    process_speech_input(speech_input)
