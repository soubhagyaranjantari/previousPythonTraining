import re

txt = "The rain in Spain"

# Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-z]+ [A-Z]+", txt)
print(x)
