# atbash cipher thing

# def makePlainText():
#     plain_text = "";
#     for i in range(97,123):
#         plain_text += chr(i);
#     return plain_text;

# plain_text = [ch for ch in makePlainText()];
# cipher_text = [plain_text[-i] for i in range(1, len(plain_text)+1)];

# encrypt_key = dict(zip(plain_text, cipher_text));

# flag = 'CDEFGHIJSTUVWXYZcdefghijstuvwxyz'
# decrypted_flag = "";

# for flag_c in flag:
#     enc_c = encrypt_key[flag_c.lower()];
#     if(flag_c.isupper()):
#         decrypted_flag += enc_c.upper();
#     else:
#         decrypted_flag += enc_c;

# print(decrypted_flag);

# from PIL import Image;

# atbash_image = Image.open('./solutions/atbash.jpg')

# width, height = atbash_image.size; # 465, 455

# for y in range(200):
#     for x in range(width):
#         print(atbash_image.getpixel((x, y)));


text = 'CDEFGHIJSTUVWXYZcdefghijstuvwxyz'

alphabet = 'abcdefghijklmnopqrstuvwxyz';

decryptedText = '';
 
for char in text:
    # isUpper = char.isupper;
    index = alphabet.find(char.lower());
    replacemnt = alphabet[-(index+1)];
    if(char.isupper()):
        replacemnt = replacemnt.upper();
    decryptedText += replacemnt;
print(decryptedText);