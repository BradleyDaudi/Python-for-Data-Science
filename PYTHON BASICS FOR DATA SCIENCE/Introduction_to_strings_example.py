{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "12330396",
   "metadata": {},
   "source": [
    "<div align=\"center\" style=\" font-size: 80%; text-align: center; margin: 0 auto\">\n",
    "<img src=\"https://raw.githubusercontent.com/Explore-AI/Pictures/master/Python-Notebook-Banners/Examples.png\"  style=\"display: block; margin-left: auto; margin-right: auto;\";/>\n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f662d169",
   "metadata": {},
   "source": [
    "# Examples: Introduction to strings\n",
    "© ExploreAI Academy"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "26af890c",
   "metadata": {},
   "source": [
    "In this train, we'll explore Python strings and their creation as well as special character utilisation. We will also delve into the sequential nature of strings and their immutability."
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
    "In this example notebook we will be able to:\n",
    "- Create strings in Python using both single and double quotes, encompassing letters, numbers, symbols, and spaces.\n",
    "- Understand positive and negative indexing of strings, enabling the retrieval of individual characters using different counting directions.\n",
    "- Describe the immutability of strings in Python, realising that modifications to strings create new instances rather than altering existing ones."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "da8ebd5a",
   "metadata": {},
   "source": [
    "## Outline\n",
    "  1. [Introduction](#introduction)\n",
    "  2. [Characteristics of strings](#characteristics-of-strings)\n",
    "     * [Sequence of characters](#1-sequence-of-characters)\n",
    "     * [Immutable](#2-immutable)\n",
    "  3. [The `print()` function](#the-print-function)\n",
    "  4. [Special characters](#special-characters)\n",
    "  5. [Examples](#examples)\n",
    "     * [Example 1: String indexing](#example-1-string-indexing)\n",
    "     * [Example 2: String concatenation](#example-2-string-concatenation)\n",
    "     * [Example 3: String manipulation](#example-3-string-manipulation)\n",
    "     * [Example 4: String methods](#example-4-string-methods)\n",
    "  6. [Summary](#summary)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "841d60bd",
   "metadata": {},
   "source": [
    "## Introduction\n",
    "\n",
    "In Python, a string is a data type used to represent text. \n",
    "\n",
    "Strings in Python can be created using either single quotes (`'`) or double quotes (`\"`), and they can include letters, numbers, symbols, and even spaces."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fa11ed72",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Creating a string using single quotes.\n",
      "Creating a string using double quotes.\n"
     ]
    }
   ],
   "source": [
    "# Example: Creating a string variable\n",
    "\n",
    "single_quotes = 'Creating a string using single quotes.'\n",
    "double_quotes = \"Creating a string using double quotes.\"\n",
    "\n",
    "# Print the variables\n",
    "print(single_quotes)\n",
    "print(double_quotes)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8d2d26f7",
   "metadata": {},
   "source": [
    "## Characteristics of strings\n",
    "\n",
    "The two characteristics of strings in Python include:\n",
    "\n",
    "### 1. Sequence of characters\n",
    "\n",
    "A string in Python is fundamentally a sequence of characters. This means that a string is an ordered collection where each character has a specific position or index within the sequence. \n",
    "\n",
    "<div align=\"center\" style=\" font-size: 80%; text-align: center; margin: 0 auto\">\n",
    "    <img src=\"https://raw.githubusercontent.com/Explore-AI/Pictures/master/Python_strings.jpg\"  style=\"width:50%\";/>\n",
    "    <br>\n",
    "    <br>\n",
    "    <em>Figure 1: String – a sequence of characters</em>\n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1d4f741d",
   "metadata": {},
   "source": [
    "In Python, string indexing allows us to access individual characters within a string. \n",
    "\n",
    "Positive and negative indexing are two ways to reference characters in a string, and they provide different ways to count positions.\n",
    "\n",
    "<div align=\"center\" style=\" font-size: 80%; text-align: center; margin: 0 auto\">\n",
    "<img src=\"https://raw.githubusercontent.com/Explore-AI/Pictures/master/Python_string_indexing.jpg\"  style=\"width:50%\";/>\n",
    "<br>\n",
    "<br>\n",
    "    <em>Figure 2: Positive and negative indexing</em>\n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "144d29f3",
   "metadata": {},
   "source": [
    "**Positive indexing** starts from the beginning of the string, therefore, string characters are accessed from left to right.\n",
    "The first character has an index of 0, the second has an index of 1, and so on."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "2e6f5365",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Positive indexing:\n",
      "First character: H\n",
      "Second character: e\n",
      "Last character: !\n"
     ]
    }
   ],
   "source": [
    "# Example: positive indexing\n",
    "my_string = \"Hello, World!\"\n",
    "\n",
    "# Accessing characters using positive indexing\n",
    "first_char = my_string[0]\n",
    "second_char = my_string[1]\n",
    "last_char = my_string[12]\n",
    "\n",
    "print(\"Positive indexing:\")\n",
    "print(\"First character:\", first_char)\n",
    "print(\"Second character:\", second_char)\n",
    "print(\"Last character:\", last_char)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7ae306b9",
   "metadata": {},
   "source": [
    "**Negative indexing**, on the other hand, starts from the end of the string, which means that characters are accessed from right to left. The last character has an index of -1, the second-to-last has an index of -2, and so on."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f1031655",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Negative indexing:\n",
      "Last character: !\n",
      "Second last character: d\n",
      "First character: H\n"
     ]
    }
   ],
   "source": [
    "# Example: negative indexing\n",
    "# Accessing characters using negative indexing\n",
    "last_char_negative = my_string[-1]\n",
    "second_last_char = my_string[-2]\n",
    "first_char_negative = my_string[-13]\n",
    "\n",
    "print(\"\\nNegative indexing:\")\n",
    "print(\"Last character:\", last_char_negative)\n",
    "print(\"Second last character:\", second_last_char)\n",
    "print(\"First character:\", first_char_negative)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ebc41121",
   "metadata": {},
   "source": [
    "Using both positive and negative indexing provides flexibility when working with strings, allowing us to choose the most convenient direction based on our specific task. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bf88f39c",
   "metadata": {},
   "source": [
    "### 2. Immutable \n",
    "\n",
    "Strings in Python are immutable, meaning that once a string is created, it cannot be changed. However, we can create new strings based on the original one.\n",
    "\n",
    "For example, attempting to modify a character at a specific index in the string will raise a `TypeError` because strings do not support item assignment, which means we cannot change or modify individual characters of a string once it has been created."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "99fab222",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'str' object does not support item assignment",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[4], line 6\u001b[0m\n\u001b[0;32m      3\u001b[0m original_string \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mHello, World!\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m      5\u001b[0m \u001b[38;5;66;03m# The line below gives an error\u001b[39;00m\n\u001b[1;32m----> 6\u001b[0m \u001b[43moriginal_string\u001b[49m\u001b[43m[\u001b[49m\u001b[38;5;241;43m0\u001b[39;49m\u001b[43m]\u001b[49m \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mh\u001b[39m\u001b[38;5;124m'\u001b[39m\n",
      "\u001b[1;31mTypeError\u001b[0m: 'str' object does not support item assignment"
     ]
    }
   ],
   "source": [
    "# Example: immutability\n",
    "\n",
    "original_string = \"Hello, World!\"\n",
    "\n",
    "# The line below gives an error\n",
    "original_string[0] = 'h'"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "af8a6b0a",
   "metadata": {},
   "source": [
    "Since we cannot modify a string in place, any operation that seems to modify a string actually creates a new string with the modified content. For example, concatenation or slicing operations result in a new string."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "d34f3d77",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello, World!\n"
     ]
    }
   ],
   "source": [
    "# Example: Creating a new string by concatenation\n",
    "\n",
    "original_string = \"Hello\"\n",
    "new_string = original_string + \", World!\"\n",
    "\n",
    "# Print the new variable\n",
    "print(new_string)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ba8ee6a7",
   "metadata": {},
   "source": [
    "But hold on, what if we modify the entire string instead of trying to change a specific character within the string? Wouldn't that mute the concept of immutability in strings?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "dd3474e8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello. World?\n"
     ]
    }
   ],
   "source": [
    "# Example: Modifying the entire string\n",
    "\n",
    "original_string = \"Hello, World!\"\n",
    "original_string = \"hello. World?\"\n",
    "\n",
    "# The variable's value has changed. \n",
    "# What does this mean for immutability in strings?\n",
    "print(original_string)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7900a140",
   "metadata": {},
   "source": [
    "In the same way we cannot modify individual characters in a string due to its immutability, we also cannot modify the original string in its entirety. Instead, we are creating a new string and assigning it to the variable `original_string`. \n",
    "\n",
    "Here's the breakdown:\n",
    "\n",
    "* `original_string = \"Hello, World!\"`\n",
    "  \n",
    "  This line creates a string object with the value `\"Hello, World!\"` and assigns it to the variable `original_string`.\n",
    "\n",
    "* `original_string = \"hello. World?\"`\n",
    "  \n",
    "  This line then creates a new string object with the value `\"hello. World?\"` and assigns it to the same variable `original_string`. \n",
    "  \n",
    "  This does not modify the original string `\"Hello, World!\"` in place. Instead, it *rebinds* the variable `original_string` to a new string object.\n",
    "\n",
    "* `print(original_string)`\n",
    "  \n",
    "  Consequently, this line prints the current value of `original_string`, which is the most recent string assigned to it: `\"hello. World?\"`."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ab1ec117",
   "metadata": {},
   "source": [
    "## The `print()` function\n",
    "\n",
    "The `print()` function in Python is a versatile tool that allows us to display information to the console. It is crucial for debugging, displaying results, and communicating with users. In this section, we will delve into the basics of using the `print()` function, showcasing its utility in printing both variables and strings, and how it can be employed for printing multiline outputs to enhance readability.\n",
    "\n",
    "The `print()` function is straightforward to use. It takes one or more arguments and prints them to the console. Let's start with a simple example:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "111a20d7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello, Python!\n"
     ]
    }
   ],
   "source": [
    "# Example: basic use of print()\n",
    "\n",
    "print(\"Hello, Python!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "87405a20",
   "metadata": {},
   "source": [
    "We'll often need to display the values stored in variables or combine them with strings for meaningful output."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "32c0b0c0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name: Alice\n",
      "Age: 25\n"
     ]
    }
   ],
   "source": [
    "# Example: combining strings and variables\n",
    "\n",
    "name = \"Alice\"\n",
    "age = 25\n",
    "\n",
    "print(\"Name:\", name)\n",
    "print(\"Age:\", age)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c5d38aa7",
   "metadata": {},
   "source": [
    "To enhance the readability of output, especially when dealing with complex information or structured data, multiline outputs are beneficial. Python allows for multiline strings using triple quotes (`'''` or `\"\"\"`):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "230fd81e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This is a multiline string.\n",
      "It spans multiple lines.\n",
      "Printed using the print() function.\n"
     ]
    }
   ],
   "source": [
    "# Example: printing multiline output\n",
    "\n",
    "multiline_text = '''This is a multiline string.\n",
    "It spans multiple lines.\n",
    "Printed using the print() function.'''\n",
    "print(multiline_text)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e553310b",
   "metadata": {},
   "source": [
    "## Special characters\n",
    "\n",
    "Special characters play a crucial role in enhancing the flexibility and expressiveness of strings. They are characters that, when included in a string, carry a specific meaning beyond their literal representation. Some common special characters include:\n",
    "\n",
    "| Character | Name | Function |\n",
    "|---|---|---|\n",
    "| '\\n' | Newline | Inserts a new line in a string. Useful for structuring text output or displaying information on separate lines. |\n",
    "| '\\t' | Tab | Creates horizontal spacing within a string. Valuable for aligning text or data in a visually organised manner. |\n",
    "| '\\\\' | Backslash | Acts as an escape character. Used when including special characters in a string without triggering their usual meaning. For example, to include a literal backslash in a string, we would use '\\\\'. |\n",
    "| '\\'' | Single quote | Used within strings declared with single quotes. Prevents confusion with the opening and closing of the string when a single quote needs to be included. |\n",
    "| '\"' | Double quote | Used within strings declared with double quotes. Prevents ambiguity and allows the inclusion of double quotes without prematurely ending the string. |\n",
    "| '\\r' | Carriage return | Moves the cursor to the beginning of the line without advancing to the next line. Useful for overwriting or modifying existing text. |\n",
    "| '\\b' | Backspace | Removes the preceding character. Often used for editing or correcting input. |\n",
    "| '\\a' | Alert | Produces an audible or visible alert. Its effectiveness may vary across different platforms. |\n",
    "| '\\ooo' | Octal representation | Represents a character using its octal value. For example, '\\110' represents the character 'H'. |\n",
    "| '\\xhh' | Hexadecimal representation | Represents a character using its hexadecimal value. For example, '\\x48' represents the character 'H'. |\n",
    "<div align=\"center\">\n",
    "    <em style=\"align:center\">Table 1: Special characters</em>\n",
    "</div>\n",
    "\n",
    "Understanding these special characters and their functions is crucial for effective string manipulation in Python."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "80ff1afe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello,\n",
      "World!\n"
     ]
    }
   ],
   "source": [
    "# Example: newline (\\n)\n",
    "\n",
    "print(\"Hello,\\nWorld!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "2b02b2c8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name:\tJohn\n",
      "Age:\t25\n"
     ]
    }
   ],
   "source": [
    "# Example: tab (\\t)\n",
    "\n",
    "print(\"Name:\\tJohn\\nAge:\\t25\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "3d9b0c47",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This is a backslash: \\\n"
     ]
    }
   ],
   "source": [
    "# Example: backslash (\\\\)\n",
    "\n",
    "print(\"This is a backslash: \\\\\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "8232f5d4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "He said, 'Hello!'\n"
     ]
    }
   ],
   "source": [
    "# Example: single quote (\\')\n",
    "\n",
    "print('He said, \\'Hello!\\'')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "74c03d27",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "She exclaimed, \"Wow!\"\n"
     ]
    }
   ],
   "source": [
    "# Example: double quote (\\\")\n",
    "\n",
    "print(\"She exclaimed, \\\"Wow!\\\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "ac06febb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Overwrite\r",
      "This text.\n"
     ]
    }
   ],
   "source": [
    "# Example: carriage return (\\r)\n",
    "\n",
    "print(\"Overwrite\\rThis text.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "28d20440",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Remove\b This\n"
     ]
    }
   ],
   "source": [
    "# Example: backspace (\\b)\n",
    "\n",
    "print(\"Remove\\b This\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "30728247",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This is an alert!\u0007\n"
     ]
    }
   ],
   "source": [
    "# Example: alert (\\a)\n",
    "\n",
    "print(\"This is an alert!\\a\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "86e348c2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Octal representation: H\n"
     ]
    }
   ],
   "source": [
    "# Example: octal representation (\\ooo)\n",
    "\n",
    "print(\"Octal representation: \\110\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "4dd4d2f3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hexadecimal representation: H\n"
     ]
    }
   ],
   "source": [
    "# Example: hexadecimal representation (\\xhh)\n",
    "\n",
    "print(\"Hexadecimal representation: \\x48\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2e1a6910",
   "metadata": {},
   "source": [
    "## Examples\n",
    "\n",
    "Now that we have gone through the theory, let's get our hands dirty by trying out some example problems! \n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d049b6d0",
   "metadata": {},
   "source": [
    "### Example 1: String indexing \n",
    "\n",
    "Given the string below, perform the following tasks:\n",
    "\n",
    "1. Print the third character of the string using positive indexing.\n",
    "2. Print the last character of the string using negative indexing.\n",
    "3. Print a substring that includes characters from index 6 to 10 (inclusive)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "815fe3c0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "t\n",
      "!\n",
      "IsAwe\n"
     ]
    }
   ],
   "source": [
    "challenge_string = \"PythonIsAwesome!\"\n",
    "\n",
    "#third character\n",
    "print(challenge_string[2])\n",
    "#last character\n",
    "print(challenge_string[15])\n",
    "#substrings from index  6 - 10\n",
    "print(challenge_string[6:11])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ed742409",
   "metadata": {},
   "source": [
    "### Example 2: String concatenation \n",
    "\n",
    "Concatenate these strings and print the result."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "c97f0814",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Programming is fun!\n"
     ]
    }
   ],
   "source": [
    "string1 = \"Programming\"\n",
    "string2 = \" is fun!\"\n",
    "\n",
    "# concatenation\n",
    "concat = string1 + string2\n",
    "print(concat)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0f202ce3",
   "metadata": {},
   "source": [
    "### Example 3: Special characters\n",
    "\n",
    "We are given the following information about special characters in strings. Using this knowledge, create a multiline string that includes the following information:\n",
    "\n",
    "* Your name and age on the first line.\n",
    "* A sentence with a newline character to separate lines.\n",
    "* A sentence with a tab character to align text.\n",
    "* A sentence containing a backslash character.\n",
    "* A sentence containing both single and double quotes.\n",
    "* A sentence using the carriage return character to overwrite part of the text.\n",
    "* A sentence with a backspace character to remove the preceding character.\n",
    "  \n",
    "Print the multiline string."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "eceb4c01",
   "metadata": {},
   "source": [
    "**Expected output:**\n",
    "\n",
    "`John, Age: 30`\n",
    "\n",
    "`This is a multiline string.`\n",
    " \n",
    "`Name:    John`\n",
    "\n",
    "`Age:     30`\n",
    "\n",
    "`This is a backslash: \\`\n",
    "\n",
    "`He said, 'Hello!'`\n",
    "\n",
    "`She exclaimed, \"Wow!\"`\n",
    "\n",
    "`Overwrite This text.`\n",
    "\n",
    "`Remove This`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "7d92cefc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "John, Age: 30\n",
      "This is a multiline string.\n",
      "Name:\tJohn\n",
      "Age:\t30\n",
      "This is a backslash: \\\n",
      "He said, 'Hello!'\n",
      "She exclaimed, \"Wow!\"\n",
      "Overwrite\r",
      "This text.\n",
      "Remove\b This\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Creating a multiline string using special characters\n",
    "multiline_string = '''John, Age: 30\n",
    "This is a multiline string.\n",
    "Name:\\tJohn\n",
    "Age:\\t30\n",
    "This is a backslash: \\\\\n",
    "He said, 'Hello!'\n",
    "She exclaimed, \"Wow!\"\n",
    "Overwrite\\rThis text.\n",
    "Remove\\b This\n",
    "'''\n",
    "\n",
    "# Printing the multiline string\n",
    "print(multiline_string)\n"
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
    "Strings in Python represent text and can be created with single or double quotes. They are sequences of characters, accessed through positive or negative indexing. Strings are immutable, meaning they can't be changed in place, but new strings can be created based on the original. The `print()` function is essential for displaying information. Special characters enhance string flexibility, and string manipulation includes techniques like concatenation, replication, and slicing. "
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
