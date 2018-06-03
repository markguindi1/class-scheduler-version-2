# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 00:52:58 2017

@author: Mark
"""

import ast

from class_scheduler_v2_func import class_scheduler_v2
from courses_from_file_func import courses_from_file
from sorting_func import create_priority_func_dict



# function to interact with user, get all information from user through console
def get_user_input_main(): 
    
    #Get infile name with all courses information
    courses_filename = input("Please enter an input file name with courses information. " \
    "If it is a text file, be sure to add '.txt' to the end.\n\n")
    
    # Output file name for generation schedules
    schedules_filename = input("Please enter a file name to output all possible schedules. " \
    "If it is a text file, be sure to add '.txt' to the end.\n\n")
    
    # Used to print courses to console, so user has a sorted list of all courses
    course_dict = courses_from_file(courses_filename) 
    course_lst = [course for course in course_dict]
    course_lst.sort()
    print("\nThe following is a list of your courses: \n", course_lst, sep = "\n", end = "\n\n")
    
    # Prompt user to enter lists of mandatory/optional courses
    # User-friendly, making it easier if some are mandatory & all rest are optional, etc.
    
    print("Would you like to enter your mandatory courses first, or optional/electives " \
    "courses first?\n" 
    "Please enter the word 'mandatory' or 'optional' .\n")
    choice_first = input().lower()
    mandatory, optional = get_both_lists_user(course_lst, choice_first)
    
    # Minimum number of credits to be taken. Schedules may exceed this number slightly
    min_credits = int(input("Enter the minimum number of credits. Note that some schedules " \
    "may have credit counts that are slightly higher than the minimum: \n\n"))
    
    # Offers user different ways to sort schedules
    priority_lst = get_priority_lst_user()
    
    # Calls the "grand" scheduler function, passes all parameters
    class_scheduler_v2(courses_filename, schedules_filename, mandatory, optional, \
    min_credits, priority_lst)
    
    #Confirms there were no errors
    print("\n" + "Done with no errors")    





# Uses helper functions, gets mandatory and optional course lists from user
def get_both_lists_user(course_lst, choice_first):
    if choice_first == "mandatory":
        mandatory = get_first_lst_user(course_lst, "mandatory")
        
        if mandatory != course_lst:  #If courses can be added to optional, prompts user
            optional = get_second_lst_user(course_lst, "optional/electives", mandatory)
        else: #All courses are already mandatory, no use prompting user for optional list
            optional = []
    else:
        optional = get_first_lst_user(course_lst, "optional/electives")
        
        if optional != course_lst:  #If courses can be added to mandatory, prompts user
            mandatory  = get_second_lst_user(course_lst, "mandatory", optional)        
        else: #All courses are already optional, no use prompting user for mandatory list
            mandatory = []
        
        
    return mandatory, optional


def get_first_lst_user(course_lst, mand_or_opt):
    #mand_or_opt is string or mandatory or optional/electives, to format instructions
    
    #Careful instructions for inputing list of courses
    instruct1 = "Please enter a list of courses that are {}.".format(mand_or_opt)
    instruct2 = "Start the list with an open bracket '[' and end with a close bracket ']'"
    instruct3 = "Type course names surrounded by single or double quotes."
    instruct4 = "Separate each course name with a comma, except after the last course."
    instruct5 = "You do not have to worry about corequisites, as they will be added automatically."
    instruct6 = "Ex: ['AA 1111', 'BB 2222', 'CC 3333']"
    instruct7 = "If there are no {} courses, enter an empty set of brackets '[]' ".format(mand_or_opt)
    instruct8 = "If all the courses are {}, enter the word 'all' .".format(mand_or_opt)
    
    #print instructions
    print(instruct1, instruct2, instruct3, instruct4, instruct5, instruct6, \
    instruct7, instruct8, sep = "\n")
    
    #gets input, creates list based on input
    user_input = input()
    if user_input.lower() == "all": #first_lst is entire lits of courses
        first_lst = course_lst
    else: #eveluate input list
        first_lst = ast.literal_eval(user_input)
        
    return first_lst


def get_second_lst_user(course_lst, mand_or_opt, first_lst):
    #same insturctions as above, mand_or_opt is also str, first_lst is the first list user entered
    #this is in case user wants remaining courses in second_lst, so all courses in course list
    #unless they're already in first_lst
    
    instruct1 = "Please enter a list of courses that are {}.".format(mand_or_opt)
    instruct2 = "Follow the same exact rules as entering the optional course list above."
    instruct3 = "If there are no {} courses, enter an empty set of brackets '[]' ".format(mand_or_opt)
    instruct4 = "If all of your remaining courses are {}, enter the word 'all' .".format(mand_or_opt)
    
    print(instruct1, instruct2, instruct3, instruct4, sep = "\n")
    
    user_input = input()
    if user_input.lower() == "all": #adds all courses unless course already in first_lst
        second_lst = [course for course in course_lst if course not in first_lst]
    else:
        second_lst = ast.literal_eval(user_input)
    
    return second_lst


def get_priority_lst_user():
    #prompts user to input careful list of attributes to sort by, each layered one atop another    
    
    #dictionary containing tuples, containing string name of attribute, and get_attribute
    # function object,  (sort_str, sort_func). Keys to dictionary and ints 1 : len(dict)
    sort_by_dict = create_priority_func_dict()
    
    print("\nYou can sort your schedules by the following attributes: ")
    for i in range(1, len(sort_by_dict)+1):
        print(str(i) + ". " + sort_by_dict[i][0]) #prints str name of atribute
    
    #prints careful instructions for inputing list of tuples
    print("\n" + "You can also sort them by your chosen attribute, in increasing or decreasing order.")
    print(" The number 1 represents increasing order. -1 represents decreasing order.  \n")
    print("Please enter a list [] of tuples () with attribute number and "
    "increasing/decreasing number; everything, as above, separated by commas.")
    print("Ex. [(8, 1), (7, 1), (5, -1)] ")
    
    priority_lst = ast.literal_eval(input()) #evaluates
    
    return priority_lst


get_user_input_main()







