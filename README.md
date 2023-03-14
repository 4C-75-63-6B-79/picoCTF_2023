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
<summary>Template</summary>

### Description


### Steps taken to solve the problem.
- content
</details>


