"""
dlList.py
A circular doubly linked List interface and implementation in Python
author: Steven Carnovale and Vinita Narayanamurthi
"""

from dlnode import DoublyLinkedNode
class DoublyLinkedList:

    __slots__ = '__head'

    def __init__( self ):
        """ Create an empty list.
        """
        self.__head = None


    def append( self, new_value ):
        # we will need to append the node to the end
        # It can have two possibilities - head is null or node already exists
        # if head is null -
                        #  create the new node,
                          # - newnode next is pointed to itlsef
                         # - new node prev also is pointed to itself
        # else
                    # head.prev will give yu last node
                    # then make the next of last node point to the newnode
                    # also the newnode prev shd point to the last node
                    #newnode next shd point to head
                    # head.prev will point to new node

        node = self.__head
        newNode = DoublyLinkedNode(new_value)


        if node == None:
            # newNode.next = None
            # newNode.prev = None
            # self.__head = newNode
            newNode.next = newNode
            newNode.prev = newNode
            self.__head = newNode
        else:

            # while node.next != None:
            #     node = node.next
            # node.next = newNode
            # newNode.prev = node
            # newNode.next = None
            node_last = self.__head.prev
            node_last.next = newNode
            newNode.prev = node_last
            newNode.next = self.__head
            self.__head.prev = newNode






    def prepend(self, new_value):
        """ Add value to the beginning of the list.
            List is modified.
            :param new_value: the value to add
            :return: None
        """
        """
        Prepend again has two options:
        head is null - similar to append
        head not null - 
        head prev to newnode (here node is head)
        newnode next to node 
        newnode prev to None
        """
        #self.__head = DoublyLinkedNode( new_value, self.__front )
        node = self.__head
        newNode = DoublyLinkedNode(new_value)
        if node == None:
            # newNode.prev = None
            # newNode.next = None
            # self.__head = newNode
            newNode.prev = newNode
            newNode.next = newNode
            self.__head = newNode
        else:
            # node.prev = newNode
            # newNode.next = node
            # newNode.prev = None
            # self.__head = newNode
            node_last = self.__head.prev
            node.prev = newNode
            node_last.next = newNode
            newNode.prev = node_last
            newNode.next = node
            self.__head = newNode

    def move_clockwise(self, num):
        print('The music starts (' + str(num) +'): ')
        curr_node = self.__head
        while(num >= 0):
            print(curr_node.value + '->', end=' ')
            curr_node = curr_node.next
            num -=1
        print(curr_node.prev.value + ' is stuck holding the potato')
        # print(curr_node.prev.prev.value)
        # print(curr_node.prev.prev.next.value)
        # print('before changing', curr_node.prev.value)
        curr_node.prev = curr_node.prev.prev
        # print('after changing', curr_node.prev.value)

        curr_node.prev.next = curr_node
        self.__head = curr_node
        # print('finally we have', curr_node.prev.next.value)


    def move_anticlockwise(self, num):
        print('The music starts (' + str(num) + '): ')
        num = abs(num)
        curr_node = self.__head
        while (num >= 0):
            # print('potato passing anticlock to', curr_node.value)
            print(curr_node.value + '->', end=' ')
            curr_node = curr_node.prev
            num -= 1

        print( curr_node.next.value + ' is stuck holding the potato')
        # print(' before changind curr node next is', curr_node.next)
        curr_node.next = curr_node.next.next
        # print(' after changing curr node next is', curr_node.next)
        # print('before  chaning u have ', curr_node.next.prev )
        curr_node.next.prev = curr_node
        # print('also changed is ', curr_node.next.prev )
        self.__head = curr_node






    def print_clockwise(self):

        curr = self.__head
        if(curr is curr.next):
            print(curr.value)
        while(curr.next != self.__head):
            print(curr.value )
            curr = curr.next
        print(curr.value)
    def  exists(self):
        return self.__head



