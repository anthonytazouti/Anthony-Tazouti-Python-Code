#1
def label(names):
    if names[-1]:
        names.append('and '+str(names[-1]))
        names.remove(names[-2])
    for i in range(len(names)):
        print(''+names[i]+', ')

n = ["Greg", "Marcia", "Peter", "Jan", "Bobby", "Cindy"]
label(n)




#2
def mergeSorted(a,b):
    l1=len(a)
    l2=len(b)
    i=j=0
    l=[]
    while i<l1 and j<l2:
        if a[i]<b[j]:
            l.append(a[i])
            i=i+1
        else:
            l.append(b[j])
            j=j+1
    while i<l1:
        l.append(a[i])
        i=i+1
    while j<l2:
        l.append(b[j])
        j=j+1
    return l

print(mergeSorted([1,4,9,16],[4,7,9,9,11]))


#3
def stripVowels(letters):
    newstr = letters
    vowels = ('a', 'e', 'i', 'o', 'u')
    for x in letters.lower():
        if x in vowels:
            newstr = newstr.replace(x,"")

    return newstr


#4
def filter_by_type(list_to_test, type_of):
    return [n for n in list_to_test if isinstance(n, type_of)]

mixedlist = [1, "pizza", "potato", 9, "tomato", 3, "apple", 101, 99, 45, "banana", 34, "watermelon"]
nums = filter_by_type(mixedlist,int)
strs = filter_by_type(mixedlist,str)
print (nums, strs)

#5
def swap(lst):
    lst[0], lst[-1] = lst[-1], lst[0]


values_list = input().split(',')
swap(values_list)
print(values_list)
