{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "Ee-v8I_P8rfp"
   },
   "source": [
    "<div align=\"center\" style=\" font-size: 80%; text-align: center; margin: 0 auto\">\n",
    "<img src=\"https://raw.githubusercontent.com/Explore-AI/Pictures/master/Python-Notebook-Banners/Exercise.png\"  style=\"display: block; margin-left: auto; margin-right: auto;\";/>\n",
    "</div>\n",
    "\n",
    "# Exercise: Working with DataFrames\n",
    "© ExploreAI Academy\n",
    "\n",
    "In this exercise, we'll be exploring some ways in which we can manipulate the data stored within a Pandas DataFrame."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "ITqrvAqq8xSC"
   },
   "source": [
    "## Learning objectives\n",
    "\n",
    "By the end of this train, you should be able to:\n",
    "* Sort, filter, and group a Pandas DataFrame.\n",
    "* Create and delete columns in a Pandas DataFrame.\n",
    "* Transform a Pandas DataFrame."
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
   "metadata": {},
   "source": [
    "### Import libraries and dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We are using a dataset named `Animals.csv` that stores information about a variety of animal species."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "animal_df = pd.read_csv('https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/Python/Animals.csv')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise 1\n",
    "\n",
    "Filter the dataset to show only species that have an `Average Lifespan (Years)` **greater than 20** and are classified as `Vulnerable` in `Conservation Status`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Species</th>\n",
       "      <th>Average Lifespan (Years)</th>\n",
       "      <th>Habitat</th>\n",
       "      <th>Conservation Status</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Empty DataFrame\n",
       "Columns: [Species, Average Lifespan (Years), Habitat, Conservation Status]\n",
       "Index: []"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_spec = animal_df[(animal_df['Average Lifespan (Years)'] > 20)& (animal_df['Conservation Status'] == 'Vulneable')]\n",
    "\n",
    "new_spec.head()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise 2\n",
    "\n",
    "**a)** Create a new column `Lifespan in Months` by converting the `Average Lifespan (Years)` to months.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Species</th>\n",
       "      <th>Average Lifespan (Years)</th>\n",
       "      <th>Habitat</th>\n",
       "      <th>Conservation Status</th>\n",
       "      <th>Lifespan in Months</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Empty DataFrame\n",
       "Columns: [Species, Average Lifespan (Years), Habitat, Conservation Status, Lifespan in Months]\n",
       "Index: []"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "animal_df['Lifespan in Months'] = animal_df['Average Lifespan (Years)']*12\n",
    "animal_df\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**b)** Delete the `Lifespan in Months` column from the DataFrame."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Species</th>\n",
       "      <th>Average Lifespan (Years)</th>\n",
       "      <th>Habitat</th>\n",
       "      <th>Conservation Status</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Empty DataFrame\n",
       "Columns: [Species, Average Lifespan (Years), Habitat, Conservation Status]\n",
       "Index: []"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "animal_df.drop(columns='Lifespan in Months', inplace = True)\n",
    "animal_df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise 3\n",
    "\n",
    "**a)** Filter the DataFrame `animal_df` to include only species with an `Average Lifespan (Years)` **greater than 50 years**. Store the result in a new DataFrame `Long_lived_species`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Species</th>\n",
       "      <th>Average Lifespan (Years)</th>\n",
       "      <th>Habitat</th>\n",
       "      <th>Conservation Status</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Empty DataFrame\n",
       "Columns: [Species, Average Lifespan (Years), Habitat, Conservation Status]\n",
       "Index: []"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Long_lived_species = animal_df[animal_df['Average Lifespan (Years)']>50]\n",
    "Long_lived_species"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**b)** Using the `apply` and `lambda` functions, convert the `Average Lifespan (Years)` of all species into the float data type in `Long_lived_species`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Species</th>\n",
       "      <th>Average Lifespan (Years)</th>\n",
       "      <th>Habitat</th>\n",
       "      <th>Conservation Status</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Empty DataFrame\n",
       "Columns: [Species, Average Lifespan (Years), Habitat, Conservation Status]\n",
       "Index: []"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Transform the Average Lifespan (Years) column to the floats\n",
    "Long_lived_species['Average Lifespan (Years)'] = Long_lived_species['Average Lifespan (Years)'].apply(lambda x: float(x))\n",
    "\n",
    "# Display the updated DataFrame \n",
    "Long_lived_species"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise 4\n",
    "\n",
    "List all columns for species that have the string \"`Endangered`\" as part of their conservation status."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Species</th>\n",
       "      <th>Average Lifespan (Years)</th>\n",
       "      <th>Habitat</th>\n",
       "      <th>Conservation Status</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Empty DataFrame\n",
       "Columns: [Species, Average Lifespan (Years), Habitat, Conservation Status]\n",
       "Index: []"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Filtering to find species with 'Endangered' in their conservation status\n",
    "Endangered_species = animal_df[animal_df['Conservation Status'].str.contains('Endangered')]\n",
    "\n",
    "# Display the filtered DataFrame\n",
    "Endangered_species"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise 5\n",
    "\n",
    "List the mean `Average Lifespan (Years)` of species for each `Habitat` in descending order."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Series([], Name: Average Lifespan (Years), dtype: float64)"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Mean_lifespan_by_habitat = animal_df.groupby('Habitat')['Average Lifespan (Years)'].mean().sort_values(ascending=False)\n",
    "\n",
    "Mean_lifespan_by_habitat"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercise 6\n",
    "\n",
    "Create a column `Threat Level` that categorises species into `High`, `Medium`, or `Low` based on their `Conservation Status`: \n",
    "- **High** for `Critically Endangered` and `Endangered` \n",
    "- **Medium** for `Vulnerable` and `Near Threatened`\n",
    "- **Low** for `Least Concern`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Species</th>\n",
       "      <th>Average Lifespan (Years)</th>\n",
       "      <th>Habitat</th>\n",
       "      <th>Conservation Status</th>\n",
       "      <th>Threat Level</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Empty DataFrame\n",
       "Columns: [Species, Average Lifespan (Years), Habitat, Conservation Status, Threat Level]\n",
       "Index: []"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Function to categorise species based on their conservation status.\n",
    "def categorise_threat(status):\n",
    "    if status in ['Critically Endangered', 'Endangered']:\n",
    "        return 'High'\n",
    "    elif status in ['Vulnerable', 'Near Threatened']:\n",
    "        return 'Medium'\n",
    "    else:\n",
    "        return 'Low'\n",
    "# Apply the 'categorise_threat' function to the 'Conservation Status' column\n",
    "animal_df['Threat Level'] = animal_df['Conservation Status'].apply(categorise_threat)\n",
    "\n",
    "animal_df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We define the `categorise_threat` function which uses conditional statements to categorise species based on their conservation status.\n",
    "\n",
    "We then use the `apply` method to apply the function to each row in the `Conservation Status` column.\n",
    "\n",
    "The results are stored in a new column, `Threat Level`."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div align=\"center\" style=\" font-size: 80%; text-align: center; margin: 0 auto\">\n",
    "<img src=\"https://raw.githubusercontent.com/Explore-AI/Pictures/master/ExploreAI_logos/EAI_Blue_Dark.png\"  style=\"width:200px\";/>\n",
    "</div>"
   ]
  }
 ],
 "metadata": {
  "colab": {
   "authorship_tag": "ABX9TyPZFCZhaikX+N2/Bg7W6SY+",
   "collapsed_sections": [],
   "name": "Search_algorithms.ipynb",
   "provenance": [],
   "toc_visible": true
  },
  "interpreter": {
   "hash": "6b5ebbc2c6bde2831bc6c0426f75aca8137ccfc69d329557556ed73faee126ae"
  },
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
 "nbformat_minor": 2
}
