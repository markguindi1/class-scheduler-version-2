# class_scheduler

This program's function is to generate all possible non-conflicting schedules of courses. The program consists of multiple Python files. This version of the program implements many of the functionalities which version 1 did not implement. Some of the features are:

* Given multiple courses and the number of credits being taken, the program will generate all possible schedules composed of all combinations of all of the courses, even if all of the courses given will add up to greater than the number of credits being taken. 
* Courses can be specified to be mandatory (so they will be included in every schedule), and optional.
* Co-requisite courses can be specified, so if a course is part of a schedule, its co-requisites will be added as well (provided they stay within the credits taken). 
* "Exclude" courses can be specified, so if a course is part of a schedule, its excluded courses will NOT be part of the same schedule.
* Users can sort schedules based on attributes of the schedules(descending or acsending). Many attributes can be used for sorting, which will recursively be used to sort ties. These attributes are:
	1. Earliest Start
	2. Earliest End
	3. Latest Start
	4. Latest End
	5. Average Start
	6. Average End
	7. Average Duration
	8. Priority Score (A priority for each course can be provided by the user in the input file. The more 		desirable a course is, the lower priority it should have (e.g. the most desirable course should have a 		priority of 0 or 1)
* The format of the output is quite informative, providing a full list of mandatory & optional courses, the attributes which were used for sorting, and the schedules. Each schedule is presented in a clear manner, clearly outlining the weekly schedule in an easy-to-see format, and the schedules attributes are also readily seen.

The program can be invoked in two methods:
`main_user_func.py` : a command-line interface which accepts user input
`main_no_user_func.py` : a Python file in which the user can enter the relevant information using Python code, and run the program from there. 

Exact instructions on how to create the input file can be found in the `input-instructions.txt` file. 

Explanation of files:

* `Course_class.py` : contains the definition of the `Course` class, which is the class which holds information about each course and its sections
* `MeetingTime_class.py` : contains the definition of the `MeetingTime` class, which is essentially a class which holds the day of the week and a time range (to represent a weekly meeting time)
* `Schedule_class.py` : contains the definition of the `MeetingTime` class, which represents a schedule. An instance of this class contains a list of courses that make up a VALID schedule (meaning, only after schedules have been generated and validated are they wrapped in the `Schedule` class). This class also calculates and stores the above attributes of its schedule.
* `main_user_func.py` : the function for accepting user input from the command line (one of the "entry points" of the application)
* `main_no_user_func.py` : the file where the user can enter the relevant information into a Python file, in Python constructs (another "entry point" of the application)
* `class_scheduler_v2_func.py` : the "grand" file, which makes the calls to all the other processes of the application (creating Courses, calculating schedules, sorting, output, etc.)
* `courses_from_file_func.py` : parses the input file, and generated `Course` objects
* `course_combinations_func.py` : generates ALL course combinations that satisfy the credits taken
* `all_schedule_lists_lst_func.py` : generates schedules with non-conflicting times
* `create_Schedule_objects_func.py` : wraps schedules into multiple `Schedule` objects
* `sorting_func.py` : sorts `Schedule` objects by attributes provided by user
* `print_Schedules_to_file_func.py` : outputs schedules to file in fully sorted order

The following files are Data structures used in the program, implemented in my Data Structures and Algorithms course:
* `heap.py` : implements a heap/priority queue
* `my_queue.py` : implements a queue

* `development.py` : an empty Python file I would use just to test small snippets of code











