{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "f514af7c",
   "metadata": {},
   "source": [
    "<div align=\"center\" style=\" font-size: 80%; text-align: center; margin: 0 auto\">\n",
    "<img src=\"https://raw.githubusercontent.com/Explore-AI/Pictures/master/Python-Notebook-Banners/Exercise.png\"  style=\"display: block; margin-left: auto; margin-right: auto;\";/>\n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f662d169",
   "metadata": {},
   "source": [
    "# Exercise: Data types and operators \n",
    "© ExploreAI Academy"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "26af890c",
   "metadata": {},
   "source": [
    "In this exercise, we'll get comfortable with using the different data types we've been introduced to as well as using the correct data types and operators to solve problems. \n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2d230d14",
   "metadata": {
    "tags": []
   },
   "source": [
    "## Learning objectives\n",
    "\n",
    "In this train, we will practise:\n",
    "- How to declare variables, perform basic arithmetic operations, and print results using Python.\n",
    "- String manipulation, type casting, and solving practical problems. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ee8320c9",
   "metadata": {},
   "source": [
    "## Outline\n",
    "\n",
    "1. [Exercises](#exercises)\n",
    "    * [Exercise 1](#exercise-1)\n",
    "    * [Exercise 2](#exercise-2)\n",
    "    * [Exercise 3](#exercise-3)\n",
    "    * [Exercise 4](#exercise-4)\n",
    "    * [Comprehensive exercise](#comprehensive-exercise)\n",
    "2. [Solutions](#solutions)\n",
    "    * [Exercise 1](#exercise-1)\n",
    "    * [Exercise 2](#exercise-2)\n",
    "    * [Exercise 3](#exercise-3)\n",
    "    * [Exercise 4](#exercise-4)\n",
    "    * [Comprehensive exercise](#comprehensive-exercise)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "997fefb3",
   "metadata": {},
   "source": [
    "## Exercises"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5a0b7683",
   "metadata": {
    "tags": []
   },
   "source": [
    "### Exercise 1\n",
    "\n",
    "Declare two variables, `num1` and `num2`, and assign them values of `15` and `7`, respectively. Calculate and store the result of their sum, difference, product, and division (as floating-point number), in separate variables. Print the newly created variables. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "b9c37c50",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "summation: 22\n",
      "product: 105\n",
      "difference: 8\n",
      "division: 2.142857142857143\n"
     ]
    }
   ],
   "source": [
    "#variables\n",
    "num1 = 15\n",
    "num2 = 7\n",
    "\n",
    "summation = num1 + num2\n",
    "print(\"summation:\", summation)\n",
    "\n",
    "product = num1 * num2\n",
    "print(\"product:\",product)\n",
    "\n",
    "difference = num1 - num2\n",
    "print(\"difference:\", difference)\n",
    "\n",
    "division = num1 / num2\n",
    "print(\"division:\", division)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a977d94e",
   "metadata": {},
   "source": [
    "### Exercise 2\n",
    "\n",
    "Create two string variables, `first_name` and `last_name`, with your first and last names. Concatenate them to form a full name and assign it to a new variable `full_name`. Print the `full_name` in uppercase.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "3f3a3085",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Full name in uppercase: JANE DOE\n"
     ]
    }
   ],
   "source": [
    "# Variable creation\n",
    "first_name = \"Jane\"\n",
    "last_name = \"Doe\"\n",
    "\n",
    "# String manipulation and concatenation\n",
    "full_name = first_name + \" \" + last_name\n",
    "\n",
    "# Display result in uppercase\n",
    "print(\"Full name in uppercase:\", full_name.upper())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7792ce08",
   "metadata": {},
   "source": [
    "### Exercise 3\n",
    "\n",
    "You have a variable `num_of_books` storing the number of books you have read this month, but it's currently in the form of a string. Create a new variable `books_read` by casting `num_of_books` to an integer. Then calculate the average number of books read per week, assuming there are four weeks in a month. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "3d61f181",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You have read an average of 3.75 books per week.\n"
     ]
    }
   ],
   "source": [
    "num_of_books = \"15\"\n",
    "\n",
    "# Casting to integer\n",
    "books_read = int(num_of_books)\n",
    "\n",
    "# Calculate average books read per week\n",
    "weeks_in_month = 4\n",
    "average_books_per_week = books_read / weeks_in_month\n",
    "\n",
    "# Print result\n",
    "print(\"You have read an average of \" + str(average_books_per_week) + \" books per week.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "23a20d64",
   "metadata": {},
   "source": [
    "### Exercise 4\n",
    "\n",
    "We have been given the following information about a person:\n",
    "\n",
    "- Name: John Doe\n",
    "- Age: 25\n",
    "- Height: 1.75 metres\n",
    "- Weight: 68.5 kilograms\n",
    "\n",
    "Create variables of appropriate data types to store this information. Then calculate the Body Mass Index (BMI) using the formula:\n",
    "\n",
    "$BMI = \\frac{{\\text{{Weight}}}}{{\\text{{Height}}^2}}$\n",
    "\n",
    "Print the result."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "7afdce29",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "John Doe's BMI is: 22.367346938775512\n"
     ]
    }
   ],
   "source": [
    "# Given information\n",
    "name = \"John Doe\"\n",
    "age = 25\n",
    "height = 1.75  # in metres\n",
    "weight = 68.5  # in kilograms\n",
    "\n",
    "# Calculate BMI\n",
    "bmi = weight / (height ** 2)\n",
    "\n",
    "# Print result\n",
    "print(str(name) + \"\\'s BMI is: \"+ str(bmi))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "33899903",
   "metadata": {},
   "source": [
    "### Comprehensive exercise\n",
    "\n",
    "You are tasked with creating a program to manage inventory for a store. The program should have the following features:\n",
    "\n",
    "1. Create variables to store the following information:\n",
    "   - Product name (string)\n",
    "   - Initial quantity in stock (integer)\n",
    "   - Price per unit (float)\n",
    "   - Discount percentage (float)\n",
    "\n",
    "2. Perform the following operations:\n",
    "   - Calculate the total value of the initial stock (quantity * price per unit).\n",
    "   - Apply the discount to the total value and calculate the discounted value of stock.\n",
    "   - Update the quantity in stock based on new stock received (assume a shipment of 30 units).\n",
    "\n",
    "3. Display the results:\n",
    "   - Print a summary message that includes the product name, initial quantity, price per unit, discount percentage, total value, discounted value, and the updated quantity in stock."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "1df2abb9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Product name: Widget XYZ\n",
      "Initial quantity: 100\n",
      "Price per unit: $ 12.5\n",
      "Discount percentage: 15.0 %\n",
      "\n",
      "--- Results ---\n",
      "Total value of initial stock: $ 1250.0\n",
      "Discounted value: $ 1062.5\n",
      "Updated quantity in stock: 130\n"
     ]
    }
   ],
   "source": [
    "# Given the variables\n",
    "product_name = \"Widget XYZ\"\n",
    "initial_quantity = 100\n",
    "price_per_unit = 12.50\n",
    "discount_percentage = 0.15\n",
    "\n",
    "# Calculate total value of initial stock\n",
    "total_value = initial_quantity * price_per_unit\n",
    "\n",
    "# Apply discount and calculate discounted price\n",
    "discounted_value = total_value - (total_value * discount_percentage)\n",
    "\n",
    "# Update quantity based on new shipment\n",
    "new_shipment = 30\n",
    "updated_quantity = initial_quantity + new_shipment\n",
    "\n",
    "# Display results\n",
    "print(\"Product name:\", product_name)\n",
    "print(\"Initial quantity:\", initial_quantity)\n",
    "print(\"Price per unit: $\", price_per_unit)\n",
    "print(\"Discount percentage:\", discount_percentage * 100, \"%\")\n",
    "\n",
    "print(\"\\n--- Results ---\")\n",
    "print(\"Total value of initial stock: $\", total_value)\n",
    "print(\"Discounted value: $\", discounted_value)\n",
    "print(\"Updated quantity in stock:\", updated_quantity)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "26fd094b-0fee-46f1-a4b8-73766813c42b",
   "metadata": {
    "tags": []
   },
   "source": [
    "#  \n",
    "\n",
    "<div align=\"center\" style=\" font-size: 80%; text-align: center; margin: 0 auto\">\n",
    "<img src=\"https://raw.githubusercontent.com/Explore-AI/Pictures/master/ExploreAI_logos/EAI_Blue_Dark.png\"  style=\"width:200px\";/>\n",
    "</div>"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}