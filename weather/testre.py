import re
'''
pattern = re.compile(r'(Agent \w)(\w*)')
text = "Agent Alice told Agent Carol that Agent Eve kewn Agent Boobie is a double Agent."
result = pattern.sub(r'\1****',text)
print(result)
'''
def fun(soustr,desstr=''):
     if desstr=='':
         pattern = re.compile(r'^\s*|\s*$')
         print(1)
     else:
         pattern = re.compile(desstr)
         print(desstr)
     soustr = pattern.sub('', soustr)
     return soustr
result = fun('xielinee','e')
print('==='+ result + '===')