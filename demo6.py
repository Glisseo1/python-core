#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# 变量x是字符串，并且格式化%d
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"

# 变量y是字符串， 并且格式化 %s
y = "Those who know %s and those who %s." % (binary, do_not)

print(x)
print(y)

print("I said: %r." % x)
print("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print(joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
