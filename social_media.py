import re

file = open('social_media_users.csv')

#for line in file:
#   line = line.rstrip()
#   ir.research('.+@', line):
#       print(line)

file_as_text = open('social_media_users.csv').read()
emails = re.findall('[a-z]+[0-9]+@yahoo\.com', file_as_text)
print(emails)
print(len(emails))