import math
import sys
import numpy


class Function:
    def __init__(self, choose):
        self.choose = choose

    def f(self, x):
        match self.choose:
            case 1:
                return 1 / (1 + math.exp(-x))
            case 2:
                if x < 0:
                    return x / 100
                if x > 1:
                    return x / 100
                return x
            case 3:
                if x < 0:
                    return (math.exp(x) - math.exp(-x)) / (100 * (math.exp(x) + math.exp(-x)))

    def f_for_vector_arrays(self, array):
        new_array = [0] * len(array)
        for i in range(len(array)):
            new_array[i] = Function.f(self, array[i])
        return new_array


class Matrix:
    def __init__(self, rows, cols, matrix):
        self.rows = rows
        self.cols = cols
        self.matrix = matrix

    def multiplication_with_vector(self, rows, array):
        if rows != self.cols:
            exit("rows != cols in multiplication")
        result = [0] * self.rows
        for i in range(self.rows):
            for j in range(self.cols):
                result[i] += array[j] * self.matrix[i][j]
        return result

    def sum_vector_arrays(self, a, b):
        if len(a)!=len(b):
            exit('err in sum vector arrays')
        c=[]
        for i in range(len(b)):
            c.append(a[i]+b[i])
        return c


class Network:
    def __init__(self, size, choose, inputs, func):
        self.network = []
        self.network.append(inputs)
        self.func = func
        weights_file = open("weights" + choose + ".txt")
        weights_file_string_array = weights_file.readlines()
        weights_file_array = []
        for i in range(len(weights_file_string_array)):
            weights_file_array.append(list(map(float, weights_file_string_array[i].split())))
        weights = []
        bios = []
        current_index = 0  # That's because final matrix is 3d, but file is 2d, so I need to convert 3d to 2d by
        # adding special index
        for i in range(len(size) - 1):
            bios.append(numpy.zeros((size[i + 1])))
            weights.append(numpy.zeros((size[i + 1], size[i])))
            for j in range(size[i + 1]):
                bios[i][j] = weights_file_array[current_index + j][0]
                for k in range(size[i]):
                    weights[i][j][k] = weights_file_array[current_index + j][k + 1]
            current_index += size[i + 1]
        self.weights = weights
        self.bios = bios
        weights_file.close()

    def forward_feed(self):
        for i in range(len(size) - 1):
            a = Matrix
            Matrix.__init__(a, size[i + 1], size[i], self.weights[i])
            b = self.network[i]
            self.network.append(Function.f_for_vector_arrays(self.func, Matrix.sum_vector_arrays(Matrix,Matrix.multiplication_with_vector(a, len(b), b), self.bios[i])))


cfg = sys.argv[1:]
inputs = list(map(float, cfg[-1].split()))
func = Function
Function.__init__(func, int(cfg[-2]))

while len(inputs) == int(cfg[0]):
    size = list(map(int, cfg[:-2]))
    Net = Network
    Network.__init__(Net, size, cfg[-2][:1], inputs, func)
    Network.forward_feed(Net)
    print(Net.network[-1])
    output_string = ''
    for x in Net.network[-1]:
        output_string += str(round(x)) + ' '
    print(f'Result: {output_string[:-1]}')
    inputs = list(map(float, input(f'Insert new input ( to stop press "Enter")\n').split()))
