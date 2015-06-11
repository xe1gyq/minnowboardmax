import mraa
import time

class Gpio(object):

    def __init__(self):
        self.gp = mraa.Gpio(21)
        self.gp.dir(mraa.DIR_OUT)

    def toggle(self):
        self.gp.write(1)
        time.sleep(1)
        self.gp.write(0)
        time.sleep(1)

# End of File
