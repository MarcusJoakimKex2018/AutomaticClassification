# -*- coding: utf-8 -*-
"""
@author: Marcus Östling, Joakim Lilja

Cell type accuracy distribution

Draw the histograms for each classifier.
Data from ../data/after1000runs.json
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
# Using sypder the file '../data/after1000runs.json' was
# copied into data as code.
with open('../data/after1000runs.json', 'r') as myfile:
    data2=myfile.read().replace('\n', '')

data = eval(data2)
'''

names = []
values = []

ditems = list(data.keys())
for k,v in data[ditems[0]].items():
    names.append(k)
    values.append(v[0]+v[1])
    print(k, str(v[0]+v[1]))

plt.xticks(rotation=-90)
plt.gcf().subplots_adjust(bottom=0.40)
plt.bar(names, values, align='center')
plt.title("Cell type distribution")
plt.ylabel('Number of cells')
plt.show()