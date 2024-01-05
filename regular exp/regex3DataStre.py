import re
data = '''We went to Taco Bell. I didn't even know it was a date!! 
        We were friends and unaware we both had crushes on each other. 
        He ordered 20 tacos for us to share,20/03/2022 and I knew I wanted to be together.'''
val=re.search('[0-9].{2}[0-9].{2}[0-9}.{4}',data)
print(val)