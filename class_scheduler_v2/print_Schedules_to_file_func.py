# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 15:20:36 2017

@author: Mark
"""

from sorting_func import create_priority_func_dict, sorted_by_str

def print_schedules_to_file(outfile_name, sorted_schedules_list, mandatory_lst, \
optional_lst, min_credits, priority_lst):
    
    no_schedules = len(sorted_schedules_list) #number of schedules, for printing purposes
    
    outfile = open(outfile_name, "w")   #portal to output file, passed into funcs as param
    
    print_heading_to_file(outfile, no_schedules) #print heading, blah blah blah
    
    print_sorted_by_to_file(outfile, priority_lst) #print how schedules were sorted
    print("", file = outfile) #empty line
    
    # prints mandatory, optional course lists, credits, etc.
    print_courses_info_to_file(outfile, mandatory_lst, optional_lst, min_credits) 
    print("", file = outfile)
    
    # prints "rules" about the output file, how to understand it, etc.
    print_clarification_to_file(outfile)
    
    print("-" * 70, "\n", file = outfile) # prints breakup line
    
    print_all_schedules_to_file(outfile, sorted_schedules_list) #prints schedules (FINALLY!!)
    
    print(no_schedules, "Possible Schedules \n", file = outfile) #prints total no schedules at end
    
    outfile.close()



def print_heading_to_file(outfile_var, no_schedules):
    print("Spring 2018 Schedules \n", file = outfile_var)
    print(no_schedules, "Possible Schedules \n", file = outfile_var)
    

def print_sorted_by_to_file(outfile_var, priority_lst):
    if len(priority_lst) > 0:
        print("Sorted by the following criteria, in listed order: \n", file = outfile_var)   
        priority_dict = create_priority_func_dict()
        
        # description strings of how schedules were sorted, "Average End Time", "increasing", etc.
        sorted_by_strings = [sorted_by_str(priority_dict, sort_by_ind, inc_or_dec) \
        for sort_by_ind, inc_or_dec in priority_lst]
        
        # print sorted by, first attribute
        first_sorted_by = "Sorted by {} in {} order.".format(sorted_by_strings[0][0], \
                                                             sorted_by_strings[0][1])
        print(first_sorted_by, file = outfile_var)
        
        # print "then by" second, third, etc. attributes
        for i in range(1, len(sorted_by_strings)):
            curr_sorted_by = "Then by {} in {} order. ".format(sorted_by_strings[i][0], \
                                                               sorted_by_strings[i][1])
            print(curr_sorted_by, file = outfile_var)


def print_courses_info_to_file(outfile_var, mandatory_lst, optional_lst, min_credits):
    print("Mandatory Courses: [", end = "", file = outfile_var)
    
    # no more than 4 courses on a line
    for i in range(len(mandatory_lst)):
        print(mandatory_lst[i], sep = "", end = "", file = outfile_var)
        if (i < len(mandatory_lst) - 1):
            print(", ", end = "", file = outfile_var)
        if ((i + 1) % 4 == 0):
            print(file = outfile_var)
    print("]\n", file = outfile_var)
    
    
    print("Optional/Elective Courses: [", end = "", file = outfile_var)
    
     # no more than 4 courses on a line
    for i in range(len(optional_lst)):
        print(optional_lst[i], sep = "", end = "", file = outfile_var)
        if (i < len(optional_lst) - 1):
            print(", ", end = "", file = outfile_var)
        if ((i + 1) % 4 == 0):
            print(file = outfile_var)
    print("]\n", file = outfile_var)    

    print("Minimum Number of Credits: ", min_credits, file = outfile_var)

#how to understand & interpret file
def print_clarification_to_file(outfile_var):
    clarification_str_1 = "Each schedule contains all mandatory courses. \n"
    clarification_str_2 = "Not all schedules contain each optional/elective course. \n"
    clarification_str_3 = "Course lists also contain course corequisites. \n"
    clarification_str_4 = "Schedules may meet or exceed minimum number of credits. \n"
    
    print(clarification_str_1, clarification_str_2, clarification_str_3, \
    clarification_str_4, sep = "", file = outfile_var)


# given list of Schedule objects, prints each to file
def print_all_schedules_to_file(outfile_var, schedules_lst):
    counter = 0 #counts schedule numbers
    for schedule in schedules_lst:
        print_single_schedule_to_file(outfile_var, schedule, counter + 1) #print single sched
        print("-" * 70 + "\n", file = outfile_var) #break line
        counter += 1

#print single schedule to file
def print_single_schedule_to_file(outfile_var, schedule, number):
    # attributes
    earliest_start = schedule.earliest_start_str()
    earliest_end = schedule.earliest_end_str()
    latest_start = schedule.latest_start_str()
    latest_end = schedule.latest_end_str()        
    avg_start = schedule.avg_start_str()
    avg_end = schedule.avg_end_str()
    avg_duration = schedule.avg_duration_str()
    no_credits = schedule.no_credits()
    priority_score = str(schedule.priority_score)
    
    #print attributes in equally spaced columns
    print("Schedule #", number, "\n", file = outfile_var)
    
    print("[", end = "", file = outfile_var)
    
     # no more than 4 courses on a line
    for i in range(len(schedule.schedule_list)):
        print(schedule.schedule_list[i], sep = "", end = "", file = outfile_var)
        if (i < len(schedule.schedule_list) - 1):
            print(", ", end = "", file = outfile_var)
        if ((i + 1) % 4 == 0):
            print(file = outfile_var)
    print("]\n", file = outfile_var)    
    
    
    print("\t" + "Earliest Start:" + " " * (20-len("Earliest Start:"))  + earliest_start \
            + "\t\t" + "Earliest End:" + " " * (17-len("Earliest End:")) + earliest_end,\
            file = outfile_var)
            
    print("\t" + "Latest Start:" + " " * (20-len("Latest Start:")) + latest_start \
            + "\t\t" + "Latest End:" + " " * (17-len("Latest End:")) + latest_end, \
            file = outfile_var)
            
    print("\t" + "Average Start:" + " " * (20-len("Average Start:")) + avg_start \
            + "\t\t" + "Average End:" + " " * (17-len("Average End:")) + avg_end, \
            file = outfile_var)
            
    print("\t" + "Average Duration:" + " " * (20-len("Average Duration:")) + avg_duration \
            + "\t\t" + "Credits:" + " " * (17-len("Credits:")) + str(no_credits), \
            file = outfile_var)
            
    print("\t" + "Priority Score:" + " " * (20-len("Priority Score:")) + priority_score, \
            file = outfile_var)
            
    print("\n\n", file = outfile_var)
    
    #print times for each day of week
    for day_str in schedule.iter_days_of_week_str():
        print("\t\t\t\t", day_str, file = outfile_var)
    
    print("", file = outfile_var) #empty line






