{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "250ac15e",
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
    "# Graded code challenge: Data structures and types\n",
    "© ExploreAI Academy"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "26af890c",
   "metadata": {},
   "source": [
    "⚠️ **NOTE that this code challenge is graded and will contribute to your overall marks for this module.**\n",
    "\n",
    "### Instructions\n",
    "\n",
    "- **Do not add or remove cells in this notebook. Do not edit or remove the `### START FUNCTION` or `### END FUNCTION` comments. Do not add any code outside of the functions you are required to edit. Doing any of this will lead to a mark of 0%!**\n",
    "\n",
    "- Answer the questions according to the specifications provided.\n",
    "\n",
    "- Use the given cell in each question to see if your function matches the expected outputs.\n",
    "\n",
    "- Do not hard-code answers to the questions.\n",
    "\n",
    "- The use of StackOverflow, Google, and other online tools is permitted. However, copying a fellow student's code is not permissible and is considered a breach of the Honour code. Doing this will result in a mark of 0%.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5a0b7683",
   "metadata": {
    "tags": []
   },
   "source": [
    "## Introduction\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "I hope you are buzzing with the satisfaction of having completed the water infrastructure project in Maji Ndogo. Your brilliant work has not only improved lives but also opened doors to new possibilities. Now, we have another thrilling challenge ahead of us, and I believe it's right up our alley!\n",
    "\n",
    "We're stepping into a domain where technology meets agriculture. Maji Ndogo, with your help, is looking to revolutionise its farming industry through automation, using the power of data science and AI. The long-term goal? Fully autonomous farming equipment that can intelligently manage and optimise agricultural processes. Exciting, isn't it?\n",
    "\n",
    "<div align=\"center\" style=\"font-size: 80%; text-align: center; margin: 0 auto\">\n",
    "    <img src=\"https://raw.githubusercontent.com/Explore-AI/Pictures/457505ff64842b573a30ca654e645854e447c406/alx_ds_python/Code_challenges/Sanaa_Ayo_avatar.png\" \n",
    "         style=\"display: block; margin-left: auto; margin-right: auto; width: 50%; height: auto;\"/>\n",
    "</div>\n",
    "\n",
    "However, before we dive into the world of AI-driven tractors and smart irrigation systems, we need to lay the groundwork. Our first step is to tackle how we can programmatically represent this problem. Think of it as creating a 'Digital Twin' of the farming ecosystem in Maji Ndogo.\n",
    "\n",
    "This Digital Twin will be our sandbox, where we can experiment, analyse, and fine-tune our approaches before implementing them in the real world. But how do we build such a model? How do we ensure it accurately reflects the complexities of a real farm?\n",
    "\n",
    "Here's where our Python skills come into play. We’ll start by representing various elements of a farm - like fields, crops, and farming equipment. We will have to encapsulate operations like planting, watering, and harvesting.\n",
    "\n",
    "Of course, this is just scratching the surface. We'll encounter and solve various challenges along the way, using more advanced concepts and techniques. But I'm confident that with your skills and enthusiasm, we'll make this project another success story.\n",
    "\n",
    "Looking forward to embarking on this journey with you all. Let's turn the fields of Maji Ndogo into a beacon of technological advancement in agriculture!\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "df3ad76c",
   "metadata": {},
   "source": [
    "\n",
    "## Challenge 1: Represent a Tractor with a dictionary\n",
    "In the world of digital farming, the first step is to bring our farm machinery into the digital realm. Let's start with the tractor, the workhorse of the farm. Digitising the tractor allows us to simulate and analyse its performance, maintenance needs, and usage patterns. This data-driven approach can lead to more efficient use of machinery, saving time and resources.\n",
    "\n",
    "Why use a dictionary for this? In Python, a dictionary is a versatile and intuitive way to store and access data. It allows us to create a clear, structured representation of an object by mapping keys (property names) to values (property details). This is ideal for representing complex objects like tractors with multiple attributes.\n",
    "\n",
    "### Task\n",
    "Modify the function `create_tractor()` that uses the four parameters - `model`, `colour`, `horsepower`, and `fuel_capacity` - and use these to create and return a dictionary representing a tractor. \n",
    "\n",
    "The dictionary should include the following keys: \n",
    "`model`, `colour`, `horsepower`, and `fuel_capacity`. You can choose appropriate values for these keys based on what a typical tractor might have."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2ef9c6f4",
   "metadata": {},
   "source": [
    "Answer:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "996764dc",
   "metadata": {},
   "outputs": [],
   "source": [
    "### START FUNCTION\n",
    "def create_tractor(model, colour, horsepower, fuel_capacity):\n",
    "    # Insert your code here\n",
    "    return\n",
    "### END FUNCTION"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "709f07f6",
   "metadata": {},
   "source": [
    "### Expected Outputs"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3226feab",
   "metadata": {},
   "source": [
    "**Input 1:**\n",
    "\n",
    "Expected output: `{'model': 'TX-1300', 'colour': 'Green', 'horsepower': 150, 'fuel_capacity': 60}`\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eea58967",
   "metadata": {},
   "outputs": [],
   "source": [
    "# input 1\n",
    "create_tractor('TX-1300', 'Green', 150, 60)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "58c369cf",
   "metadata": {},
   "source": [
    "<br>\n",
    "\n",
    "**Input 2:**\n",
    "\n",
    "Expected output: `{'model': 'RX-850', 'colour': 'Red', 'horsepower': 120, 'fuel_capacity': 45}`\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "64746d51",
   "metadata": {},
   "outputs": [],
   "source": [
    "# input 2\n",
    "create_tractor('RX-850', 'Red', 120, 45)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d663c5a4",
   "metadata": {},
   "source": [
    "## Challenge 2: Represent a field\n",
    "\n",
    "Now that we have our tractor in the digital realm, let's focus on another crucial aspect of the farm: the fields. A field is where the magic happens, where crops are grown and nurtured. In our digital twin of the farm, representing fields accurately is vital for planning, monitoring crop growth, and managing resources.\n",
    "\n",
    "To digitally represent a field, we'll use a list of lists in Python. This structure is akin to a grid, where each sublist can represent a section or row of the farm field, allowing us to simulate and analyse different areas of the field individually.\n",
    "\n",
    "When we have planted a row of crops in a field, we can represent it as a 1, while a 0 would represent a part of the field that is not planted. The unplanted field can be represented as a list of lists:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dc75de08",
   "metadata": {},
   "outputs": [],
   "source": [
    "unplanted_field = [\n",
    "[0, 0, 0],\n",
    "[0, 0, 0],\n",
    "[0, 0, 0]\n",
    "]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0c6c5f3a",
   "metadata": {},
   "source": [
    "This next variable would represent a field that is 3x3 in size, containing a row of plants at `index = 1`. \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "437a1c3b",
   "metadata": {},
   "outputs": [],
   "source": [
    "planted_field = [\n",
    "[0, 0, 0],\n",
    "[1, 1, 1],\n",
    "[0, 0, 0]\n",
    "]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cbaab2d2",
   "metadata": {},
   "source": [
    "### Task\n",
    "\n",
    "Given **any size field**, and **the index** of the row we would like to plant, convert the unplanted field into a planted one by specifying which row should be planted:\n",
    "\n",
    "`plant_row(field, row_to_plant):` takes two parameters:\n",
    "\n",
    "- `field`: a nested list representing a field.\n",
    "\n",
    "- `row_to_plant`: an integer representing the **index** of the row to be planted.\n",
    "\n",
    "Modify the function to **modify the specified row** in the field by setting all its elements to 1 (representing planting) and return the modified field. It should work regardless of the size of the field. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "aad1f787",
   "metadata": {},
   "source": [
    "**Hint:** To create a list of 1's, multiply `[1]` with the length of the required list:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3d37111e",
   "metadata": {},
   "outputs": [],
   "source": [
    "[1] *10"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9d446911",
   "metadata": {},
   "source": [
    "Answer:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3efdf970",
   "metadata": {},
   "outputs": [],
   "source": [
    "### START FUNCTION\n",
    "def plant_row(field, row_to_plant):\n",
    "    # Insert your code here\n",
    "    return \n",
    "### END FUNCTION"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ede1b85f",
   "metadata": {},
   "source": [
    "### Expected Outputs"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2611864e",
   "metadata": {},
   "source": [
    "**Input 1:** \n",
    "\n",
    "Expected output: `[[0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]]`\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f60c79b0",
   "metadata": {},
   "outputs": [],
   "source": [
    "# input 1\n",
    "plant_row([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], 1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1c2811e7",
   "metadata": {},
   "source": [
    "<br>\n",
    "\n",
    "**Input 2:** \n",
    "\n",
    "Expected output: `[[1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]`\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "27232159",
   "metadata": {},
   "outputs": [],
   "source": [
    "plant_row([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 0)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "58081d6b",
   "metadata": {},
   "source": [
    "## Challenge 3: Represent all farm vehicles\n",
    "In our digital twin farm, managing a diverse fleet of farm vehicles efficiently is key to optimizing farm operations. Each vehicle in our fleet, such as tractors and harvesters, has specific attributes like model, colour, horsepower, and fuel capacity. By keeping a digital record of these vehicles, we can simulate various scenarios, like the impact of new vehicle acquisitions on our farming operations.\n",
    "\n",
    "### Task\n",
    "\n",
    "Modify `add_vehicle(vehicles, new_vehicle):` that adds a new vehicle to an existing list of vehicles. The function will take two parameters:\n",
    "\n",
    "- `vehicles`: a list of dictionaries, where each dictionary represents a vehicle.\n",
    "\n",
    "- `new_vehicle_params`: A list representing the new vehicle. It will contain values for `model`, `colour`, `horsepower`, and `fuel_capacity`, in that order."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "02b51950",
   "metadata": {},
   "outputs": [],
   "source": [
    "existing_vehicles = [\n",
    "    {'model': 'TX-130', 'colour': 'Green', 'horsepower': 150, 'fuel_capacity': 60},\n",
    "    {'model': 'RX-850', 'colour': 'Red', 'horsepower': 120, 'fuel_capacity': 45}\n",
    "]\n",
    "\n",
    "new_vehicle_params = ('ZX-500', 'Blue', 130, 55)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a34aacd7",
   "metadata": {},
   "outputs": [],
   "source": [
    "### START FUNCTION\n",
    "def add_vehicle(vehicles, new_vehicle_params):\n",
    "    # Insert your code here\n",
    "    return\n",
    "### END FUNCTION"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a6153b57",
   "metadata": {},
   "source": [
    "### Expected Outputs:"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "81dc7e84",
   "metadata": {},
   "source": [
    "**Input 1:**\n",
    "\n",
    "Expected output:\n",
    "\n",
    "`[{'model': 'TX-130',\n",
    "  'colour': 'Green',   'horsepower': 150,  'fuel_capacity': 60},\n",
    " {'model': 'RX-850', 'colour': 'Red', 'horsepower': 120, 'fuel_capacity': 45},\n",
    " {'model': 'SX-750',   'colour': 'White',  'horsepower': 180,  'fuel_capacity': 80}]`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "60c28123",
   "metadata": {},
   "outputs": [],
   "source": [
    "# input 1\n",
    "existing_vehicles = [\n",
    "    {'model': 'TX-130', 'colour': 'Green', 'horsepower': 150, 'fuel_capacity': 60},\n",
    "    {'model': 'RX-850', 'colour': 'Red', 'horsepower': 120, 'fuel_capacity': 45}\n",
    "]\n",
    "\n",
    "new_vehicle =  ('SX-750', 'White', 180, 80)\n",
    "add_vehicle(existing_vehicles, new_vehicle)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a5f42a77",
   "metadata": {},
   "source": [
    "<br>\n",
    "\n",
    "**Input 2:** \n",
    "\n",
    "Expected output:\n",
    "\n",
    "`[{'model': 'TX-130',  'colour': 'Green',  'horsepower': 150,  'fuel_capacity': 60},\n",
    " {'model': 'RX-850', 'colour': 'Red', 'horsepower': 120, 'fuel_capacity': 45},\n",
    " {'model': 'ZX-500', 'colour': 'Blue', 'horsepower': 130, 'fuel_capacity': 55}]`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "756d1515",
   "metadata": {},
   "outputs": [],
   "source": [
    "# input 2\n",
    "existing_vehicles = [\n",
    "    {'model': 'TX-130', 'colour': 'Green', 'horsepower': 150, 'fuel_capacity': 60},\n",
    "    {'model': 'RX-850', 'colour': 'Red', 'horsepower': 120, 'fuel_capacity': 45}\n",
    "]\n",
    "\n",
    "new_vehicle_params = ('ZX-500', 'Blue', 130, 55)\n",
    "add_vehicle(existing_vehicles, new_vehicle_params)"
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
  },
  {
   "cell_type": "markdown",
   "id": "a56df372",
   "metadata": {},
   "source": []
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
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
