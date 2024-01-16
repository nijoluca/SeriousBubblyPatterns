def SearchString(string,e):
  if e.lower() in (string.lower()):
    pos=string.find(e.lower())
    return pos+1
  else:
    return -1


string="Hello world"
e="O"

output=SearchString(string,e)
if output == -1:
  print(f'string {e} NOT FOUND')
else:
  print(f'The string is found at position {output}')