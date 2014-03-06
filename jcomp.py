#!/usr/bin/env python3

import json
import pprint

def get_file(): # Function: Open files

    file_name = input("Enter name of JSON File: ") # Set .json file as "file_name"
    with open(file_name) as json_file: # Open "file_name" as "json_file"
        json_data = json.load(json_file) # Parse "json_file" as "json_data" | json objects -> python dict / json array -> python lists
        return json_data 

def list_diff(file1, file2): # Compare list, file 2 to file 1 and print differences

    for i in file1:
        if i in file2: # Value is in BOTH files
            print('     "' + str(i) + '"')
        elif i not in file2: # Value is MISSING in file 2
            print('-    "' + str(i) + '"')
    for i in file2:
        if i not in file1: # Value is ONLY in file 2
            print('+    "' + str(i) + '"')

def dict_diff(file1, file2): # Compare dict, file 2 to file 1 and print differences

    for n in file1: # Compare Keys
        if n not in file2: # Key is MISSING in file 2
            print('-   "' + str(n) + '":')
    for n in file2:
        if n not in file1: # Key is ONLY in file 2
            print('+   "' + str(n) + '":')
            continue
        if file2[n] != file1[n]: # Compare values, value is ONLY in file 2
            if type(file2[n]) not in (dict, list): # Check, file 2 value is NOT a dict or list
                print('-   "' + str(n) + '" : "' + str(file1[n]) + '"')
                print('+   "' + str(n) + '" : "' + str(file2[n]) + '"')
            else:
                if type(file2[n]) == dict: # File 2 value is type dict
                    print('+   "' + str(n) + '" : {') # Print Key file 2
                    dict_diff(file1[n], file2[n]) # Recursion, compare dict in file 2 to value in file 1
                    continue
        else:
            if type(file1[n]) == dict: # Value in BOTH files, and is type dict
                print('    "' + str(n) + '" : {')
                pprint.pprint(file1[n], indent=4) # Pretty print file 1 dict
            else: # Value in BOTH files, not dict or list
                print('    "' + str(n) + '" : "' + str(file1[n]) + '"')
    return

def file_match(file1, file2): # Compare, file 1 and file 2

    if type(file1) == list and type(file2) == list: # if BOTH elements are list
        list_diff(file1, file2)
    elif type(file1) == dict and type(file2) == dict: # if BOTH elements are dict
        dict_diff(file1, file2)
    return

def type_check(file1, file2): # Check, both files are JSON object or JSON Array

    if type(file1) == type(file2):
        print("Type Check: Match " + str(type(file1)))
        return True
    elif type(file1) != type(file2):
        print("Type Check: Failed (type must match) \n\n File#1: " + str(type(file1)) + "\n File#2: " + str(type(file2)))
    return False

def main():

    file1 = get_file() # Load files
    file2 = get_file()
    check = type_check(file1, file2) # Check file types
    if check == True: 
        file_match(file1, file2) # Compare files
    
if __name__ == "__main__":
    main()
