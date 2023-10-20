import requests

res2=requests.post("https://akpufey.iot.gz.baidubce.com/pub?topic=AAA&qos=0",
headers={"Accept":"application/json","Content-Type": "application/octet-stream","token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJJT1RfQVVUSCIsImNvbnRleHQiOiJ7XCJsaWZlU3BhbkluU2VjXCI6MzAwMCxcImF1dG9SZWZyZXNoXCI6dHJ1ZSxcImlvdENvcmVJZFwiOlwiYWtwdWZleVwiLFwiY2FsbGVySWRcIjpcImtvbmd6aGkwMDFcIixcImNhbGxlckluZm9cIjpcImV5SWtaM0p2ZFhCTFpYa2lPaUpyYjI1bmVtaHBNREF4SWl3aUpHOWlhbFI1Y0dVaU9pSjBlWEUwYldJNGJ5SjlcIn0iLCJpbmRleCI6NywiZXhwIjoxNjk3MzAwMjMzfQ.5trTokQmEkCTJvJy7SvydYA-mlW27wg_RD2ebGXKg1o"},
       
)


print(res2.status_code)
print(res2.text)