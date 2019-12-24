# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 12:14:14 2019

@author: s.nouri
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
	
from random import *
randBinList = lambda n: [randint(0,1) for b in range(1,n+1)]

from ortools.sat.python import cp_model


def create_data_model(Num_var):
    """Create the data for the example."""
    data = {}
    weights = randBinList(Num_var)
    # weights = np.random.rand(Num_var) * 4
    values = weights
    data['num_items'] = len(weights)
    data['all_items'] = range(data['num_items'])
    data['weights'] = weights
    data['values'] = values
    data['bin_capacities'] = [10, 15,30]
    data['num_bins'] = len(data['bin_capacities'])
    data['all_bins'] = range(data['num_bins'])
    return data




def print_solutions(data, solver, x):
    """Display the solution."""
    total_weight = 0
    total_value = 0
    for b in data['all_bins']:
        print('Bin', b, '\n')
        bin_weight = 0
        bin_value = 0
        for idx, val in enumerate(data['weights']):
            if solver.Value(x[(idx, b)]) > 0:
                print('Item', idx, '-  Weight:', val, ' Value:',
                      data['values'][idx])
                bin_weight += val
                bin_value += data['values'][idx]
        print('Packed bin weight:', bin_weight)
        print('Packed bin value:', bin_value, '\n')
        total_weight += bin_weight
        total_value += bin_value
    print('Total packed weight:', total_weight)
    print('Total packed value:', total_value)
    return total_value




def main():
    data = create_data_model(Num_var)

    model = cp_model.CpModel()

    # Main variables.
    x = {}
    for idx in data['all_items']:
        for b in data['all_bins']:
            x[(idx, b)] = model.NewIntVar(0, 1, 'x_%i_%i' % (idx, b))
    max_value = sum(data['values'])
    # value[b] is the value of bin b when packed.
    value = [
        model.NewIntVar(0, max_value, 'value_%i' % b) for b in data['all_bins']
    ]
    for b in data['all_bins']:
        model.Add(value[b] == sum(
            x[(i, b)] * data['values'][i] for i in data['all_items']))

    # Each item can be in at most one bin.
    for idx in data['all_items']:
        model.Add(sum(x[idx, b] for b in data['all_bins']) <= 1)

    # The amount packed in each bin cannot exceed its capacity.
    for b in data['all_bins']:
        model.Add(
            sum(x[(i, b)] * data['weights'][i]
                for i in data['all_items']) <= data['bin_capacities'][b])

    # Maximize total value of packed items.
    model.Maximize(sum(value))

    solver = cp_model.CpSolver()

    status = solver.Solve(model)

    if status == cp_model.OPTIMAL:
       total_value = print_solutions(data, solver, x)
       return total_value

###################===========================================================
       
Num_Service = 3
Num_Server = 4
Num_Resource = 3
Num_var = Num_Resource * Num_Server * Num_Service

Itr = 1
Max_Service = 50
value = []
x = []
for Num_Service in range(Max_Service):
    Num_var = Num_Resource * Num_Server * Num_Service
    value = np.zeros((Itr,), dtype=int)
    for i in range(Itr):
        if __name__ == '__main__':
            total_value =  main()
        value[i] =(total_value)
    x.append(np.mean((value[Num_Service])))

y = np.arange(1, Max_Service + 1) * Num_Server * Num_Resource

plt.plot(y, x/y)
plt.xlabel('Num of Slices or Services')
plt.ylabel('Ratio of admitted Services')
    
