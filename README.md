#module_structure1
##1. Project description:

The goal is to know more about Tensors. The objective of the
project is to create a Python module that can perform various operations 
on 2-dimensional Pytorch Tensors.

##2. Tensor Calculator

The TensorCalculator module provides functions for common operations on two-dimensional tensors using PyTorch.

##3. Installation

To use the python tensor_operator.py you will have to install using the pip install
Using the following command in on your Conda environment for example

pip install -U git+https://github.com/jaimelhd/module_structure1.git

Then, in a new python file for example in Jupiter you will do the following:
You will have to import -> from module_structure1.tensor_operator import TensorCalculator

And initialize a TensorCalculator objetc.

tc = Tensor.calculator()

With these, you can start using the functions.

##Usage of the functions.
For  the zeros,ones and random tensors, you can use 

zeros_tensor = tc.tensor_zeros(3, 3)

print(zeros_tensor)

ones_tensor = tc.tensor_ones(2, 2)

print(ones_tensor)

random_tensor = tc.tensor_random(4, 4)

print(random_tensor)

If you want to visualize the result, you can print it.

And for the sum, product, flipped, blurred, and substraction.

You will intialize t1 and t2

t1 = torch.tensor([[1, 2], [3, 4]])

t2 = torch.tensor([[5, 6], [7, 8]])

And then aplly this to the functions

sum_result = tc.tensor_sum(t1, t2)

print(sum_result)

product_result = tc.tensor_product(t1, t2)

print(product_result)

flipped_tensor = tc.tensor_flip(t1, axis=0)

print(flipped_tensor)

blurred_tensor = tc.tensor_blur(random_tensor, kernel_size=3)

print(blurred_tensor)

subtraction_result = tc.tensor_subtract(t1, t2)

print(subtraction_result)


## 4. Error Handling

### Handling Size Mismatch

If you encounter an error message stating "Error! TENSOR must have the same size", it means that the input tensors provided to the tensor_sum or tensor_product
functions have different dimensions. 
Make sure to pass tensors with the same dimensions 
to these functions.

### Handling Invalid Inputs

If you provide invalid input to any of the functions, 
such as passing non-integer values or incorrect data types, 
you may encounter a TypeError or ValueError. Double-check that your inputs are in the correct format before calling the functions.

### Handling Other Errors

If you encounter any other errors or unexpected behavior, please check the documentation and make sure you are using the functions correctly. If the issue persists, feel free to open an issue in the repository or seek help from the community.


##5. Contributing

We welcome the contributions from the community.
If you'd like to contribute to this project, please follow these steps:

1. **Fork** the repository. Click on the Fork button.
2. **Clone** the repository. Use git clone to clone the repository.

    git clone https://github.com/jaimelhd/module_structure1.git 

3. Create a new branch
4. Make changes
5. Commit changes
6. Push
I recommend using Pycharm to make the changes.

7.Then pull request and merge it!

Thank you for contributing to the project!!!

##License

Under MIT license..








