{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "d5050581",
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
    "# Exercise: Using and controlling loops\n",
    "© ExploreAI Academy"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "26af890c",
   "metadata": {},
   "source": [
    "This notebook has a series of exercises testing your ability to solve problems using loops."
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
    "In this train, we will:\n",
    "- Learn how to create various `for` and `while` loops.\n",
    "- Control the flow of loops.\n",
    "- Build problem-solving skills using loops."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9f2422a5",
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
    "### Exercise 1: Marine species counter\n",
    "\n",
    "**Objective:** Use a `for` loop to count the number of endangered marine species in a list.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ec1c7891",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of endangered marine species: 3\n"
     ]
    }
   ],
   "source": [
    "endangered_marine_species = ['Hawksbill Turtle', 'Vaquita', 'Blue Whale', 'Staghorn Coral', 'Green Turtle']\n",
    "endangered_count = 0\n",
    "\n",
    "# Your task: Use a for loop to count the number of species in the list\n",
    "for species in endangered_marine_species:\n",
    "    if \"Turtle\" in species or \"Coral\" in species:\n",
    "        endangered_count += 1\n",
    "\n",
    "print(f\"Number of endangered marine species: {endangered_count}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c4d97aa4",
   "metadata": {},
   "source": [
    "**Hint:** Use the loop to iterate over the `endangered_marine_species` list and increment the `endangered_count` variable by 1 for each species."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "17bba74e",
   "metadata": {},
   "source": [
    "### Exercise 2: Deforestation alert\n",
    "\n",
    "**Objective:** Use a `while` loop to simulate a deforestation monitoring system that alerts when the forested area falls below a critical threshold.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b3bb4756",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Years until critical deforestation level: 7\n"
     ]
    }
   ],
   "source": [
    "initial_forested_area = 1000  # in square kilometres\n",
    "deforestation_rate = 20       # square kilometres per year\n",
    "\n",
    "# Your task: Use a while loop to determine how many years it takes for the forested area to fall below 500 square kilometres\n",
    "years = 0\n",
    "while initial_forested_area > 500:\n",
    "    years += 1\n",
    "    initial_forested_area -= deforestation_rate * years\n",
    "\n",
    "print(f\"Years until critical deforestation level: {years}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1711f162",
   "metadata": {},
   "source": [
    "**Hint:** In each iteration of the `while` loop, decrease the `initial_forested_area` by `deforestation_rate` and increment the `years` by 1."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "efaae06e",
   "metadata": {},
   "source": [
    "### Exercise 3: Biodiversity analysis\n",
    "\n",
    "**Objective:** Write a `for` loop to analyse a list of animals, printing out whether they are endangered or not."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "13ff9ce0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Tiger is endangered.\n",
      "Blue Whale is endangered.\n",
      "African Elephant is endangered.\n",
      "Koala is not endangered.\n",
      "Panda is not endangered.\n"
     ]
    }
   ],
   "source": [
    "animals = ['Tiger', 'Blue Whale', 'African Elephant', 'Koala', 'Panda']\n",
    "endangered_animals = ['Tiger', 'Blue Whale', 'African Elephant']\n",
    "\n",
    "# Your task: Use a for loop to print out each animal's name and its endangered status\n",
    "for animal in animals:\n",
    "    if animal in endangered_animals:\n",
    "        print(animal + \" is endangered.\")\n",
    "    else:\n",
    "        print(animal + \" is not endangered.\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fd05b0b1",
   "metadata": {},
   "source": [
    "**Hint:** Check if each animal in the `animals` list is also `in` the `endangered_animals` list, and print the appropriate status."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "09a79878",
   "metadata": {},
   "source": [
    "### Exercise 4: Ocean pollution tracker\n",
    "\n",
    "**Objective:** Use loops to process and display information about ocean pollution levels in different regions."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "180572c0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Average pollution level in the Pacific Ocean: 3.33\n",
      "Average pollution level in the Atlantic Ocean: 4.33\n",
      "Average pollution level in the Indian Ocean: 3.00\n"
     ]
    }
   ],
   "source": [
    "ocean_pollution_data = {\n",
    "    'Pacific Ocean': [3, 5, 2],  # pollution levels\n",
    "    'Atlantic Ocean': [7, 2, 4],\n",
    "    'Indian Ocean': [5, 1, 3]\n",
    "}\n",
    "\n",
    "for ocean, pollution_levels in ocean_pollution_data.items():\n",
    "    total_pollution = sum(pollution_levels)\n",
    "    average_pollution = total_pollution / len(pollution_levels)\n",
    "    print(f\"Average pollution level in the {ocean}: {average_pollution:.2f}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d1a00eaa",
   "metadata": {},
   "source": [
    "**Hint:** Use a `for` loop to sum the pollution levels for each ocean, then calculate and print the average."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "65fd599f",
   "metadata": {},
   "source": [
    "### Exercise 5: Species conservation\n",
    "\n",
    "**Objective:** Implement a `while` loop to simulate a conservation effort, stopping when a certain population target is reached."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "cf960543",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Years to reach target population: 18\n"
     ]
    }
   ],
   "source": [
    "current_population = 150  # of a particular endangered species\n",
    "target_population = 500\n",
    "years = 0\n",
    "growth_rate = 1.07  # 7% annual growth due to conservation efforts\n",
    "\n",
    "# Your task: Use a while loop to calculate how many years it takes to reach the target population\n",
    "while current_population < target_population:\n",
    "    current_population *= growth_rate\n",
    "    years += 1\n",
    "\n",
    "\n",
    "print(f\"Years to reach target population: {years}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "99498807",
   "metadata": {},
   "source": [
    "**Hint:** In each iteration of the `while` loop, multiply the `current_population` by `growth_rate`, and increment `years` by 1."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f75d4350",
   "metadata": {},
   "source": [
    "### Exercise 6: Basic list comprehension\n",
    "\n",
    "**Instructions:** Fill in the comprehension line to create a list of squares of numbers from 1 to 10."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "0cb026b6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]\n"
     ]
    }
   ],
   "source": [
    "numbers = range(1, 11)\n",
    "# Fill in the list comprehension\n",
    "squares = [x**2 for x in numbers]\n",
    "print(squares)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3bff7e58",
   "metadata": {},
   "source": [
    "### Exercise 7: List comprehension with a conditional\n",
    "\n",
    "**Instructions:** Use list comprehension to create a list of only even numbers from 1 to 20."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "566521f1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]\n"
     ]
    }
   ],
   "source": [
    "numbers = range(1, 21)\n",
    "even_numbers = [x for x in numbers if x % 2 == 0]\n",
    "print(even_numbers)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f077f605",
   "metadata": {},
   "source": [
    "### Exercise 8: Dictionary comprehension\n",
    "\n",
    "**Instructions:** Create a dictionary that categorises each marine animal in the list as 'Aquatic' using dictionary comprehension."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "b86bdd38",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Dolphin': 'Aquatic', 'Shark': 'Aquatic', 'Turtle': 'Aquatic'}\n"
     ]
    }
   ],
   "source": [
    "marine_animals = ['Dolphin', 'Shark', 'Turtle']\n",
    "# Desired Output: {'Dolphin': 'Aquatic', 'Shark': 'Aquatic', 'Turtle': 'Aquatic'}\n",
    "\n",
    "animal_categories = {animal: 'Aquatic' for animal in marine_animals}\n",
    "print(animal_categories)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1101dc22",
   "metadata": {},
   "source": [
    "### Exercise 9: Data mapping with dictionary comprehension\n",
    "Quite often in data science working with data in key-value pairs like dictionaries is simpler. Often we have to use data from lists to create these data structures. We can use dictionary comprehension to map data from two lists together.\n",
    "\n",
    "**Instructions:** Use dictionary comprehension to create a mapping of each marine species to its conservation status based on the given lists. Only include species marked as 'Endangered'."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "a4843a03",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Dolphins': 'Endangered', 'Sea Turtles': 'Endangered'}\n"
     ]
    }
   ],
   "source": [
    "species = ['Dolphins', 'Whales', 'Sea Turtles', 'Seals']\n",
    "status = ['Endangered', 'Vulnerable', 'Endangered', 'Least Concern']\n",
    "# Desired Output: {'Dolphins': 'Endangered', 'Sea Turtles': 'Endangered'}\n",
    "number_of_species = range(len(species))\n",
    "\n",
    "endangered_species = {species[i]: status[i] for i in number_of_species if status[i] == 'Endangered'}\n",
    "print(endangered_species)\n"
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
    "This notebook provided a comprehensive and engaging exploration of using loops in Python to solve a variety of problems. Through a series of exercises, we gained practical experience with both `for` and `while` loops, as well as list and dictionary comprehension."
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
