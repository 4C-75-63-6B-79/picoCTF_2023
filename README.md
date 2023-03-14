# picoCTF_comp_2023

## Solved
--------------------------------------------------------------------------------------------------------
<details>
<summary>chrono</summary>

### Description
How to automate tasks to run at intervals on linux servers?
Use ssh to connect to this server:
Server: saturn.picoctf.net
Port: 57690
Username: picoplayer 
Password: RmhP1XBDEg

### Steps taken to solve the problem.
- I had to first figure out how to ssh to a server. ssh user@address -p port and then enter the password.
- After that I ls the folder had nothing then I went back that means did cd .. 2 times.
- Then did ls and saw a folder challenge cd into it. Did ls in it. It had metadata.json file.
- I cat it and it had the flag.
- flag: picoCTF{Sch3DUL7NG_T45K3_L1NUX_dbc85700}.
</details>

--------------------------------------------------------------------------------------------------------
<details>
<summary>repetitions</summary>

### Description
Can you make sense of this file?
Download the file [here](https://artifacts.picoctf.net/c/297/enc_flag).

### Steps taken to solve the problem.
- Wget the file on the web shell.
- Cat the file. I had equal to at the end. So may be base64  encoded file.
- Base64 decode it ```cat enc_flag | base64 -d```. The output again had equal to at the end. So may be base64 decode again.
- Output again looked like base64 encoded. So base64 decode again.
- Had to base64 decode a couple more times to get the flag. ```cat enc_flag | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d```
- flag: picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_c0ac1752}
</details>

--------------------------------------------------------------------------------------------------------
<details>
<summary>PcapPoisoning</summary>

### Description
How about some hide and seek heh?
Download this [file](https://artifacts.picoctf.net/c/404/trace.pcap) and find the flag.

### Steps taken to solve the problem.
- Downloaded the file and opened it in the wireshark.
- Looked at various row thing by clicking on them most of them had same text of gcv2 something something.
- Scrolled down to find the black things. First black thing had the flag.
- flag: picoCTF{P64P_4N4L7S1S_SU55355FUL_dd89e21b}
- I need to learn how to use wireshark and what all the information means.
</details>

--------------------------------------------------------------------------------------------------------
<details>
<summary>hideme</summary>

### Description
Every file gets a flag.
The SOC analyst saw one image been sent back and forth between two people. They decided to investigate and found out that there was more than what meets the eye [here](https://artifacts.picoctf.net/c/493/flag.png).

### Steps taken to solve the problem.
- Downloaded the file it is simply png file with logo of picoctf.
- Size is also small.
- Went to [wikipedia article](https://en.wikipedia.org/wiki/PNG). To find the bits which I can change to increase the width and height of the image. Did that couple of time no success.
- Looked at the end of the file in the hexeditor. Found some secret file things at the end thought to do unzip on this.
- Wget into the webshell. Unzip got a new folder secret.
- Folder had another flag.png file. Tried to unzip it got error. 
- So wget the file on my machine. Then unzip it.
- Found the flag file in the secret folder. I had the flag.
- flag: picoCTF{Hiddinng_An_imag3_within_@n_ima9e_5cf64968}
</details>

--------------------------------------------------------------------------------------------------------
<details>
<summary>rotation</summary>

### Description
You will find the flag after decrypting this file
Download the encrypted flag [here](https://artifacts.picoctf.net/c/451/encrypted.txt).

### Steps taken to solve the problem.
- Wget the file in the webshell. It is a txt file.
- Cat the contents of the file. Lookes like a ceaser cipher of the flag.
- Copied the encrypted flag. ```xqkwKBN{z0bib1wv_l3kzgxb3l_7mkl1k61}```.
- Made [this](/solutions/rotation.py) program to get all the ciphers.
- Run the program and enter the encrypted flag. You will get all the cipher for the 26 keys. See which is in the picoCTF format.
- Mine was with key 18.
- flag: picoCTF{r0tat1on_d3crypt3d_7ecd1c61}
</details>

--------------------------------------------------------------------------------------------------------
<details>
<summary>Reverse</summary>

### Description
Try reversing this file? Can ya?
I forgot the password to this [file](https://artifacts.picoctf.net/c/369/ret). Please find it for me?

### Steps taken to solve the problem.
- Wget the file in the webshell. It is a elf file. Not my strong point.
- Opened the file in the nano. The flag was there in plain text.
- flag: picoCTF{3lf_r3v3r5ing_succe55ful_fe733618}
- This was straight up luck to find the flag. I don't know how to reverse the elf file.
</details>

--------------------------------------------------------------------------------------------------------
<details>
<summary>Rules 2023</summary>

### Description
Read the rules of the competition and get a little bonus!
[Rules](https://picoctf.org/competitions/2023-spring-rules.html)

### Steps taken to solve the problem.
- Wget the file in webshell. It is a HTML file
- Opened in nano. Scrolled through the file. Found the flag in plain text format in the **alt** attribute of the element **img**.
- flag: picoCTF{h34rd_und3r5700d_4ck_cba1c711}
</details>

--------------------------------------------------------------------------------------------------------
<details>
<summary>Safe Opener 2</summary>

### Description
What can you do with this file?
I forgot the key to my safe but this [file](https://artifacts.picoctf.net/c/318/SafeOpener.class) is supposed to help me with retrieving the lost key. Can you help me unlock my safe?

### Steps taken to solve the problem.
- Wget the file in the webshell. File .class file. 
- Ran the file using ``` java SafeOpener```. Prompts to enter the password of the safe. Enter password.
- Give a string which looks base64 encoded and also a warning that we have 2 attempts left.
- Enter password 2 more times. Gave the same string value each time. "cGFzc3dvcmQ="
- Base64 decode this string to get password.
- The program base64 encodeds the entered password and then prints it out.
- Opened the file in the nano. The flag was there in plain text.
- flag: picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_d6afee27}
</details>

--------------------------------------------------------------------------------------------------------
<details>
<summary>ReadMyCert</summary>

### Description
How about we take you on an adventure on exploring certificate signing requests
Take a look at this CSR file [here](https://artifacts.picoctf.net/c/383/readmycert.csr).

### Steps taken to solve the problem.
- Wget the file on the webshell. 
- Cat the file and see the file has text which may be base64 encoded.
- Use this [online base64](https://www.base64decode.org/) decoder and find the flag format string.
- flag: picoCTF{read_mycert_7834c5f2}
</details>


--------------------------------------------------------------------------------------------------------
<details>
<summary>timer</summary>

### Description
You will find the flag after analysing this apk
Download [here](https://artifacts.picoctf.net/c/421/timer.apk).
**Hint-1** Decompile
**Hint-2** mobsf or jadx 

### Steps taken to solve the problem.
- Wget the file in the webshell. The file is apk file.
- Opened the apk file in nano and saw a lot of gibberish.
- Strings the file and piped it into grep to find the picoCTF. No success.
- Installed the apk file on my phone. It is a normal timer with no stop button and no success.
- Looked at the hint.
- Had android studio installed on the pc. Opened the apk file in the android studio using option File > Profile or Debug APK.
- The flag was in the manifests > AndroidManifest.xml file on line 5.
- flag: picoCTF{t1m3r_r3v3rs3d_succ355fully_17496}.
</details>

--------------------------------------------------------------------------------------------------------
<details>
<summary>Virtual Machine 0</summary>

### Description
Can you crack this black box?
We grabbed this design doc from enemy servers: [Download](https://artifacts.picoctf.net/c/472/Virtual-Machine-0.zip). We know that the rotation of the red axle is input and the rotation of the blue axle is output. The following input gives the flag as output: [Download](https://artifacts.picoctf.net/c/472/input.txt).
**Hint** Rotating the axle that number of times is obviously not feasible. Can you model the mathematical relationship between red and blue?

### Steps taken to solve the problem.
- Wget both the files in the webshell. One file is a txt file and other is a zip file.
- Input file had this string of number 39722847074734820757600524178581224432297292490103995919748682209850899737
- Unzip the zip file gave a .dae file. Don't know what it is.
- Opened the file in nano in hope to find the flag in plain text. No success.
- Saw a term Collada in the file. Googled what is collada. Helps people to share and edit 3d files.
- Googled how to open collada file. It showed we can open it in Blender. Had it on my pc.
- Downloaded the file on my pc.
- Imported the file in blender. Something like a lego thing.
- Grabbed all the black legos and the base and moved them along the z axis to find some gears in there.
- There are 8 teeth on the gear splined with the blue axle.
- The big gear splined with the red axle has 40 teeth.
- Problem mentions that input of the red axle is input and the output is at the blue axle.
- So if we rotate red axle one the the blue axle will rotate 5 times.
- So if we rotate the red axle the input number of times the blue axle will rotate 5 * input. 
- Input * 5 = 198614235373674103788002620892906122161486462450519979598743411049254498685
- Looked at the hint, which said to have a mathematical relationship between read and blue which is red 1 turn equals blue 5 turns.
- Now we take the output value and convert then into hex using ``` hex(198614235373674103788002620892906122161486462450519979598743411049254498685) ```. 
- We get 0x7069636f4354467b67333472355f30665f6d3072335f36313730613162317d. Which has the hex value of the pico which is 7069636f. I thought this step to convert into hex because I did the problems previously related to RSA and there we converted the number to hex.
- Now to get the plain text we can do is import binascii and then do ``` binascii.unhexlify('7069636f4354467b67333472355f30665f6d3072335f36313730613162317d') ```.
- And we get the flag.
- flag: picoCTF{g34r5_0f_m0r3_6170a1b1}
</details>

--------------------------------------------------------------------------------------------------------
<details>
<summary>Template</summary>

### Description


### Steps taken to solve the problem.
- content
</details>


