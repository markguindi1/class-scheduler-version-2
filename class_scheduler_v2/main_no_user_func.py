# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 15:17:35 2017

@author: Mark
"""

from class_scheduler_v2_func import class_scheduler_v2


"""
Indices for sorting schedules. Create list of tuples with index and increasing (1) 
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


def no_user_main():
    
    # infile name with all courses information
    courses_filename = "spring_18_all_courses.txt"
    # outfile name with schedules
    schedules_filename = "schedules_171029.txt"
    
    # mandatory and optional lists; do not worry about coreqs, they are taken care of later
    mandatory = ['CS 2204 LEC', 'MG 2304 LEC', 'CS 2413 LEC', 'CS 3913 LEC']
    optional = ['CS 2214-A LEC', 'CS 2214-B LEC'] # 'CS 4613 LEC', 
    
    # min number of credits to be taken. Some scheules may exceed this number slightly
    min_credits = 18
    
    #list of tuples in how to sort schedules, as shown in example above
    priority_lst = [(8, 1), (7, 1), (6, 1)]
    
    # Calls the "grand" scheduler function, passes all parameters
    class_scheduler_v2(courses_filename, schedules_filename, mandatory, optional, \
    min_credits, priority_lst)   
        
    print("\n" + "Done with no errors")
    
no_user_main()