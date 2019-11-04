import snowboydecoder
from record import start_recording
from noise_filter import noise_filter
import os
import sys
import signal

interrupted = False

def detected():
    data, open_wave = start_recording()
    noise_filter(data, open_wave)
    global interrupted
    interrupted = True # signal to the detector to stop after first detection

def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted


# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector("Klauba.pmdl", sensitivity=0.5)
print('Listening... Press Ctrl+C to exit')

# main loop
detector.start(detected_callback=detected,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

