{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "1bc8fd93",
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
    "# Exercise: Basic Python loops\n",
    "© ExploreAI Academy"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "26af890c",
   "metadata": {},
   "source": [
    "In this notebook we will have the opportunity to solve some problems involving basic loops, helping you to master one of Python's core concepts. \n"
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
    "In this train we will learn:\n",
    "- How to create basic `for` and `while` loops\n",
    "- How to control the flow of loops"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2ab2650d",
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
    "### Exercise 1: Basic `for` loop\n",
    "\n",
    "**Objective:** Print each animal's name from the animals list using a `for` loop."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0e3acd00",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Great White Shark\n",
      "Blue Whale\n",
      "African Elephant\n",
      "Bald Eagle\n",
      "Orangutan\n",
      "Tiger\n",
      "Panda\n",
      "Koala\n"
     ]
    }
   ],
   "source": [
    "animals = ['Great White Shark', 'Blue Whale', 'African Elephant', 'Bald Eagle', 'Orangutan', 'Tiger', 'Panda', 'Koala']\n",
    "\n",
    "# Write a for loop to print each animal's name\n",
    "for animal in animals:\n",
    "    print(animal)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c2096612",
   "metadata": {},
   "source": [
    "### Exercise 2: `while` loop with condition\n",
    "\n",
    "**Objective:** Use a `while` loop to print numbers from 0 to 4.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "467fd84f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n"
     ]
    }
   ],
   "source": [
    "# Initialize a variable 'i' to 0\n",
    "i = 0\n",
    "\n",
    "# Write a while loop that prints 'i' and increments it by 1 each time, until it reaches 4\n",
    "i = 0\n",
    "while i < 5:\n",
    "    print(i)\n",
    "    i += 1\n",
    "    \n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5e825fe0",
   "metadata": {
    "vscode": {
     "languageId": "plaintext"
    }
   },
   "source": [
    "### Exercise 3: Using `break` in a loop\n",
    "\n",
    "**Objective:** Stop the loop once you find `Orangutan` in the animals list."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "3aba36fb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Great White Shark\n",
      "Blue Whale\n",
      "African Elephant\n",
      "Bald Eagle\n"
     ]
    }
   ],
   "source": [
    "# Write a for loop with a break statement to stop the loop when 'Orangutan' is found\n",
    "for animal in animals:\n",
    "    if animal == 'Orangutan':\n",
    "        break\n",
    "    print(animal)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ffee6d2c",
   "metadata": {},
   "source": [
    "### Exercise 4: Using `continue` in a loop\n",
    "\n",
    "**Objective:** Print all animals except 'Bald Eagle' using a for loop and continue statement."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "d1c33f26",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Great White Shark\n",
      "Blue Whale\n",
      "African Elephant\n",
      "Orangutan\n",
      "Tiger\n",
      "Panda\n",
      "Koala\n"
     ]
    }
   ],
   "source": [
    "# Write a for loop with a continue statement to skip 'Bald Eagle' and print other animals\n",
    "for animal in animals:\n",
    "    if animal == 'Bald Eagle':\n",
    "        continue\n",
    "    print(animal)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f02c2669",
   "metadata": {},
   "source": [
    "### Exercise 5: Using `pass` in a loop\n",
    "\n",
    "**Objective:** Create a loop that does nothing when 'Panda' is encountered, but prints other animals."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "a915748c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Great White Shark\n",
      "Blue Whale\n",
      "African Elephant\n",
      "Bald Eagle\n",
      "Orangutan\n",
      "Tiger\n",
      "Panda\n",
      "Koala\n"
     ]
    }
   ],
   "source": [
    "# Write a for loop with a pass statement for 'Panda' and print other animals\n",
    "for animal in animals:\n",
    "    if animal == \"panda\":\n",
    "        pass\n",
    "    else:\n",
    "        print(animal)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e9956efe",
   "metadata": {
    "tags": []
   },
   "source": [
    "## Summary\n",
    "\n",
    "These exercises provided practical experience with basic `for` and `while` loops in Python, as well as with loop control statements like `break`, `continue`, and `pass`. Through these exercises, you've seen how `for` loops are **ideal for iterating over a sequence**, `while` loops are used **when a condition determines the continuation of the loop**, `break` can be used to exit a loop immediately, `continue` skips the rest of the current loop iteration, and `pass` acts as a placeholder without affecting loop execution. "
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
   "version": "3.12.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}