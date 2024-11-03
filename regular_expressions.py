import re

file_object = open("regular_expression.py")

text_from_file = file_object.read()
# print(text_from_files)

emails = re.findall('[a-z]+@gmail\.com',text_from_file)
print(emails)

are_emails = re.search('[a-z]+@gmail\.com',text_from_file)
# print