infile = open("words.txt", "r")
items = infile.readlines()
n = len(items)
items = list(map(lambda s: s.strip(), items))
print(items)




def sel_sort(data):
    new_data = data[:]

    n = len(new_data)
    for i in range(n - 1):
        small_value = i
        for j in range(i + 1, n):
            if (new_data[j] < new_data[small_value]):
                small_value = j
        new_data[i], new_data[small_value] = new_data[small_value], new_data[i]

    return new_data




def bin_search_new(list_search, pre):
    low = 0
    high = len(list_search) - 1

    if pre == "":
        return -1

    while (low <= high):
        mid = (low + high) // 2

        item = str(list_search[mid])
        if (item.startswith(pre)) is True:
            check_before_index = mid

            while (check_before_index >= low):

                if (list_search[check_before_index].startswith(pre)):
                    mid = check_before_index
                else:
                    break
                check_before_index -= 1
            print('index start',mid)
            return mid

        elif str(pre) < item:
            high = mid - 1

        else:
            low = mid + 1

def lin_search(list_search, start_ind):
    final_list = []
    for i in range(start_ind, len(list_search)-1):
        if (list_search[i].startswith(pre)):
            final_list.append(list_search[i])
    print(final_list)




if __name__ == '__main__':
    sort_list = (sel_sort(items))
    print('The sorted list: ', sort_list)
    print('Welcome  to Auto-complete!')
    while True:
        pre = str(input('Enter a prefix please: '))
        stored_prefix = ""
        if(pre == ""):
            print('taking previous prefix')
            pre = stored_prefix
        else:
            stored_prefix = pre
            for item in sort_list:
                print('list elts',item)
                if(item.startswith(pre)):
                    print('it is inside')
                    break
        break
    startind = (bin_search_new(sort_list, pre))
    print('starting index value is',startind)
    lin_search(sort_list, startind)



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



