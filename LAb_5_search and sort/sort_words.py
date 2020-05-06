infile = open("words.txt", "r")
items = infile.readlines()
n = len(items)
items = list(map(lambda s: s.strip(), items))
print(items)


def msort(data):
    if (len(data) == 1):
        return data
    midindex = len(data)//2
    first = msort(data[0:midindex])
    second = msort(data[midindex:len(data)])

    ans = []
    firstind = 0
    secondind = 0
    while firstind < len(first) and secondind < len(second):
        if first[firstind] < second[secondind]:
            ans.append(first[firstind])
            firstind += 1
        else:
            ans.append(second[secondind])
            secondind += 1
    # one array is used up
    if firstind < len(first):
        ans.extend(first[firstind:])
    else:
        ans.extend(second[secondind:])
    return ans

def sel_sort(data):
    new_data = data[:]

    n = len(new_data)
    for i in range(n-1):
        small_value = i
        for j in range(i+1, n):
            if(new_data[j] < new_data[small_value]):
                small_value = j
        new_data[i], new_data[small_value] = new_data[small_value], new_data[i]

    return new_data














# # print(msort(['baz','test', 'foo', 'two', 'zoo', 'three', 'bar', 'fool']))


# To ask a prefix from the user:
#
# while True:
#     pre = input('Enter a prefix please')
#     if pre in items:
#         break



# goal = 'not here'
# count =0
# for i in range(len(items)):
#     # print(items[i][:len(pre)])
#     if (items[i][:len(pre)] == str(pre)) & (count ==0):
#
#         print('The first match is: '+items[i] +' in the index position: ' + str(i) )
#         count +=1
#         get the middle index
#         look at the mid index first elt
#         accordinly decide which side to go
#
def bin_search_new(list_search, pre):
    low = 0
    high = len(list_search) - 1

    if pre =="":
        return -1

    while(low <= high):
        mid = (low + high)//2

        item = str(list_search[mid])
        if(item.startswith(pre)) is True:

            while(mid >= low):

                if(list_search[mid-1].startswith(pre)):
                    print('item',item)
                    print('mid val', mid-1)
                    return mid
        elif str(pre) < item:
            high = mid-1

        else:
            low = mid+1






ret = 0
def bin_search(list_search, pre, start, stop):
    global ret
    if start > stop:
        return -1

    mid = (start + stop )//2
    print('mid val', mid)
    print(list_search[mid][:len(pre)])

    if(list_search[mid][:len(pre)] == str(pre)):
        print('found matching')
        print(list_search)
        a = (list_search[mid])
        print(a)
        ret = a
        return

    elif(list_search[mid] > str(pre)):
        print('prefix is smaller than mid value')
        bin_search(list_search,pre,start, mid-1)
    else:
        print('prefix is greater than mid value')
        bin_search(list_search, pre, mid+1, stop)





if __name__ == '__main__':
    sort_list = (sel_sort(items))
    print('sorted list', sort_list)
    pre = input('Enter a prefix please: ')
    print(pre[0])
    start = 0
    stop = len(items)-1
    ans = (bin_search_new(sort_list, pre))
    print('return val ',ret)












# # i = 1
# while(i>0):
#     a = input('please enter')
#     i = i+1

    # final = []
    # while True:
    #     try:
    #         final.append(input('enter prefix'))  # Each input given by the user gets appended to the list "final"
    #
    #     except EOFError:
    #         break



