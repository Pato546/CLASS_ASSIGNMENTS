#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib import style
import csv

style.use('ggplot')

class CentralDifference():

    def __init__(self, m, c, k, T):
        self.m = m  # mass of the structure
        self.c = c  # damping of the structure
        self.k = k  # stiffness of the structure
        self.T = T  # Time span 

    def type1(self, disp_initial=0, vel_initial=0):
        load = float(input('[+] Enter the load: '))
        chg_time = float(input('[+] Enter the change in time: '))
        chg_times = []
        t = 0
        
        for i in range(T):
            chg_times.append(round(t, 1))
            t += chg_time

        a = round((self.m / chg_time**2) + (self.c / 2 * chg_time), 1) # left-hand-side coefficient
        b = round((self.c / 2 * chg_time) - (self.m / chg_time**2), 1) # coefficient of previous displacement
        e = round((2 * self.m / chg_time**2)-k, 1) # coefficient of initial displacement
        disp_initial = disp_initial
        vel_initial = vel_initial
        displacements = []
        acc_initial = (load / self.m) - (self.c / self.m) * vel_initial - (self.k / self.m) * disp_initial 

        disp_prev = round(disp_initial - chg_time * vel_initial + ((chg_time**2)/2) * acc_initial, 5)
    
        for time in chg_times:
            disp_current = (load / a) + ((b / a) * disp_prev) + (( e / a) * (disp_initial)) 
            displacements.append(round(disp_current, 5) )

            disp_prev = disp_initial
            disp_initial = disp_current

        print(chg_times)
        print(displacements)

        return chg_times, displacements        

    def type2(self, disp_initial=0, vel_initial=0):
        chg_time = float(input('[+] Enter the change in time: '))
        y = float(input('[+] Enter the y-intercept of the load function: ')) # y-intercept of the load function
        x = float(input('[+] Enter the x-intercept of the load function: ')) # x-intercept of the load function
        s = (y - 0) / (0 - x) # slope of the load function
        chg_times = []
        t = 0 # initial time

        for i in range(T):
            chg_times.append(round(t,1))
            t += chg_time

        loads = [round(y + s * time, 1) if not time > x else 0 for time in chg_times]
        disp_initial = disp_initial # initial displacement
        vel_initial = vel_initial # initial velocity
        acc_initial = (loads[0] / self.m) - (self.c / self.m) * vel_initial - (self.k / self.m) * disp_initial # initial acceleration
        displacements = []
        a = round((self.m / chg_time**2) + (self.c / 2 * chg_time), 1) # left-hand-side coefficient
        b = round((self.c / 2 * chg_time) - (self.m / chg_time**2), 1) # coefficient of previous displacement
        e = round((2 * self.m / chg_time**2)-k, 1) # coefficient of initial displacement
        disp_prev = round(disp_initial - chg_time * vel_initial + ((chg_time**2)/2) * acc_initial, 5)
    
        for load in loads:
            disp_current = (load / a) + ((b / a) * disp_prev) + (( e / a) * (disp_initial)) 
            displacements.append(round(disp_current, 5) )

            disp_prev = disp_initial
            disp_initial = disp_current

        print(displacements)
        return chg_times, displacements        

    def type3(self, disp_initial=0, vel_initial=0):

        chg_time = float(input('[+] Enter the change in time: '))

        a = round((self.m / chg_time**2) + (self.c / 2 * chg_time), 1) # left-hand-side coefficient
        b = round((self.c / 2 * chg_time) - (self.m / chg_time**2), 1) # coefficient of previous displacement
        e = round((2 * self.m / chg_time**2)-k, 1) # coefficient of initial displacement
        

        with open('El_Centro.csv') as f:
            el_data = csv.reader(f)
            chg_times = []
            displacements = []
            for data in el_data:
                t, g = data
                if t == '0':
                    t = float(t)
                    g = float(g)
                    disp_initial = disp_initial
                    vel_initial = vel_initial
                    acc_initial = -g - (self.c / self.m) * vel_initial - (self.k / self.m) * disp_initial
                    disp_prev = disp_initial - (chg_time * vel_initial) + ((chg_time**2)/2) * acc_initial 
                    print(acc_initial)
                    print(disp_prev)

                disp_current = ((-float(g) * self.m) / a) + ((b / a) * disp_prev) + (( e / a) * (disp_initial)) 
                displacements.append(disp_current)

                disp_prev = disp_initial
                disp_initial = disp_current

                chg_times.append(float(t))
        print(displacements) 
        return chg_times, displacements


    @staticmethod
    def plot(*args):
        for x, y in args:
            plt.plot(x, y)    
            plt.title('DISPLACEMENT AGAINST TIME GRAPH')
            plt.ylabel('displacement')
            plt.xlabel('time')
            plt.grid(True, color='g')
            plt.show()
    

if __name__ == '__main__':
    m = int(input('[+] Enter the mass of the structure: '))
    c = int(input('[+] Enter the damping of the structure: '))
    k = int(input('[+] Enter the stiffness of the structure: '))
    T = int(input('[+] Enter the time span of the structure: '))
    type_of_question = input('[+] Enter type of question: ')

    q = CentralDifference(m,c,k,T)
    
    if type_of_question == '1':
        q.plot(q.type1())
    elif type_of_question == '2':
        q.plot(q.type2())
    else:
        q.plot(q.type3())


















