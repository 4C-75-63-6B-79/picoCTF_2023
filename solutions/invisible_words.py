import os

img_file = open('./solutions/output.bmp', 'rb');

for i in img_file.read():
    print(chr(i));
