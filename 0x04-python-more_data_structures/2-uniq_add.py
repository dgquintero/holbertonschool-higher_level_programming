#!/usr/bin/python3
    ##sum = 0
    ##new_list = set(my_list)
    ##for i in new_list:
     ##   sum += i
    ##return sum
def uniq_add(my_list=[]):
    return sum(i for i in set(my_list))
