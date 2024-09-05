import numpy as np
# (3,224,224)
def conv_layer(input, filters, biases, stride=(1, 1)):
    input_depth, input_height, input_width = input.shape
    filter_count, filter_depth, filter_height, filter_width = filters.shape
    output_height = (input_height - filter_height) // stride[0] + 1
    output_width = (input_width - filter_width) // stride[1] + 1
    output_depth = input_depth

    output_list = np.copy(biases)
    for n in range(filter_count):
        for i in range(output_height):
            for j in range(output_width):
                for k in range(output_depth):

                    start_i = i * stride[0]
                    start_j = j * stride[1]
                    filter = filters[n][k]
                    slice = input[k, start_i:start_i + filter_height, start_j:start_j + filter_width]
                    output_list[n, i, j] += np.sum(slice * filter)
    return output_list

def max_pooling(input, pool_size=(2, 2), stride=(1, 1)):
    input_height, input_width, input_depth = input.shape

    output_height = (input_height - pool_size[0]) // stride[0] + 1
    output_width = (input_width - pool_size[1]) // stride[1] + 1
    output_depth = input_depth

    output_layer = np.zeros((output_height, output_width, output_depth))
    for i in range(output_height):
        for j in range(output_width):
            for k in range(output_depth):
                start_i = i * stride[0]
                start_j = j * stride[1]

                slice = input[start_i:start_i + pool_size[0], start_j:start_j + pool_size[1],k]

                output_layer[i, j, k] = np.max(slice)
    return output_layer

input_matrix_2d = np.array([
    [1, 1, 1, 1, 1],
    [2, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 3, 1, 1, 6],
    [1, 1, 1, 1, 1]
])

input_matrix_3d = np.stack([input_matrix_2d] * 3)

filter_2d = np.array([[1,1,1],
     [1,1,2],
     [1,1,1]])

filter_3d = np.array(
    [[[[1, 1, 1],
  [1, 1, 2],
  [1, 1, 1]],

 [[1, 1, 1],
  [1, 1, 2],
  [1, 1, 1]],

 [[1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]]],

 [[[1, 2, 3],
  [1, 1, 2],
  [1, 1, 1]],

 [[1, 1, 1],
  [1, 1, 2],
  [1, 1, 1]],

 [[1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]]]])

# print(conv_layer(
# input_matrix_3d,
#     filter_3d,(1,1)))
#
# print(max_pooling(np.array([[1,1,1,1,1],
#      [2,1,1,1,1],
#      [1,1,1,1,1],
#      [1,3,1,1,6],
#      [1,1,1,1,1]]),(3,3),(1,1)))
input = np.array([[[1, 2, 3, 0, 1],
                   [4, 5, 6, 1, 2],
                   [7, 8, 9, 2, 3],
                   [1, 2, 3, 4, 5],
                   [0, 1, 2, 3, 4]]])

filters = np.array([[[[1, 0, -1],
                      [1, 0, -1],
                      [1, 0, -1]]],

                     [[[1, 0, -1],
                      [1, 0, -1],
                      [1, 0, -1]]]])
biases = np.array(
     [[[ -4.,  1.,  14.],
       [ -8.,   6.,  16.],
       [-12.,  -4.,   6.]],
      [[  4.,   0.,  14.],
       [ -3., 13.,  11.],
       [ -5.,  -5., -23.]]])

print(conv_layer(
input,
    filters,biases,(1,1)))