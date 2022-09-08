'''
This script requires the .pkl output-file after running the "PARE" script/demo.py. 
By default it should be found at "/output_folder/name_of_file/pare_results/" (name_of_file should be replaced by your input file/folder).
'''

#import packages
import numpy as np
import os
import glob
import matplotlib.pyplot as plt
import pandas as pd
import joblib
def unit_vector(vector):
    #returns the unit vector of the numpy vector
    return vector / np.linalg.norm(vector)
def angle_between(v1, v2):
    #returns the angle between to vectors in radians.
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

path_to_folder="~/PARE/output_folder/vid_0/pare_results/" #replace with your location of PARE output
lst=glob.glob(path_to_folder+"*.pkl")
angle_list=[]
for i in range(0,len(lst)):
    output_pare=joblib.load(lst[i])
    c7=output_pare['smpl_vertices'][0,1306] #location of vertetra c7
    l5=output_pare['smpl_vertices'][0,3021] #location of vertetra l5
    rm=output_pare['smpl_vertices'][0,6728] #location of malleolus right
    lm=output_pare['smpl_vertices'][0,3327] #location of malleolus left
    leg1=np.array(l5-rm).flatten() #returns a vector that describes the right leg.
    leg2=np.array(l5-lm).flatten() #returns a vector that describes the left leg.
    back=np.array(c7-l5).flatten() #returns a vector that describes the back.

    angle_list.append((np.degrees(angle_between(leg1,back))+np.degrees(angle_between(leg2,back)))/2) #this line returns the mean of the angles between left and right malleolus.
    
angle_list=np.array(angle_list)
angle_list=angle_list.astype(int) #The result is returned as an integer. Further decimal places are clinically hardly meaningful.
