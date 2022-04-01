import matplotlib.pyplot as plt
import numpy as np
#print(plt.style.available)
# Constants
SECONDS_IN_ONE_HOUR = 3600
LAP_DISTANCE = 0.4          # Distance of one lap in Km

# Converts time from "minute.seconds" to "seconds"
def convert_to_sec(time_value):
    return (time_value-time_value%1)*60 + (time_value%1)*100;

# Returns the mean value of an array
def compute_mean(array):
    size = len(array)
    mean = 0
    for i in range(size):
        mean += array[i]
    return mean/size

# Find the lowest value on an array
def find_min(array):
    min = array[0]
    pos = 0
    for i in range(len(array)):
        if (min > array[i]):
            min = array[i]
            pos = i
    return min,pos

# Shows the plot loaded from the different runs
def show_plot(legend_array):
    plt.legend(legend_array)
    plt.ylabel('seconds')
    plt.xlabel('laps')
    plt.title('Time per lap')
    plt.grid(True)
    #plt.tight_layout()
    plt.show()
    
# Run_infos is an object containing relevant informations for a run
class Run_infos():
    def __init__(self, lap_time):
        self.lap_time = lap_time                    # array with the time for each lap in "minutes.seconds"
        self.nb_laps  = len(lap_time)               # number of laps in the run
        self.lap_time_s = []                        # array with the time for each lap in "seconds"
        self.mtpl     = 0                           # Mean Time Per Lap in seconds
        self.speed    = 0                           # Mean speed during the whole run in Km/h
        self.total_time = 0                         # Total time of the run in s
        self.total_distance = 0                     # Total distance travelled
        self.top_speed = 0                          # Speed during best lap
        self.best_time = 0
        self.best_lap = 0

    def compute_infos(self):
        for i in range(self.nb_laps):
            if (self.lap_time[i] != 0):
                self.lap_time_s.append(convert_to_sec(self.lap_time[i]))
                self.total_time += self.lap_time_s[i]
            else:
                break
        self.nb_laps = len(self.lap_time_s)
        self.mtpl = compute_mean(self.lap_time_s)
        self.speed = LAP_DISTANCE / self.mtpl * SECONDS_IN_ONE_HOUR
        self.total_distance = self.nb_laps * LAP_DISTANCE
        self.best_time,self.best_lap = find_min(self.lap_time_s)
        self.best_lap += 1
        self.top_speed = LAP_DISTANCE / self.best_time * SECONDS_IN_ONE_HOUR

    def load_plot(self):
        x = range(self.nb_laps)+np.ones(self.nb_laps)
        y = self.lap_time_s
        plt.style.use('fivethirtyeight')
        plt.plot(x,y, 'o-')#, x, np.ones(self.nb_laps)*self.mtpl, 'r')









