# dictionary = {'a':'apple','b':'ball','c':'cat','d':'dog'}
# dictionary['e']='elephant'
# print(dictionary.get('e',"'e' not found"))
#
# list = ['apple','ball','cat','dog']
# print('apple'in list)

#
# l = ['apple','ball','cat','dog']
# l.extend(['10','30','40','20'])
# print(l)
# l.remove('cat')
# print(l)
# del l[0]
# print(l)
# del l[0:2]
# print(l)
# l.insert(2,'50')
# print(l)
# l.sort()
# print(l)
# l.reverse()
# print(l)
# print(len(l))
# l = [10,20,30,40,50,60,70,80]
# print(l[0:7:3])
#
# x =[]
# for i in range(11):
#     z = i **2
#     x.append(z)
# print(x)
#
# x = [i**2 for i in range(11) if i**2%2==0]
# print(x)
#
# set1 = {1,2,3,4,5,6,7,8,9}
# set2 = {11}
# print(set1 & set2)
# print(set1 | set2)
# print(set1.union(set2))
# print(set2.issubset(set1))
#
# a= "jaydip"
# print(a.capitalize())
# print(a.upper())
# print(a.lower())
#
# name = "Mike"
# number = len(name)*3
# print("Hello {}, your lucky number is {}.".format(name,number))
# print("Hello {1}, your lucky number is {0}.".format(name,number))
#
# price = 150
# with_tax = 150+50
# print(price,with_tax)
# print("Price: Rs {:.2f}. with tax: Rs {:.2f}.".format(price,with_tax))
#

#
# fun = lambda a,b : a+b
# print(fun(10,11))
#
# ans = set(filter(lambda a:a%2==0,range(10)))
# print(ans)
#
# ans = list(map(lambda a : a**2,range(10)))
# print(ans)



# class const_dest:
#     x = 0
#     def __init__(self,color,type):
#         self.color = color
#         self.type = type
#         print("constructed")
#     def __del__(self):
#         print("Destructed")
# cd = const_dest('black','SUV')
# print(cd.color)
# print(cd.type)
#
# cd_1 = const_dest('red','Sedan')
# print(cd_1.color)
# print(cd_1.type)


# class name:
#     x = 0
#     name = ""
#     def __init__(self, z):
#         self.name  = z
#         print("hi",z)
#
# class football_fans(name):
#     points = 0
#     def pts(self):
#         print(self.name,"scores")
#
# n= name("Jaydip")
# scores = football_fans("Jim")
# scores.pts()
#
#
#
# class A:
#     def state_1(self):
#         print("state 1 present")
#     def state_2(self):
#         print("state 2 present")
#     def state_3(self):
#         print("state 3 present")
#
# class B:
#     def state_4(self):
#         print("state 4 present")
#     def state_5(self):
#         print("state 5 present")
# class C(A,B):
#     def state_6(self):
#         print("state 6 present")
#
# a = A()
# a.state_2()
#
# b=B()
# b.state_4()
#
# c = C()
# c.state_3()
# c.state_6()


# a = 1
# b = 2
# print(a + b)
# print(int.__add__(a, b))
#
# class vegetable:
#     def __init__(self, carrot,beans):
#         self.carrot = carrot
#         self.beans = beans
#     def __add__(self, other):
#         carrot = self.carrot + other.carrot
#         beans = self.beans + other.beans
#         return vegetable(carrot, beans)
#
# v1 = vegetable(5,3)
# v2 = vegetable(7,8)
# v3 = v1 + v2
# print(v3.carrot)
# print(v3.beans)

#regular Expressions
import re
# pattern = "apple"
# if re.match(pattern,"appleappball"):
#     print("True")
# else:
#     print("False")
#
# string = re.findall("xyz",pattern)
# print(string)
#
# if re.search(pattern,"apple",flags=0):
#     print("True")
# else:
#     print("False")
#
# pattern = "Cat"
# string = "dog"
# print(re.sub(pattern,"Cat",string,count=0,flags=0))

# CHARACTERS AND CHARACTER SEQUENCES
# ^ - Matches the beginning of a line
# $ - Matches the end of a line
# . - Matches any character
# \d - Matches any digit
# \D - Matches any non- digit
# \s - Matches whitespace
# \S - Matches any non- whitespace


# string = "It is a dog 56"
# pattern = "^I"
# print(re.findall(pattern,string,flags=0))
#
# pattern = "g$"
# print(re.findall(pattern,string,flags=0))
#
# pattern = "."
# print(re.findall(pattern,string,flags=0))
#
# pattern = "^I..."
# print(re.findall(pattern,string,flags=0))

# pattern = "\S"
# print(re.findall(pattern,string,flags=0))

# * - Repeats a character zero or more times
# + - Repeats a character one or more times
# ( - Indicates where string extraction is to start
# ) - Indicates where string extraction is to end
# ? - Matches the expression to 1 times

import  re

string = "From bobby.mark@gmail.com"
pattern = r"^From (\S+@\S+)"
match = re.search(pattern, string)
if match:
    print(match.group(1))

    # [ ]
    # [aeiou] - Matches a single character in the listed set
    # [^xyz] - Matches a single character
    # [a-z0-9] - Set of characters can include a range
    # {}
string = "Python 3.0"
pattern = r"[A-Z]"
match = re.findall(pattern, string)
if match:
    print(match)