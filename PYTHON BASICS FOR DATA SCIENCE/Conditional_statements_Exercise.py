{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div align=\"center\" style=\" font-size: 80%; text-align: center; margin: 0 auto\">\n",
    "<img src=\"https://raw.githubusercontent.com/Explore-AI/Pictures/master/Python-Notebook-Banners/Exercise.png\"  style=\"display: block; margin-left: auto; margin-right: auto;\";/>\n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1ceab647",
   "metadata": {},
   "source": [
    "# Exercise: Conditional statements\n",
    "© ExploreAI Academy"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e80e6089",
   "metadata": {},
   "source": [
    "In this exercise, we practise using various conditional statements to solve problems."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Learning objectives\n",
    "\n",
    "In this train, we will practise:\n",
    "- Using `if`, `elif`, `else`, and nested conditions to make decisions in Python.\n",
    "- Applying logical and ternary operators for efficient conditional logic."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercises"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "51ad27d2",
   "metadata": {},
   "source": [
    "### Exercise 1\n",
    "\n",
    "Use conditional statements to categorise an animal based on its risk status. The program should define a variable, `individuals_in_wild` (representing the number of individuals in the wild), and use it to print the correct response based on the following categories: \n",
    "- `\"Critically Endangered\"` for less than `1000` individuals. \n",
    "- `\"Endangered\"` for `1000` to `5000` individuals. \n",
    "- `\"Vulnerable\"` for `5001` to `20000` individuals. \n",
    "- `\"Safe\"` for more than `20000` individuals.\n",
    "\n",
    "Assume there are `5500` leopards left in South Africa. Assign this number to `individuals_in_wild` and note what category they fall under."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Vulnerable\n"
     ]
    }
   ],
   "source": [
    "# insert code here\n",
    "individuals_in_wild = 5500\n",
    "\n",
    "if individuals_in_wild < 1000:\n",
    "    print('Critically Endangered')\n",
    "elif individuals_in_wild <= 5000:\n",
    "    print('Endangered')\n",
    "elif individuals_in_wild <= 20000:\n",
    "    print('Vulnerable')\n",
    "else:\n",
    "    print('Safe')\n",
    "      "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e15cb96e",
   "metadata": {},
   "source": [
    "### Exercise 2\n",
    "\n",
    " Use conditional statements to determine if a region is experiencing water scarcity. The program should store two variables: `rainfall` (the average annual rainfall in mm) and `population_density` (people per square km). It should print the appropriate message based on the following criteria to determine water scarcity:\n",
    "\n",
    "- `\"Severe Scarcity\"` if rainfall is less than `500`mm and population density is more than `500` people per square km.\n",
    "- `\"Moderate Scarcity\"` if both of the following are true:\n",
    "    - Rainfall is between `500`mm and `1000`mm, inclusive.\n",
    "    - Population density is between `200` and `500`, inclusive.\n",
    "- `\"No Scarcity\"` otherwise.\n",
    "\n",
    "Assume the annual `rainfall` is `205`mm and the `population_density` is `448` per square km."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "No Scarcity\n"
     ]
    }
   ],
   "source": [
    "rainfall = 205\n",
    "population_density = 448\n",
    "\n",
    "# Check if there is water scarcity\n",
    "if rainfall < 500 and population_density > 500:\n",
    "    print(\"Severe Scarcity\")\n",
    "elif 500 <= rainfall <= 1000 and 200 <= population_density <= 500:\n",
    "    print(\"Moderate Scarcity\")\n",
    "else:\n",
    "    print(\"No Scarcity\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "926e46eb",
   "metadata": {},
   "source": [
    "### Exercise 3\n",
    "\n",
    "To assist a recycling initiative, write code that will categorise items based on their `material` type and `size`, and output the category of recycling.\n",
    "\n",
    "The program should store two variables, `material` and `size`, which can have 4 and 3 possible values, respectively:\n",
    "- `material` – possible inputs: `\"paper\"`, `\"plastic\"`, `\"metal\"`, `\"glass\"`\n",
    "- `size` – possible inputs: `\"small\"`, `\"medium\"`, `\"large\"`\n",
    "\n",
    "Output the category of recycling: \n",
    "- `\"Special Handling\"` for large metal or glass items. \n",
    "- `\"Standard Recycling\"` for all medium-sized items and small metal or glass items. \n",
    "- `\"Composting\"` for small paper items. \n",
    "- `\"Landfill\"` for small plastic items and all other cases."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Special Handling\n"
     ]
    }
   ],
   "source": [
    "material = \"glass\"\n",
    "size = \"large\"\n",
    "\n",
    "# Check recycling category\n",
    "if size == \"large\" and (material == \"metal\" or material == \"glass\"):\n",
    "    print(\"Special Handling\")\n",
    "elif size == \"medium\" or (size == \"small\" and (material == \"metal\" or material == \"glass\")):\n",
    "    print(\"Standard Recycling\")\n",
    "elif size == \"small\" and material == \"paper\":\n",
    "    print(\"Composting\")\n",
    "else:\n",
    "    print(\"Landfill\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "314b69ed",
   "metadata": {},
   "source": [
    "### Exercise 4\n",
    "\n",
    "Write a program to evaluate the use of renewable energy sources in a household. The program should define a variable `solar` that stores whether or not a household uses solar (`True` or `False` values only). If a household does not use solar, print `\"Needs Improvement\"`. Otherwise, print `\"Eco-friendly\"`.\n",
    "\n",
    "Note: You must solve this exercise using `if not`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Eco-friendly\n"
     ]
    }
   ],
   "source": [
    "solar = True\n",
    "\n",
    "if not solar:\n",
    "    print(\"Needs Improvement\")\n",
    "else:\n",
    "    print(\"Eco-friendly\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fd22165c",
   "metadata": {},
   "source": [
    "### Exercise 5\n",
    "\n",
    "Write a program that issues an alert if deforestation in an area exceeds a certain threshold. Define a variable `deforestation_rate` (it can be any number between `0` and `1`). \n",
    "\n",
    "If the `deforestation_rate` is above `0.1`, print `\"High Alert\"`. If it is not, nothing should be printed."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "High Alert\n"
     ]
    }
   ],
   "source": [
    "deforestation_rate = 0.6\n",
    "\n",
    "if deforestation_rate > 0.1:\n",
    "    print(\"High Alert\")\n",
    "else:\n",
    "    pass"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "914eba02",
   "metadata": {},
   "source": [
    "### Exercise 6\n",
    "\n",
    "Develop a program to check the air quality index (AQI).\n",
    "\n",
    "The program should define a variable `aqi` (it can be any integer value between `0` and `300`). It should then use a ternary operator to print `\"Poor Air Quality\"` if `aqi` is above `100`, or `\"Good Air Quality\"` otherwise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Good Air Quality\n"
     ]
    }
   ],
   "source": [
    "aqi = 77\n",
    "\n",
    "# Use a ternary operator to check air quality\n",
    "print(\"Poor Air Quality\") if aqi > 100 else print(\"Good Air Quality\")"
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
   "version": "3.12.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
