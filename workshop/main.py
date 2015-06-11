#!/usr/bin/python

import argparse

#===============================================================================
# Main
#===============================================================================

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='MinnowBoard Max Workshop')
    parser.add_argument('-m', '--modules', help='Module Mode')
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

# End of File
