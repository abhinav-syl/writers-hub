import requests
import json


data = requests.get('http://127.0.0.1:8000/store/api/articles')
data = data.json()[0]
print(data)

html = '''<html>
<head>
<title>''' + data['Title'] + '''
</title>
</head>
<body> ''' + data['para'] + '''
</body>
</html>
'''

f = open(data['Heading'] + '.html', "w")
f.write(html)
f.close()

