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
   "id": "f662d169",
   "metadata": {},
   "source": [
    "# Exercise: Problem solving with loops\n",
    "© ExploreAI Academy"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "26af890c",
   "metadata": {},
   "source": [
    "This notebook contains more advanced problems in loops. In this notebook, we are given code in a randomised arrangement. We have to rearrange the code to get the desired result."
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
    "In this train, we will learn how to:\n",
    "- Solve more complex problems using loops."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fe1d90f3",
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
    "### Exercise 1: Ocean cleanup analysis\n",
    "\n",
    "**Instructions:** Rearrange the code blocks to create a program that calculates the total amount of waste collected in an ocean cleanup campaign over a week. Each day's collection is stored in a list."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ec1c7891",
   "metadata": {},
   "outputs": [],
   "source": [
    "total_waste_collected = 0\n",
    "for daily_collection in weekly_collection:\n",
    "print(f\"Total waste collected over the week: {total_waste_collected} kg\")\n",
    "weekly_collection = [340, 220, 455, 300, 385, 520, 410]\n",
    "total_waste_collected += daily_collection"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "76a6b781",
   "metadata": {},
   "source": [
    "Rearranged code:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "7b4131b1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total waste collected over the week: 2630 kg\n"
     ]
    }
   ],
   "source": [
    "weekly_collection = [340, 220, 455, 300, 385, 520, 410]\n",
    "total_waste_collected = 0\n",
    "\n",
    "for daily_collection in weekly_collection:\n",
    "    total_waste_collected += daily_collection\n",
    "print(f\"Total waste collected over the week: {total_waste_collected} kg\")\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1b7d0515",
   "metadata": {},
   "source": [
    "Expected result: `Total waste collected over the week: 2630 kg`"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "be0f48b6",
   "metadata": {},
   "source": [
    "### Exercise 2: Endangered species monitoring\n",
    "\n",
    "**Instructions:** Rearrange the code to create a program that tracks sightings of endangered species over a month, stopping if a certain species is spotted."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9bb8f2e5",
   "metadata": {},
   "outputs": [],
   "source": [
    "endangered_species = ['Tiger', 'Blue Whale', 'Mountain Gorilla']\n",
    "sightings = ['Deer', 'Tiger', 'Blue Whale', 'Mountain Gorilla', 'Elephant']\n",
    "for species in sightings:\n",
    "if species in endangered_species:\n",
    "print(f\"Endangered species spotted: {species}\")\n",
    "break"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3958c1d3",
   "metadata": {},
   "source": [
    "Rearranged code:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "cba9abab",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Endangered species spotted: Tiger\n"
     ]
    }
   ],
   "source": [
    "endangered_species = ['Tiger', 'Blue Whale', 'Mountain Gorilla']\n",
    "sightings = ['Deer', 'Tiger', 'Blue Whale', 'Mountain Gorilla', 'Elephant']\n",
    "for species in sightings:\n",
    "    if species in endangered_species:\n",
    "        print(f\"Endangered species spotted: {species}\")\n",
    "        break"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4fa4b4e7",
   "metadata": {},
   "source": [
    "Expected result: `Endangered species spotted: Tiger`"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2a0da8f1",
   "metadata": {},
   "source": [
    "### Exercise 3: Forest growth monitoring\n",
    "\n",
    "**Instructions:** Rearrange the code blocks to create a program that simulates the growth of a forest over years until it reaches a specified threshold area. The forest growth is compounded annually."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1d61ce09",
   "metadata": {},
   "outputs": [],
   "source": [
    "forest_area = 1000 # Initial forest area in square kilometres\n",
    "growth_rate = 1.05 # 5% annual growth\n",
    "while forest_area < 1500:\n",
    "print(f\"Forest area after {year} years: {forest_area:.2f} sq km\")\n",
    "forest_area *= growth_rate\n",
    "year = 0\n",
    "year += 1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "61f64e32",
   "metadata": {},
   "source": [
    "Rearranged code:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "4232f2f1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Forest area after 1 years: 1050.00 sq km\n",
      "Forest area after 2 years: 1102.50 sq km\n",
      "Forest area after 3 years: 1157.62 sq km\n",
      "Forest area after 4 years: 1215.51 sq km\n",
      "Forest area after 5 years: 1276.28 sq km\n",
      "Forest area after 6 years: 1340.10 sq km\n",
      "Forest area after 7 years: 1407.10 sq km\n",
      "Forest area after 8 years: 1477.46 sq km\n",
      "Forest area after 9 years: 1551.33 sq km\n"
     ]
    }
   ],
   "source": [
    "forest_area = 1000 # Initial forest area in square kilometres\n",
    "growth_rate = 1.05 # 5% annual growth\n",
    "year = 0\n",
    "while forest_area < 1500:\n",
    "    forest_area *= growth_rate\n",
    "    year += 1\n",
    "    print(f\"Forest area after {year} years: {forest_area:.2f} sq km\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dee81ba4",
   "metadata": {},
   "source": [
    "Expected result:\n",
    " \n",
    "`Forest area after 1 years: 1050.00 sq km`\n",
    "\n",
    "`Forest area after 2 years: 1102.50 sq km`\n",
    "\n",
    "`Forest area after 3 years: 1157.62 sq km`\n",
    "\n",
    "`Forest area after 4 years: 1215.51 sq km`\n",
    "\n",
    "`Forest area after 5 years: 1276.28 sq km`\n",
    "\n",
    "`Forest area after 6 years: 1340.10 sq km`\n",
    "\n",
    "`Forest area after 7 years: 1407.10 sq km`\n",
    "\n",
    "`Forest area after 8 years: 1477.46 sq km`\n",
    "\n",
    "`Forest area after 9 years: 1551.33 sq km`"
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
    "This notebook provided a comprehensive exploration of using loops in Python to solve a variety of problems. Through a series of exercises, we gained practical experience with both `for` and `while` loops.\n",
    "\n",
    "By engaging with these exercises, we not only reinforce our understanding of loop syntax but also start to develop crucial problem-solving skills."
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
