import math
import numpy as np
from timebudget import timebudget
import ipyparallel as ipp

iterations_count = round(1e7)

def complex_operation(input_index):
    print("Complex operation. Input index: {:2d}".format(input_index))

    [math.exp(i) * math.sinh(i) for i in [1] * iterations_count]

def complex_operation_numpy(input_index):
    print("Complex operation (numpy). Input index: {:2d}".format(input_index))

    data = np.ones(iterations_count)
    np.exp(data) * np.sinh(data)

@timebudget
def run_complex_operations(operation, input, pool):
    pool.map(operation, input)

client_ids = ipp.Client()
pool = client_ids[:]

input = range(10)
run_complex_operations(complex_operation, input, pool)
run_complex_operations(complex_operation_numpy, input, pool)
