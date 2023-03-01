import datetime

start = datetime.datetime.now()
t1 = start.microsecond/1000

#####################     Задача_1    #############################

number = input("Введите целое положительное число :")

def chislo(number):
    factorial = 1
    number_int = int(number)
    for n in range(1,number_int+1):
        factorial = factorial * n
    print(f'Факториал числа "{number}"= {factorial}')
    return(factorial)
chislo(number)

#####################     Задача_2    #############################

string = 'absddsabllk'
sub_string = 'ab'
sub_len = len(sub_string)
input = 0
for i in range(len(string)):
    if string[i:i+sub_len] == sub_string:
        input += 1
print (f"Подстрока входит в строку {input} раза")

#####################     Задача_3    #############################

# nums1 = [1,3]
# nums2 = [2]

nums1 = [1,2]
nums2 = [3,4]

def findMedianSortedArrays( nums1, nums2):
    merged_array = nums1 +nums2
    merged_array_sort = sorted(merged_array)
    len_nums = len(merged_array_sort)
    del_sum = len_nums % 2
    l = (len_nums - del_sum)/2
    l1 = int(l)
    if del_sum == 1:
        median = merged_array_sort[l1]
        print(f"Медиана массивов =  {median}")
    else:
        r1 = merged_array_sort[l1-1]
        r2 = merged_array_sort[l1]
        median = (r1+r2)/2
        print(f"Медиана массивов =  {median}")
    return median

findMedianSortedArrays(nums1, nums2)


end = datetime.datetime.now()
t2 = end.microsecond/1000
print(f"Время в миллисекунда {t2-t1}")



