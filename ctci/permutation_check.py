def anagram_perm(str):
    if str == "":
        print('its empty')
        return str
    else:
        ans = []
        for w in anagram_perm(str[1:]):
            for pos in range(len(w)+1):
                ans.append(w[:pos] + str[0] + w[pos:])
        print(ans)
        return ans

g  = 'hi'
a = anagram_perm('guide')
print(a)


