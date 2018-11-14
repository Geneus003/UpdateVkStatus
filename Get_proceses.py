# This function will get proceses
import os


def get_proc():
    print(os.getppid())

    data = [(int(p), c) for p, c in [x.rstrip('\n').split(' ', 1)
                                     for x in os.popen('ps h -eo pid:1,command')]]
    return data