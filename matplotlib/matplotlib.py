from matplotlib import pyplot as plt

x = [1997 + i for i in range(13)]
y1 = [800 + i*100 for i in range(13)]
y2 = [40 + i*10 for i in range(13)]

plt.close('all')
plt.figure()
plt.plot(x, y1, color='pink', marker='o')
plt.plot(x, y2, color='gray', marker='o')
plt.title("Two Lines on One Graph")
plt.xlabel("Amazing X-axis")
plt.ylabel("Incredible Y-axis")
plt.legend(['Math doctorates awarded','Uranium US power plants'], loc=4)
plt.show()

plt.savefig('plot_testing.png')

#Change linear plot color and line style
time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]

plt.plot(time, revenue, color='purple', linestyle='--')
plt.plot(time, costs, color='#82edc9', marker='s')
plt.show()

#Zoom on plot
x = range(12)
y = [3000, 3005, 3010, 2900, 2950, 3050, 3000, 3100, 2980, 2980, 2920, 3010]
plt.plot(x, y)

#your code here
plt.axis([0, 12, 2900, 3100])
# .axis([x-min-value,x-max-value,y-min-value,y-max-value])
plt.show()

#Label axes
x = range(12)
y = [3000, 3005, 3010, 2900, 2950, 3050, 3000, 3100, 2980, 2980, 2920, 3010]
plt.plot(x, y)
plt.axis([0, 12, 2900, 3100])
plt.xlabel('Time')
plt.ylabel('Dollars spent on coffee')
plt.title('My Last Twelve Years of Coffee Drinking')
plt.show()

#Subplots
months = range(12)
temperature = [36, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]
flights_to_hawaii = [1200, 1300, 1100, 1450, 850, 750, 400, 450, 400, 860, 990, 1000]

plt.subplot(1,2,1);
plt.plot(months, temperature, color="green")
plt.title('Temperature and months')
plt.subplot(1,2,2);
plt.plot(flights_to_hawaii, temperature, "o")
plt.title('Temperature and months')
plt.show() 


#Subplot adjust
x = range(7)
straight_line = [0, 1, 2, 3, 4, 5, 6]
parabola = [0, 1, 4, 9, 16, 25, 36]
cubic = [0, 1, 8, 27, 64, 125, 216]

plt.subplot(2,1,1)
plt.plot(x, straight_line)
plt.subplot(2,2,3)
plt.plot(x, parabola)
plt.subplot(2,2,4)
plt.plot(x, cubic)
plt.subplots_adjust(wspace=0.35, bottom=0.2)
plt.show()


#Modify x and y ticks
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep","Oct", "Nov", "Dec"]
months = range(12)
conversion = [0.05, 0.08, 0.18, 0.28, 0.4, 0.66, 0.74, 0.78, 0.8, 0.81, 0.85, 0.85]

plt.xlabel("Months")
plt.ylabel("Conversion")
plt.plot(months, conversion)

# Your work here
ax = plt.subplot()
ax.set_xticks(months)
ax.set_xticklabels(month_names)
ax.set_yticks([0.10, 0.25, 0.5, 0.75])
ax.set_yticklabels(["10%", "25%", "50%", "75%"])

plt.show()

#Creating figures and modifying ticks, labels, title, 
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
visits_per_month = [9695, 7909, 10831, 12942, 12495, 16794, 14161, 12762, 12777, 12439, 10309, 8724]

# numbers of limes of different species sold each month
key_limes_per_month = [92.0, 109.0, 124.0, 70.0, 101.0, 79.0, 106.0, 101.0, 103.0, 90.0, 102.0, 106.0]
persian_limes_per_month = [67.0, 51.0, 57.0, 54.0, 83.0, 90.0, 52.0, 63.0, 51.0, 44.0, 64.0, 78.0]
blood_limes_per_month = [75.0, 75.0, 76.0, 71.0, 74.0, 77.0, 69.0, 80.0, 63.0, 69.0, 73.0, 82.0]


# create your figure here
plt.figure(figsize=(12, 8))
ax1 = plt.subplot(1,2,1)
x_values = range(len(months))
plt.plot(x_values,visits_per_month, marker='s')
plt.xlabel("Years")
plt.ylabel("Number of visits")
ax1.set_xticks(x_values)
ax1.set_xticklabels(months)
plt.title("Website visits by month")
ax2 = plt.subplot(1,2,2)
plt.plot(x_values, key_limes_per_month, color="green")
plt.plot(x_values, persian_limes_per_month, color="purple")
plt.plot(x_values, blood_limes_per_month, color="red")
plt.legend(['Key limes', 'Blood limes', 'Persian limes'])
ax2.set_xticks(x_values)
ax2.set_xticklabels(months)
plt.title('Limes sold in year')
plt.ylabel("Number of limes")
plt.subplots_adjust(wspace=0.40)
plt.show()

plt.savefig('visits_and_limes_per_year.png')


#Display error as linear plot
from matplotlib import pyplot as plt

months = range(12)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue = [16000, 14000, 17500, 19500, 21500, 21500, 22000, 23000, 20000, 19500, 18000, 16500]
y_lower = [ rev * 0.9 for rev in revenue]
y_upper = [ rev * 1.1 for rev in revenue]

#your work here
plt.fill_between(months,y_lower,y_upper,alpha=0.2)
plt.plot(months,revenue)

ax = plt.subplot()
ax.set_xticks(months)
ax.set_xticklabels(month_names)
plt.show()