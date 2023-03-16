# picoCTF_comp_2023

--------------------------------------------------------------------------------------------------------
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
<summary>FindAndOpen</summary>

### Description
Someone might have hidden the password in the trace file.
Find the key to unlock [this file](https://artifacts.picoctf.net/c/411/flag.zip). [This tracefile](https://artifacts.picoctf.net/c/411/dump.pcap) might be good to analyze.

### Steps taken to solve the problem.
- Wget both the files in the webshell. One is a txt file and other is pcap file.
- The zip file is password protected. So we might need to find the password from the pcap file to get the flag.
- Opened the pacp file in the wireshark.
- On looking at the row we se the first few have text "Flying on Ethernet secret: Is this the flag."
- The some had text "Could the flag have been splitted?"
- Some had gibberish looking text.
- Then again it came with text "May be try checking the other file".
- The various text we saw in the various bytes are here.
- Flying on Ethernet secret: Is this the flag
- iBwaWNvQ1RGe1Could the flag have been splitted?
- AABBHHPJGTFRLKVGhpcyBpcyB0aGUgc2VjcmV0OiBwaWNvQ1RGe1IzNERJTkdfTE9LZF8=
- PBwaWUvQ1RGesabababkjaASKBKSBACVVAVSDDSSSSDSKJBJS
- PBwaWUvQ1RGe1Maybe try checking the other file
- Now I used a [online base64 decoder](https://www.base64decode.org/).
- Using the combination of last plus the first and the second we get this string "<YKƲmk^rH^^z picoCTF{PWmjZz{)+my�<This is the secret: picoCTF{R34DING_LOKd_"
- picoCTF{R34DING_LOKd_ is used this as the secret password to unzip the flag file on my pc.
- After unzip we got a flag file. I opened the flag file in the notepad. Got the flag.
- flag: picoCTF{R34DING_LOKd_fil56_succ3ss_8ec01288}
</details>

--------------------------------------------------------------------------------------------------------
<details>
<summary>MatchTheRegex</summary>

### Description
How about trying to match a regular expression
Additional details will be available after launching your challenge [instance](http://saturn.picoctf.net:59685/).

### Steps taken to solve the problem.
- Started the instance and opened the website.
- Opened the developer tools and looked at the elements. I was trying to look if there was some kind of regular expression used in script.
- I saw that there was a comment in the script // ^p.....F!?. I saw the caret sign thought that the input should be begin with the p and enterd picoCTF and got the flag. One can also enter paaaAAF to get the flag but I am not sure about this.
- flag: picoCTF{succ3ssfully_matchtheregex_36f43841}
</details>

--------------------------------------------------------------------------------------------------------
<details>
<summary>who is it</summary>

### Description
Someone just sent you an email claiming to be Google's co-founder Larry Page but you suspect a scam.
Can you help us identify whose mail server the email actually originated from?
Download the email file [here](https://artifacts.picoctf.net/c/363/email-export.eml). Flag: picoCTF{FirstnameLastname}
**Hint** whois can be helpful on IP addresses also, not only domain names

### Steps taken to solve the problem.
- Wget the file in the webshell. The file is .eml file.
- Opened the file saw some sender receive things.
- Looked at the hint.
- [whois](https://who.is/) is a site.
- Google whois ip address look up. Found this [whois site](https://www.whatismyip.com/ip-whois-lookup/).
- Opened the file in nano in webshell. Found a ipaddress 173.249.33.206.
- Pasted in the search box of the website and got a long thing. Looked for name and found "Wilhelm Zwalina".
- flag: picoCTF{WilhelmZwalina}
</details>

--------------------------------------------------------------------------------------------------------
<details>
<summary>two-sum</summary>

### Description
Can you solve this?
What two positive numbers can make this possible: n1 > n1 + n2 OR n2 > n1 + n2
Enter them here nc saturn.picoctf.net 49225. [Source](https://artifacts.picoctf.net/c/252/flag.c)

### Steps taken to solve the problem.
- Nc into the server. Entered any random number nothing happened.
- Wget the source file in the webshell and opened it inside of nano.
- Looked into the flag.c file. Saw if there is a function addIntOvf which if returns 0 then the program will exit. So some how i have to enter 2 numbers such that both of them are either positive or negative but their sum is of opposite sign.
- This is something like in java if we try to hold a value which is larger than what int data type can hold it will become negative something like that I studied in a book but don't remember it. 
- Google what is integer overflow. Read the [wikipedia article](https://en.wikipedia.org/wiki/Integer_overflow).
- Google what is the size of integer in c language. It is 2 bytes or 16 bits.
- Googled largest number integer in c language can hold. 2147483647
- Ran the program with gcc flag.c then ./a.out. Entered the 2147483647 1 numbers
- Got you have an integer overflow. Flag not found please run this on server.
- By this time the instance was shut down. So again started it.
- But when I entered the above mentioned numbers nothing was happening. I don't know what to do.
- Then at later time the thing was working correctly entered the above numbers got the flag.
- flag: picoCTF{Tw0_Sum_Integer_Bu773R_0v3rfl0w_fe14e9e9}
</details>

--------------------------------------------------------------------------------------------------------
## Unsolved

--------------------------------------------------------------------------------------------------------
<details>
<summary>HideToSee</summary>

### Description
How about some hide and seek heh?
Look at this image [here](https://artifacts.picoctf.net/c/507/atbash.jpg).
**Hint** Download the image and try to extract it.

### Steps taken to solve the problem.
- Wget the file on the webshell
- The file is a jpg and has some cipher on it.
- Opened the file in on line hexedit. Had JFIF format on the start.
- Went to the JFIF file format on google. Opened the [wikipedia article](https://en.wikipedia.org/wiki/JPEG_File_Interchange_Format#:~:text=The%20JPEG%20File%20Interchange%20Format,encoded%20with%20the%20JPEG%20algorithm.). Did not understand much.
- Opened the file in the notepad to see if there is any string so that I can decode it using the ceaser cipher.
- strings the file in webshell ```strings atbash.jpg```. Got this long string "CDEFGHIJSTUVWXYZcdefghijstuvwxyz". Did ceaser cipher on the thing with no luck.
- Looked at the hint. Suggest to extract it. Did ``` unzip atbash.jpg ``` got an error.
- Googled the atbash term. Found this [wikipedia article](https://en.wikipedia.org/wiki/Atbash#:~:text=Atbash%20(Hebrew%3A%20%D7%90%D7%AA%D7%91%D7%A9%3B%20also,with%20a%20standard%20collating%20order.).
- Tried to decipher the string mentioned above using the cipher in the wikipedia article. No success.
- Again looked at the file format and checked for any error but everything is fine.
</details>


--------------------------------------------------------------------------------------------------------
<details>
<summary>money-ware</summary>

### Description
Flag format: picoCTF{Malwarename}
The first letter of the malware name should be capitalized and the rest lowercase.
Your friend just got hacked and has been asked to pay some bitcoins to 1Mz7153HMuxXTuR2R1t78mGSdzaAtNbBWX. He doesn’t seem to understand what is going on and asks you for advice. Can you identify what malware he’s being a victim of?
**Hint-1** Some crypto-currencies abuse databases exist; check them out!
**Hint-2** Maybe Google might help.

### Steps taken to solve the problem.
- Googled the string to which the bitcoins are supposed to be payed.
- Found articles on petya attack.
- Google the name of the malware no success.
</details>

--------------------------------------------------------------------------------------------------------
<details>
<summary>MSB</summary>

### Description
This image passes LSB statistical analysis, but we can't help but think there must be something to the visual artifacts present in this image...
Download the image [here](https://artifacts.picoctf.net/c/418/Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png)
**Hint** What's causing the 'corruption' of the image?

### Steps taken to solve the problem.
- Downloaded the image. Looked at it. The upper portion not good but lower portion good.
- Googled MSB which is most significant bit and LSB least significant bit.
- Looked at the hint. 
- I think since in problem it is mentioned that the image passed the LSB test. May be the image is corrupted due to some things done to its Most Significant Bit. Like a Bit flip thing.
- Tried to do the bitflip of the MSB and obtained a image but was not useful.
- Googled about MSB stegnography found this [article](http://ijcst.com/vol33/4/anil2.pdf).
- So if we go through all the pixels of the image and the find the MSB of all the pixels. Then we can convert that binary value to ascii which might be our flag.
- Failed at the above solution and got a bunch of gibberish.
- Googled how to do LSB stegnography on an image. To understand what has been done to image.
</details>

--------------------------------------------------------------------------------------------------------
<details>
<summary>Permissions</summary>

### Description
Can you read files in the root file?
The system admin has provisioned an account for you on the main server:
ssh -p 62831 picoplayer@saturn.picoctf.net
Password: cPC09LVcyM
Can you login and read the root file?
**Hint** What permissions do you have?
### Steps taken to solve the problem.
- Copied the ssh command on webshell but did not get the password prompt.
- Pasted the password anyways nothing happened.
- Ended the session.
- Tried changing the port and then ssh. Gave an error. 
- Again ssh tried typing in whoami, pwd ls commands nothing happened.
- Looked at the hint.
</details>

--------------------------------------------------------------------------------------------------------
<details>
<summary>SOAP</summary>

### Description
The web project was rushed and no security assessment was done. Can you read the /etc/passwd file?
Web Portal
**Hint** XML external entity Injection
### Steps taken to solve the problem.
- Opened the website. Used the inspect element thing nothing there.
- Tried to nc the website nothing there too.
- Tried to wget the website, it got stuck at connecting the sever.
- Looked at the hint. Google the hint.
- 
</details>

--------------------------------------------------------------------------------------------------------
<details>
<summary>findme</summary>

### Description
Help us test the form by submiting the username as test and password as test!
The website running [here](http://saturn.picoctf.net:61202/).
**Hint** any redirections?

### Steps taken to solve the problem.
- Started the instance and opened the website.
- Login the webiste with the given credentials.
- A page opened with search for flag search element.
- Opened the developer tools and went straight to the cookies thing.
- Nothing was there.
- Looked at the sources. Nothing there.
- Searched for flag in the thing nothing there too.
- Looked at the hint. Did not understand anything.
- The text in the website is similar to the hint. Text is "I was redirected here by a friend of mine but i couldnt find anything. Help me search for flags :-)".
- Looked at what is happeneing when we press the go button. The text in updates and some elements style are changed.
- Tried to wget the thing but it was stuck at the connecting. I know that this might be wrong as I really don't know what is wget. I only know that wget is used to download the files.
- 
</details>  

--------------------------------------------------------------------------------------------------------
<details>
<summary>useless</summary>

### Description
There's an interesting script in the user's home directory
The work computer is running SSH. We've been given a script which performs some basic calculations, explore the script and find a flag.
Hostname: saturn.picoctf.net
Port:     54200
Username: picoplayer
Password: password

### Steps taken to solve the problem.
- content
</details>



-----------------------------------------------------------------------------------------------------
<details>
<summary>Invisible Words</summary>

### Description
Do you recognize this cyberpunk baddie? We don't either. AI art generators are all the rage nowadays, which makes it hard to get a reliable known cover image. But we know you'll figure it out. The suspect is believed to be trafficking in classics. That probably won't help crack the stego, but we hope it will give motivation to bring this criminal to justice!
Download the image [here](https://artifacts.picoctf.net/c/416/output.bmp).
**Hints-1**Something doesn't quite add up with this image...
**Hints-2**How's the image quality?

### Steps taken to solve the problem.
- Wget the file and it is a .bmp file.
- Open it in the online hexedit. Also opened this [wikipedia article](https://en.wikipedia.org/wiki/BMP_file_format#:~:text=The%20BMP%20file%20format%20or,and%20OS%2F2%20operating%20systems.)
- Looked at the hints.
</details>


--------------------------------------------------------------------------------------------------------
<details>
<summary>SRA</summary>

### Description
I just recently learnt about the SRA public key cryptosystem... or wait, was it supposed to be RSA? Hmmm, I should probably check...
Additional details will be available after launching your challenge instance
File is [here](https://artifacts.picoctf.net/c/294/chal.py)

### Steps taken to solve the problem.
- Wget the file and opened it in nano.
- I think it is normal RSA.
- We need to find the pride string which is getting encoded.
- Googled crypto thing that is being imported to learn about the inverse function.
  ### Program Description
  - We are creating a variable pride and storing random alphabets and digits in it. The length of the word is 16.
  - We are then storing 2 prime numbers of 128 bits in the varialbes gluttony and greed.
  - Then we are storing the product of prime numbers in lust variable which is N in rsa.
  - Sloth is 655537 which is e in the rsa.
  - In the variable envy we are basically storing the private key which is d.
  - We are then converting out plain text to binary string and then converting it to base 256 number.
  - Let pride encoded string be byte string b'ab' then 256^1*97 + 256^0*98 = 29430 is what the base 256.
  - Then we raise this number it to power of sloth which is e and then mod it by lust which is N.
  - So anger variable stores the encrypted text.
  - It then prints the encrypted text and the private key.
  - We then have to enter the plain text to get the flag.
- So for the problem we know d, e and the encrypted text we have to find the plain text.
</details>


--------------------------------------------------------------------------------------------------------
## Currently Working On


--------------------------------------------------------------------------------------------------------
<details>
<summary>Virtual Machine 1</summary>

### Description
The enemy has upgraded their mechanical analog computer. Start an instance to begin.
Additional details will be available after launching your challenge instance.
##### Instance started.
We grabbed this design doc from enemy servers: [Download](https://artifacts.picoctf.net/c/324/Virtual-Machine-1.zip). We know that the rotation of the red axle is input and the rotation of the blue axle is output. Reverse engineer the mechanism and get past their checker program:
nc saturn.picoctf.net 51650
**Hint-1** The supporting structure for the machine has been removed from the given design doc.
**Hint-2** Some gears are meshed strangely, such as tooth overlapping tooth. Consider such gears as meshed correctly.
**Hint-3** Learn enough about gear ratios to abstract details from the design doc.
### Steps taken to solve the problem.
- Downloaded the file on my machine and it is a zip file. Extracted things and got a dae file.
- Imported the dae file into blender.
- Saw an entire gear train with bevel gears. One can really count all the gears and find all the gear ratio.
- Labled all the gears with number of teeth on the gears.
- Found the final gear ratio which was 18718
- Started the instance was asked that how many times the output will turn if the input is turned 14373 times.
- Entered 269033814 and the answer was wrong.
- 
</details>





--------------------------------------------------------------------------------------------------------
<details>
<summary>Template</summary>

### Description


### Steps taken to solve the problem.
- content
</details>





