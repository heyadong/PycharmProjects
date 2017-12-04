"""class Student():
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError('vlaue must be str')  # rasie
student = Student()
student.name = 123"""
import requests
import re
response = requests.get('http://blog.leanote.com/qq-alan')
print(response.status_code)
html = response.text
print(html)
#m = re.findall(r'title="全文">(.*?)</a>', html)
#m = re.findall(r'title="全文">(.*)</a>', html, re.S)
#m = re.findall(r'title="全文">(.*?)</a>', html)
m = re.findall(r'<div class="title">.*?title="全文">(.*?)</a>', html, re.S)
for t in m:
    print(t)

