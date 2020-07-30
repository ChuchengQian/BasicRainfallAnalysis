#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 20:47:34 2017

@author: chuchengqian
"""


import os
c = os.getcwd()
def lines(filename):
    m = os.path.join(c, 'files', filename)
    file = open(m, "r")
    first_line = file.readline()
    rest_lines = file.readlines()
    file.close()
    sequence = []
    for line in rest_lines:
        new_line = line.split(',')
        if len(new_line[5]) != 0:
            sequence.append(new_line)
    return sequence
        
def months(m,sequence):
    index = 0
    total_rain = 0
    month = []
    while index < len(sequence) - 1:
        new1 = sequence[index]
        new2 = sequence[index + 1]
        if int(new1[2]) == int(new2[2]):
            if int(new1[3]) == m:
                total_rain = total_rain + float(new1[5])
        else:
            if new1[3] == 12 and m==12:
                total_rain = total_rain + float(new1[5])
                month.append(round(total_rain,2))
            month.append(round(total_rain,2))
            total_rain = 0
        index = index + 1
        if index == len(sequence) - 2:
            lastline = sequence[-1]
            if int(lastline[3]) == m:
                total_rain = total_rain + float(lastline[5])
            month.append(round(total_rain,2))
    if int(sequence[-1][3]) == m:
        month[-1] = month[-1] + float(sequence[-1][5])
    return month

def days(sequence):
    day=[]
    for line in sequence:
        day.append(float(line[5]))
    return day

def years(sequence):
    year=[]
    b=0
    total_rain=0.0
    for line in sequence:
        if b == 0 :
            b = line[2]
        if line[2]== b:
            total_rain = total_rain + float(line[5])
        elif line == sequence[-1]:
            year.append(round(total_rain,2))
        else:
            year.append(round(total_rain,2))
            total_rain=0.0
            b= line[2]
    return year

def method_a_max(F,sequence):
    copy_of_sequence=sequence[:]
    copy_of_sequence.sort()
    data_above_xf=[]
    index=-2
    while index >= -len(sequence):
        xi = copy_of_sequence[index]
        index_of_xj = index + 1
        count = 0
        while index_of_xj<= -1:
            xj=copy_of_sequence[index_of_xj]
            J=sequence.index(xj)
            I=sequence.index(xi)
            if abs(J-I)>= F:
                count=count+1
            index_of_xj=index_of_xj+1
        if count != 0:
            if count == -(index+1):
                data_above_xf.append(copy_of_sequence[index])
            if count != -(index+1):
                data_above_xf.append(copy_of_sequence[-1])
                data_above_xf.sort()
                return data_above_xf
            index=index-1
        else:
            copy_of_sequence.pop()            
def method_a_min(F,sequence):
    copy_of_sequence=sequence[:]
    copy_of_sequence.sort()
    data_below_xf=[]
    index=1
    while index <= len(sequence)-1:
        xi = copy_of_sequence[index]
        index_of_xj = index - 1
        count = 0
        while index_of_xj >= 0:
            xj=copy_of_sequence[index_of_xj]
            J=sequence.index(xj)
            I=sequence.index(xi)
            if abs(I-J)>= F:
                count=count+1
            index_of_xj=index_of_xj-1
        if count != 0:
            if count == index:
                data_below_xf.append(copy_of_sequence[index])
            if count != index:
                data_below_xf.append(copy_of_sequence[0])
                data_below_xf.sort()
                return data_below_xf 
            index=index+1
        else:
            copy_of_sequence.pop(0)

def method_b(F, data):
    new_data_list = data[:]
    new_data_list.sort()
    higest_th = int(len(data)/F)
    no_replicate_data = []
    index = 0
    while index < len(new_data_list)-1:
        x1 = new_data_list[index]
        x2 = new_data_list[index+1]
        if x1 != x2:
            no_replicate_data.append(x1)
        index = index + 1
    if new_data_list[-2] != new_data_list[-1]:
        no_replicate_data.append(new_data_list[-2])
        no_replicate_data.append(new_data_list[-1])
    else:
        no_replicate_data.append(new_data_list[-1])
    return no_replicate_data[- higest_th], no_replicate_data[higest_th-1]

def above_F_value(value_F, data):
    above_F_values = []
    for value_th in data:
        if value_th >= value_F:
            above_F_values.append(value_th)
    return above_F_values 

def below_F_value(value_F, data):
    below_F_values = []
    for value_th in data:
        if value_th <= value_F:
            below_F_values.append(value_th)
    return below_F_values

def month_F(data_relate_to_xf, month, m, sequence):
    Data_relate_to_xf=data_relate_to_xf[:]
    Data_relate_to_xf.sort()
    match_year_month = []
    for n in Data_relate_to_xf:
        index = 0
        total_rain = 0
        while index < len(sequence) - 1:
            new1 = sequence[index]
            new2 = sequence[index + 1]
            if int(new1[2]) == int(new2[2]):
                if int(new1[3]) == m:
                    total_rain = total_rain + float(new1[5])
            else:
                if new1[3] == 12 and m == 12:
                    total_rain = total_rain + float(new1[5])
                    if round(total_rain,2) == n:
                        year = new1[2]
                        match_year_month.append((int(year),m)) 
                if round(total_rain,2) == n:
                    year = new1[2]
                    match_year_month.append((int(year),m))
                total_rain = 0
            index = index + 1
            if index == len(sequence) - 2:
                lastline = sequence[-1]
                if int(lastline[3]) == m:
                    total_rain = total_rain + float(lastline[5])
                    if round(total_rain) == n:
                        year = lastline[2]
                        match_year_month.append((int(year), m))
        if n == month[-1]:
            if m <= int(sequence[-1][3]):
                match_year_month.append((int(sequence[-1][2]), m))
            else:
                match_year_month.append(int(sequence[-1][2])-1, m)
    return match_year_month

def day_F(data_relate_to_xf, days, sequence):
    data_list = []
    for line in sequence:
        list_element = line[2:5]
        data_list.append(list_element)
    Data_relate_to_xf=data_relate_to_xf[:]
    Data_relate_to_xf.sort()
    match_day = []
    for n in Data_relate_to_xf:
        day_th = days.index(n)
        day = data_list[day_th]
        match_day.append(day)
    return match_day    

def year_F(data_relate_to_xf, years, sequence):
    Data_relate_to_xf=data_relate_to_xf[:]
    Data_relate_to_xf.sort()
    match_year = []
    for n in Data_relate_to_xf:
        year_th = years.index(n)
        frist_line = sequence[0]
        year = int(frist_line[2]) + year_th
        match_year.append(year)
    return match_year
       
def threshold_month(filename, m, F):
    sequence = lines(filename)
    month = months(m, sequence)
    max_xf_for_methodA=(method_a_max(F, month))[0]
    min_xf_for_methodA=(method_a_min(F, month))[-1]
    Data_above_max_xfA = method_a_max(F, month)
    Data_below_min_xfA = method_a_min(F, month)
    month_match_data_above_xfA = month_F(Data_above_max_xfA, month, m, sequence)
    month_match_data_below_xfA = month_F(Data_below_min_xfA, month, m, sequence)
    max_xf_for_methodB=(method_b(F, month))[0]
    min_xf_for_methodB=(method_a_min(F, month))[-1]
    Data_above_max_xfB = above_F_value(max_xf_for_methodB, month)
    Data_below_min_xfB = below_F_value(min_xf_for_methodB, month)
    month_match_data_above_xfB = month_F(Data_above_max_xfB, month, m, sequence)
    month_match_data_below_xfB = month_F(Data_below_min_xfB, month, m, sequence)
    print("For Method A: Threshold value for exceptionally high values is", max_xf_for_methodA, ", the months at which the data equals or exceeds it: ", month_match_data_above_xfA)
    print("For Method A: Threshold value for exceptionally low values is", min_xf_for_methodA, ", the months at which the data equals or is smaller than it: ", month_match_data_below_xfA)
    print("For Method B: Threshold value for exceptionally high values is", max_xf_for_methodB, ", the months at which the data equals or exceeds it: ", month_match_data_above_xfB)
    print("For Method B: Threshold value for exceptionally low values is", min_xf_for_methodB, ", the months at which the data equals or is smaller than it: ", month_match_data_below_xfB)
   

def threshold_days(filename, F):
    sequence = lines(filename)
    day = days(sequence)
    max_xf_for_methodA=(method_a_max(F, day))[0]
    Data_above_max_xfA = method_a_max(F, day)
    day_match_data_above_xfA = day_F(Data_above_max_xfA, day, sequence)
    max_xf_for_methodB=(method_b(F, day))[0]
    Data_above_max_xfB = above_F_value(max_xf_for_methodB, day)
    day_match_data_above_xfB = day_F(Data_above_max_xfB, day, sequence)
    print("For Method A: For Method A: Threshold value for exceptionally high values is", max_xf_for_methodA, ", the years at which the data equals or exceeds it: ", day_match_data_above_xfA)
    print("For Method B: For Method A: Threshold value for exceptionally high values is", max_xf_for_methodB, ", the years at which the data equals or exceeds it: ", day_match_data_above_xfB) 

def threshold_years(filename, F):
    sequence = lines(filename)
    year = years(sequence)
    max_xf_for_methodA=(method_a_max(F, year))[0]
    min_xf_for_methodA=(method_a_min(F, year))[-1]
    Data_above_max_xfA = method_a_max(F, year)
    Data_below_min_xfA = method_a_min(F, year)
    year_match_data_above_xfA = year_F(Data_above_max_xfA, year, sequence)
    year_match_data_below_xfA = year_F(Data_below_min_xfA, year, sequence)
    max_xf_for_methodB=(method_b(F, year))[0]
    min_xf_for_methodB=(method_a_min(F, year))[-1]
    Data_above_max_xfB = above_F_value(max_xf_for_methodB, year)
    Data_below_min_xfB = below_F_value(min_xf_for_methodB, year)
    year_match_data_above_xfB = year_F(Data_above_max_xfB, year, sequence)
    year_match_data_below_xfB = year_F(Data_below_min_xfB, year, sequence)
    print("For Method A: For Method A: Threshold value for exceptionally high values is", max_xf_for_methodA, ", the years at which the data equals or exceeds it: ", year_match_data_above_xfA)
    print("For Method A: For Method A: Threshold value for exceptionally low values is", min_xf_for_methodA, ", the years at which the data equals or is smaller than it: ", year_match_data_below_xfA)
    print("For Method B: For Method A: Threshold value for exceptionally high values is", max_xf_for_methodB, ", the years at which the data equals or exceeds it: ", year_match_data_above_xfB)
    print("For Method B: For Method A: Threshold value for exceptionally low values is", min_xf_for_methodB, ", the years at which the data equals or is smaller than it: ", year_match_data_below_xfB)
   