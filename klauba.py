import snowboydecoder
from record import start_recording
from noise_filter import noise_filter
import os
import sys
import signal

interrupted = False
kill_script = False
def detected():
    global detector
    detector.terminate()
    print("Starting recording")
    data, open_wave = start_recording()
    open_wave.close()
    print("Recording complete")
    # print("Starting noise filter")
    # noise_filter(data, open_wave)
    # print("Noise filter complete")
    global interrupted
    interrupted = True # signal to the detector to stop after first detection

def signal_handler(signal, frame):
    global interrupted
    interrupted = True
    
    global kill_script
    kill_script = True


def interrupt_callback():
    global interrupted
    return interrupted


# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector("Klauba.pmdl", sensitivity=0.5)
print('Listening for Klauba...')

# main loop
detector.start(detected_callback=detected,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)
if kill_script:
    sys.exit(1) # the user hit cntrl-c
else:
    sys.exit(0) # the user did not hit cntrl-c
