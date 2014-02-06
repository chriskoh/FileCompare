#!/usr/bin/env python2

import json
import pprint

def get_json():
    file_name = raw_input("Enter name of JSON File: ")
    with open(file_name) as json_file:
        json_data = json.load(json_file)
        return json_data

#def list_comp(json1, json2):
    

def print_diff(json1, json2):
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
                    print_diff(json1[n], json2[n])
                    continue
        else:
            if type(json1[n]) == dict:
                json1[n].pop('{',0)
                print('    "' + str(n) + '" : {')
                pprint.pprint(json1[n], indent=4)
            else:
                print('    "' + str(n) + '" : "' + str(json1[n]) + '"')
    return


def main():
    file1 = get_json()
    file2 = get_json()
    print_diff(file1, file2)

if __name__ == "__main__":
    main()
