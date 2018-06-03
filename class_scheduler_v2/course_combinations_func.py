# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 14:57:00 2017

@author: Mark
"""

import my_queue
import copy

def course_combinations(min_credits, course_dict, optional_lst = [], mandatory_lst = []):
    # Given ~min number of credits to take, dict with Course objects, list of optional/elective
    # courses to take, and optional parameter of mandatory courses that must be taken.
    # Returns list containing lists of courses, each list representing different combination of
    # courses (mandatory courses are always listed first).

    
    comb_queue = my_queue.ArrayQueue()    #use queue to store temporary uncompleted combinations

    complete_course_combinations = [] #complete combinations
    
    #remove coreqs from lists, will be added again later for clarity
    remove_all_coreqs_from_list(course_dict, mandatory_lst) 
    remove_all_coreqs_from_list(course_dict, optional_lst)
    

    #first elem of each comb list stores # of credits so far
    mandatory_lst_to_ret = [0] 
    
    for course in mandatory_lst:
        add_course_and_coreqs_to_combination(course_dict, course, mandatory_lst_to_ret)
    mandatory_lst_to_ret.append(0) #first index of optional list/next class to add
    
    initial_comb = mandatory_lst_to_ret #create first base combination, with mandatory courses
    comb_queue.enqueue(initial_comb) #put base comb in queue
     
    
    # while loop looks at last course added to current comb, makes copies of curr comb,
    # looks at courses after last course in curr comb, annd adds each of those courses to
    # a copy of curr_comb. Then checks if copy meets credit req, if yes, done, if not, back in queue
    
    while not (comb_queue.is_empty()): #once queue is empty, all combinations with min_credits made
        
        curr_comb = comb_queue.dequeue() #current combination to add courses to
        
        if (curr_comb[0] >= min_credits): # curr_comb_copy fulfills min_credits requirement
            
                if satisfies_excluded(course_dict, curr_comb):
                    curr_comb.pop() #remove index of next course to add, no longer needed
                    complete_course_combinations.append(curr_comb) #add to completed combinations
                # does nothing with it if it doesn't satisfy excluded
        else:
            
            next_courses_start_ind = curr_comb.pop() # start index of new courses to add
            
            # for all courses to add...
            for course_ind in range(next_courses_start_ind, len(optional_lst)):
                course = optional_lst[course_ind] # current course to add
                curr_comb_copy = copy.deepcopy(curr_comb) #make copy of current combination
                add_course_and_coreqs_to_combination(course_dict, course, curr_comb_copy) # duh
                # start index of new courses to add next time around
                curr_comb_copy.append(course_ind + 1)

                comb_queue.enqueue(curr_comb_copy) #put back in queue
    
    
    # adds all coreqs to list again, in place
    add_all_coreqs_to_list(course_dict, mandatory_lst)
    add_all_coreqs_to_list(course_dict, optional_lst)
      
    return complete_course_combinations



# removes all coreqs from list, so they're not put into combinations twice

def remove_all_coreqs_from_list(course_dict, course_lst):
    course_ind = 0
    while course_ind < len(course_lst):
        remove_coreqs_from_list(course_dict, course_lst, course_ind)
        course_ind += 1
        
# removes coreqs of an individual course
def remove_coreqs_from_list(course_dict, course_lst, course_ind):
    course = course_lst[course_ind]
    course_coreqs = course_dict[course].coreqs
    
    coreq_ind = course_ind + 1 
    while coreq_ind < len(course_lst):
        course_to_check = course_lst[coreq_ind]
        if course_to_check in course_coreqs:
            del course_lst[coreq_ind]
        else:
            coreq_ind += 1

# adds course, coreqs, and credits to a combination
def add_course_and_coreqs_to_combination(course_dict, course, comb):
    comb.append(course)
    comb[0] += course_dict[course].no_credits()
    for coreq in course_dict[course].coreqs:
        if coreq not in comb:
            comb.append(coreq)
            comb[0] += course_dict[coreq].no_credits()
    

# if course_combination has courses that are supposed to be excluded, throw out
def satisfies_excluded(course_dict, courses_comb):
    for i in range(1, len(courses_comb) - 1):
        course = courses_comb[i] 
        for exclude in course_dict[course].exclude:
            if exclude in courses_comb:
                return False               
    return True   
  
  
# adds coreqs back to list in place, for clarity    

def add_all_coreqs_to_list(course_dict, course_lst):
    course_ind = 0   
    while course_ind < len(course_lst):
        # adds coreqs to list, returns index of next course to add coreqs of
        course_ind = add_coreqs_to_list(course_dict, course_lst, course_ind)

# adds individual course's coreqs
def add_coreqs_to_list(course_dict, course_lst, course_ind):
    course = course_lst[course_ind]
    course_coreqs = course_dict[course].coreqs
    
    coreq_ind = course_ind + 1
    
    for coreq in course_coreqs:
        course_lst.insert(coreq_ind, coreq)
        coreq_ind += 1
    return coreq_ind # this is now the index of the next course to add coreqs of
    
        