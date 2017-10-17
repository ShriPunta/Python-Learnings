import re
pattern = re.compile('^(?:https?:\/\/)?(?:[^@\/\n]+@)?(?:www\.)?(?P<dom>[^:\/\n]+)')
print (pattern)
url = "https://regex101.com/r/wN6cZ7/63"
matc = pattern.match(url)
if matc is not None:
    dom = matc.groupdict()['dom']
    print('Dom',dom)

print(url[:-4])