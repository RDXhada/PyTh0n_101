# function to validate a phone number
# say the first 2 numbers are the city - sofia - 02


def validate_phone_str(number) :
    if number[:2] == '02' :
        return validate_phone_str(number[:2])
    elif number[:3] == '042' :
        return validate_phone_str(number[3:])
    elif number[:5] == '09172' :
        return validate_phone_str(number[5:])
    if all([c.isdigit() for c in number]) and number[0] > 4 : 
        return 5 <= len(number) <= 7 
    return False

import re
from tokenize import group
# regex version (faster and simpler)
def validate_with_regex(number) :
    pattern = r'^(02|042|09172)?[5-9]\d{4,6}$'
    return bool(re.search(pattern, number))


# number = '02123456'
# print(validate_with_regex(number))

# import re - the module that realises the PCRE functionalities
# excaping with '\' - this way you escape special symbols

# excerise
# s* means that there are 0 or more repeating of the s
# s+ searches for one more repeatings of s
# s? matches with 0 or 1 occurences of s
# s{m,n} means between m and n repeatings of s
# s{, n} means 0 to n occurences/repeatings
# s{m, } means at least m occurences/repeatings
# . matches with one random symbol (new line symbols do not!)
# ^ matches the start of the string {or line if its a multiline string}
# $ matches the end of the string {or line if its multiline string}
# pipe symbol '|' is like 'or' 
# say we have day|nice [it will search for words (day or (nice)]
# da(y|n)ce will search for (dance) or (day)
# it retuns the first occurence/match!       

# symbol classes
# if we have [aobcd] and have Google as input it will 
# return G(o)oogle as if its the first occurence of any of the symbols 
# examples
#matcher('[aeoui]', 'Google') # 'G(o)ogle'
# matcher('[^CBL][aeoui]', 'Cobol') # 'Co(bo)l' 
# matcher('[0-9]{1,3}-[a-z]', 'Figure 42-b') # 'Figure (42-b)' matcher('[^a-zA-Z-]', 'Figure-42-b') # 'Figure-(4)2-b'
# \d is [0,9] (ine number between 0 and 9)
# \D is one symbol, which is not a number [^0-9]
# \s one whitespace symbol [like \t, \r,\n,\f, \v]
# \S one symbol which is not a whitespace [like ^\t, \r,\n,\f, \v]
# \w is one letter
# \W is one symbol, which is not a letter or number
# \b is the '0' symbol, but the border of a word
# groups are with '(a)'

print(re.search(r'(. )( .)(\1\2)*', 'a ba ba bc'))

def matcher(regex, string) :
    match = re.search(regex, string) 
    if match is None :
        return string
    start, end = match.span()
    return (string[:start] + 
            '(' + 
            string[start:end] + 
            ')' + 
            string[end:])

print(matcher('[hH]o+', 'Hohohoho...'))
print(matcher('([hH]o)+', 'Hohohoho...'))


print(matcher('day|nice', 'A nice dance-day.'))
print(matcher('da(y|n)ce', 'A nice dance-day.'))

print(matcher('[aeoui]', 'Google'))
print(matcher('[^CBL][aeoui]', 'Cobol'))

print(matcher(r'\d+', 'Phone number: 5551234'))
print(matcher(r'\w+', 'Phone number: 5551234'))

print(matcher('[0-9]{1,3}-[a-z]', 'Figure 42-b'))

print(matcher(r'(\b\w+\b).*\1', 'Matches str if str repeats one of its words.'))


# re methods are re.search, re.match, re.findall, re.finditer

# highest level implosion - groups for advanced learners

input_string = "The 4 Horsemen of the Apocalypse"
result = re.search(r'(\w+) \d', group(input_string))
print(result)
print(re.search(r'\w+\s*(?P<number_of_horses>\d)\s*\w+', group(input_string)))
#look ahead ?=...
print(re.search(r'[Tt]he(?=\s*Apocalypse)',group(input_string)))
# negative look ahead ?!...
print(re.search(r'[Tt]he(?!\s*4)', 'The 4 Horsemen of the Apocalypse'))
# look behind ?<=...
print(re.search(r'(?<=\s)[Tt]he', 'The 4 Horsemen of the Apocalypse'))

# more re methods
# re.sub, re.split, re.escape, help(re)
# flags
# re.I - ignore case sensitive search
# re.L - locale \w \W \b \B 
# re.M - multiline, basically '^' corresponds with the start of a line, and '$' with the end of a line
# re.S - '.' will match with every symbol, including new line
# re.X - ignore white spaces and comments
# re.A - \w, \W, \b, \B, \d, \D correpond to the ASCII classes


# we dont use regex with xml, html
# using 'or' or 'in' operators can be easier - so regex might not be best option
# when we want to parse a lnguage we need a parser, not a regex 
