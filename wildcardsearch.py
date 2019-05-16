import re
regex = re.compile('t.')
l = ['this', 'is', 'just', 'a', 'test','thos','thus','isad','isu','thailand','thinanus']
matches = [string for string in l if re.match(regex, string)]

print(matches)