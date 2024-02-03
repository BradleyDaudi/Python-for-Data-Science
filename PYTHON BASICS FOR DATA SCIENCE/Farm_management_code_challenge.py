{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "9ed33a4d",
   "metadata": {},
   "source": [
    "<div align=\"center\" style=\" font-size: 80%; text-align: center; margin: 0 auto\">\n",
    "<img src=\"https://raw.githubusercontent.com/Explore-AI/Pictures/master/Python-Notebook-Banners/Code_challenge.png\"  style=\"display: block; margin-left: auto; margin-right: auto;\";/>\n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f662d169",
   "metadata": {},
   "source": [
    "# Code challenge: Farm harvest management\n",
    "© ExploreAI Academy"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "26af890c",
   "metadata": {},
   "source": [
    "In this code challenge, we will assist a farmer in calculating the total harvest from two fields (wheat and potatoes) and the overall expenses and profits for this season.\n",
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
    "In this train, we will:\n",
    "- Understand how to perform basic arithmetic operations in a Jupyter notebook.\n",
    "- Know how to assign numerical values to variables.\n",
    "- Know how to use the print() function to display our results.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "86c8e674",
   "metadata": {},
   "source": [
    "## Instructions\n",
    "\n",
    "- **This code challenge does not count for marks.**\n",
    "- Do not add or remove cells in this notebook.\n",
    "- Answer the questions according to the specifications provided.\n",
    "- Use the given cell in each question to see if your function matches the expected outputs."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "82bf868b",
   "metadata": {},
   "source": [
    "## Challenge 1\n",
    "Calculate the total harvest for the farmer."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "209b7ec5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total harvest in kilograms: 5650\n"
     ]
    }
   ],
   "source": [
    "total_kgs_wheat_harvest = 2050\n",
    "total_kgs_potato_harvest = 3600\n",
    "\n",
    "total_kgs_harvest = total_kgs_wheat_harvest + total_kgs_potato_harvest\n",
    "print(\"Total harvest in kilograms:\", total_kgs_harvest)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "25d3dc32",
   "metadata": {},
   "source": [
    "**Expected outputs:**\n",
    "```python\n",
    "Total harvest in kilograms: 5650\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3872d229",
   "metadata": {},
   "source": [
    "## Challenge 2\n",
    "Calculate the total expenses (in dollars) and print the result."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a30e5234",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total expenses in dollars: 3720\n"
     ]
    }
   ],
   "source": [
    "seed_expense = 650\n",
    "labour_expense = 3070\n",
    "\n",
    "total_expenses_dollars = seed_expense + labour_expense\n",
    "print(\"Total expenses in dollars:\", total_expenses_dollars)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fcb6c019",
   "metadata": {},
   "source": [
    "**Expected outputs:**\n",
    "```python\n",
    "Total expenses in dollars: 3720\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "218f756c",
   "metadata": {},
   "source": [
    "## Challenge 3\n",
    "Calculate the total revenue (in dollars) and print the result."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "6c1bb59d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total revenue in dollars 9140.0\n"
     ]
    }
   ],
   "source": [
    "price_per_kg_wheat = 2\n",
    "price_per_kg_potato = 1.4\n",
    "\n",
    "total_revenue_dollars = price_per_kg_wheat*total_kgs_wheat_harvest + price_per_kg_potato*total_kgs_potato_harvest\n",
    "print(\"Total revenue in dollars\", total_revenue_dollars)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "88755e59",
   "metadata": {},
   "source": [
    "**Expected outputs:**\n",
    "```python\n",
    "Total revenue in dollars: 9140\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "db4b7916",
   "metadata": {},
   "source": [
    "## Challenge 4\n",
    "Calculate the total profit (in dollars) and print the result."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "e98273ee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total profit in dollars: 5420.0\n"
     ]
    }
   ],
   "source": [
    "total_profit_dollars = total_revenue_dollars - (seed_expense + labour_expense)\n",
    "print(\"Total profit in dollars:\", total_profit_dollars) "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c70f8264",
   "metadata": {},
   "source": [
    "**Expected outputs:**\n",
    "```python\n",
    "Total profit in dollars: 5420 \n",
    "```"
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
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
