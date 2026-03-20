import numpy as np
import pandas as pd

phase_a=np.linspace(0,23.61,30, False) #23,61m/s = 85km/h 
phase_s=np.linspace(23.61,25,15, False) #25m/s = 90km/h
phase_f=np.linspace(25,2.77,15, True) #2.77mS = 10 km/h
phases=phase_a,phase_s,phase_f

timestamp=np.linspace(0,60,60)

speeds=np.concatenate(phases)
noise=np.random.normal(0,0.5,60)
speeds_withnoise=speeds+noise

distances_a_s=np.random.uniform(18,21,45)
distances_f=np.linspace(distances_a_s[-1], 8, 15)
distances=np.concatenate((distances_a_s,distances_f))

acceleration=np.gradient(speeds,timestamp)

data={'timestamp_s':timestamp, 'speed_mps': speeds_withnoise, 'distance_m': distances, 'accel_mps2': acceleration}
dataframe=pd.DataFrame(data)
dataframe.to_csv('data/vehicle_log.csv', index=False)

