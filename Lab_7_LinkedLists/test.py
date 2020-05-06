
from node import LinkedNode

class Queue:

    __slots__ = "front", "back"

    def __init__( self ):
        """ Create a new empty queue.
        """
        self.front = None
        self.back = None

    # def __str__( self ):
    #     """ Return a string representation of the contents of
    #         this queue, oldest value first.
    #     """
    #     print("in string rep")
    #     # result = "Queue["
    #     if(self.front != None):
    #         return "Queue [" + self.__str__(self.front.value) + \
    #            self.__str__(self.front.link ) + "]"

        # return "LinkedNode(" + repr(self.value) + "," + \
        #        repr(self.link) + ")"

        # while n != None:
        #     result += " " + str( n.value )
        #     n = n.link
        # result += " ]"
        # return result

    def is_empty( self ):
        return self.front == None

    def enqueue( self, newValue ):
        newNode = LinkedNode( newValue )
        if self.front == None:
            self.front = newNode
        else:
            self.back.link = newNode
        self.back = newNode

    def dequeue( self ):
        assert not self.is_empty(), "Dequeue from empty queue"
        self.front = self.front.link
        if self.front == None:
            self.back = None

    def peek( self ):
        assert not self.is_empty(), "peek on empty stack"
        return self.front.value

    insert = enqueue
    remove = dequeue

def test():
    s = Queue()
    print( s )
    for value in 1, 2, 3:
        s.enqueue( value )
        print(  )
    print('hey',s.is_empty)
    # s.__str__()



if __name__ == "__main__":
    test()
