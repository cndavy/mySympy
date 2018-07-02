import base64

a='\\u751F\\u5316\\u5371\\u673A'
b=['\\u751F\\u5316\\u5371\\u673A']
print (a.encode('utf-8'),b[0].encode('utf-8'))
print (a.encode('utf-8').decode('unicode_escape'))
print (b[0].encode('utf-8').decode('unicode_escape'))
c=0x44
print(chr(c+2))
print(ord('a'))
print (u'aaa'.encode('gbk') ==  'aaa'.encode('utf8'))
print ( "abcder" [-1:0:-1])

a = 'aabbccddeeff'
import  struct
a_bytes=bytes.fromhex(a)
#a_bytes = a.decode('hex')
print(a_bytes)
aa = a_bytes.hex()
print (aa)
bytes.hex(b"\x22")
import binascii
print(   (binascii.hexlify(b'\x12\x34\x56\x78')).hex() )

print (bytes.fromhex("31313131").decode('ascii'))

print (base64.b64encode(b'\x12\x34\x56\x78'))
print ((base64.b64encode('喊喊'.encode('gbk'))))
print ((base64.b64encode('喊喊'.encode('utf'))))
print ((base64.b32encode('喊喊'.encode('utf'))))

print (base64.b64decode(base64.b64encode(b'12345678')))