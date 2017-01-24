'''
https://backdoor.sdslabs.co/challenges/2013-MISC-75
'''

import re
import httplib
import urllib, urllib2, cookielib

def find_sum_of_first_N_prime_numbers(N):
	sum = 0
	n = 0
	num = 1
	while n < N:
		# prime numbers are greater than 1
		if num > 1:
			for i in range(2,num):
				if (num % i) == 0:
					break
			else:
				sum += num
				n = n+1
		num = num+1
	return sum

conn = httplib.HTTPConnection("hack.bckdr.in")
response = conn.request("GET", 'http://hack.bckdr.in/2013-MISC-75/misc75.php')
response = conn.getresponse()
text = response.read()
num_in_page = [int(s) for s in text.split() if s.isdigit()]
N = num_in_page[1]
sum = find_sum_of_first_N_prime_numbers(N)

headers = response.getheaders()
cookie = headers[2][1]

headers = {"Content-type": "application/x-www-form-urlencoded"
			, "Cookie": cookie
			, "Host": "hack.bckdr.in"
			, "Connection" : "keep-alive"
			, "Cache-Control" : "max-age=0"
			, "Origin": "http://hack.bckdr.in"
			, "Referer": "http://hack.bckdr.in/2013-MISC-75/misc75.php"
			, "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36"}

params = urllib.urlencode({'answer': sum, 'submit': 'Submit'})

response = conn.request("POST", 'http://hack.bckdr.in/2013-MISC-75/misc75.php', params, headers)
response = conn.getresponse()
print(response.read())