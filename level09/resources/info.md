# First Search

```
$ ls -la
-rwsr-sr-x 1 flag09  level09 7640 Mar  5  2016 level09
----r--r-- 1 flag09  level09   26 Mar  5  2016 token

$ ./level09 
You need to provied only one arg.

$ cat token
f4kmm6p|=�p�n��DB�Du{��

./level09 token
tpmhr

./level09 $(cat token)
f5mpq;v�E��{�{��TS�W�����

./level09 111
123

./level09 aaa
abc
```

we can think that the token has been encoded by the executable

# Solution 

we make a program (here in python) to decode the token

```
import sys

if __name__=="__main__":
	res = ''
	for i, c in enumerate(sys.argv[1].encode("utf-8", errors="surrogateescape")):
		res += chr(c - i)
	print(res)
```

so

```
$ python decode.py $(cat token)
f3iji1ju5yuevaus41q1afiuq

$ su flag09
Password: 
Don't forget to launch getflag !
