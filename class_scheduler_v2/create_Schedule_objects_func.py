# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 15:13:45 2017

@author: Mark
"""

from Schedule_class import Schedule

def create_Schedule_objects(course_dict, schedules_list):
    # Initialize empty list to store Schedule objects
    schedule_object_list = [None for i in range(len(schedules_list))]
    
    for i in range(len(schedules_list)): #for each schedule list
        schedule = schedules_list[i]
        schedule_object = Schedule(course_dict, schedule) # Schedule object
        schedule_object_list[i] = schedule_object # put Schedule object into list
        
    return schedule_object_list #return list of Schedule objects