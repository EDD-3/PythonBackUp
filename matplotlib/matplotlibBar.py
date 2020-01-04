from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]

plt.bar(range(len(drinks)), sales)

#create your ax object here



ax = plt.subplot()
ax.set_xticks(range(len(drinks)))
ax.set_xticklabels(drinks)

plt.show()


#Side by side bars
from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

#Paste the x_values code here
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = 6 # Number of sets of bars
w = 0.8 # Width of each bar
store1_x = [t*element + w*n for element
             in range(d)] #Never change list comprehension

n = 2  # This is our second dataset (out of 2)
t = 2 # Number of datasets
d = 6 # Number of sets of bars
w = 0.8 # Width of each bar
store2_x = [t*element + w*n for element
             in range(d)]

plt.bar(store1_x, sales1)
plt.bar(store2_x, sales2)

plt.show()

#Stacked bars
from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

plt.bar(range(len(sales1)),sales1,label='Location 1')
plt.legend()
plt.bar(range(len(sales2)),sales2,bottom=sales1,label='Location 2')
plt.legend()
plt.show()

#Multiple stacked bars
# Given the follow y values for 3 groups of data
group1 = [1, 1, 1, 1]
group2 = [2, 2, 2, 2]
group3 = [3, 3, 3, 3]

x = [0, 1, 2, 3] # x positions

# First layer of bars
plt.bar(x, group1)

# Second layer of bars
plt.bar(x, group2, bottom=group1)

# Adding a third layer of bars.
# Calculate the bottom height of the third layer
# by adding together all lower layer heights.
bottom_of_3 = [1+2, 1+2, 1+2, 1+2] # [3, 3, 3, 3]

# Third layer of bars
plt.bar(x, group3, bottom=bottom_of_3)

#Error bars
from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
ounces_of_milk = [6, 9, 4, 0, 9, 0]
error = [0.6, 0.9, 0.4, 0, 0.9, 0]

# Plot the bar graph here
plt.bar(range(len(ounces_of_milk)),ounces_of_milk, yerr=error, capsize=5)

plt.show()