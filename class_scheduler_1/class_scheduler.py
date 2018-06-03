# -*- coding: utf-8 -*-
"""
Created on Fri May  5 01:05:52 2017

@author: Mark
"""

#NEEDS POLISHING UP AND DOCUMENTATION!!!!


import my_queue
import copy

class Course:
    
    class Section:
                        
        def __init__(self, section_num):
            self.section_num = section_num
            self.meeting_times = []
            
        def add_meeting_time(self, day_of_week, start_time, end_time):
            meeting_time_tup = (day_of_week, start_time, end_time)
            self.meeting_times.append(meeting_time_tup)
        
        def meeting_times_list(self):
            return self.meeting_times
        
        def __iter__(self):
            for meeting_time in self.meeting_times:
                yield meeting_time
        
        
    def __init__(self, class_num_str, title = None):
        self.class_num = class_num_str
        self.title = title
        self.sections = {} #Map of section num to Section object
    
    def course_number(self):
        return self.class_num
        
    def add_section(self, section_num_str):
        section = self.Section(section_num_str)
        self.sections[section_num_str] = section
        
    def sections_list(self):
        sections_lst = [section_num for section_num in self.sections]
        return sections_lst
    
    def __iter__(self):
        for section_num in self.sections:
            yield section_num
    
    def __getitem__(self, section):
        if section not in self.sections:
            self.add_section(section)
        return self.sections[section]



def generate_courses_from_file(file_name):
    curr_course = None
    curr_section = None
    course_dict = {}
    file = open(file_name, "r")
    for line in file:
        line_lst = line.split()
        if (len(line_lst) == 0):
            if curr_course is not None:
                course_dict[curr_course.course_number()] = curr_course
            else:
                pass
        elif (line_lst[0] == "Course"):
            if curr_course is not None:
                course_dict[curr_course.course_number()] = curr_course
            curr_course = Course(line_lst[1] + " " + line_lst[2])
        elif (line_lst[0] == "Section"):
            curr_section = line_lst[1]
            curr_course.add_section(curr_section)
        else:
            day = line_lst[0]
            start = line_lst[1]
            end = line_lst[2]
            curr_course[curr_section].add_meeting_time(day, int(start), int(end))
    file.close()
    course_lst = [key for key in course_dict]
    return course_dict, course_lst
        

def generate_schedules_list_do_not_conflict(course_dict, course_lst):
    checked_courses_queue = my_queue.ArrayQueue()
    first_course = course_lst[0]
    
    for section in course_dict[first_course]:
        checked_courses_queue.enqueue( [ (first_course, section) ] )
        
    for i in range(1, len(course_lst)): #For each course to add...
        curr_course = course_lst[i]
        for j in range(len(checked_courses_queue)): #For each created schedule...
            curr_perm = checked_courses_queue.dequeue()
            for section in course_dict[curr_course]: #For each section in the course to add...
                curr_section_tup = (curr_course, section)
                does_not_conflict_with_anything = True
                for checked_course in curr_perm: #Check if section fits into schedule...
                    if sections_do_not_conflict(course_dict, curr_section_tup, checked_course) is False:
                        does_not_conflict_with_anything = False
                if does_not_conflict_with_anything:
                    perm_to_put_back_in_queue = copy.deepcopy(curr_perm)
                    perm_to_put_back_in_queue.append(curr_section_tup)
                    checked_courses_queue.enqueue(perm_to_put_back_in_queue)
    
    schedules_lst = [checked_courses_queue.dequeue() for i in range(len(checked_courses_queue))]
    
    return schedules_lst


def sections_do_not_conflict(course_dict, course_sec_tup1, course_sec_tup2):
    course1 = course_sec_tup1[0]
    sec1 = course_sec_tup1[1]
    course2 = course_sec_tup2[0]
    sec2 = course_sec_tup2[1]
    
    do_not_conflict = True
    for meeting_time1 in course_dict[course1][sec1]:
        for meeting_time2 in course_dict[course2][sec2]:
            if (meeting_time1[0] == meeting_time2[0]) and (meeting_time1[1] <= meeting_time2[1] < meeting_time1[2]):
                do_not_conflict = False
            elif (meeting_time1[0] == meeting_time2[0]) and (meeting_time2[1] <= meeting_time1[1] < meeting_time2[2]):
                do_not_conflict = False
            else:
                pass
    return do_not_conflict


def print_combinations_to_file(schedules_list, output_file_name):
    output_file = open(output_file_name, "w")
    num_of_combinations = len(schedules_list)
    
    for schedule in schedules_list:
        print(schedule, end = "\n", file = output_file)
    print("Number of possible combinations:", num_of_combinations, file = output_file)
    print("Done")
    output_file.close()



my_course_dict, my_course_lst = generate_courses_from_file("fall17_001.txt")
schedules_queue = generate_schedules_list_do_not_conflict(my_course_dict, my_course_lst)
print_combinations_to_file(schedules_queue, "fall17scheds001.txt")


#my_course_dict, my_course_lst = generate_courses_from_file("test2.txt")
#schedules_lst = generate_schedules_list_do_not_conflict(my_course_dict, my_course_lst)
#print_combinations_to_file(schedules_lst, "combs2.txt")
    

    
    