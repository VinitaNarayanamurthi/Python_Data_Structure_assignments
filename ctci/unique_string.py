"""To write a program to check if a string has all unique charaters only.
We consider the ascii set of 128 characters. We initialise a boolean array of 128 elts to false. First encounter of every elt
changes it to true. Second encounter of the same elt makes it false."""

def unique_str(string):
    if len(string) > 128:
        return False
    char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char)
        print(val)
        print(char_set[val])
        if(char_set[val]):
            return False
        char_set[val] = 1

    return True

a = unique_str('abc')
print(a)