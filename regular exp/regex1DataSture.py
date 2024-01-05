import re
data='Soubhagya Ranajan Tarai'
val=(re.search('Soubh[a-z]gy[a-z]',data))
if val!=None:
    print('Pattern found')
else:
    print('Pattern not found')
