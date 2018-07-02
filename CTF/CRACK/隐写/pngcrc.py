import binascii
import struct

'''
恢复 png 文件的尺寸
域的名称
字节数
说明
Width	4 bytes	图像宽度，以像素为单位
Height	4 bytes	图像高度，以像素为单位
Bit depth	1 byte	图像深度： 
            索引彩色图像：1，2，4或8 
            灰度图像：1，2，4，8或16 
            真彩色图像：8或16
ColorType	1 byte	颜色类型：
            0：灰度图像, 1，2，4，8或16 
            2：真彩色图像，8或16 
            3：索引彩色图像，1，2，4或8 
            4：带α通道数据的灰度图像，8或16 
            6：带α通道数据的真彩色图像，8或16
Compression method	1 byte	压缩方法(LZ77派生算法)
Filter method	1 byte	滤波器方法
Interlace method	1 byte	隔行扫描方法：
            0：非隔行扫描 
            1： Adam7(由Adam M. Costello开发的7遍隔行扫描方法)
'''
filename=u'D:\git\mySympy\CTF\CRACK\隐写\demo.png'
f = open(filename , "rb+")
f.seek(12)
data=f.read(21)
f.close()
crc=(data[17:21])#b'\xf4x\xd4\xfa'
for j in range(1,2000):
    w = struct.pack(">i", j)
    for i in range(1,2000):
        h=struct.pack(">i",i)
        #h=binascii.hexlify(h)
        #data="4948445200000200"+str(h,"utf8")+"0806000000"
        data1 = data[:4]+w+h+data[12:17]
        crc32=binascii.crc32(data1) &0xffffffff
        if crc32 == int.from_bytes(crc,'big'):
            print(binascii.hexlify(w))
            print (binascii.hexlify(h))
            f = open(filename, "rb+")
            f.seek(16)
            f.write(w)
            f.write(h)
            f.flush()
            f.close()

