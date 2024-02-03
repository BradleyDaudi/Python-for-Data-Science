{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "fa24daad",
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
    "# Examples: Dictionaries\n",
    "© ExploreAI Academy"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "26af890c",
   "metadata": {},
   "source": [
    "We have already briefly introduced dictionaries as a data structure. In this notebook, we'll be looking at further examples of how dictionaries can be used for storing and retrieving structured data. \n"
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
    "After working through these examples, we will:\n",
    "- Be able to create both regular and nested dictionaries\n",
    "- Be familiar with basic operations that can be performed on dictionaries\n",
    "- Have learnt how to access keys and values in a dictionary\n",
    "- Know the basic characteristics of dictionaries"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b4cf1ef8",
   "metadata": {},
   "source": [
    "## Examples"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "704eca69",
   "metadata": {},
   "source": [
    "### Example 1\n",
    "#### 1. Creating a very basic dictionary\n",
    "\n",
    "In their simplest form, dictionaries can be initialised by assigning empty curly brackets `{}` to a variable. This will create an empty dictionary, as illustrated by the output from the `type()` function below.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f4e8d64b",
   "metadata": {},
   "outputs": [],
   "source": [
    "our_first_dictionary = {}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "dc4e7058",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(our_first_dictionary)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "da66b3c3",
   "metadata": {},
   "source": [
    "In order to add key-value pairs to the dictionary, we have a few options. The first is by simply **assigning the value to the variable's key**. In our basic example, we want to associate the value, `first_value`, to the key, `first_key`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "0ee1e825",
   "metadata": {},
   "outputs": [],
   "source": [
    "our_first_dictionary['first_key']='first_value'"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bff75692",
   "metadata": {},
   "source": [
    "Now if we print our dictionary, we can see that it does in fact contain the key, and the value associated with it."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "72b28bb9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'first_key': 'first_value'}"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "our_first_dictionary"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c06386a1",
   "metadata": {},
   "source": [
    "If we wanted to extract the **value** for this key, we could do it by using the **key as an index**. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "ec921305",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'first_value'"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "our_first_dictionary['first_key']"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0cbf019c",
   "metadata": {},
   "source": [
    "#### 2. Characteristics of dictionaries\n",
    "\n",
    "**Dictionary items are unique**, specifically referring to the **keys**. If we were to duplicate a key when creating a dictionary, the original key's value is replaced by the new value, rather than being added to the dictionary. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "76ee209f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'first_key': 'second_value', 'extra_key': 'extra_value'}"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# accidental duplicate keys in dictionary definition\n",
    "duplicate_key_dict = {'first_key': 'first_value', 'first_key': 'second_value', 'extra_key': 'extra_value'}\n",
    "duplicate_key_dict"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "31139379",
   "metadata": {},
   "source": [
    "From Python 3.7 onwards, dictionaries are **ordered data structures**, meaning that the order is always the same when calling the variables.\n",
    "<br> \n",
    "\n",
    "Another useful characteristic is that **dictionaries are mutable** - enabling us to **update** these variables with **new values** for existing keys, **add new key-value pairs** and **remove existing key-value pairs**. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "e8804a2d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'first_key': 'first_value'}\n",
      "{'first_key': 100}\n"
     ]
    }
   ],
   "source": [
    "print(our_first_dictionary)\n",
    "\n",
    "# changing a value for an existing key again\n",
    "our_first_dictionary['first_key'] = 100\n",
    "print(our_first_dictionary)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "185890c6",
   "metadata": {},
   "source": [
    "#### 3. Adding key-value pairs to the dictionary\n",
    "We can also add additional key-value pairs to the dictionary, by using the `update()` method. Note that there is a catch to this - the new key-value pair has to be in a dictionary-format in order to add it to the existing dictionary. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "144c0850",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'first_key': 100,\n",
       " 'extra_key': 'extra_value',\n",
       " 'another_extra_key': 'another_value'}"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# adding two new key-value pairs to an existing dictionary\n",
    "an_extra_key_value_dict = {'extra_key':'extra_value', 'another_extra_key':'another_value'}\n",
    "our_first_dictionary.update(an_extra_key_value_dict)\n",
    "our_first_dictionary"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "750ccf27",
   "metadata": {},
   "source": [
    "#### 4. Removing key-value pair from dictionary\n",
    "We can use the `del` keyword to delete a key-value pair from the dictionary.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "dab5c70c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original our_first_dictionary:  {'first_key': 100, 'extra_key': 'extra_value', 'another_extra_key': 'another_value'}\n",
      "Updated our_first_dictionary:  {'first_key': 100, 'extra_key': 'extra_value'}\n"
     ]
    }
   ],
   "source": [
    "print(\"Original our_first_dictionary: \", our_first_dictionary)\n",
    "\n",
    "# using del keyword to remove the key-value pair\n",
    "del our_first_dictionary[\"another_extra_key\"]\n",
    "print(\"Updated our_first_dictionary: \", our_first_dictionary)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a031581e",
   "metadata": {},
   "source": [
    "#### 5. Using the `dict()` function to create a dictionary\n",
    "We can also create a dictionary by specifying the values from the start, and then making use of the `dict()` function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "4bd2b9ca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'first_key': 'first_value', 'extra_key': 'extra_value'}"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# recreating our_first_dictionary with dict()\n",
    "\n",
    "our_first_dictionary = dict(first_key='first_value', extra_key='extra_value')\n",
    "our_first_dictionary\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d16e2bfc",
   "metadata": {},
   "source": [
    "We have now shown two ways of creating dictionaries, the first by specifying it with curly brackets, and the second by using the `dict()` function. Note that when we use the `dict()` function, we don't need to put the keys in quotes, which could save us some time when creating longer dictionaries!"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "155d67cf",
   "metadata": {},
   "source": [
    "#### 6. Printing the key and value in a dictionary\n",
    "When printing the contents of a dictionary, we can show dictionaries in their entirety, or per key, formatted using f-strings. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "acbf14e1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'first_key': 'first_value', 'extra_key': 'extra_value'}\n",
      "first_key: first_value\n"
     ]
    }
   ],
   "source": [
    "print(our_first_dictionary)\n",
    "\n",
    "# using an f-string\n",
    "print(f\"first_key: {our_first_dictionary['first_key']}\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "957174ff",
   "metadata": {},
   "source": [
    "Now that we've covered the very basics of dictionaries, let's look at slightly more interesting and complex examples for a better idea of how we might use them in the real world. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "882d6747",
   "metadata": {},
   "source": [
    "<br> \n",
    "\n",
    "### Example 2\n",
    "\n",
    "Fynbos is a unique vegetation frequently found in the Western Cape, South Africa. The Cape Floristic Region is the smallest of the six floral kingdoms of the world, and in an area of 90,000km2 there are almost 9,000 species of flowering plants. \n",
    "\n",
    "Source: Field Guide to Fynbos, 2018, Struik Nature. Author: John Manning\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c1a00bab",
   "metadata": {},
   "source": [
    "#### 1. Creating a nested dictionary\n",
    "We have data for the number of species in five fynbos families found in South Africa. We have the number of species for each of the fynbos families in the Cape Floristic Region, and for comparison purposes, the number of species found worldwide. \n",
    "\n",
    "This data can easily be stored in a special type of dictionary, namely a **nested dictionary**. \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "c63b34e3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# creating a nested dictionary\n",
    "fynbos_families = { 'Erica': {'Cape Floristic Region': 670, 'Worldwide': 4500},\n",
    "                         'Protea': {'Cape Floristic Region': 330, 'Worldwide': 1350},\n",
    "                         'Restio':{'Cape Floristic Region': 320, 'Worldwide': 400},\n",
    "                         'Citrus':{'Cape Floristic Region': 273, 'Worldwide': 1650},\n",
    "                         'Phylica':{'Cape Floristic Region': 137, 'Worldwide': 900}\n",
    "                        }"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "6b8643d7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(fynbos_families)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "df726ecf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(fynbos_families['Erica'])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "602bd939",
   "metadata": {},
   "source": [
    "When we examine the **type** of the `fynbos_families` variable, we can see that it is a dictionary. The 'nested' part in the name, 'nested dictionary', refers to the fact that the value associated with the keys in this dictionary is, in turn, **also a dictionary**. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b1eac388",
   "metadata": {},
   "source": [
    "#### 2. Accessing values in a nested dictionary\n",
    "\n",
    "In order to access the values in a nested dictionary, the same rules apply as for a normal dictionary. The keys can be used as an index to refer to the value. The only difference is that there are additional layers to work through to get to the value of interest. \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "efd1a974",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Cape Floristic Region': 670, 'Worldwide': 4500}"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# accessing the value of the 'Erica' key - result is a dictionary\n",
    "fynbos_families['Erica']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "0922fef6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "330"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# find the number of species in the Cape Floristic Region for the Protea family\n",
    "fynbos_families['Protea']['Cape Floristic Region']"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "52b06466",
   "metadata": {},
   "source": [
    "#### 3. Keys, values, and items objects\n",
    "Suppose we are only interested in the Protea family and the number of species within it. Create a new dictionary that consists only of the Protea species numbers by region, by using the existing nested `fynbos_families` variable.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "dbd9ea08",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Cape Floristic Region': 330, 'Worldwide': 1350}"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "protea_species = fynbos_families['Protea']\n",
    "protea_species"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3fc06c60",
   "metadata": {},
   "source": [
    "Python has several methods designed for dictionaries to simplify our lives when trying to access keys and their associated values. \n",
    "\n",
    "We can extract the keys for this dictionary with a special method, `keys()`. The keys will be returned as a key object, which can easily be converted to a list, allowing us to access the individual elements."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "6ec8de60",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Cape Floristic Region', 'Worldwide']"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "key_list = list(protea_species.keys())\n",
    "key_list"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "54a1c878",
   "metadata": {},
   "source": [
    "Similarly, we can use the `values()` method to extract a values object, which can also be converted to a list in order to access the elements. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "55d93db4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[330, 1350]"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "value_list = list(protea_species.values())\n",
    "value_list"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2bd0862b",
   "metadata": {},
   "source": [
    "We can also extract the combined key-value pairs in tuples, by using the `items()` method. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "bad77a52",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('Cape Floristic Region', 330), ('Worldwide', 1350)]"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "items_list = list(protea_species.items())\n",
    "items_list"
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
    "In this notebook we looked at creating both nested and regular dictionaries, as well as how to update and change them. Dictionaries provide a fast and efficient way to store and access small sets of structured data. Be sure to take a look at the Python documentation for more examples and useful commands. "
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
   "version": "3.11.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
