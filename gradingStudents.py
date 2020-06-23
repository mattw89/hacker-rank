#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 17:55:22 2018

@author: matt
"""

def gradingStudents(grades):
    final = []
    for student in grades:
        if student >= 38 and student < 40:
            final.append(40)
        elif student > 40:
            if student % 10 < 5 and student % 10 >= 3:
                final.append(student + (5 - student % 10))
            elif student % 10 > 7:
                final.append(student + (10 - student % 10))
            else:
                final.append(student)
        else:
                final.append(student)
    return final



grades = [73, 67, 38, 33]
grades = [23, 99, 49, 1]
print(gradingStudents(grades))
            