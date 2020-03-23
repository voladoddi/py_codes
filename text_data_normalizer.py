#!/usr/bin/python
import argparse
import math
import sys
import re

class CourseDetail:
    # Initializer / Instance attributes
    def __init__(self, dept, course_number, year, semester):
        self.department = dept
        self.course_number = course_number
        self.year = year
        self.semester = semester
    
    def describe(self):
        pass    # {TODO: Add code to create a dictionary from class attributes}


def query_runner_trial_one(course_query):
    # Init classround)ct
    course_details = CourseDetail("","","","")

    # Split by whitespace - O(n) to extract tokentokens = [i.lower() for i in course_query.split()]
    # print (tokens)
    # NOTE: There is always a space between course-number and semester-year
    # So I should have at least 2 splits.
    # Find year if present first since processing rest is easier.
    # Since year / semester can be represented variably, identidying dept/course number seems to be easier
    # Dept is always followed b # If even number, then the space is in the middle. If not, floor(len/2)
    # These result in two groups, first one is going to be consistent of <department + course number>
    # second one is going to contain y course number, and course number is always followed by a space
    # Find dept and course, and identify the remaining string.
    '''for token in tokens:
        # 1 or more alphabetic characters + (optional) delimiter + 1 or more numeric characters
        # followed by a space.
        if 'cs' in token:
            dept = token.find('cs')
            print(dept)'''
        # At this point I realize there is no order as well as finite list of courses
        # The only way to do this is to use regex matches.
        # (1 or more alpha characters + delimiter + course number) -- group1
        # (1 or more alpha characters i.e. semester + 2 or 4 year number) -- group2
        # I only know course number comes first and there is a space between group1 and group2. 
        # These are the only invariants.
    
    encapsulated_words = re.findall(r'(?:\w)+', course_query)
    encapsulated_words = [i.lower() for i in encapsulated_words]
    if encapsulated_words:
        # If even number of matches, then the space is in the middle. If not, floor(len/2)
        # These result in two subgroups, first one is going to be consistent of <department + course number>
        #                                second one (onwards) is going to contain <year> and <semester> in any order
        print('Encapsulated words in query: {}'.format(encapsulated_words))
        num_words = len(encapsulated_words)
        subgroup_split_idx = int(math.floor(num_words)/2)
        
        print('Split index : {}'.format(subgroup_split_idx))
        
        # 1st subgroup : <department> and <course number>
        dept_course_group = encapsulated_words[:subgroup_split_idx]
        # 2nd subgroup : <year> and <semester>
        year_semester_group = encapsulated_words[subgroup_split_idx:]

        if len(dept_course_group)==1:
            dept = re.search(r"\w[a-z]",dept_course_group[0])
            course = dept_course_group[0][dept.span()[1]:]
            if not course:
                course = encapsulated_words[1]
                year_semester_group = encapsulated_words[2:]
            print ("Dept: {} Course: {}".format(dept.group(), course))
        else:
            dept = dept_course_group[0]
            course = dept_course_group[1]
            print ("Dept: {} Course: {}".format(dept, course))

        # To deal with a query that has : num_words is odd, there is a possibility that the middle word is either a course number / year
        # I make use of the fact that my second subgroup either starts from 2 or 1.
        # If I've used up [1] for course group, then start idx=2 for 2nd subgroup.
        for year in year_semester_group:
            year_formatter = re.search(r"(\d\d\d\d)|(\d\d)", year)
            # abbreviations | abbreviations with year | words 
            # [f|s|w|su] or [fall|spring|winter|summer]
            # [fYY] or [YYf] or [fYYYY] or [YYYYf])
            # [fall16] or [16fall] or [f2016] or [f16]
            semester_formatters = []
            if year_formatter:
                print('Length of Year : {}'.format(len(year_formatter.group())))
                print('Year : {}'.format(year_formatter.group()))




if __name__ == '__main__':
    query_list = [  "CS-111 f2016",
                    "CS-111 Fall 2016",
                    "CS 111 F2016",
                    "CS:111 2016 Fall", 
                    "CS 111 F 16",
                    "CS111 F16",
                    "CS111 F 16",
                    "CS111 16F",
                    "CS111 16 FALL",
                    "CS111 2016 FALL"
                    ]
    for q in query_list:
        query_runner_trial_one(q)