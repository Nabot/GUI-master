#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep

std_speed = 100
std_time = 1000

#stops all motors, takes a list of motors
def stop(motors):
	for m in motors:
		m.stop(stop_action='brake')

#moves the large motors
def move(motors, speed=std_speed):
	for m in motors:
		m.run_forever(speed_sp=speed)

#lifts the arms using the medium motor
def lift(lifting_motor, waiting_motors):
	move(waiting_motors, speed=0)
	lifting_motor.run_to_rel_pos(speed_sp = 50, position_sp=50, stop_action='brake')
	sleep(0.1)
	lifting_motor.wait_while('running')
	stop(waiting_motors)
	stop([lifting_motor])



#turns the robot using the move() function
def turn(motors, dir):
	if dir == 'left':
		#changes polarity of left wheel
		motors[0].polarity = 'inversed'
		motors[1].polarity = 'normal'
		move(motors)
	else:
		#changes polarity of right wheel
		motors[0].polarity = 'normal'
		motors[1].polarity = 'inversed'
		move(motors)
	motors[0].polarity = 'normal'
	motors[1].polarity = 'normal'

#script


#initiate motors
left_motor = LargeMotor('outA')
right_motor = LargeMotor('outD')
medium_motor = MediumMotor('outB')

#initiate motor sets
large_motors = [left_motor, right_motor]
all_motors = [left_motor,right_motor,medium_motor]

#initiate sensors
cs = ColorSensor('in1')
gs = GyroSensor('in2')
us = UltrasonicSensor('in4')

#reset gyrosensor
gs.mode = 'GYRO-RATE'
gs.mode = 'GYRO-ANG'
turning = 0

#script to run, lift, turn left if object close, turn right if moving onto white paper
move(large_motors)
while True:
	angle = gs.angle
	distance = us.distance_centimeters
	light = cs.reflected_light_intensity
	print(light)
	if (abs(angle) > 78) and turning:
		stop(all_motors)
		gs.mode = 'GYRO-RATE'
		gs.mode = 'GYRO-ANG'
		turning = 0
		move(large_motors)
	elif (light < 15) and not turning:
		stop(all_motors)
		#lift(medium_motor, large_motors)
		turn(large_motors, 'right')
		turning = 1
	elif (light < 89) and not turning:
		stop(all_motors)
		#lift(medium_motor, large_motors)
		turn(large_motors, 'right')
		turning = 1
	elif (distance < 50) and not turning:	
		stop(all_motors)
		lift(medium_motor, large_motors)
		turning = 1
		exit()
		


"""
while True:
	#initiate values used in loop
	light = cs.reflected_light_intensity		
	distance = us.distance_centimeters
	angle = gs.angle
	if (distance < 105) and not turning:	
		stop(all_motors)
		lift(medium_motor, large_motors)
		turn(large_motors, 'left')
		turning = 1
	if (light > 80) and not turning:
		stop(all_motors)
		lift(medium_motor, large_motors)
		turn(large_motors, 'right')
		turning = 1			
	if (abs(angle) > 90) and turning:
		stop(all_motors)
		gs.mode = 'GYRO-RATE'
		gs.mode = 'GYRO-ANG'
		turning = 0
		exit()
"""