import math
from operator import mod


def main()
    angle = int(input("Enter angle of ball"))
    force  = int(input("Enter force of ball"))
    mass= int(input("mass of ball"))
    time_interval=int(input("select time intervals"))
    total_time=int(input("select total time"))
    
    time=0
    while time < total_time:
        print("Acceleration at time t=",time, "(",accelerationx(force,angle,mass),accelerationy,")")
        print("Velocity at time t=",time,"(",velocityx(accelerationx,time),velocityy(accelerationy,time),")")
        print("Posesion at time t=",time,"(",distancex(accelerationx,time),distancey(accelerationy,time),")")
        time += time_interval


# this is a funtion so needs to be called like accelerationx(force, mass, angle) or wont work
def accelerationx(force,angle,mass):
    return int(force*math.cos(angle)/mass)

# this is a value so can be called without the brackets
accelerationy=-9.81

def velocityx(accelerationx,time):
    return int(accelerationx(force, mass, angle)*time)

def velocityy(accelerationy,time):
    return int(accelerationy*time)

def distancex(accelerationx,time):
    return int(0.5*accelerationx(force, mass, angle)*time**2)

def distancey(accelerationy, time):
    return int(0.5*accelerationy*time**2)


if __name__ == "__main__":
    main()





