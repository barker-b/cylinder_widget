import math

def major_area(bore):
    return math.pi * bore**2 /4

def rod_area(rod):
    return math.pi * rod**2 / 4

def minor_area(bore, rod):
    return major_area(bore) - rod_area(rod)

def force(psi, bore, rod):
    push = psi * major_area(bore)
    pull = psi * minor_area(bore, rod)
    return push, pull

def cyl_speed(flow, bore, rod):
    ext_speed = flow * 231 / major_area(bore)
    ret_speed = flow * 231 / minor_area(bore, rod)
    return ext_speed, ret_speed

def time(flow, stroke, bore, rod):
    ext_speed, ret_speed = cyl_speed(flow, bore, rod)
    ext_time = stroke / ext_speed * 60
    ret_time = stroke / ret_speed * 60
    return ext_time, ret_time

def desired_speed(des_speed, bore):
    need_flow = des_speed * major_area(bore) / 231
    return need_flow

def mot_speed(flow, displacement):
    speed =  231 * flow / displacement
    return speed

def torque(pressure, displacement):
    torque = (pressure * displacement) / (2 * math.pi)
    return torque

def desired_motor_speed():
    need_flow = motorspeed * displacement
    pass