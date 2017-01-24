import os, zipfile, time

'''
Hint: If you get stuck, go one step back.

in 0723.zip
	git log
	git checkout 93d630215b9c5c49f2c7f3c6b9fe1b55efd93cd1

in 0397.zip
	git log
	git checkout 27dbde667908b19d59eb6d8e3ed8802ebf34ab9b

in 0046.zip
	git log
	will found zip password


in 0001.zip
	git status
	git checkout egg12.png
'''

i = 1000
while i > 0:
	with zipfile.ZipFile(format(i, "04d")+'.zip', "r") as z:
		z.extractall(".")
	os.system("rmdir .git /s /q")
	time.sleep(0.1)
	os.system("move ./"+format(i, "04d")+"/.git .")
	time.sleep(0.1)
	os.system("rmdir "+format(i, "04d")+" /s /q")
	if i == 911:
		i = i-1
	os.system("git checkout "+format(i-1, "04d")+".zip")
	time.sleep(0.1)
	i = i-1