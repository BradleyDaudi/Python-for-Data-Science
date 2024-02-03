{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "cd88ea27",
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
    "# Exercise: Dictionaries\n",
    "© ExploreAI Academy"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "26af890c",
   "metadata": {},
   "source": [
    "In this exercise, we'll be exploring problems involving dictionaries – how to create, manipulate, and use their characteristics to create efficient code. \n"
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
    "Following this exercise, we will:\n",
    "- Understand how to create dictionaries.\n",
    "- Be able to manipulate the key-value pairs using assignment and slicing.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "de45a481",
   "metadata": {},
   "source": [
    "## Exercises"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a4195479",
   "metadata": {},
   "source": [
    "### Exercise 1\n",
    "\n",
    "1. Create a dictionary called `tree` with the following key-value pairs: <br> \n",
    "- `tree_type – Pepper-bark tree` \n",
    "- `age – 15`\n",
    "- `family – Canellaceae`\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "00ef21f6",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'tree_type': 'Pepper-bark tree', 'age': 15, 'family': 'Canellaceae'}\n"
     ]
    }
   ],
   "source": [
    "# creating a dict\n",
    "tree = {}\n",
    "tree[\"tree_type\"] = \"Pepper-bark tree\"\n",
    "tree[\"age\"] = 15\n",
    "tree[\"family\"] = \"Canellaceae\"\n",
    "print(tree)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ace28eb0",
   "metadata": {},
   "source": [
    "2. Print the value associated with the key `age`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "a5aa5d8f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "15\n"
     ]
    }
   ],
   "source": [
    "print(tree[\"age\"])\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8d665835",
   "metadata": {},
   "source": [
    "3. When we created this dictionary in the first step, we accidentally left out one of the information categories, namely 'kingdom'. Fortunately, dictionaries are mutable, and we can add a new key-value pair to the dictionary: `kingdom – Plantae`. Do this in the code cell below. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "59e7d365",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'tree_type': 'Pepper-bark tree', 'age': 15, 'family': 'Canellaceae', 'kingdom': 'Plantae'}\n"
     ]
    }
   ],
   "source": [
    "# insert code here\n",
    "tree[\"kingdom\"] = \"Plantae\"\n",
    "print(tree)\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ff95cb43",
   "metadata": {},
   "source": [
    "4. We have found that people are no longer interested in one of the key-value pairs in our dictionary. Remove the `family` key-value pair from the dictionary."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "b619fe91",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'tree_type': 'Pepper-bark tree', 'age': 15, 'kingdom': 'Plantae'}\n"
     ]
    }
   ],
   "source": [
    "# insert code here\n",
    " del tree[\"family\"]\n",
    "print(tree)\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "17fe171e",
   "metadata": {},
   "source": [
    "5. Update the dictionary by changing the `tree_type` key to `Wild Cinnamon`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "c0647f08",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'tree_type': 'Wild Cinnamon', 'age': 15, 'kingdom': 'Plantae'}\n"
     ]
    }
   ],
   "source": [
    "# insert code here\n",
    "tree[\"tree_type\"] = \"Wild Cinnamon\"\n",
    "print(tree)\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ee218a08",
   "metadata": {},
   "source": [
    "6. Extract the keys and values from our `tree` dictionary, and store the values in two separate lists, `key_list` and `value_list`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "553ce78c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Key list:  ['tree_type', 'age', 'kingdom']\n",
      "Value list:  ['Wild Cinnamon', 15, 'Plantae']\n"
     ]
    }
   ],
   "source": [
    "key_list = list(tree.keys())\n",
    "value_list = list(tree.values())\n",
    "print(\"Key list: \",key_list)\n",
    "print(\"Value list: \",value_list)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "604fb0ac",
   "metadata": {},
   "source": [
    "7. Extract the key-value pairs from our `tree` dictionary in tuples, and store the values in a single list, `item_list`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "8d6b6bde",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'dict_items'>\n",
      "[('tree_type', 'Wild Cinnamon'), ('age', 15), ('kingdom', 'Plantae')]\n"
     ]
    }
   ],
   "source": [
    "print(type(tree.items()))\n",
    "\n",
    "item_list = list(tree.items())\n",
    "print(item_list)\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0e588848",
   "metadata": {},
   "source": [
    "### Exercise 2\n",
    "\n",
    "1. We have been provided with a basic nested dictionary containing African tree species. We have just received more detailed information on these trees and need to add it to this nested dictionary. Use the code provided as a starting point, adding in the extra information where required. \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "b51ffe85",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Baobab': {'common_name': 'Baobab', 'scientific_name': 'Adansonia'}, 'Acacia': {'common_name': 'Acacia', 'scientific_name': 'Acacia'}}\n"
     ]
    }
   ],
   "source": [
    "# basic dictionary provided \n",
    "african_trees = {\n",
    "    \"Baobab\": {\n",
    "        \"common_name\": \"Baobab\",\n",
    "        \"scientific_name\": \"Adansonia\",\n",
    "    },\n",
    "    \"Acacia\": {\n",
    "        \"common_name\": \"Acacia\",\n",
    "        \"scientific_name\": \"Acacia\",\n",
    "    }\n",
    "}\n",
    "print(african_trees)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "98e7591b",
   "metadata": {},
   "source": [
    "**New information**\n",
    "\n",
    "Baobab: \n",
    "- country – Zimbabwe\n",
    "- average_height – 25\n",
    "\n",
    "Acacia:\n",
    "- country – South Africa\n",
    "- average_height – 15\n",
    "\n",
    "**Hint**: \n",
    "- Print the dictionary to view the current structure. \n",
    "- Use the keys to access the Baobab and Acacia dictionaries and append the additional information.\n",
    "- The new keys will be `country` and `average_height`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "233a2393",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Baobab': {'common_name': 'Baobab',\n",
       "  'scientific_name': 'Adansonia',\n",
       "  'country': 'Zimbabwe',\n",
       "  'average_height': 25},\n",
       " 'Acacia': {'common_name': 'Acacia',\n",
       "  'scientific_name': 'Acacia',\n",
       "  'country': 'South Africa',\n",
       "  'average_height': 15}}"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_baobab = {\"country\":\"Zimbabwe\",\"average_height\":25}\n",
    "african_trees['Baobab'].update(new_baobab)\n",
    "new_acacia = {\"country\":\"South Africa\",\"average_height\":15}\n",
    "african_trees['Acacia'].update(new_acacia)\n",
    "\n",
    "african_trees\n",
    "\n"
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
    "Dictionaries provide a **fast and efficient** way to work with **structured data**. In this exercise, we looked at ways of creating dictionaries, how to update them, and how to extract their attributes. Remember to look into the Python documentation to learn more about these data structures! "
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
