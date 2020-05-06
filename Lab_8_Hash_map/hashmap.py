import re
from collections import namedtuple


Entry = namedtuple('Entry', ('key', 'value'))

'''
To make sure that the DELETED sentinel does not match
anything we actually want to have in the table, make it
a unique (content-free!) object.
'''


class _delobj: pass


DELETED = Entry(_delobj(), None)


class Hashmap:
    __slots__ = 'table', 'numkeys', 'cap', 'maxload', 'hash_map_type', 'collision', 'probe_count'

    def __init__(self, initsz=100, maxload=0.7, hash_map_type=0):
        '''
        Creates an open-addressed hash map of given size and maximum load factor
        :param initsz: Initial size (default 100)
        :param maxload: Max load factor (default 0.7)
        '''
        self.cap = initsz
        self.table = [None for _ in range(self.cap)]
        self.numkeys = 0
        self.maxload = maxload
        self.hash_map_type = hash_map_type
        self.collision =0
        self.probe_count=0

    def put(self, key, value):
        '''
        Adds the given (key,value) to the map, replacing entry with same key if present.
        :param key: Key of new entry
        :param value: Value of new entry
        '''
        firstDeleted = None  # we have to search through the whole line to to make sure we aren't adding duplicates
        # print('hash value for -> ' + key + ' is ' + str(self.hash_func(key)))
        index = self.hash_func(key) % self.cap

        '''Adding the collision part - occurs when two keys have the same hash value
                '''

        if self.table[index] is not None and self.table[index] != DELETED:
            self.collision +=1
        # if self.table[index] is not None and self.table[index].key == key:
        #     self.table[index].value +=1

        #
        # '''Adding the probing part - keeps track of the contents of the cell in the table
        # '''
        # probe_ind = index
        # self.probe_count =0
        # while self.table[probe_ind] is not None and self.table[probe_ind] != DELETED:
        #     probe_ind+=1
        #     self.probe_count +=1


        # self.probe_count =0
        while self.table[index] is not None and \
                self.table[index].key != key:
            if self.table[index] == DELETED and firstDeleted == None:
                firstDeleted = index
            index += 1
            self.probe_count+=1
            if index == len(self.table):
                index = 0
        # if we encountered a deleted and we didn't find the key change the key index to the first deleted index
        if firstDeleted != None and (self.table[index] == None or self.table[index].key != key):
            index = firstDeleted
        # otherwise if we haven't found the index then increase the size of the occupied cells
        elif self.table[index] is None:
            self.numkeys += 1

        self.table[index] = Entry(key, value)
        if self.numkeys / self.cap > self.maxload:

            # rehashing
            oldtable = self.table
            # refresh the table
            self.cap *= 2
            self.table = [None for _ in range(self.cap)]
            self.numkeys = 0
            # put items in new table
            for entry in oldtable:
                if entry is not None:
                    self.put(entry[0], entry[1])

    def remove(self, key):
        '''
        Remove an item from the table
        :param key: Key of item to remove
        :return: Value of given key
        '''
        index = self.hash_func(key) % self.cap
        while self.table[index] is not None and self.table[index].key != key:
            index += 1
            if index == len(self.table):
                index = 0
        if self.table[index] is not None:
            self.table[index] = DELETED

    def get(self, key):
        '''
        Return the value associated with the given key
        :param key: Key to look up
        :return: Value (or KeyError if key not present)
        '''
        index = self.hash_func(key) % self.cap
        while self.table[index] is not None and self.table[index].key != key:
            index += 1
            self.probe_count +=1
            if index == self.cap:
                index = 0
        if self.table[index] is not None:
            return self.table[index].value
        else:
            raise KeyError('Key ' + str(key) + ' not present')

    def contains(self, key):
        '''
        Returns True/False whether key is present in map
        :param key: Key to look up
        :return: Whether key is present (boolean)
        '''
        index = self.hash_func(key) % self.cap
        while self.table[index] is not None and self.table[index].key != key:
            index += 1
            self.probe_count +=1
            if index == self.cap:
                index = 0
        return self.table[index] is not None

    def hash_func(self, key):
        '''

        :param key: Key to store
        :return: Hash value for that key
        '''
        if self.hash_map_type ==0:
            return hash(key)

        elif self.hash_map_type ==1:
            val =0
            for i in range (len(key)):
                val+= (ord(key[i]) - ord('a'))*(26**(len(key)-1-i))
            return val
        else:
            val1, val2=0,0
            low =0
            high = len(key)-1
            mid = (low+high)//2
            for i in range(0,mid+1):
                val1+= (ord(key[high])+(ord(key[i])-ord('a')))
            for j in range(mid+1, high+1):
                val2 += (ord(key[low]) + (ord(key[j]) - ord('a')))
            return val1+val2


    # otherwise use this:
    # return len(key)


def printMap(map):
    for i in range(map.cap):
        print(str(i) + ": " + str(map.table[i]))

def word_search(filename, map):
    word_list = []
    word_list_append =[]
    max_occ_word = 'n/a'
    max_freq_count = 0
    infile = open(filename, "r")
    for line in infile:

        word_list = re.split('\W+', line)
        # print(word_list)
        if word_list is '\n':
            word_list.remove('\n')
        word_list_append.extend(word_list)


    for i in word_list_append:
        new_val =1
        i = i.lower()

        if map.contains(i):

            new_val = map.get(i)
            new_val+=1
            if(new_val > max_freq_count):
                max_freq_count = new_val
                max_occ_word = i
            # print('value is ',new_val)
            map.put(i, new_val)

        else:
            map.put(i,new_val)

    printMap(map)
    print('Maximum Repeated Word: ',max_occ_word)
    print('Number of probing: ', map.probe_count)
    print('No. of collisions: ', map.collision)



def main():
    map = Hashmap(initsz=5, hash_map_type=0)
    word_search('popularHistoryOfEngland.txt', map)
    map = Hashmap(initsz=5, hash_map_type=0)
    word_search('popularHistoryOfEngland.txt', map)
    map1 = Hashmap(initsz=100, maxload=0.5, hash_map_type=0)
    word_search('popularHistoryOfEngland.txt', map1)
    map2 = Hashmap(initsz=100, maxload=0.7, hash_map_type=1)
    word_search('popularHistoryOfEngland.txt', map2)
    map3 = Hashmap(initsz=100, maxload=0.9, hash_map_type=2)
    word_search('popularHistoryOfEngland.txt', map3)



if __name__ == '__main__':
    main()
