#Jaime López de Heredia
import torch


my_tensor = torch.tensor([[4, 1], [5,3], [2,1]])


# Return all ZEROS
zeros_tensor = torch.zeros_like(my_tensor)

print(zeros_tensor)

# Return all ONES
ones_tensor = torch.ones_like(my_tensor)

print(ones_tensor)

#Random Tensor
random_tensor = torch.randn((3, 2))

print(random_tensor)

#SUM of two tensors
my_tensor2 = torch.tensor([[5, 3], [6,1], [2,1]])

x = my_tensor + my_tensor2

print(x)


#MULTIPLICATION of two tensors

x = my_tensor * my_tensor2

print(x)

#ADITTIONAL FUNCTIONS
#1. GIRAR UN TENSOR
import torch

def tensor_flip(tensor, axis):
    """Voltea un tensor con un axis especifico"""

    return torch.flip(tensor, dims=(axis,))

my_tensor = torch.tensor([[1, 2], [3, 4]])

# Voltear el tensor a lo largo del primer eje (axis=0)
flipped_tensor = tensor_flip(my_tensor, axis=0)

print("Tensor original:")
print(my_tensor)

print("\nTensor dado la vuelta:")
print(flipped_tensor)



#2.
def tensor_blur(tensor, kernel_size):
    """ Creamos un filtro para que nos de el valor promedio.Es decir, el desenfoque"""

    blur_kernel = torch.ones((kernel_size, kernel_size), dtype=torch.float32) / (kernel_size**2)
    return torch.nn.functional.conv2d(tensor.unsqueeze(0).unsqueeze(0), blur_kernel.unsqueeze(0).unsqueeze(0))

my_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])

#Aplicamos desenfoque al tensor
blurred_tensor = tensor_blur(my_tensor, kernel_size=2)

print("Tensor Original:")
print(my_tensor)

print("\nTensor Desenfocado:")
print(blurred_tensor)
