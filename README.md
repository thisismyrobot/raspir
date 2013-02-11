RasPIR
------

Aim is get a Raspberry Pi to read from a simple 5v PIR sensor, maybe even
trigger the taking of a photo or something :)

The sensor is http://littlebirdelectronics.com/products/pir-motion-sensor

Obviously this'll be a Python project, using Python 2.7.3 on the Pi.

Usage
-----

Would be nice to be able to call with a IO pin (1-26), a target state and a
command to run eg:

    sudo python raspir.py 11 low logger Movement detected!

Dependencies
------------

    sudo apt-get install python-rpi.gpio

Electronics
-----------

Will connect to P1-02 (5V), P1-06 (GND) and P1-03 (GPIO00). I've chosen P1-03 as
it has a built-in pull-up resistor to 3.3v so will work with the PIR sensor's
open-collector output.

Datasheets
----------

    PIR Sensor http://www.sparkfun.com/datasheets/Sensors/Proximity/SE-10.pdf