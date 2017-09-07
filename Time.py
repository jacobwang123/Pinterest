#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 21:14:35 2017

@author: jacob
"""

from datetime import datetime
import pandas as pd
import json
import re
import requests
from bs4 import BeautifulSoup

# def stripper(str):
#     return str.rstrip('\n')

def choose_longest_list(l):
    longest = []
    for i in l:
        if len(i) > len(longest):
            longest = i
    return i

def get_pin_count(user):
    doc = requests.get('https://www.pinterest.com/' + user + '/pins/').text
    soup = BeautifulSoup(doc, 'html.parser')
    try:
        countStat = soup.select('div.countStat')
        pin_num = countStat[0].find('span', class_='value').contents[0]
        pin_num = int(pin_num.replace(',',''))
        return pin_num
    except:
        return 0

# with open('/Users/jacob/Desktop/Python/Pinterest/source_ids4.txt') as infile, open('/Users/jacob/Downloads/source_ids4.txt', 'a') as outfile, open('/Users/jacob/Downloads/backup.txt', 'a') as backup:
#     pins = infile.readlines()
#     for line in pins:
#         jObj = json.loads(line)
#         time = datetime.strptime(jObj['timestamp'], '%Y-%m-%d %H:%M:%S')
#         if time >= datetime(year=2017, month=5, day=1):
#             outfile.write(line)
#             backup.write(jObj['pinID'] + '\n')

# with open('/Users/jacob/Downloads/backup.txt') as backup, open('/Users/jacob/Desktop/Python/Pinterest/repin_users.txt') as infile, open('/Users/jacob/Downloads/repin_users.txt', 'a') as outfile:
#     repins = infile.readlines()
#     ids = backup.readlines()
#     ids = [id.rstrip('\n') for id in ids]
#     for line in repins:
#         id = line.split(':', 1)[0].lstrip('{"').rstrip('"')
#         if id in ids:
#             outfile.write(line)

# with open('/Users/jacob/Downloads/test.txt') as infile, open('/Users/jacob/Downloads/test1.txt', 'w') as outfile:
#     repins = infile.readlines()
#     for line in repins:
#         line.lstrip('{').rstrip('}')
#         id, users = line.split(':', 1)
#         outfile.write('{"pinID": ' + id + ', "users"' + users + '}')

# with open('/Users/jacob/Desktop/Python/Pinterest/repin_users.txt') as infile, open('/Users/jacob/Downloads/repin_users.txt', 'a') as outfile:
#     l = infile.readlines()
#     l1 = list(set(l))
#     for line in l1:
#         outfile.write(line)

# with open('/Users/jacob/Desktop/Python/Pinterest/repin_users.txt')  as infile, open('/Users/jacob/Downloads/repin_users.txt', 'a') as outfile:
#     lines = infile.readlines()
#     for line in lines:
#         if line.rstrip('\n').endswith('["]}'):
#             continue
#         else:
#             outfile.write(line)

# sourceDF = pd.read_json('/Users/jacob/Desktop/Python/Pinterest/source_ids.txt', lines=True, encoding='utf-8')
# sourceDF['timestamp'] = pd.to_datetime(sourceDF['timestamp'])
# grouped = sourceDF.groupby(['pinID'])['label'].apply(list)
# del sourceDF['label']
# sourceDF = sourceDF.drop_duplicates()
# sourceDF = sourceDF.join(grouped, on='pinID')
# cols = sourceDF.columns.tolist()
# c = []
# c.append(cols[1])
# c.append(cols[0])
# c.append(cols[3])
# c.append(cols[2])
# sourceDF = sourceDF[c]
# sourceDF.to_csv('/Users/jacob/Downloads/source_ids.txt', sep='\t', index=False)            
            
# repins = pd.read_json('/Users/jacob/Desktop/Python/Pinterest/repin_users.txt',\
#                       dtype={"pinID":str, "users":list}, lines=True, encoding='utf-8')
# grouped = pd.DataFrame(repins.groupby(['pinID'])['users'].apply(list))
# grouped['users'] = grouped['users'].apply(choose_longest_list)
# grouped['pinID'] = grouped.index
# grouped = grouped[['pinID', 'users']]
# grouped.to_csv('/Users/jacob/Downloads/repin_users_grp.txt', sep='\t', index=False)

cols = ['id','user','url','dscp']
for i in ['0','1','2','3','4']:
    df = pd.read_csv('/Users/jacob/Desktop/Python/Pinterest/user_pins_' + i + '.txt', header=None, names=cols, sep='\t')
    df = df.drop_duplicates()
    df.to_csv('/Users/jacob/Desktop/Python/Pinterest/user_pins0.txt', sep='\t', index=False, header=False, mode='a')

# user_pins = []
# with open('/Users/jacob/Desktop/Python/Pinterest/user_pins.txt') as f:
#     data = f.readlines()
#     for line in data:
#         if line[:8].isdigit():
#             user_pins.append(line)
#         else:
#             user_pins[-1] = user_pins[-1].rstrip('\n') + line
# with open('/Users/jacob/Desktop/Python/Pinterest/user_pins_0.txt', 'w') as f:
#     for line in user_pins:
#         f.write(line)
   
# df_pins = pd.read_csv('/Users/jacob/Desktop/Python/Pinterest/user_pins_0.txt', header=None, names=cols, sep='\t', usecols=['id','user'])         
# df_pins = df_pins.groupby(['user']).count()
# df_pins['user'] = df_pins.index

# df_users = pd.read_csv('/Users/jacob/Desktop/Python/Pinterest/user_list_sample_Jacob.csv')
# boolean = df_users['UserID'].isin(df_pins['user'])
# missing_user = df_users.loc[~boolean, :]
# del missing_user['Unnamed: 0']
# missing_user.to_csv('/Users/jacob/Desktop/Python/Pinterest/missing_users.txt', index=False, header=False)

# df_pins['real_count'] = df_pins['user'].map(get_pin_count)
# df_pins.to_csv('/Users/jacob/Desktop/Python/Pinterest/user_pin_count.csv', index=False)

# df_pins = pd.read_csv('/Users/jacob/Desktop/Python/Pinterest/user_pin_count.csv', header=0)
# rate = (df_pins['id'] < df_pins['real_count'] * 0.95).mean()
# print(rate)

# for f in ['followers','followings']:
#     for i in ['0','1','2','3','4']:
#         df = pd.read_csv('/Users/jacob/Desktop/Python/Pinterest/user_'+f+'_'+i+'.txt',
#                          header=None, names=['id','fList'], sep='\t')
#         grouped = pd.DataFrame(df.groupby(['id'])['fList'].apply(list))
#         grouped['fList'] = grouped['fList'].apply(choose_longest_list)
#         grouped['id'] = grouped.index
#         grouped = grouped[['id', 'fList']]
#         grouped.to_csv('/Users/jacob/Downloads/user_'+f+'.txt', sep='\t', index=False, header=False, mode='a')