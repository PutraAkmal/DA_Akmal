import requests
url = 'http://172.17.50.43/hr2'
r = requests.get(url)

print('Status code:OK')
print(r.status_code)
print('******')
h = requests.head(url)
for line in  h.headers:
    print(line,":",h.headers[line])
print('******')

url2 = 'http://172.17.50.43/headers.php'
fake_headers = {
    'User-Agent': 'Mobile'
}
r2 = requests.get(url2, headers = fake_headers)
print(r2.text)
