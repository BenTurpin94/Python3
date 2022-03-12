import math
from operator import mod



angle = int(input("Enter angle of ball"))
force  = int(input("Enter force of ball"))
mass= int(input("mass of ball"))
time_interval=int(input("select time intervals"))
total_time=int(input("select total time"))

def accelerationx(force,angle,mass):
    int(force*math.cos(angle)/mass)

accelerationy=-9.81

def velocityx(accelerationx,time):
    int(accelerationx*time)

def velocityy(accelerationy,time):
    int(accelerationy*time)

def distancex(accelerationx,time):
    int(0.5*accelerationx*time**2)

def distancey(accelerationy, time):
    int(0.5*accelerationy*time**2)

time=0
while time < total_time:
    print("Acceleration at time t=",time, "(",accelerationx(force,angle,mass),accelerationy,")")
    print("Velocity at time t=",time,"(",velocityx(accelerationx,time),velocityy(accelerationy,time),")")
    print("Posesion at time t=",time,"(",distancex(accelerationx,time),distancey(accelerationy,time),")")
    time += time_interval









