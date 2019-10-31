# https://www.youtube.com/watch?v=K8L6KVGG-7o this is the link to the good youtube video

# .       - Any Character Except New Line
# \d      - Digit (0-9)
# \D      - Not a Digit (0-9)
# \w      - Word Character (a-z, A-Z, 0-9, _)
# \W      - Not a Word Character
# \s      - Whitespace (space, tab, newline)
# \S      - Not Whitespace (space, tab, newline)
#
# \b      - Word Boundary
# \B      - Not a Word Boundary
# ^       - Beginning of a String
# $       - End of a String
#
# []      - Matches Characters in brackets
# [^ ]    - Matches Characters NOT in brackets
# |       - Either Or
# ( )     - Group
#
# Quantifiers:
# *       - 0 or More
# +       - 1 or More
# ?       - 0 or One
# {3}     - Exact Number
# {3,4}   - Range of Numbers (Minimum, Maximum)


#### Sample Regexs ####

# [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+

import re
print('\tTab')
# precede an r in front of a string will make the string as a raw string, which means python will just
# treat it as literally what it is. \t is not an escape for tab anymore, it is just \t
print(r'\tTab')

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-.555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

pattern=  re.compile(r'abc') # this is case sensitive and order sensitive
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

print(text_to_search[1:4])


period = re.compile(r'\.') # if you want to search for an actual period, you need to escape it,
                            # since period means something special in regular expression
period_matches = period.finditer(text_to_search)
for period_match in period_matches:
    print(period_match)


# \b      - Word Boundary###################
# Ha HaHa this line contains Ha in the long string. The two got matched is the first and the second, since both new line and
# whitespace are word boundaries
Ha = re.compile(r'\bHa')
Ha_matches = Ha.finditer(text_to_search)
print()
print(r"\b Ha matches: ")
for Ha_match in Ha_matches:
    print(Ha_match)

# \B      - Not a Word Boundary######################
# this time only the third Ha is matched since it is the only one that does not have a word boundary before it
HaB = re.compile(r'\BHa')
HaB_matches = HaB.finditer(text_to_search)
print()
print(r"\B Ha matches: ")
for HaB_match in HaB_matches:
    print(HaB_match)



sentence = "Start a sentence and then bring it to an end"
# ^       - Beginning of a String#######################
# note ^something means we want to match a something and this something must be at the beginning of a string
# it does not mean that we want to match a string that starts with something

# this can match the first Start since it is actually a 'Start' at the beginning of the string
start = re.compile(r'^Start')
start_matches = start.finditer(sentence)

# this doesnot match anything since there is not a then word that is at the beginning of the string
then = re.compile(r'^then')
then_matches = then.finditer(sentence)
print()
print(r"Start matches: ")
for start_match in start_matches:
    print(start_match)

print()
print(r"then matches: ")
print("this doesnot match anything since there is not a then word that is at the beginning of the string")
for then_match in then_matches:
    print(then_match)

# $       - End of a String#####################
# note unlike the ^ is put in front of something, $ should be put behind something
end = re.compile(r'end$')
end_matches = end.finditer(sentence)
print()
print(r"end matches: ")
for end_match in end_matches:
    print(end_match)

# Now we parse the phone numbers in the long string

# there are three kind of phone numbers 123*555*1234  123.555.1234 321-555-4321
# There three three four digits pattern can be seperated by * . or -
# in this case, we use . in our regular expression, since . means anything
# so * . - can all be matched by a . in regular expression
phonenum = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
phonenum_matches = phonenum.finditer(text_to_search)
print()
print(r"phone number matches: ")
for phonenum_match in phonenum_matches:
    print(phonenum_match)

# if we only want to match phone numbers that are seperated by - or .  (we don't want any seperated by *)
# [] is a character set, means that all strings that has a - or . that occupies this place will be matched
# note . does not need to be escaped when within []
# note that although there are multiple characters within the [], but the [] only talks about one place in the string
# which means 321-.555-4321 or 321--555-4321 can not be matched
phonenum2 = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
phonenum2_matches = phonenum2.finditer(text_to_search)
print()
print(r"phone number seperated by - and . matches: ")
for phonenum2_match in phonenum2_matches:
    print(phonenum2_match)

# now let's see another example of character set
# say we only want to match phone numbers that starts with 800 or 900
phonenum89 = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
phonenum89_matches = phonenum89.finditer(text_to_search)
print()
print(r"phone number starts with 800 or 900 matches: ")
for phonenum89_match in phonenum89_matches:
    print(phonenum89_match)

# within a character set you can use [1-5] to match for all number between 1 and 5, [a-z] to match all lower case
# and [a-zA-Z] to match all letters
# [^a-zA-Z] matches anything that is not a letter, since outside of a character set ^ means beginning but inside a
# character set, ^ means negate

####### Quantifiers ###########
# Quantifiers:
# *       - 0 or More
# +       - 1 or More
# ?       - 0 or One
# {3}     - Exact Number
# {3,4}   - Range of Numbers (Minimum, Maximum)

phonenumq = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')
phonenumq_matches = phonenumq.finditer(text_to_search)
print()
print(r"Using Quantifiers phone number seperated by - and . matches: ")
for phonenumq_match in phonenumq_matches:
    print(phonenumq_match)

# |       - Either Or ##################
# ( )     - Group     ##################
# (Mr|Ms|Mrs) means strings that starts with Mr or Ms or Mrs all qualifies
# \.? means that folowing the prefix there can be one or zero .
# \s means a whitespace
# [A-Z] means following the whitespace has to be an upper case letter
# \w* means that following the uppercase letter there can be 0 or more word characters
name = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
name_matches = name.finditer(text_to_search)
print()
print(r"names matches: ")
for name_match in name_matches:
    print(name_match)

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.com
corey-321-schafer@my-work.net
'''

# [a-zA-Z0-9.-]+ means match one or more letter or digit or . or -
# [a-zA-Z-]+ means match one or more letter or -
# \. match the literal .
# (com|edu|net) means strings that end with com or edu or net all qualify
emailpattern=re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
email_matches = emailpattern.finditer(emails)
print()
print(r"email matches: ")
for email_match in email_matches:
    print(email_match)

urls= '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

# you can use () to identify a group and this group will be saved in each match object
# (www\.)? means the first www. group which is optional indicated by the ?
# (\w+) means the second group the domain name
# (\.\w+) means the third group, the .com or .gov etc.
urlpattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
url_matches = urlpattern.finditer(urls)

for match in url_matches:
    # group 0 is everything matched
    print("group 0 is")
    print(match.group(0))
    print()
    print("group 1 is")
    print(match.group(1))
    print()
    print("group 2 is")
    print(match.group(2))
    print()
    print("group 3 is")
    print(match.group(3))
    print()


# the .sub method with replace all the matches with only the second and the third group within each match
subbed_urls = urlpattern.sub(r'\2\3',urls)
print("The subbed_urls are: ")
print(subbed_urls)

# there are other methods within the re package besides the finditer

# the findall, which will return a list of strings if there are one or no groups
# it will return a list of tuples if there are more than one groups within the regular expression
name = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
name_matches = name.findall(text_to_search)
print()
print(r"names matches: ")
for name_match in name_matches:
    print(name_match)
print()


# the search method
# the method return the first match of that pattern within the string
sentence = "Start a sentence and then bring it to an end"
pattern = re.compile(r'bring')
matches = pattern.search(sentence)
print("the first appearance of bring in sentence is:")
print(matches)
print()

##### flags #######
sentence = "Start a sentence and then bring it to an end"
pattern = re.compile(r'start',re.IGNORECASE)
# you can also write pattern = re.compile(r'[Ss][Tt][Aa][Rr][Tt]')
matches = pattern.search(sentence)
print("the first appearance of start(ignore case) in sentence is:")
print(matches)