"""Module #8 Assignment
Julie Haas
LIS 5937
Spring 2021"""

import itertools
from itertools import chain
import copy


#data sets
nums = [1,2,3,4]
nums2 = []
names = ['Jolly','Olive','Yan','Grego','Barry','Indigo','Violet']

#print data sets
print("DATA SETS: ")
print("nums = ", nums)
print("nums2 = ", nums2)
print("names = ", names)
print('\n')

#create nums2 dataset
print("FILLING IN NUMS2")
for i in itertools.count (5):
    nums2.append(i)
    if i > 8:
        break
    print("nums2 = ", nums2)
print('\n')

#zip two lists together
print ("ZIP")
for x, y in zip(nums,names):
    print(x,y)
print('\n')

#print two lists in sequence
print ("CHAIN")
for x in itertools.chain(nums,nums2):
    print (x, end = '\n')
print('\n')
    
#cycle through list
count = 0
print ("CYCLING")
for i in itertools.cycle(nums):
    if count > 15:
        break
    else:
        print(i, end = " \n")
        count += 1
print('\n')

#repeat list x number of times
print("REPEATING")
for i in itertools.repeat (nums,4):
    print(i)
print('\n')

#copy lists
print("COPYING LISTS")

print("names = original list")
print("names2 = assignment copy of names")
print("names3 = shallow copy of names2")
print("names4 = deep copy of names3")
print('\n')

names2 = names
names3 = copy.copy(names2)
names4 = copy.deepcopy(names3)

#print original lists
print("   Unmodified lists...")
print("   names =  ", names)
print("   names2 = ", names2)
print("   names3 = ", names3)
print("   names4 = ", names4)
print('\n')

#modify names2
print("   Modifying names2...")
names2[0]=('HAZEL')

#print lists again
print("   names =  ", names)
print("   names2 = ", names2)
print("   names3 = ", names3)
print("   names4 = ", names4)
print('\n')

#modify names3
print("   Modifying names3...")
names3[1]=('BARBARA')
del names3[-1]

#print lists again
print("   names =  ", names)
print("   names2 = ", names2)
print("   names3 = ", names3)
print("   names4 = ", names4)
print('\n')

#modify names4
print("   Modifying names4...")
names4.append('BRUNO')
names4[0]=('TOM')

#print lists again
print("   names =  ", names)
print("   names2 = ", names2)
print("   names3 = ", names3)
print("   names4 = ", names4)
print('\n')
