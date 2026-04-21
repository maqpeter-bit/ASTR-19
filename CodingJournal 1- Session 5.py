# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 17:55:11 2026

@author: mrdan
"""
import numpy as np
from astropy.table import Table

def main():
    #This creates 1000 values between 0 and 2pi. 
    x = np.linspace(0, 2 * np.pi, 1000)
    
    y = np.sin(x)

    #Table creation here. 
    table = Table([x, y], names=('x', 'sin(x)'))

    # Print table
    print(table)

if __name__ == "__main__":
    main()