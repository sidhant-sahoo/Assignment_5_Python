# Task 2: Demonstrate List Slicing

l = list(range(1,11))
org_l = l
print("Origilnal list:",org_l)

ext_ele = l[0:5]
print('Extracted first five elementa:',ext_ele)

rev_ext_ele = list(reversed(ext_ele))
print('Reversed extracted elements:',rev_ext_ele)