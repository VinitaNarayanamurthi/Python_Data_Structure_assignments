
import sys
from dlnode import DoublyLinkedNode
from dlList import DoublyLinkedList

print('Welcome to the Hot Potato Game!')
print('Reading from: players.txt')
print('Using random number generator seed: ', sys.argv[2])

file_name = sys.argv[1]

infile = open(file_name, "r")
items = infile.readlines()

n = len(items)
items = list(map(lambda s: s.strip(), items))
print('Ready to play Hot Potato. Contestants are:', items)




names = DoublyLinkedList()
for i in range(len(items)):
    # print(items[i])
    names.append(items[i])


def main():

    import random
    random.seed(sys.argv[2])
    x=random.randint(-2*n,2*n)
    count=n
    while count>1:

        if x < 0:
            names.move_anticlockwise(x)
        else:
            names.move_clockwise(x)
        count-=1
        x=random.randint((2*-count),(2*count))
    a = names.exists()
    print(a,"is the winner! ")



if __name__ == '__main__':
    main()

