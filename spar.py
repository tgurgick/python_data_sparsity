#!/usr/bin/env python3

'''
STAND ALONE FUNCTION 
QUICK SPARSITY CALCULATION OF A GIVEN DATA SET FOR TWO VARIABLES
NOVEMBER 2018 

FUNCTION EXPLANATION
1. Imports data set from given path (NOTE: check current directory ($ pwd) to see where to start path)
		>>>> assumes structure of columns is line, variable A, variable B, varibale C 
2. Counts total data points available in the set (maximum otpions for 100% coverage)
3. Counts the uniques for variable A 
4. Counts the uniques for variable B
5. calculates sparsity by simply doing total / ((unqiue var A)*(unique var B))
'''

__author__ = "Trevor Gurgick"
__copyright__ = "Copyright (c) 2018, Trevor Gurgick"
__license__ = "GPL"
__version__ = "0.0.1"

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def calc(table):
	table.rename(columns = {list(table)[0]:'A',
		list(table)[1]:'B',
		list(table)[2]:'C'}, 
		inplace=True)
	column_a = table['A']
	column_b = table['B']
	n_total = float(len(table))
	n_col_a = float(len(np.unique(column_a)))
	n_col_b = float(len(np.unique(column_b)))
	sparsity = (n_total / (n_col_a * n_col_b)) * 100.0
	return float(sparsity)
	#print ("Sparsity of Dataset is", sparsity, "Percent")

if __name__ == '__main__':
	calc(table)
