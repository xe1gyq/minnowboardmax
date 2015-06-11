#!/usr/bin/env python

import mraa
import time

class Pwm(object):

    def __init__(self):
        self.pwm = mraa.Pwm(22)
        self.pwm.period_us(70)
        self.pwm.enable(True)
        self.value= 0.0

    def start(self):

        while True:
            self.pwm.write(self.value)
            time.sleep(0.01)
            self.value = self.value + 0.01
            if self.value >= 2:
                self.value = 0.0
