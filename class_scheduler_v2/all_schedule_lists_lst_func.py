# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 14:59:46 2017

@author: Mark
"""

import my_queue
import copy

def all_schedules_list(course_dict, course_combs_lst):
    # Given list containing lists of course combinations, uses helper functions 
    # to create schedule combinations for each combination of courses.
    # Returns list of lists of tuples (course, section)
    all_combinations_lst = []

    for comb_lst in course_combs_lst:
        flatten_out_list(comb_lst)
        #for a single course combination, a list of possible schedules is created, 
        # and each of those schedules is added to list of all schedules
        course_comb_schedule_combs = course_combination_schedules(course_dict, comb_lst)
        all_combinations_lst += course_comb_schedule_combs
    
    return all_combinations_lst #returns single list of all schedules
        

def flatten_out_list(lst): #flattens out list of tuples
    i = 0
    finished = False
    while not finished:
        elem = lst[i] #this is elem to be potentially expanded
        if isinstance(elem, tuple):
            lst[i] = elem[0] #first, replace tuple in list with 1st elem of tuple for efficiency
            for j in range(1, len(elem)):
                subelem = elem[j] #tup elems
                i += 1 #i is index of where to insert rest of tup elems
                lst.insert(i, subelem)
        i += 1 #increment i, to go to next element
        if i == len(lst):
            finished = True


def course_combination_schedules(course_dict, comb_lst):
    # Given a single combination of courses (that was already checked and verified that
    # those courses can be taken together), creates all possible schedules of those courses' sections.

    sched_queue = my_queue.ArrayQueue() #queue for storing incomplete schedules
    
    # Index of last elem (course) in combination list, to be passed into recursive function
    ind_of_last_class = len(comb_lst) - 1
    
    # Recursive function. For current course in list of courses (ind), adds course to all possible
    # schedule combinations of the courses that were before it (see the recursive definition??).
    # This recursive function has no return value, rather it just adds everything to the queue, 
    # until it has done all the courses.
    course_combination_helper(course_dict, comb_lst, ind_of_last_class, sched_queue)
    
    # Adds all the combinations in the queue to a list
    sched_lst = [sched_queue.dequeue() for i in range(len(sched_queue))]
    
    return sched_lst


def course_combination_helper(course_dict, comb_lst, ind, sched_queue):
    # Recursive function, takes course name at current index of combination list,
    # and adds all possible sections of course to the already-made schedules of 
    # courses that came before it (see the recursive definition??). 
    
    
    # Base case, need to initialize with schedules, for first course in comb_lst.
    # I do not need to check schedules here. Once it is found that any single 
    # course-section does not fit into any schedule, it will be discarded automatically
    if ind == 1: 
        curr_course_name = comb_lst[ind]
        sections_lst = course_dict[curr_course_name].sections_list() # list of section names strings
        for section_num in sections_lst:
            course_section_tup = (curr_course_name, section_num) # tuple of course and section
            sched_queue.enqueue([course_section_tup]) # enqueues tuple inside a list, to add
                                                      # other courses to that list
           
    else:
        #Recursive call, before anything, goes to base case, then goes to most recent/deepest call
        course_combination_helper(course_dict, comb_lst, ind - 1, sched_queue)
        curr_course_name = comb_lst[ind]
        sections_lst = course_dict[curr_course_name].sections_list()
        
        for i in range(len(sched_queue)): # For each tentative schedule in the queue...
            curr_sched_lst = sched_queue.dequeue() #current schedule
            
            for section_num in sections_lst: 
            # For each section of current course, see if fits in
            # current schedule, if it does, make copy of schedule and put back in queue
                course_section_tup = (curr_course_name, section_num) #tuple of current course-section
                fits_in_sched = fits_into_schedule(course_dict, curr_sched_lst, course_section_tup)
                # helper function which checks if course-section fits into current schedule
                if fits_in_sched:
                    new_sched = copy.deepcopy(curr_sched_lst) # create copy of current schedule
                    new_sched.append(course_section_tup) # add current course-section tuple to sched
                    sched_queue.enqueue(new_sched) #put back in queue to add rest of courses
                

def fits_into_schedule(course_dict, sched_lst, course_section_tup):
    # takes course_dictionary, single schedule in the form of a list, and 
    # a course-section tuple. Checks if course-section fits in schedule, returns bool    
    
    for checked_tup in sched_lst: 
    #checked_tup is tuple of c/s (course-section) already checked and in schedule
    #for each class already in schedule, check if fits with class to add
        checked_and_new_fit = two_classes_fit_together(course_dict, checked_tup, course_section_tup)
        if not checked_and_new_fit: 
        # once it's discovered that c/s to add doesn't fit with any one of the checked c/s 's,
            return False # you return False, it cannot fit into schedule
    return True # reaches this if False was not returned -- so fits into shedule
            

def two_classes_fit_together(course_dict, class1_tup, class2_tup): 
    # takes course dictionary, 2 tuples of course-section    
    
    class1_name, class1_section = class1_tup[0], class1_tup[1] #class1 name and section
    class2_name, class2_section = class2_tup[0], class2_tup[1] #class2 name and section
    
    class1section_obj = course_dict[class1_name][class1_section] # course-section object
    class2section_obj = course_dict[class2_name][class2_section] # course-section object
       
    for time1 in class1section_obj: # for MeetingTime in c-s 1
        for time2 in class2section_obj: #for MeetingTime in c-s 2
            times_fit = meeting_times_fit(time1, time2) # check if two meeting times fit
            if not times_fit: # if any two meeting times don't fit
                return False # the two c-s do not fit
    return True # reaches this if False was not returned -- so two c-s fit together
    

def meeting_times_fit(time1, time2):
    if time1.day == time2.day: # only compare times of two days if the same day
        if time1.start_time <= time2.start_time < time1.end_time: 
            return False # MeetingTime 2 starts in middle of 1, conflict!!
        elif time2.start_time <= time1.start_time < time2.end_time: 
            return False # MeetingTime 1 starts in middle of 2, conflict!!
        else:
            return True # Even though they're the same day, they fit together, so return True
    else: #if not same day, times do not conflict whatsoever
        return True



