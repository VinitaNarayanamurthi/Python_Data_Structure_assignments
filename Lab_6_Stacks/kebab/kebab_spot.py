"""
A module that represents "spots" on the skewer.

Author: Sean Strout @ RITCS
"""

class KebabSpot:
    """
    Class: KebabSpot
    Description: This class is used to represent an individual
        spot on the skewer.  Each spot contains a food item,
        and a reference to the next spot.  
    """
    __slots__ = "item", "next"
    def __init__(self, item, next):
        """
        Construct a KebabSpot instance.
        :param item: the item (Food) to store at this spot
        :param next: the next KebabSpot on the skewer

        """
        self.item = item
        self.next = next


    def size(self):
        """
        Return the number of elements from this KebabSpot instance to the end
        of the skewer.
        :return: the number of elements (int)
        """
        #return 0
        return  1 + self.size_helper(self.next)
    def size_helper(self, node):


        if node is None:
            return 0
        else:

            return  1 + (self.size_helper(node.next))

    # def size(self):
    #     if self.item is None:
    #         return 0
    #     else:
    #         self.next = self.next.next
    #         return 1 + self.size()

    def is_vegan(self):
        """
        Return whether there are all vegetables from this spot to the end of
        the skewer.
        :return True if there are no vegetables from this spot down, 
        False otherwise.
        """

        while (self is not  None):

            if self.item.veg == True:
                if (self is not None):
                    # self.item = self.next.item
                    self = self.next

            else:
                return False
        return True



        # print("its in")
        # while(self.item != None):
        #     print("inside while")
        #     print('is it veg', self.item.veg)
        #     if self.item.veg == True:
        #         if(self.next != None):
        #             #self.item = self.next.item
        #             self = self.next
        #
        #     else:
        #         return False
        # return True



    def calories(self):

        calory_store = 0
        while(self is not None):
            # print('item name', self.item.name)
            # print('item calorie', self.item.no_of_calories)
            calory_store += self.item.no_of_calories
            self = self.next
        return calory_store











    def has(self, name):

        """
        Return whether there are any vegetable from this spot to the end of
        the skewer.
        :param name: the name (string) being searched for.
        :return True if any of the spots hold a Food item that equals the
        name, False otherwise.
        """

        # print('next next item', self.next.next.item.name)
        # Spot(1)
            # item
                # name = Pork
            # next

        # Spot(2)
            # item
                # name = Pork
            # next
        spot = self
        while(spot is not  None):


            if(name == spot.item.name):

                return True
            else:

                spot = spot.next

        return False


    def string_em(self):
        """
        Return a string that contains the list of items in the skewer from
        this spot down, with a comma after each entry.
        :return A string containing the names of each of the Food items from
        this spot down.

        """

        return str(self.item.name)   + "," + self.helper_string_em(self.next, "")
    def helper_string_em(self, node, total):
        if node is None:

            return total
        else:
            total += str(node.item.name) + ","

            return self.helper_string_em(node.next, total)



    #     if node is None:
    #         return ""
    #     else:
    #         total = total + str(self.item.name) + ","
    #         return  total + self.helper_string_em(node.next, total)


    def get_item(self):
        if self.item != None:
            return self.item
        else:
            print('nothing is here')