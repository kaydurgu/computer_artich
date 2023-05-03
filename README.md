# computer_artich

# Team members
Bakytbek uulu Zhanbolot

# Boolean Function Optimizer

The Boolean Function Optimizer is a program that simplifies Boolean expressions by reducing them to their lowest number of terms using the Quine-McCluskey method. It is designed to help reduce the cost and complexity of circuits, especially when dealing with functions that have a large number of Boolean variables.

# User Interaction

The user interacts with the program through a user interface in which they can input the names of each Boolean variable and enter the truth table in the form of minterms. The program then performs the Quine-McCluskey method to simplify the function and outputs the result.

# Program Structure

The program follows a Model-View-Controller software design pattern. The user interface and controller are combined in the "UserInterface.py" file. This file receives input from the user and calls the "CalculateAnswer.py" file to perform the necessary calculations. The "CalculateAnswer.py" file uses methods from the "GetCoreMinterms.py" and "BooleanFunctionSimplifier.py" files to simplify the Boolean function. Once the calculation is complete, the answer is returned to the "UserInterface.py" file to be displayed to the user.

# Usage
To use the Boolean Function Optimizer, you need to have Python installed on your computer. Once you have Python installed, download the source code and run the "UserInterface.py" file. Follow the prompts to input the names of the Boolean variables and the truth table in the form of minterms. The program will then simplify the function and output the result.

# Conclusion
The Boolean Function Optimizer is a powerful tool for simplifying Boolean expressions. By reducing them to their lowest number of terms, it can help reduce the cost and complexity of circuits. Its user-friendly interface and straightforward design make it a valuable resource for anyone working with Boolean functions.


