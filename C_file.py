# Constants
SPEED_START = 8.5           # In Km/h
SPEED_INCREMENT = 0.5       # In Km/h
INC_FREQ = 0.2              # The speed increases by 0.5 Km/h every 200 meters

from B_file1 import convert_to_sec
total_time = 18.25                      # In minutes:seconds
total_time = convert_to_sec(total_time) # In seconds
total_time = total_time/3600            # In hours

total_dist = 0
time = 0
last_time = 0
speed = SPEED_START
level = 0

while time < total_time:
    if time+INC_FREQ/speed < total_time:
        level += 1
        total_dist += INC_FREQ
        time += INC_FREQ/speed
        speed += SPEED_INCREMENT
    else:
        last_time = total_time-time
        total_dist += speed*last_time
        time += last_time

mean_speed = total_dist/time
# reverting back to minutes:seconds
time *= 3600
time = (time-time%60)/60 + (time%60)/100

x = speed*last_time*1000
print("Mean speed of the run:               %0.3f Km/h" % mean_speed )
print("Running speed during last level:     %f Km/h" % speed)
print("Run ended after %0.1f meters" % x, "in level: %d" % level)
print("Total distance runned :              %0.3f Km" % total_dist)




