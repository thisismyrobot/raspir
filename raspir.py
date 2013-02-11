import os
import RPi.GPIO
import sys
import time


def monitor(pin, state, command):
    RPi.GPIO.setmode(RPi.GPIO.BOARD)
    RPi.GPIO.setup(pin, RPi.GPIO.IN)
    while True:
        input_value = RPi.GPIO.input(pin)
        if input_value == state:
            os.system(command)
        time.sleep(1)


if __name__ == '__main__':
    pin = command = state = None
    try:
        if len(sys.argv) < 4 or sys.argv[2].lower() not in ('low', 'high'):
            raise Exception
        pin = int(sys.argv[1])
        state = sys.argv[2].lower() == 'high'
        command = ' '.join(sys.argv[3:]).strip()
    except:
        print 'Usage: ./raspir.py [header pin (1-26)] [state (low/high)] [Command to run]'
        sys.exit(1)

    monitor(pin, state, command)

