# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 15:16:18 2017

@author: Mark
"""

from Schedule_class import Schedule
import heap

"""
Indices for sorting schedules. Create list of tuples with index and increasing(1) 
or decreasing (-1) order.


1. Earliest Start
2. Earliest End
3. Latest Start
4. Latest End
5. Average Start
6. Average End
7. Average Duration
8. Priority Score


Ex: [(8, 1), (7, 1), (5, -1)]
"""

# Priority functions. Accepts Schedule objet as parameter, returns attribute
# of Schedule, to be used as priority in sorting

def priority_earliest_start(sched):
    return sched.earliest_start()
def priority_earliest_end(sched):
    return sched.earliest_end()
def priority_latest_start(sched):
    return sched.latest_start()
def priority_latest_end(sched):
    return sched.latest_end()
def priority_avg_start(sched):
    return sched.avg_start()
def priority_avg_end(sched):
    return sched.avg_end()
def priority_avg_duration(sched):
    duration_in_mins = sched.avg_times.get_duration_minutes()
    return duration_in_mins
def priority_priority_score(sched):
    return sched.priority_score


# Creates dictionary of priority function objects. 
# Dictionary holds tuples, containing the string name of the priority/attribute,
# and the function object: (string, function). Keys of dictionary are integers 1 - 8

def create_priority_func_dict():
    priority_func_lst = [priority_earliest_start, priority_earliest_end, \
                        priority_latest_start, priority_latest_end, \
                        priority_avg_start, priority_avg_end, \
                        priority_avg_duration, priority_priority_score]    
    
    priority_str_lst = ["Earliest Start", "Earliest End", \
                        "Latest Start", "Latest End", \
                        "Average Start", "Average End", \
                        "Average Duration", "Priority Score"]
    
    priority_func_dict = {}
    for i in range(len(priority_func_lst)):
        priority_func_dict[i + 1] = (priority_str_lst[i], priority_func_lst[i])
    return priority_func_dict


# given list of Schedule objects and user-provided 
# list of priorities to sort by (prio_ref_lst), sorts in 
# order of priorities. Returns flattened out, fully sorted list of Schedules.
# Calls recursive helper function. This function is called by the main class scheduler func.

def sort_by_list_of_priorities(scheds_lst, prio_ref_lst):
    
    # Creates dictionary of priority functions, passed into recursive helper func.
    priority_dict = create_priority_func_dict()
    
    #ind of first priority in prio_ref_lst, passed into helper func.
    prio_ref_lst_ind = 0    
    
    # call to recursive helper func.
    fully_sorted_scheds_list = sort_by_list_of_priorities_helper(scheds_lst, \
    prio_ref_lst, prio_ref_lst_ind, priority_dict)
    
    return fully_sorted_scheds_list


# This function is recursive. priority_dict is a parameter so it doesn't create 
# new copy of dict for every recursive call

def sort_by_list_of_priorities_helper(scheds_lst, prio_ref_lst, prio_ref_lst_ind, priority_dict):
    #Base case. If no more priorites to sort by, returns itself without doing anything
    if prio_ref_lst_ind == len(prio_ref_lst):
        return scheds_lst
    
    #Recursive part of func. 
    else:
        
        priority_ind = prio_ref_lst[prio_ref_lst_ind][0] # index of priority func in priority_lst
        priority_func = priority_dict[priority_ind][1] # priority func obj, from tuple in prio_dict
        inc_or_dec = prio_ref_lst[prio_ref_lst_ind][1] # integer for increasing/decreasing order
        
        # sort Schedules by priority of priority func.
        all_sorted_scheds = sort_schedules(scheds_lst, priority_func, inc_or_dec) 
        # now that it is sorted but together, split into diff. lists by priority
        all_sorted_split_up = split_by_priority(all_sorted_scheds, priority_func)
        
        # for each list of same-priority-schedules in big list
        for i in range(len(all_sorted_split_up)):
            
            # assign single list of scheds of same priority
            small_sched_lst = all_sorted_split_up[i] 
            
            #sort this small single list of scheds recursively by next priority
            small_sched_sorted = sort_by_list_of_priorities_helper(small_sched_lst, prio_ref_lst, \
            prio_ref_lst_ind + 1, priority_dict)
            
            # in bigger list, replace unsorted-small-list by sorted-small-list
            all_sorted_split_up[i] = small_sched_sorted
        
        # after sorted, flatten up list, so no nested lists
        flattened_ret_lst = flat_list(all_sorted_split_up, 0, len(all_sorted_split_up) - 1)
        return flattened_ret_lst


# uses heap data structure to sort schedules by priority func
def sort_schedules(schedule_obj_lst, priority_func, inc1_or_dec_neg1):
    # create list of priority values for each Sched
    priority_lst = [priority_func(sched) for sched in schedule_obj_lst]
    # increasing/decreasing order
    for i in range(len(priority_lst)):
        priority_lst[i] *= inc1_or_dec_neg1
    # put all into heap, becomes sorted
    sort_heap = heap.ArrayMinHeap(priority_lst, schedule_obj_lst)
    # pop out only Schedule object (index [1]) into list, now sorted
    sorted_list = [sort_heap.delete_min()[1] for i in range(len(sort_heap))]
    return sorted_list

# Given list of sorted Schedules, splits up by same-priority-value into diff lists
# inside a bigger list

def split_by_priority(scheds_lst, priority_func):
    listed_by_priority = []
    same_priority_lst = []
    if len(scheds_lst) > 0:
        curr_priority = priority_func(scheds_lst[0])
        for sched in scheds_lst:
            if priority_func(sched) == curr_priority:
                same_priority_lst.append(sched)
            else:
                listed_by_priority.append(same_priority_lst)
                curr_priority = priority_func(sched)
                same_priority_lst = [sched]
    listed_by_priority.append(same_priority_lst)
    return listed_by_priority


# Recursively flattens nested lists.
def flat_list(nested_lst, low, high):
    ret_lst = []
    if low >= 0:
        if (low == high) and (not isinstance(nested_lst[low], list)):
            ret_lst.append(nested_lst[low])
        elif (low == high):
            ret_lst = flat_list(nested_lst[low], 0, len(nested_lst[low]) - 1)
        elif (not isinstance(nested_lst[low], list)):
            first = [nested_lst[low]]
            rest = flat_list(nested_lst, low + 1, high)
            ret_lst = first + rest
        else:
            first = flat_list(nested_lst, low, low)
            rest = flat_list(nested_lst, low + 1, high)
            ret_lst = first + rest
    return ret_lst



# Returns tuple of strings of how Schedules were sorted, by str name of attribute, & inc/dec
def sorted_by_str(priority_dict, ind, inc_or_dec):
    if inc_or_dec == 1:
        order = "increasing"
    else:
        order = "decreasing"
    sorted_by = priority_dict[ind][0]
    return (sorted_by, order)