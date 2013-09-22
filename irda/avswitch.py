#!/usr/bin/python2

import irtoy
import serial

with serial.Serial('/dev/ttyACM0') as serialdev:
    toy = irtoy.IrToy(serialdev)
    data = [0, 112, 0, 28, 0, 55, 0, 28, 0, 27, 0, 28, 0, 55, 0, 28, 0, 28, 0, 28, 0, 27, 0, 28, 0, 55, 0, 28, 0, 27, 0, 28, 0, 55, 0, 28, 0, 27, 0, 28, 0, 28, 0, 28, 0, 27, 0, 28, 0, 27, 4, 177, 0, 112, 0, 28, 0, 56, 0, 28, 0, 27, 0, 28, 0, 55, 0, 28, 0, 27, 0, 28, 0, 28, 0, 28, 0, 56, 0, 28, 0, 28, 0, 28, 0, 55, 0, 28, 0, 27, 0, 28, 0, 27, 0, 28, 0, 27, 0, 28, 0, 28, 4, 178, 0, 111, 0, 28, 0, 56, 0, 28, 0, 27, 0, 28, 0, 56, 0, 28, 0, 27, 0, 28, 0, 27, 0, 28, 0, 55, 0, 28, 0, 27, 0, 28, 0, 55, 0, 28, 0, 27, 0, 28, 0, 27, 0, 28, 0, 27, 0, 28, 0, 27, 4, 178, 0, 113, 0, 26, 0, 57, 0, 26, 0, 29, 0, 26, 0, 58, 0, 26, 0, 29, 0, 26, 0, 29, 0, 26, 0, 58, 0, 26, 0, 28, 0, 27, 0, 56, 0, 27, 0, 28, 0, 26, 0, 29, 0, 27, 0, 29, 0, 27, 0, 27, 4, 178, 0, 112, 0, 27, 0, 56, 0, 27, 0, 28, 0, 28, 0, 55, 0, 28, 0, 27, 0, 28, 0, 28, 0, 27, 0, 56, 0, 28, 0, 27, 0, 28, 0, 55, 0, 28, 0, 28, 0, 28, 0, 27, 0, 28, 0, 27, 0, 28, 0, 27, 4, 178, 0, 111, 0, 28, 0, 56, 0, 28, 0, 28, 0, 28, 0, 56, 0, 28, 0, 28, 0, 28, 0, 27, 0, 28, 0, 56, 0, 28, 0, 27, 0, 28, 0, 56, 0, 28, 0, 28, 0, 28, 0, 28, 0, 27, 0, 28, 0, 27, 0, 28, 4, 178, 0, 113, 0, 26, 0, 57, 0, 26, 0, 28, 0, 27, 0, 57, 0, 26, 0, 29, 0, 26, 0, 29, 0, 27, 0, 56, 0, 27, 0, 28, 0, 26, 0, 57, 0, 26, 0, 29, 0, 26, 0, 29, 0, 26, 0, 29, 0, 27, 0, 28, 255, 255]
    toy.transmit(data)
    print("sent data once")
