import numpy as np
import math
import CubicEquationSolver as ces

mu_sun = 1.327e20		#Standard gravitational parameter of the sun
mu_earth = 3.986e14 	#Standard gravitational parameter of the earth
mu_mars = 4.283e13      #Standard gravitational parameter of mars
r_earth = 6.378e6 		#Radius of the earth
r_mars = 3.390e6  		#Radius of mars
a_earth = 149.6e9 		#Mean distance sun-earth
a_mars = 228e9          #Mean distance sun-mars
M_mars = 6.417e23  	    #Mass of mars
a_deimos = 23463.2e3 	#Mean distance mars-deimos
v_deimos = 1.3513e3 	#Orbital speed of deimos

#PHASE 1
T_earth = 24*60*60
omega = 2*np.pi/T_earth
a = (a_earth+a_mars)/2
#1a)
v_d_inf = (2*mu_sun/a_earth-mu_sun/a)**0.5-(mu_sun/a_earth)**0.5
#1b)
sol,_,_ = ces.solve(omega**2,0,-(v_d_inf**2),-2*mu_earth)
#1c)
v_a_inf = (2*mu_sun/a_mars-mu_sun/a)**0.5-(mu_sun/a_mars)**0.5
#1d) 
#d_inf
a = mu_mars/(v_a_inf**2)
rp = 2000e3+r_mars
d_inf = ((a+rp)**2-a**2)**0.5
#dv
v_esc = (2*mu_mars/rp)**0.5
v_p = (v_esc**2+v_a_inf**2)**0.5
ra = a_deimos
a = (ra+rp)/2
v_desired = (2*mu_mars/rp-mu_mars/a)**0.5
delta_v1 = v_desired-v_p


#PHASE 2
#2a)
theta = 36*np.pi/180
v_circle = (mu_mars/ra)**0.5
print(v_circle)
v_apo = (2*mu_mars/ra - mu_mars/a)**0.5
delta_v2 = v_circle - v_apo
#2b)
delta_v = -4
delta_x = 3*np.pi*(ra-1/(2/ra-1/mu_mars*(delta_v+v_circle)**2))
k = -6*np.pi*ra/v_circle
dist = theta*ra
factor_1 = 2*np.pi*dist/k*(ra**3/mu_mars)**0.5
factor_2 = 3*factor_1/v_circle
time = 60*60*24*7
desired_delta_v = factor_1/(time-factor_2)
#2c)

#PHASE 3
#3a)
a = (a_earth+a_mars)/2
v_esc_mars = (2*mu_mars/a_deimos)**0.5
v_d_inf_r = (2*mu_sun/a_mars-mu_sun/a)**0.5-(mu_sun/a_mars)**0.5
v_departure = (v_d_inf_r**2+v_esc_mars**2)**0.5
#3b)
rp = 500e3+r_earth
v_esc_earth = (2*mu_earth/rp)**0.5
v_a_inf_r = (mu_sun/a_earth)**0.5-(2*mu_sun/a_earth-mu_sun/a)**0.5
v_perigee = (v_a_inf_r**2 + v_esc_earth**2)**0.5
v_desired_earth = (mu_earth/rp)**0.5
delta_v_final = v_desired_earth - v_perigee
#3c)
delta_v_total = (np.abs([delta_v1,delta_v2,v_departure,delta_v_final])).sum()
Isp = 350
g = mu_earth/r_earth**2
mf = 2000 #kg
mi = mf*math.exp(delta_v_total/g/Isp)
m_used = mi-mf
m_used = 1.05*m_used





print("SOLUTIONS")
print("PHASE 1")
print("a) v_d_inf: ",round(v_d_inf/1000,4),"km/s")
print("b) alt: ",(sol-r_earth)/1000,"km")
print("c) v_a_inf: ",round(v_a_inf/1000,4),"km/s")
print("d) d_inf: ", round(d_inf/1000,4), "km and delta_v1: ", round(delta_v1/1000,4),"km/s")
print("")
print("PHASE 2")
print("a) delta_v2: ", round(delta_v2/1000,4),"km/s")
print("b) k: ", round(k))
print("test delta_x: ", round(delta_x/1000,4),"km | test k: ", round(k*delta_v/1000,4),"km")
print("factors: ", round(factor_1),round(factor_2),"and desired delta_v: ", round(desired_delta_v/1000,8),"km/s")
print("c) ")
print("")
print("PHASE 3")
print("a) v_d_inf_r: ", round(v_d_inf_r/1000,4),"km/s and v_departure: ", np.round(v_departure/1000,4),"km/s")
print("b) desired final delta_v: ", round(delta_v_final/1000,4),"km/s")
print(" v_esc_earth: ", round(v_esc_earth/1000,4),"km/s | v_a_inf_r: ", round(v_a_inf_r/1000,4),"km/s")
print(" v_perigee: ", round(v_perigee/1000,4),"km/s | v_desired_earth: ", round(v_desired_earth/1000,4),"km/s")
print("c) total delta v", round(delta_v_total/1000,4), "km/s and mass used: ",round(m_used/1000,4),"tones")
print("initial mass:",mi,"and difference:",mi-mf)




#sol,_,_ = ces.solve(omega**2,2*r_earth*omega**2,-(v_d_inf**2),(r_earth**2)*(omega**2)-2*mu_earth)
