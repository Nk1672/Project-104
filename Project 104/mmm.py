from collections import Counter

import csv


def find_median(total_entries, sorted_data):
    if total_entries%2 == 0:
        median1=float(sorted_data[total_entries//2])
        median2=float(sorted_data[total_entries//2-1])
        median=(median1+median2)/2
    else:
        median=float(sorted_data[total_entries//2])
    print("Median is: ",median)

def find_mean(total_weight, total_entries):
    mean=total_weight/total_entries
    print("Mean is: ",mean)

def find_mode(sorted_data):
    data=Counter(sorted_data)
    mode_data_for_range={
        "75-85":0,
        "85-95":0,
        "95-105":0,
        "105-115":0,
        "115-125":0,
        "125-135":0,
        "135-145":0,
        "145-155":0,
        "155-165":0,
        "165-175":0
    }

    for weight,occurence in data.items():
        if 75<weight<85:
            mode_data_for_range["75-85"]+=occurence
        if 85<weight<95:
            mode_data_for_range["85-95"]+=occurence
        if 95<weight<105:
            mode_data_for_range["95-105"]+=occurence
        if 105<weight<115:
            mode_data_for_range["105-115"]+=occurence
        if 115<weight<125:
            mode_data_for_range["115-125"]+=occurence
        if 125<weight<135:
            mode_data_for_range["125-135"]+=occurence
        if 135<weight<145:
            mode_data_for_range["135-145"]+=occurence
        if 145<weight<155:
            mode_data_for_range["145-155"]+=occurence
        if 155<weight<165:
            mode_data_for_range["155-165"]+=occurence
        if 165<weight<175:
            mode_data_for_range["165-175"]+=occurence
    
    mode_range, mode_occurence=0,0
    for range, occurence in mode_data_for_range.items():
        if occurence>mode_occurence:
            mode_range, mode_occurence = [int(range.split('-')[0]), int(range.split('-')[1])], occurence
        
    mode=float((mode_range[0]+mode_range[1])/2)
    print("Mode is: ",mode)

with open('data.csv', newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)

total_weight=0
total_entries=len(file_data)
sorted_data=[]

for person_data in file_data:
    total_weight+= float(person_data[2])
    sorted_data.append(float(person_data[2]))

sorted_data.sort()

find_mean(total_weight, total_entries)
find_median(total_entries, sorted_data)
find_mode(sorted_data)