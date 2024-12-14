# MLP with Custom Trainable Activation Functions from Scratch in JAX

This project demonstrates how to build a multi-layer perceptron (MLP) neural network from scratch using JAX, incorporating custom trainable activation functions. The goal is to showcase the implementation of flexible and customizable activation functions for neural networks and to train them using gradient descent with JAX's automatic differentiation capabilities.

## Key Features
- **Custom Trainable Activation Functions:** A generalized version of the Swish activation function is implemented and used in the MLP.
- **Gradient Descent Optimization:** The model is trained using gradient descent, with backpropagation handled by JAX's automatic differentiation.
- **End-to-End Training:** The project covers data preprocessing, model definition, training, and evaluation.
- **Visualization:** Loss curves and output functions are visualized to track training progress and approximation quality.

## Dataset
The project uses the [Iris dataset](https://www.tensorflow.org/datasets/community_catalog/huggingface/iris), a classic dataset for classification tasks, to train and evaluate the model.
