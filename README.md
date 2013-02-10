RasPIR
------

Aim is get a Raspberry Pi to read from a simple 5v PIR sensor, maybe even
trigger the taking of a photo or something :)

The sensor is http://littlebirdelectronics.com/products/pir-motion-sensor

Obviously this'll be a Python project, using Python 2.7.3 on the Pi.

Usage
-----

Would be nice to be able to call with a IO pin and a command to run eg:

    ./raspir.py 11 logger Movement detected!

Dependencies
------------

    sudo apt-get install python-rpi.gpio