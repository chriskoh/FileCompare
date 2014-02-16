#!/usr/bin/env python3

import json
import pprint

def get_json():
    file_name = input("Enter name of JSON File: ")
    with open(file_name) as json_file:
        json_data = json.load(json_file)
        return json_data

def list_diff(json1, json2):
    for i in json1:
        if i in json2:
            print('     "' + str(i) + '"')
        elif i not in json2:
            print('-    "' + str(i) + '"')
    for i in json2:
        if i not in json1:
            print('+    "' + str(i) + '"')

def dict_diff(json1, json2):
    for n in json1:
        if n not in json2:
            print('-   "' + str(n) + '":')
    for n in json2:
        if n not in json1:
            print('+   "' + str(n) + '":')
            continue
        if json2[n] != json1[n]:
            if type(json2[n]) not in (dict, list):
                print('-   "' + str(n) + '" : "' + str(json1[n]) + '"')
                print('+   "' + str(n) + '" : "' + str(json2[n]) + '"')
            else:
                if type(json2[n]) == dict:
                    print('    "' + str(n) + '" : {')
                    dict_diff(json1[n], json2[n])
                    continue
        else:
            if type(json1[n]) == dict:
                print('    "' + str(n) + '" : {')
                pprint.pprint(json1[n], indent=4)
            else:
                print('    "' + str(n) + '" : "' + str(json1[n]) + '"')
    return

def file_match(file1, file2):
    if type(file1) == list and type(file2) == list:
        list_diff(file1, file2)
    elif type(file1) == dict and type(file2) == dict:
        dict_diff(file1, file2)
    return

def type_check(json1, json2):
    if type(json1) == type(json2):
        print("Type Check: Match " + str(type(json1)))
    elif type(json1) != type(json2):
        print("Type Check: Failed (type must match) \n\n File#1: " + str(type(json1)) + "\n File#2: " + str(type(json2)))
    return

def main():
    file1 = get_json()
    file2 = get_json()
    type_check(file1, file2)
    file_match(file1, file2)
    
if __name__ == "__main__":
    main()
