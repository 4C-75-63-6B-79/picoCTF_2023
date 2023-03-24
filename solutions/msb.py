# All the things commented out below the code represent my failed attempt to solve the problem
# So I have Commented that stuff out so people can focus on the problem.

# --------------------------------------------------------------------------------------------

# I am import Image from pillow module. You need to have pillow module installed to run this program.
from PIL import Image;

# Opening the image given in the problem. Make sure to change the path of the image if there is error.
try:
    scrambled_img = Image.open('solutions\img.png');
except:
    print('Please make sure you have the program in the solution folder and the image is also present in the solution folder.')

# opening a file to write the message which is stored in the MSB of the image.
try:
    text_file = open('./solutions/message.txt', 'w');
except: 
    print('Please make sure you have program in the solutions folder else change the path of text file in the program')

# storing the height and width of the image.
width, height = scrambled_img.size; 

# variable that store the MSB bits of the color of the each pixel
bits = [];

# we have this try block since when the stego in the image ends it throws error so to make sure that he program solve nicely.
try:
    for y in range(height): # looping on the first row of the pixel
        for x in range(width): # looping the each pixel in each row
            r, g, b = scrambled_img.getpixel((x, y));  # storing the rgb values of the each pixel
            # converting the r int value to a 8 bit binary number and then storing the msb in the bits array
            # r  = 253 then "{:08b}".format(r) = 11111101 and then we are taking the character at the first index of this string and appending it into bits array
            bits.append("{:08b}".format(r)[0]) 
            bits.append("{:08b}".format(g)[0])
            bits.append("{:08b}".format(b)[0])

            if(len(bits) > 8):  # checking if the length of the bits array is more than 8
                val = "".join(bits[0:8]);  # storing the first 8 elements of the bits array and converting them into string
                text_file.write(chr(int(val, 2))); # then converting the binary to its ascii value and then storing it in the text file
                del bits[0:8]; # then removing those 8 bits from the array to make sure that the program is not slwo.

except:
    print("Error has occured and this marks the end of stego");
    text_file.close();



# ---------------------------------------------------------------------------------------


# from PIL import Image;

# def flipBit(val):
#     if(val > 128):
#         return val // 2;
#     return val * 2

# def getMSB(val):
#     return bin(val)[2:4];

# scrambled_img = Image.open('solutions\img.png');


# width, height = scrambled_img.size; 

# # print(height, width); # 1500 1074

# text = [];
# bits = [];
# rgb_values = [];

# text_file = open('./solutions/message.txt', 'w');

# try:
#     for y in range(height):
#         for x in range(width):
#             r, g, b = scrambled_img.getpixel((x, y));
#             bits.append("{:08b}".format(r)[0])
#             bits.append("{:08b}".format(g)[0])
#             bits.append("{:08b}".format(b)[0])

#             if(len(bits) > 8):
#                 val = "".join(bits[0:8]);
#                 # print(chr(int(val, 2)), end="")
#                 text_file.write(chr(int(val, 2)));
#                 del bits[0:8];
#         # text_file.write('\n');
# except:
#     print("Error has occured and this marks the end of stego");
#     text_file.close();
# # print(len(bits));


