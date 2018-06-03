# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 19:07:50 2017

@author: Mark
"""

#from development import *

from courses_from_file_func import courses_from_file
from course_combinations_func import course_combinations
from all_schedule_lists_lst_func import all_schedules_list
from create_Schedule_objects_func import create_Schedule_objects
from sorting_func import sort_by_list_of_priorities
from print_Schedules_to_file_func import print_schedules_to_file


def class_scheduler_v2(courses_filename, output_filename, mandatory, optional, \
    min_credits, priority_lst):
    # courses_filename = filename str of courses info
    # output_filename = filename of output file with schedules,
    # mandatory = list of strings of mandatory course names, optional = optional course names,
    # min_credits = minimum num of credits, schedules may exceed this number slightly
    # priority_lst = list of tuples or priorities to sort schedules by; (sort_by, inc or_dec)
    # sort_by is the attribute to sort schedules by (priority, avg start, etc)
    # inc_or_dec is whether to sort by attribute in increasing\decreasing order (1/-1)
        
    # get course info from file, create dict with Course objects
    course_dict = courses_from_file(courses_filename)
    

    #create list with lists of course combinations (no sections/schedules yet)
    course_combinations_list = course_combinations(min_credits, course_dict, optional, mandatory)
        
    #create list with lists of POSSIBLE course/section combinations (schedules)
    schedules_list = all_schedules_list(course_dict, course_combinations_list)
        
    #from schedule lists create Schedule objects
    sched_object_lst = create_Schedule_objects(course_dict, schedules_list)
    
    #sort Schedule objects by attributes picked by user
    sorted_scheds_lst = sort_by_list_of_priorities(sched_object_lst, priority_lst)
    
    #print sorted schedules to output file
    print_schedules_to_file(output_filename, sorted_scheds_lst, mandatory, optional, \
    min_credits, priority_lst)
    







    