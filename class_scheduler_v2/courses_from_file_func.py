# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 14:15:22 2017

@author: Mark
"""

from Course_class import Course


def courses_from_file(in_file): #given an input file, returns dictionary with course objects
    
    file = open(in_file, "r")
    lines_lst = file.readlines()
    
    
    course_dict = {} # Dictionary keeps all the Course objects, and are accessed through string keys
    
    curr_course_str = "" # Str key to access Course object from course_dict
    curr_section_str = ""    # Str key to access Section object from course_dict[curr_course]
    
    for curr_line in lines_lst: #for each line in file, create course, section, or meeting time
    
        curr_line_lst = curr_line.split() #splits words into list of strings
        
        if len(curr_line_lst) == 0: #empty line
            pass
        
        elif curr_line_lst[0].lower() == "course": #new course
            curr_course_str = " ".join(curr_line_lst[1:]) # excludes the word Course
            course_dict[curr_course_str] = Course(curr_course_str)
        
        elif curr_line_lst[0].lower() == "credits":
            course_dict[curr_course_str].num_of_credits = int(curr_line_lst[1])
        
        elif curr_line_lst[0].lower() == "priority": #assigns priority rating to current course
            course_dict[curr_course_str].priority = int(curr_line_lst[1])
        
        # coreqs, condition done this way so no difference between "coreq" and "coreqs"
        elif ("coreq" in curr_line_lst[0].lower()):
            coreqs_str = " ".join(curr_line_lst[1:]) #str without "coreq"
            coreqs_lst = coreqs_str.split(",") #split by commas
            for i in range(len(coreqs_lst)):
                coreqs_lst[i] = coreqs_lst[i].strip() #strip of whitespace
            course_dict[curr_course_str].coreqs = coreqs_lst
            
       #courses that cannot be taken together with current course
        elif curr_line_lst[0].lower() == "exclude":
            exclude_str = " ".join(curr_line_lst[1:]) #str without "exclude"
            exclude_lst = exclude_str.split(",") #split by commas
            for i in range(len(exclude_lst)):
                exclude_lst[i] = exclude_lst[i].strip() #strip of whitespace
            course_dict[curr_course_str].exclude = exclude_lst
        
        elif curr_line_lst[0].lower() == "section": #new section
            curr_section_str = " ".join(curr_line_lst[1:]) # excludes the word Section
            course_dict[curr_course_str].add_section(curr_section_str) #add section to current course
            
        else:  #new meeting time
            start_time = int(curr_line_lst[-2]) #MUST BE INT
            end_time = int(curr_line_lst[-1]) #MUST BE INT
            
            # Loop goes through only beginning of list (days of week),
            # stops before start and end times, which are last 2 elems of list
            for elem in curr_line_lst[:-2]: 
                day_of_week = elem
                course_dict[curr_course_str].add_meeting_time(curr_section_str, \
                day_of_week, start_time, end_time) #add meeting times to current section
    
    file.close()
        
    return course_dict #dict holds Course objects, keys are course name strings