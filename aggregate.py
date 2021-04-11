#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 23:00:13 2021

@author: jessica
"""

from os import listdir
from os.path import isfile, join
import pandas as pd
import numpy as np
import re 

relative_path = './dataset/'
compare = 'India'
country = 'China'

year_start = 2015
year_end = 2021
year_tradewar = 2018

def set_policy(mat):
    for i in range(year_tradewar - year_start, year_end - year_start + 1) :
        mat[i][2] = 1

country_fresh = np.zeros([year_end - year_start + 1, 3])
compare_fresh = np.zeros([year_end - year_start + 1, 3])
country_other = np.zeros([year_end - year_start + 1, 3])
compare_other = np.zeros([year_end - year_start + 1, 3])

set_policy(country_fresh)
set_policy(compare_fresh)
set_policy((country_other))
set_policy(compare_other)

files = [f for f in listdir('./dataset/') if isfile(join('./dataset/', f))]
for file in files:
    file_string = file.split('.')[0]
    year = int(file_string[0: 2]) + 2000
    df = pd.read_csv(relative_path + file, encoding='UTF-16', delimiter='\t')
    df = df.fillna(0)
    if ( file_string[-1] == 'f' ):
        country_fresh[year-year_start][0] = year 
        country_row = df.loc[df['Unnamed: 0'] == 'CHN']
        if country_row.empty == 0 :
            country_fresh[year-year_start][1] += country_row['Female'].values.astype(int)[0] \
                    + country_row['Male'].values.astype(int)[0]
        compare_row = df.loc[df['Unnamed: 0'] == 'IND']
        if compare_row.empty == 0 :
            compare_fresh[year-year_start][1] += compare_row['Female'].values.astype(int)[0] \
                    + compare_row['Male'].values.astype(int)[0]
    else:
        country_other[year-year_start][0] = year 
        country_row = df.loc[df['Unnamed: 0'] == 'CHN']
        if country_row.empty == 0 :
            country_other[year-year_start][1] += country_row['Female'].values.astype(int)[0] \
                    + country_row['Male'].values.astype(int)[0]
        compare_row = df.loc[df['Unnamed: 0'] == 'IND']
        if compare_row.empty == 0 :
            compare_other[year-year_start][1] += compare_row['Female'].values.astype(int)[0] \
                    + compare_row['Male'].values.astype(int)[0]
        

columns = ['year', 'total', 'tradewar?']
def change_to_df(mat):
    mat = pd.DataFrame(data = mat, columns = columns)
    return mat

country_fresh = change_to_df(country_fresh)
compare_fresh = change_to_df(compare_fresh)
country_other = change_to_df(country_other)
compare_other = change_to_df(compare_other)

country_fresh.to_csv(country + 'freshman.csv')
compare_fresh.to_csv(compare + 'freshman.csv')
country_other.to_csv(country + 'othergrades.csv')
compare_other.to_csv(compare + 'othergrades.csv')
    
    
    
    