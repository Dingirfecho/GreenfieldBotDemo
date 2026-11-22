import json
data=open('data.json').read()
html=open('template.html').read().replace('__DATA__',data)
open('index.html','w').write(html)
