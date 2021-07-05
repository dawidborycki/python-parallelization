import math
import numpy as np
from timebudget import timebudget
from multiprocessing import Pool

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

processes_count = 10

if __name__ == '__main__':
    processes_pool = Pool(processes_count)

    run_complex_operations(complex_operation, range(10), processes_pool)
    run_complex_operations(complex_operation_numpy, range(10), processes_pool)    