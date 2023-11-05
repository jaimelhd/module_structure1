import torch

__all__ = ['TensorCalculator']


class TensorCalculator():

    def __init__(self):
        return None

    # Return all ZEROS
    def tensor_zeros(self, dim_x, dim_y):
        zeros = torch.zeros([dim_x, dim_y])
        return zeros
    # Return all ONES
    def tensor_ones(self, dim_x, dim_y):
        ones = torch.ones([dim_x, dim_y])
        return ones
    #Random Tensor
    def tensor_random(self, dim_x, dim_y):
        random = torch.rand([dim_x, dim_y])
        return random
    #SUM of two tensors
    def tensor_sum(self, t1, t2):
        if t1.size() != t2.size():
            print("Error! TENSOR must have the same size.")
            return None
        else:
            sum_tensors = torch.add(t1, t2)
            return sum_tensors
    #MULTIPLICATION of two tensors
    def tensor_product(self, t1, t2):
        if t1.size() != t2.size():
            print("Error! TENSORS must have the same size.")
            return None
        else:
            product_tensors = torch.mul(t1, t2)
            return product_tensors
    #ADITTIONAL FUNCTIONS
    def tensor_flip(self, t1, axis=0):
        flipped_tensor = torch.flip(t1, [axis])
        return flipped_tensor

    def tensor_blur(self, t1, kernel_size):
        blur_kernel = torch.ones((kernel_size, kernel_size), dtype=torch.float32) / (kernel_size ** 2)
        return torch.nn.functional.conv2d(t1.unsqueeze(0).unsqueeze(0), blur_kernel.unsqueeze(0).unsqueeze(0))

    def tensor_subtract(self, t1, t2):
        if t1.size() != t2.size():
            print("Error: Both tensors must have the same size.")
            return None
        else:
            subtraction_tensor = torch.sub(t1, t2)
            return subtraction_tensor

