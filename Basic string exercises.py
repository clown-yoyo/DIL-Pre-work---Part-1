# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 23:52:27 2016

@author: M-HERSENT
"""

# coding: utf-8

# ## Basic string exercises

# Fill in the code for the functions below. main() is already set up to call the functions with a few different inputs,
# printing 'OK' when each function is correct. The starter code for each function includes a 'return'
# which is just a placeholder for your code.

# ## A. donuts

# Given an int count of a number of donuts, return a string of the form 'Number of donuts: <count>', where <count> is the number passed in. However, if the count is 10 or more, then use the word 'many' instead of the actual count. 
# 
# So donuts(5) returns 'Number of donuts: 5' and donuts(23) returns 'Number of donuts: many'

# In[2]:

def donuts(count):
    
    if count < 10:
        print 'Number of donuts:', count
    else: 
        print 'Number of donuts: many'        
    return

donuts(4)
donuts(11)
# ## B. both_ends

# Given a string s, return a string made of the first 2 and the last 2 chars of 
# the original string, so 'spring' yields 'spng'. 
# However, if the string length is less than 2, return instead the empty string.

# In[ ]:

def both_ends(s):
    result = []
    if len(s) > 2:
        result = s[:2] + s[-2:]
            
    return result

both_ends('spring')


# ## C. fix_start

# Given a string s, return a string where all occurences of its first char have 
# been changed to '*', except do not change the first char itself. 
# 
# e.g. 'babble' yields 'ba\**le'
# 
# Assume that the string is length 1 or more. 
# Hint: s.replace(stra, strb) returns a version of string s where all instances of stra have been replaced by strb.

# In[ ]:

def fix_start(s): 
    result = s[0] + s[1:].replace(s[0], '*')
    return result
fix_start('babble')

# ## D. MixUp

# Given strings a and b, return a single string with a and b separated by a space ```'<a> <b>'```, except swap the first 2 chars of each string.
# 
# e.g.
#     
#     'mix', pod' -> 'pox mid'
#     
#     'dog', 'dinner' -> 'dig donner'
# 
# Assume a and b are length 2 or more.

# In[ ]:

def mix_up(a, b):
    result = b[:2] + a[2:] + ' '+ a[:2] + b[2:]
    return result

mix_up('mix', 'pod')
mix_up('dog', 'dinner')

# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.

# In[3]:

def test(got, expected):
    prefix = 'OK' if got == expected else ' X'
    # !r prints a Python representation of the strings (complete with quotes)
    print ' {} got: {!r} expected: {!r}'.format(prefix, got, expected)


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.

# In[ ]:

def main():
    print 'donuts'
    # Each line calls donuts, compares its result to the expected for that call.
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print
    print 'both_ends'
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

  
    print
    print 'fix_start'
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print
    print 'mix_up'
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')


# We call the main function.

# In[ ]:

main()


# ## D. verbing

# Given a string, if its length is at least 3, add 'ing' to its end. 
# Unless it already ends in 'ing', in which case
# add 'ly' instead. If the string length is less than 3, leave it unchanged. 
# Return the resulting string.

# In[ ]:

def verbing(s):
    if len(s) < 3:
        result = s
    elif s[-3:] == 'ing':
        result = s + 'ly'
    else:
        result = s + 'ing'
    
    return result

verbing('hello')

# ## E. not_bad

# Given a string, find the first appearance of the substring 'not' and 'bad'. If the 'bad' follows the 'not', replace the whole 'not'...'bad' substring with 'good'.
# 
# Return the resulting string.
# 
# So 'This dinner is not that bad!' yields: This dinner is good!

# In[ ]:

def not_bad(s):
    # +++your code here+++
    return


# ## F. front_back

# Consider dividing a string into two halves. If the length is even, the front and back halves are the same length. If the length is odd, we'll say that the extra char goes in the front half.
# 
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# 
# Given 2 strings, a and b, return a string of the form a-front + b-front + a-back + b-back

# In[ ]:

def front_back(a, b):
    # +++your code here+++
    return


# In[ ]:

def main():
    print 'verbing'
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')
    
    print
    print 'not_bad'
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print
    print 'front_back'
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')


# We call the main function.

# In[ ]:

main()



