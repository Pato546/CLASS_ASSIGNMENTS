#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

mass = 100
number_of_iterations = 9
last_iterated_value = 0.8
chg_in_time = 0.8 / 8
chg_in_times = np.linspace(0, 0.8, 9)
loads = [round(10 - 20 * time, 1) if not time > 0.5 else 0 for time in chg_in_times]
stiffness = 6000
acc_initial = 0.1
disp_initial = 0
vel_initial = 0
displacements = []
a = round(chg_in_time ** 2 / mass, 5)
b = 2 - a * stiffness

disp_prev = round(disp_initial - chg_in_time * vel_initial + ((chg_in_time**2)/2) * acc_initial, 5)

for load in loads:
    disp_current = (a * load) - (disp_prev) + (b * disp_initial) 
    displacements.append(disp_current)

    disp_prev = disp_initial
    disp_initial = disp_current

print(displacements)



plt.plot(chg_in_times, displacements)    
plt.title('DISPLACEMENT AGAINST TIME GRAPH')
plt.ylabel('displacement')
plt.xlabel('time')
plt.grid(True, color='g')
plt.show()

    
