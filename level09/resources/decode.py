import sys

if __name__=="__main__":
	res = ''
	for i, c in enumerate(sys.argv[1].encode("utf-8", errors="surrogateescape")):
		res += chr(c - i)
	print(res)