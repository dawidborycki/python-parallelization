import math
import numpy as np
from timebudget import timebudget
import ray

iterations_count = round(1e7)

@ray.remote
def complex_operation(input_index):
    print("Complex operation. Input index: {:2d}".format(input_index))

    [math.exp(i) * math.sinh(i) for i in [1] * iterations_count]

@ray.remote
def complex_operation_numpy(input_index):
    print("Complex operation (numpy). Input index: {:2d}".format(input_index))

    data = np.ones(iterations_count)
    np.exp(data) * np.sinh(data)

@timebudget
def run_complex_operations(operation, input):
    for i in input:
        operation.remote(i)  

ray.init(num_cpus=10, num_gpus=0)

input = range(10)
run_complex_operations(complex_operation, input)
run_complex_operations(complex_operation_numpy, input)
