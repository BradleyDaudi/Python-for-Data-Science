{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "a2039a6c",
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
    "# Examples: String manipulation techniques\n",
    "© ExploreAI Academy"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "26af890c",
   "metadata": {},
   "source": [
    "In this train, we'll explore essential techniques like concatenation, replication, and slicing for effective string manipulation, as well as built-in methods that operate on string data types."
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
    "By the end of this example notebook, we should be able to:\n",
    "- Use manipulation techniques, including concatenation, replication, and slicing, to modify, combine, and extract information from strings.\n",
    "- Use built-in methods to manipulate strings."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d0f73a56",
   "metadata": {},
   "source": [
    "## Outline\n",
    "  1. [Introduction](#introduction)\n",
    "     * [Concatenation](#1-concatenation)\n",
    "     * [Replication](#2-replication)\n",
    "     * [Slicing](#3-slicing)\n",
    "  2. [Built-in string methods](#built-in-string-methods)\n",
    "     * [`upper()`](#1-upper)\n",
    "     * [`lower()`](#2-lower)\n",
    "     * [`capitalize()`](#3-capitalize)\n",
    "     * [`strip()`](#5-strip)\n",
    "     * [`replace()`](#6-replace)\n",
    "     * [`find()`](#7-find)\n",
    "  3. [Examples](#examples)\n",
    "     * [Example 1: String indexing](#example-1-string-indexing)\n",
    "     * [Example 2: String concatenation](#example-2-string-concatenation)\n",
    "     * [Example 3: String manipulation](#example-3-string-manipulation)\n",
    "     * [Example 4: String methods](#example-4-string-methods)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "babd9c9a",
   "metadata": {},
   "source": [
    "## Introduction\n",
    "\n",
    "String manipulation techniques refer to the various operations and methods used to modify, combine, or extract information from strings in a programming language. In the context of Python, here are some common string manipulation techniques:\n",
    "\n",
    "### 1. Concatenation\n",
    "\n",
    "String concatenation is the process of combining two or more strings into a single string. In Python, the `+` operator is used for concatenation. When we use the `+` operator with two strings, they are joined together, creating a new string that contains the characters of both original strings."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a5f88626",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello World\n"
     ]
    }
   ],
   "source": [
    "# Example: concatenation\n",
    "\n",
    "string1 = \"Hello\"\n",
    "string2 = \"World\"\n",
    "result = string1 + \" \" + string2\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "be0e209f",
   "metadata": {},
   "source": [
    "### 2. Replication\n",
    "\n",
    "String replication involves creating repeated patterns of a string. The `*` operator is used for replication. By multiplying a string with a number, we can generate a new string with multiple repetitions of the original string."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9b04ae42",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "PythonPythonPython\n"
     ]
    }
   ],
   "source": [
    "# Example: replication\n",
    "\n",
    "original_string = \"Python\"\n",
    "replicated_string = original_string * 3\n",
    "print(replicated_string)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f45f1aec",
   "metadata": {},
   "source": [
    "### 3. Slicing\n",
    "\n",
    "String slicing is the process of extracting specific portions of a string. It allows us to work with substrings and manipulate parts of a string as needed. Slicing in Python is done using square brackets `[]`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "bb817f87",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Python\n"
     ]
    }
   ],
   "source": [
    "# Example: slicing – positive indexing\n",
    "\n",
    "text = \"Python is amazing\"\n",
    "substring = text[0:6]\n",
    "print(substring)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "0534d531",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "amazin\n"
     ]
    }
   ],
   "source": [
    "# Example: slicing – negative indexing 1\n",
    "\n",
    "text = \"Python is amazing\"\n",
    "substring = text[-7:-1]\n",
    "print(substring)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b2f8372d",
   "metadata": {},
   "source": [
    "The index `-1` corresponds to the last character 'g' in \"amazing,\" and the index `-7` corresponds to the character 'a'. When we slice the string using `text[-7:-1]`, we include the character at index `-7` and exclude the character at index `-1`. Therefore, we get the substring \"amazin\" which includes the characters from 'a' to 'n' but excludes the last 'g'.\n",
    "\n",
    "To include the last character 'g', we can modify the slicing to `text[-7:]`, which means \"start from index -7 and go until the end of the string\"."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "7b74ffd5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "amazing\n"
     ]
    }
   ],
   "source": [
    "# Example: slicing – negative indexing 2\n",
    "\n",
    "text = \"Python is amazing\"\n",
    "substring = text[-7:]\n",
    "print(substring)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a3f4013e",
   "metadata": {},
   "source": [
    "## Built-in string methods\n",
    "\n",
    "In Python, built-in methods are pre-defined functions that operate on various data types, including strings. These methods provide a powerful set of tools for manipulating and transforming string data. Unlike standalone functions, methods are associated with specific data types and can be directly applied to instances of those types.\n",
    "\n",
    "Understanding and utilising built-in string methods is crucial for effective string manipulation. These methods streamline common operations, making code more concise, readable, and efficient. By leveraging these methods, developers can perform tasks such as modifying case, formatting, and joining strings with greater ease."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a3a48ea8",
   "metadata": {},
   "source": [
    "### 1. `upper()`\n",
    "\n",
    "The `upper()` method transforms all characters in a string to uppercase."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "9701e3e3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "HELLO, WORLD!\n"
     ]
    }
   ],
   "source": [
    "# Example: upper() method\n",
    "\n",
    "original_string = \"hello, world!\"\n",
    "uppercase_string = original_string.upper()\n",
    "print(uppercase_string)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4737e265",
   "metadata": {},
   "source": [
    "### 2. `lower()`\n",
    "\n",
    "The `lower()` method converts all characters in a string to lowercase."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "59ed7db6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello, world!\n"
     ]
    }
   ],
   "source": [
    "# Example: lower() method\n",
    "\n",
    "original_string = \"Hello, World!\"\n",
    "lowercase_string = original_string.lower()\n",
    "print(lowercase_string)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "abd2e84e",
   "metadata": {},
   "source": [
    "### 3. `capitalize()`\n",
    "\n",
    "The `capitalize()` method capitalises the first character of a string."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "07d0f447",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello, world!\n"
     ]
    }
   ],
   "source": [
    "# Example: capitalize() method\n",
    "\n",
    "original_string = \"hello, world!\"\n",
    "capitalised_string = original_string.capitalize()\n",
    "print(capitalised_string)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "03214909",
   "metadata": {},
   "source": [
    "### 4. `strip()` \n",
    "\n",
    "The `strip()` method is used to remove leading and trailing whitespaces from a string. This is particularly useful when dealing with user inputs or processing data from external sources."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "4cde1708",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This is a sentence with spaces.\n"
     ]
    }
   ],
   "source": [
    "# Example: strip() method\n",
    "\n",
    "raw_input = \"    This is a sentence with spaces.    \"\n",
    "trimmed_input = raw_input.strip()\n",
    "print(trimmed_input)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "139383e8",
   "metadata": {},
   "source": [
    "### 5. `replace()`\n",
    "\n",
    "The `replace()` method facilitates the substitution of specific substrings within a string. This is beneficial when we need to modify or update specific parts of a text.\n",
    "\n",
    "Utilising `replace()` is a common practice for dynamic content generation or when adapting text to different contexts."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "9669ddda",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "JavaScript is a powerful programming language.\n"
     ]
    }
   ],
   "source": [
    "# Example: replace() method\n",
    "\n",
    "original_text = \"Python is a powerful programming language.\"\n",
    "modified_text = original_text.replace(\"Python\", \"JavaScript\")\n",
    "print(modified_text)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e9ce2503",
   "metadata": {},
   "source": [
    "### 6. `find()`\n",
    "\n",
    "The `find()` method is employed to locate the index of a substring within a string. It returns the index of the first occurrence of the specified substring or `-1` if the substring is not found.\n",
    "\n",
    "This method is particularly handy for tasks such as parsing data or extracting specific information from strings based on known patterns."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "727aa3da",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "16\n"
     ]
    }
   ],
   "source": [
    "sentence = \"Searching for a keyword in this sentence.\"\n",
    "index = sentence.find(\"keyword\")\n",
    "print(index)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1db73ef4",
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
   "id": "0cf539d6",
   "metadata": {},
   "source": [
    "### Example 1: String concatenation\n",
    "\n",
    "Imagine we are building a greeting message generator. We have three strings: `greeting`, `name`, and `punctuation`. Our task is to concatenate these strings to create a personalised greeting message. The greeting and punctuation strings are fixed, but the name can vary."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "0d90954f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hey Alice!\n"
     ]
    }
   ],
   "source": [
    "greeting = \"Hey\"\n",
    "name = \"Alice\"\n",
    "punctuation = \"!\"\n",
    "\n",
    "#concatenation\n",
    "personalised_greeting = greeting + \" \" + name + punctuation\n",
    "\n",
    "print(personalised_greeting)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "771b5248",
   "metadata": {},
   "source": [
    "### Example 2: Replication \n",
    "\n",
    "We are developing a program that requires a repeated pattern of characters. We have a string pattern that needs to be repeated five times. Our task is to use string replication to achieve this."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "2ef3a03e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ABCABCABCABCABC\n"
     ]
    }
   ],
   "source": [
    "pattern = \"ABC\"\n",
    "\n",
    "# repetition\n",
    "repeated_pattern = pattern *5\n",
    "\n",
    "print(repeated_pattern)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fa74051e",
   "metadata": {},
   "source": [
    "### Example 3: String manipulation \n",
    "\n",
    "Given the string below:\n",
    "* Convert the entire string to uppercase.\n",
    "* Capitalise the first letter of the string.\n",
    "* Replace the word \"string\" with \"text.\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "ac2830fa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "PYTHON STRING MANIPULATION\n",
      "Python string manipulation\n",
      "python text manipulation\n"
     ]
    }
   ],
   "source": [
    "manipulation_string = \"python string manipulation\"\n",
    "\n",
    "#converting to uppercase\n",
    "uppercase = manipulation_string.upper()\n",
    "print(uppercase)\n",
    "#capitalizing each word\n",
    "capitalized = manipulation_string.capitalize()\n",
    "print(capitalized)\n",
    "# replacing\n",
    "replaced = manipulation_string.replace(\"string\", \"text\")\n",
    "print(replaced)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8c1f6b43",
   "metadata": {},
   "source": [
    "### Example 4: String methods \n",
    "\n",
    "Given the following string, replace all occurrences of \"apple\" with \"orange\", and print the result."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "7d539d1a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "orange pie, orange juice, orange tart\n"
     ]
    }
   ],
   "source": [
    "complex_string = \"apple pie, apple juice, apple tart\"\n",
    "\n",
    "# replacing\n",
    "new_complex = complex_string.replace(\"apple\", \"orange\")\n",
    "print(new_complex)"
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
