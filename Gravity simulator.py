import math
import matplotlib.pyplot as plt
import numpy as np
from operator import mod



angle = float(input("Enter angle of ball"))
velocity  = float(input("Enter velocity  of ball"))
mass= float(input("mass of ball"))
time_interval=float(input("select time intervals"))
total_time=float(input("select total time"))

def intvelx(velocity,angle):
    return float(velocity*math.cos(angle))

def intvely(velocity,angle):
    return float(velocity*math.sin(angle))    


#def accelerationx(force,angle,mass):
 #   return float(force*math.cos(angle)/mass)

accelerationy=-9.81

def velocityx(intvelx):
    return float(intvelx)

def velocityy(intvely,accelerationy,time):
    return float(intvely+accelerationy*time)

def distancex(intvelx,time):
    return float(intvelx*time)

def distancey(accelerationy,time,velocityy,intvely):
    return float(velocityy(intvely,accelerationy,time)*time + 0.5*accelerationy*time**2)

time=0
while time < total_time:
    print("Acceleration at time t=",time, "(",0,accelerationy,")")
    print("Velocity at time t=",time,"(",velocityx(intvelx(velocity,angle)),velocityy(intvely(velocity,angle),accelerationy,time),")")
    print("Posesion at time t=",time,"(",distancex(intvelx(velocity,angle),time),distancey(accelerationy,time,velocityy(intvely(velocity,angle),accelerationy,time),intvely(velocity,angle)),")")
    time += time_interval
   # plt.plot(float(distancex(intvelx,time)),float(distancey(accelerationy,time,velocityy)),'o')
    #if float(distancey(accelerationy,time,velocityy)) < 0:
    #    break
#plt.show()









