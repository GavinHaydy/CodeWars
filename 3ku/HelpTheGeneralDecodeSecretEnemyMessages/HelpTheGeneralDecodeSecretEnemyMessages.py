# print(encode("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
# print(
# encode("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
# print(encode("!@#$%^&*()_+-"))
# a,b,c = "", "", ""
# for w in "abcdefghijklmnopqrstuvwxyz":
#     a += encode(  "" + w)[0]
#     b += encode( "_" + w)[1]
#     c += encode("__" + w)[2]
# print(a)
# print(b)
# print(c)

# a = "Hello World"
# b = "atC5kcOuKAr"
# for i in range(len(a)):
#     print(ord(a[i])-ord(b[i]))
# print([ord(u) for u in a])
# print([ord(u) for u in b])
Key = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,? "
# def _encrypt_one101(c, n):
#     for i in range(n):
#         ind = Key.find(c)#26 27*2 -1 53 % 67
#         print(ind)
#         c = Key[((ind+1) * 2 - 1) % len(Key)]
#         print(((ind+1) * 2 - 1),len(Key), c)
#     return c

# def encode(s):
#     return "".join(_encrypt_one101(c,i+1) if c in Key else c for i, c in enumerate(s))
# print(encode("**"))

# print(Key[len(Key)% Key.index("H")-1])
# print(Key[(Key.index("e")+1)*2*2-1])
# print(Key[(Key.index("H")+1)*2-1])
# print(len(Key)% Key.index("e"))
# print(((Key.index("H")+1)*2-1)%len(Key))
# 5%2=1
# 17%3=2
# 2n-1%67=1
# 34%67=1
# print((Key.index("H")+1))#34 (2**(i+1))-1 *2 -1
# x+1 * 2**n %  67=0  n已知 
# x+1 *2 <= 68 
# 34 * 1 ==33
# H  ((33+1)*(2**1)-1)%66+1
# I  ((34+1)*(2**2)-1)%66+1
# x * 4 -1 % 67 == 5
# x * 4 % 67 =5
# x = 67 +33 /4     


def encode(s):
    result = ''
    for i in range(len(s)):
        result += Key[((Key.index(s[i])+1)*(2**(i+1))-1)%(len(Key)+1)] if s[i] in Key else s[i]
    return result
# print(encode("Hello World!"))

# print(67+1 /2)
def decode(s):

    def _index(index,remainder):
        for i in range(len(Key)+1):
            if (i * (2**index) -1) %67 == remainder:
                return i -1

    result = ''
    for i in range(len(s)):
        for x in range(len(Key)+1):
            if s[i] in Key:
                result += Key[_index(i+1,Key.index(s[i]))]
                break
                # pass
            else:
                result += s[i]
                break
    return result


print(encode("Hello World!"))
r = ''
for i in "Hello World!":
    r += encode(i)
print(r)
print(decode("atC5kcOuKAr!"))
# print(decode(encode("Hello World!")))
# print(len(Key))
# print(Key.index("I"))
# print(((Key.index("I")+1) * 2 -1)%67)
# print(encode("I"))

# print(Key.index("H"))
# print(((Key.index("H")+1) * 2 -1)%67)
# print(encode("H"))

# for i in range(68):
#     if i * 2 %67 ==0:
#         print(i)

#I =18 34  35+66
#H =67 33 33+1 * 2 -1 % (66 +1)
# = 34*2 -1 %67
# = 68 -1 %67 = 0
# 67 +1 =68
# 68 /2 

#I = 34 +1 * 4 -1 % (66+1)
#= 35 * 4 -1 %67
#= 140 -1 %67=5
#= 67 * n +5+1 =140
#= 
# for i in range(67):
#     if (i * 4 -1) %67 == 5:
#         print(i)

""" best
 """
