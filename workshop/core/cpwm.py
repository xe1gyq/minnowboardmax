#!/usr/bin/env python

import mraa
import time

class Cpwm(object):

    def __init__(self):

        self.pwmo = mraa.Pwm(22)
        self.pwmo.period_us(70)
        self.pwmo.enable(True)

        self.pwms = mraa.Pwm(24)
        self.pwms.period_us(70)
        self.pwms.enable(True)

        self.value= 0.0

    def start(self):

        while True:
            self.pwmo.write(self.value)
            self.pwms.write(self.value)
            time.sleep(0.01)
            self.value = self.value + 0.01
            if self.value >= 2:
                self.value = 0.0
