import binascii
import struct

'''


'''
filename=u'D:\git\mySympy\CTF\CRACK\隐写\demo.png'
f = open(filename , "rb+")
f.seek(12)
data=f.read(21)
f.close()
crc=(data[17:21])#b'\xf4x\xd4\xfa'
for i in range(512,65535):
    h=struct.pack(">i",i)
    #h=binascii.hexlify(h)
    #data="4948445200000200"+str(h,"utf8")+"0806000000"
    data1 = data[:8]+h+data[12:17]
    crc32=binascii.crc32(data1) &0xffffffff
    if crc32 == int.from_bytes(crc,'big'):

        print (binascii.hexlify(h))
        f = open(filename, "rb+")
        f.seek(20)
        f.write(h)
        f.flush()
        f.close()

