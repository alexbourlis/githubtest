# 1st file unique to branch A
# ************************************************************************************************************
# Main File collecting the times of every lap for each run. In this file we declare the objects "Run" of class
# "Run_infos" containing different relevant informations for each run we have stored in the run_data.txt. This
# file also displays those informations and plots the time per lap for each run
# Creator: Corbaz Alexandre
# Date: 17/03/2022
# ************************************************************************************************************
from B_file1 import *
import dis

def ordinal(number):
    if number==0: return "ERROR"
    elif number==1: return "1st"
    elif number==2: return "2nd"
    elif number==3: return "3rd"
    else: return "%dth" % number
# imaginary runs:
# 1.50,1.50,1.48,1.45,1.48,1.52,1.58,1.55,2,1.57,1.57,1.50,1.56,1.51,1.45,1.40
# 1.50,1.50,1.48,1.50,1.48,1.45,1.40,1.41,1.45,1.5,1.57,1.56,1.56,1.51,1.45,1.38
data_file = np.loadtxt('run_data.txt', delimiter=',')
lap_time = np.array(data_file[0:,0:])
n = lap_time.shape[0]

RunsArray = []

for i in range(n):
    Run = Run_infos(lap_time[i,:])
    Run.compute_infos()
    RunsArray.append(Run)

count = 1
legend_array = []
plt.rcParams["figure.figsize"] = (11,7.4)
for Run in RunsArray:
    print("Informations for the", ordinal(count), "run")
    print("mean time per lap:                %0.3f s" % Run.mtpl)
    print("mean speed of the whole run:     ", "%0.3f" % Run.speed, "Km/h")
    print("Top mean Speed of: %0.3f Km/h" % Run.top_speed, "during the", ordinal(Run.best_lap), "lap")
    print("Total time of the run            ", Run.total_time, "s")
    print("Total distance travelled:         %0.1f" % Run.total_distance, "Km\n\n")
    Run.load_plot()
    legend_array.append("%s Run" % ordinal(count))
    count += 1

show_plot(legend_array)

#dis.dis(dis)
