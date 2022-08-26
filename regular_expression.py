import re

'''
Functions in regex:
match  -> match only if the pattern is there in beginning of the string
search  -> match the patter if it is in the string anywhere
findall
sub
split
compile-finditer
'''
line="pet:cat i love cat pet:dog i love dog"
#matches=re.match('pet:cat', line)
#matches=re.match('pet:...', line)
# matches=re.match('pet:dog', line)
# print(matches.group(0))

#matches=re.search('pet:...', line)
# matches=re.search(r'PET:DOG', line, re.I)
# print(matches)

# matches=re.findall('pet:...', line)
# print(matches)

#print(re.sub('love','like',line))
#print(re.split(' ',line))

mystr="""
abcdefghijklmnopqrstuvwzyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

~!@#$%^&*()_+

+91-9898766199
9898766199
98987661119
989876666
8898766199
7898766199
6898766199
5898766199
4898766199
3898766199
2898766199
1898766199

https://www.cognixia.com
http://www.amazon.com
https://google.com
https://www.cognixia.co.in

762-432-5546
323_453_2232
221 212 1211
122.424.2111

raghulramesh@gmail.com
raghul_ramesh@yahoo.com
raghul.ramesh@outlook.com
ramesh@hotmail.com
"""
pattern=re.compile('(\w+\.)?\w+@\w+\.com')
#pattern=re.compile('\d{3}[-_ ]\d{3}[-_ ]\d{4}')
#pattern=re.compile('https?://(www\.)?\w+\.com?(\.in)?')
#pattern=re.compile('.')
matches=pattern.finditer(mystr)
for x in matches:
    print(x.group(0))