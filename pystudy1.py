#! /usr/bin/python3


do 			= 'plays '
who			= 'li '
something	= 'ball '

str1 = who + do + something

print (str1)


word = 'friend'
find_the_eivl_in_your_friend = word[0] +word[2:4] + word[-3:-1]

print (find_the_eivl_in_your_friend)


phone_number = '185 0077 8114'
hiding_number = phone_number.replace (phone_number[0:9], "*" * 9)

print(hiding_number)

print('{} a word she can get what she {} for.' .format('With','came'))
print('{preposition} a word she can get what she {verb} for.' .format(preposition = 'with', verb = 'came'))
print('{0} a word she can get what she {1} for.'.format('with','came'))
