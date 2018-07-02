import hashlib
import  struct
import binascii

import sys


for i in range (999999):
    md5=hashlib.md5
    sha1=hashlib.sha1
    a = str(i).encode("utf8")
    print(str(i),end="|")
    print(md5(a).hexdigest(),end='|')
    print(md5(md5(a).hexdigest().encode("utf8")).hexdigest(),end='|')
    print(sha1(a).hexdigest())
