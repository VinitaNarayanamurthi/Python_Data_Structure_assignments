def mystery(s):
    if s == "" or len(s) == 1:
        return s
    else:
        return mystery(s[2:]) + s[0]
if __name__ == "__main__":
    print( mystery("trash") )
