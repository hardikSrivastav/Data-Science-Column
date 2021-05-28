from random import random as rand

# 100 Million

flip_result_100mil = []
counter_100mil = 0

for i in range(100000001):
    if rand() >= 0.5:
        flip_result_100mil.append(1)
    elif rand() <= 0.5:
        flip_result_100mil.append(0)
    counter_100mil = i

sum_of_values_100mil = sum(flip_result_100mil)
prob_100mil = sum_of_values_100mil/counter_100mil * 100

# 10 Million

flip_result_10mil = []
counter_10mil = 0

for i in range(10000001):
    if rand() >= 0.5:
        flip_result_10mil.append(1)
    elif rand() <= 0.5:
        flip_result_10mil.append(0)
    counter_10mil = i

sum_of_values_10mil = sum(flip_result_10mil)
prob_10mil = sum_of_values_10mil/counter_10mil * 100

# 1 Million

flip_result_1mil = []
counter_1mil = 0

for i in range(1000001):
    if rand() >= 0.5:
        flip_result_1mil.append(1)
    elif rand() <= 0.5:
        flip_result_1mil.append(0)
    counter_1mil = i

sum_of_values_1mil = sum(flip_result_1mil)
prob_1mil = sum_of_values_1mil/counter_1mil * 100

# 100 Thousand

flip_result_100thou = []
counter_100thou = 0

for i in range(100001):
    if rand() >= 0.5:
        flip_result_100thou.append(1)
    elif rand() <= 0.5:
        flip_result_100thou.append(0)
    counter_100thou = i

sum_of_values_100thou = sum(flip_result_100thou)
prob_100000 = sum_of_values_100thou/counter_100thou * 100

# 10 Thousand

flip_result_10thou = []
counter_10thou = 0

for i in range(10001):
    if rand() >= 0.5:
        flip_result_10thou.append(1)
    elif rand() <= 0.5:
        flip_result_10thou.append(0)
    counter_10thou = i

sum_of_values_10thou = sum(flip_result_10thou)
prob_10000 = sum_of_values_10thou/counter_10thou * 100

# 1 Thousand

flip_result_1thou = []
counter_1thou = 0

for i in range(1001):
    if rand() >= 0.5:
        flip_result_1thou.append(1)
    elif rand() <= 0.5:
        flip_result_1thou.append(0)
    counter_1thou = i

sum_of_values_1thou = sum(flip_result_1thou)
prob_1000 = sum_of_values_1thou/counter_1thou * 100

# 1 Hundred

flip_result_hund = []
counter_hund = 0

for i in range(101):
    if rand() >= 0.5:
        flip_result_hund.append(1)
    elif rand() <= 0.5:
        flip_result_hund.append(0)
    counter_hund = i

sum_of_values_hund = sum(flip_result_hund)
prob_100 = sum_of_values_hund/counter_hund * 100

# Tens

flip_result_10 = []
counter_10 = 0

for i in range(11):
    if rand() >= 0.5:
        flip_result_10.append(1)
    elif rand() <= 0.5:
        flip_result_10.append(0)
    counter_10 = i

sum_of_values_10 = sum(flip_result_10)
prob_10 = sum_of_values_10/counter_10 * 100

# Removing chances of Co-incidences

series_100mil = [49.996471, 49.99847, 49.991541, 49.998379, 49.998779, 49.99611, 49.997831, 49.993915, 50.000566, 50.005078999999995]
series_10mil = [49.97355, 49.96741, 50.010960000000004, 49.99436, 49.98839, 50.022009999999995, 49.985079999999996, 50.0043, 49.99295, 49.97551]
series_1mil = [50.029500000000006, 49.9621, 50.0264, 50.0212, 50.0485, 49.9998, 50.134299999999996, 50.029, 49.9871, 50.013200000000005]
series_100thou = [49.577, 49.958999999999996, 49.85, 49.906, 49.95, 49.905, 50.077000000000005, 49.961, 50.097, 50.073] 
series_10thou = [49.39, 49.93, 50.81, 50.59, 48.63, 50.019999999999996, 49.62, 49.059999999999995, 51.09, 50.129999999999995]
series_1thou = [50.2, 51.300000000000004, 49.8, 52.6, 51.7, 50.0, 48.1, 49.3, 50.9, 48.699999999999996]
series_100 = [49.0, 51.0, 44.0, 54.0, 42.0, 45.0, 47.0, 56.00000000000001, 40.0, 40.0]
series_10 = [80.0, 60.0, 40.0, 60.0, 30.0, 50.0, 70.0, 60.0, 60.0, 40.0]

name_length = {}

def len_and_dic_creator(array_variables, array_variables_text):
    lengths = []
    for i in range(len(array_variables)):
        lengths.append(len(array_variables[i]))
    
    for i in range(len(array_variables)):
        name_length[array_variables_text[i]] = lengths[i]
    return print(name_length)

series, series_text = [series_100mil, series_10mil, series_1mil, series_100thou, series_10thou, series_1thou, series_100, series_10], ['series_100mil', 'series_10mil', 'series_1mil', 'series_100thou', 'series_10thou', 'series_1thou', 'series_100', 'series_10']

# Defining and Interpreting Attributes

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family': 'serif'})

averages = [np.average(series_10), np.average(series_100), np.average(series_1thou), np.average(series_10thou), np.average(series_100thou), np.average(series_1mil), np.average(series_10mil),  np.average(series_100mil)]
min_ = [min(series_10), min(series_100), min(series_1thou), min(series_10thou), min(series_100thou), min(series_1mil), min(series_10mil), min(series_100mil)]
max_ = [max(series_10), max(series_100), max(series_1thou), max(series_10thou), max(series_100thou), max(series_1mil), max(series_10mil), max(series_100mil)]
std_dev = [np.std(series_10), np.std(series_100), np.std(series_1thou), np.std(series_10thou), np.std(series_100thou), np.std(series_1mil), np.std(series_10mil),  np.std(series_100mil)]
difference = []

def difference_cal():
    for i in range(len(min_)):
        difference.append(max_[i] - min_[i])
    return difference

numbers = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]
numbers2 = ['10', '100', '1,000', '10,000', '100,000', '1 Mil', '10 Mil', '100 Mil']
data_attributes = pd.DataFrame({
    'Observations': numbers,
    'Statistical Mean': averages,
    'Minimum': min_,
    'Maximum': max_,
    'Difference': difference_cal(),
    'Standard Deviation': std_dev
})

y_err = data_attributes.iloc[:, -1].values

# Plotting the result

plt.scatter(numbers2, averages, s = 25, c = 'C0')
plt.plot(numbers2, averages, c = '#ff9248')
plt.errorbar(numbers2, averages, y_err, fmt = 'o', capsize=2, ecolor='#ff9248')
plt.annotate('Standard Deviation', xy = (0, 60), xytext=(0.6, 60), color='#ff9248', verticalalignment = 'center', arrowprops=dict(arrowstyle = '->', fc = '#ff9248', ec = '#ff9248'))
plt.annotate('', xy = (4, 50.25), xytext=(5, 50.3), color='C0', arrowprops=dict(ls = None, arrowstyle = '<->', connectionstyle="bar", ec = 'C0'))
plt.annotate('Statistical Mean(s)', xy = (4.5, 52.575), horizontalalignment='center', c = 'C0')
plt.title('Proving the Law of Large Numbers', size=16)
plt.xlabel('Number of Observations', size=10)
plt.ylabel('Probability (%)', size=10)

    # Credit for the following function goes to Tony S. Yu from https://tonysyu.github.io/

def errorfill(numbers2, averages, y_err, color='#ff9248', alpha_fill=0.3, ax=None):
    ax = ax if ax is not None else plt.gca()
    if np.isscalar(y_err) or len(y_err) == len(averages):
        ymin = averages - y_err
        ymax = averages + y_err
    elif len(y_err) == 2:
        ymin, ymax = y_err
    ax.plot(numbers2, averages, color='C0')
    ax.fill_between(numbers2, ymax, ymin, color=color, alpha=alpha_fill)

errorfill(numbers2, averages, y_err)
#plt.savefig('Proof of Law of Large Numbers', dpi=700)
plt.show()
