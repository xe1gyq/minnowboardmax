#!/usr/bin/python

import argparse

#===============================================================================
# Main
#===============================================================================

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='MinnowBoard Max Workshop')
    parser.add_argument('-m', '--modules', help='Module Mode')
    parser.add_argument('-c', '--calamari', help='Calamari Mode')
    args = parser.parse_args()

    if args.modules == 'alive':

        from core.alive import Alive

        alive = Alive()
        alive.report()

    if args.modules == 'system':

        from core.system import System

        system = System()
        print system.cpuUser()
        print system.cpuSystem()

    if args.modules == 'mraa':

        from core.mraalib import MraaLib

        mraalib = MraaLib()
        mraalib.version()

    if args.modules == 'bpta':

        from core.bpta import Bpta

        bpta = Bpta()
        bpta.data()

    if args.modules == 'plotly':

        from core.plotlylib import PlotLyLib

        plotly = PlotLyLib()
        plotly.graph()

    if args.modules == 'gpio':

        from core.gpio import Gpio

        gpio = Gpio()
        gpio.toggle()

    if args.modules == 'pwm':

        from core.pwm import Pwm

        pwm = Pwm()
        pwm.start()

    if args.modules == 'i2c':

        from core.i2c import I2c

        i2c = I2c()
        i2c.read()

    if args.calamari == 'rgb':

        from core.crgb import Crgb

        crgb = Crgb()
        crgb.start()

    if args.calamari == '7seg':

        from core.c7seg import C7seg

        c7seg = C7seg()
        c7seg.start()

    if args.calamari == 'pwm':

        from core.cpwm import Cpwm

        cpwm = Cpwm()
        cpwm.start()

# End of File
