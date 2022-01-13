#!/usr/bin/env python3

import sys
import os
import numpy as np
import matplotlib.pyplot as plt
sys.path.append(os.path.abspath('..'))
moving_average = __import__('4-moving_average').moving_average

if __name__ == '__main__':
        data = [72, 78, 71, 68, 66, 69, 79, 79, 65, 64, 66, 78, 64, 64, 81, 71, 69,
                65, 72, 64, 60, 61, 62, 66, 72, 72, 67, 67, 67, 68, 75]
        days = list(range(1, len(data) + 1))
        m_avg = moving_average(data, 0.9)
        print(m_avg)
        plt.plot(days, data, 'r', days, m_avg, 'b')
        plt.xlabel('Day of Month')
        plt.ylabel('Temperature (Fahrenheit)')
        plt.title('SF Maximum Temperatures in October 2018')
        plt.legend(['actual', 'moving_average'])
        plt.show()


def halo(self, name, sound, num_legs=4):
    """ hvafdg tg wrth rht h

    Parameters
    ----------
    name : str
        The name of the animal
    sound : str
        The sound the animal makes
    num_legs : int, optional
        The number of legs the animal (default is 4)

    Returns
    -------
    list
        a list of strings used that are the header columns


This script requires that `pandas` be installed within the Python
environment you are running this script in.

    * get_spreadsheet_cols - returns the column headers of the file
    * main - the main function of the scrip

    @section{Parameters}
"""
