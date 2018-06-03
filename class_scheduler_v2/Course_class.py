# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 14:06:52 2017

@author: Mark
"""

from MeetingTime_class import MeetingTime

class Course:
    
    class Section:
        
        def __init__(self, section_number):
            self.section_number = section_number #string
            self.meeting_times = [] #list of MeetingTime objects
        
        def section_add_meeting_time(self, day, start_time, end_time): #Section method
            meeting_time = MeetingTime(day, start_time, end_time)
            self.meeting_times.append(meeting_time)
        
        def __iter__(self): #yields MeetingTime object, to be used primarily for str output
            for meeting_time in self.meeting_times:
                yield meeting_time
            
    def __init__(self, course_name):
        self.course_name = course_name #string
        
        name_lst = course_name.split()    
        # The second word of name is the #, last digit of # is noCredits
        if name_lst[-1].isdigit() or name_lst[-1].lower() == "lec":
            self.num_of_credits = int(name_lst[1][3]) #
        else: # second word of name is not #, and it is not LEC
            self.num_of_credits = 0
        
        self.sections_dict = {}     #Dictionary holding Section objects, section # are keys
        
        self.coreqs = [] # corequisite courses; courses that must be taken with self course
        
        self.exclude = [] # exclude courses; courses that cannot be taken with self course
        
        self.priority = 3
    
    def add_section(self, section_num_str): #Creates Section object, adds to sections dict
        if section_num_str not in self.sections_dict:
            self.sections_dict[section_num_str] = self.Section(section_num_str)
    
    def add_meeting_time(self, section_num, day, start_time, end_time): #Course method, sec. is param
        curr_section = self.sections_dict[section_num]
        curr_section.section_add_meeting_time(day, start_time, end_time)
        
    def __str__(self): #returns string of course name
        return self.course_name
        
    def __repr__(self):
        return str(self)
        
    def sections_list(self): #returns sorted list of strings of sections nums
        sections_lst = [section for section in self.sections_dict]
        sections_lst.sort()
        return sections_lst
    
    def no_credits(self): #returns num of credits
        return self.num_of_credits
    
    def __iter__(self): #yields Section object (for checking attributes)
        for section_num in self.sections_list():
            yield self.sections_dict[section_num]
    
    def __getitem__(self, section_num): #returns Section object
        if section_num not in self.sections_dict:
            self.add_section(section_num)
        return self.sections_dict[section_num]