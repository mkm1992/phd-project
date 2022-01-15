"""Solves a multiple knapsack problem using the CP-SAT solver."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from ortools.sat.python import cp_model



def create_data_model():
    """Create the data for the example."""
    data = {}
    weights = [48, 30, 42, 36, 36, 48, 42, 42, 36, 24, 30, 30, 42, 36, 36]
    values = [10, 30, 25, 50, 35, 30, 15, 40, 30, 35, 45, 10, 20, 30, 25]
    data['num_items'] = len(weights)
    data['all_items'] = range(data['num_items'])
    data['weights'] = weights
    data['values'] = values
    data['bin_capacities'] = [100, 100, 100, 100, 100]
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




def main():
    data = create_data_model()

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
        print_solutions(data, solver, x)


if __name__ == '__main__':
    main()