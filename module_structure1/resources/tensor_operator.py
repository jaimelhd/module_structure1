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
