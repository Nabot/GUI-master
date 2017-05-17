#!/usr/bin/env python3
from ev3dev.ev3 import *

mA = LargeMotor('outA')
mB = MediumMotor('outB')
mD = LargeMotor('outD')

mA.stop()
mB.stop()
mD.stop()