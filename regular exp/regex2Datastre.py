import re
data="Soubhagya12345# @Ranjan !Tarai"
val=re.findall('[A-Z]+',data)#it will show all upper character
val=re.findall('[a-z]+',data)#it will show all lower character
val=re.findall('\d+',data)#it will show all Number character
val=re.findall('\D+',data)#it will show all the chr whitout Number
val=re.findall('[^@#!]+',data)#it will remove the character what we mentioned
val=re.findall('\w+',data)#it will return white speace whitout special character
val=re.findall('\W+',data)#it will return white speace with special character
val=re.findall('\s+',data)#it will return only white speace
val=re.findall('\S+',data)#it will return white speace character
print(val)