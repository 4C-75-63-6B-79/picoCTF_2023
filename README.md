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
- The thing was later fixed and I could ssh correctly into it.
- Then I cd ../.. . And then found a challenge folder in there.
- cd into the challenge folder and there was metadatd.json file. I cat it and there was flag in it.
- flag: picoCTF{uS1ng_v1m_3dit0r_021d10ab}
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
- I ssh into the thing using this command ```ssh -p 51325 picoplayer@saturn.picoctf.net```
- I ls and there was a file with name useless.
- cat useless. Contents of the file are below.
    ```
    #!/bin/bash
    # Basic mathematical operations via command-line arguments

    if [ $# != 3 ]
    then
    echo "Read the code first"
    else
            if [[ "$1" == "add" ]]
            then 
            sum=$(( $2 + $3 ))
            echo "The Sum is: $sum"  

            elif [[ "$1" == "sub" ]]
            then 
            sub=$(( $2 - $3 ))
            echo "The Substract is: $sub" 

            elif [[ "$1" == "div" ]]
            then 
            div=$(( $2 / $3 ))
            echo "The quotient is: $div" 

            elif [[ "$1" == "mul" ]]
            then
            mul=$(( $2 * $3 ))
            echo "The product is: $mul" 

            else
            echo "Read the manual"
            
            fi
    fi
    ```
- This is a bash script. I don't know what it is doing. I had to google how to run a bash script. Found [this article](https://www.baeldung.com/linux/use-command-line-arguments-in-bash-script).
- Ran the bash script ``` sh useless ```. It printed that Read the manual.
- To read manual in terminal means to use ``` man ``` command. So I ran ``` man useless ``` which opened the man page for the useless and there was the flag at the bottom under the authors heading.
- flag: picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_5562}
</details>

--------------------------------------------------------------------------------------------------------
<details>
<summary>Ready Gladiator 0</summary>

### Description
Can you make a CoreWars warrior that always loses, no ties?
Your opponent is the Imp. The source is available [here](https://artifacts.picoctf.net/c/314/imp.red). If you wanted to pit the Imp against himself, you could download the Imp and connect to the CoreWars server like this:
nc saturn.picoctf.net 60784 < imp.red

### Steps taken to solve the problem.
- Wget the source in the webshell.
- Then ran the nc command.
- I did a few things and ended with message "Try again. Your warrior (warrior 1) must lose all rounds, no ties.".
- I opened the file in the nano and looked at the code and did not understand anything.
- There was mov command changed the 1 to 5. Then again ran the nc command and this time it gave me the flag. This was total hit and miss for me.
- flag: picoCTF{h3r0_t0_z3r0_4m1r1gh7_e1610ed2}
</details>

--------------------------------------------------------------------------------------------------------
<details>
<summary>Ready Gladiator 1</summary>

### Description
Can you make a CoreWars warrior that wins?
Your opponent is the Imp. The source is available [here](https://artifacts.picoctf.net/c/407/imp.red). If you wanted to pit the Imp against himself, you could download the Imp and connect to the CoreWars server like this:
nc saturn.picoctf.net 62981 < imp.red
To get the flag, you must beat the Imp at least once out of the many rounds.
**Hint** You may be able to find a viable warrior in beginner docs

### Steps taken to solve the problem.
- Wget the source file in the webshell and then ran the netcat command.
- It gave a message of 100 ties and said that my warrior must win once.
- So again I opened the imp file in nano and changed the mov from 0, 1 to 0, 2 and ran the nc command.
- This time the warrior 2 wins 100 times.
- So again change the move to some higher value like 11 and again I lose all the time.
- This time I changed the assert line to 3 and then also lost all the tries. 
- Looked at the hint.
- Googled the begineer docs for core wars and found this [site](https://vyznev.net/corewar/guide.html#start_imp). Did not understand much.
- Found another [site](http://www.koth.org/info/corewars_for_dummies/dummies.html) and read things understood little then copied on of the program.
- Program ```
  ;redcode
  ;name Imp Ex
  ;assert 1
  add #10, #-1
  mov 2, @-1
  jmp -2, 0
  dat #33, #33
  end
  ```
- Won 12 times ties 88 and got the flag.
- flag: picoCTF{1mp_1n_7h3_cr055h41r5_441be1fc}
</details>

--------------------------------------------------------------------------------------------------------
<details>
<summary>Ready Gladiator 2</summary>

### Description
Can you make a CoreWars warrior that wins every single round?
Your opponent is the Imp. The source is available [here](https://artifacts.picoctf.net/c/280/imp.red). If you wanted to pit the Imp against himself, you could download the Imp and connect to the CoreWars server like this:
nc saturn.picoctf.net 51703 < imp.red
To get the flag, you must beat the Imp all 100 rounds.
**Hint** If your warrior is close, try again, it may work on subsequent tries... why is that?

### Steps taken to solve the problem.
- Wget the file and changed the assert line to 0
- Ran the  nc command gave an error.
- Changed the assert line to 1.
- Added another mov line with 1, 5 and still did not win any thing.
- Copied the code from the **Ready Gladiator 1** from the solved section and the ran the nc command.
- Won 19 times and tied 81 times. Looked at the hint.
- Ran nc command again this time won 17 times and ties 83 times.
- Read this [guide](https://vyznev.net/corewar/guide.html).
- Read the above guide and understood a little bit of things but still could not write my own program. What I learned from the guide that there are warriors.
- So googled warriors for core wars and found this [startegy page](https://corewar.co.uk/strategy.htm). Tried copy pasting various warriors and ran them.
- Tried dwarf, paper and then stone/imp.
- Tried the clear-imp and got a win of 98 highest.
- Tried Digitalis in clear/imp example section scored 91 and dust 0.7 also scored 99(on mutiple tries) and then ran rise of dragon won 99 times.
- Code for [rise of dragons](https://corewar.co.uk/riseofthedragon.htm) ```                                                                                                   
  ;redcode
  ;name Imp Ex
  ;assert 1

          org    qscan

  gate    dat    4000,       1700
  bomb    dat    >2667,      11

          for    4
          dat    0,0
          rof

          spl    #4000,      >gate
  clear   mov    bomb,       >gate
          djn.f  clear,      >gate

          for    23
          dat    0,0
          rof

          istep  equ 1143           ; (CORESIZE+1)/7

  warr    spl    clear-1,    <3700
          mov    imp,        *launch
          spl    1,          <3600  ; 32 parallel processes
          spl    1,          <3500
          spl    1,          <3400
          spl    1,          <3300
          spl    1,          <3200
          spl    nxpoint,    <3100
  launch  djn.f  3600,       <4000

          for    2
          dat    0,0
          rof

  nxpoint add.f  #istep,     launch
          djn.f  clear-1,    <3000

  imp     mov.i  #3,         istep

          for    24
          dat    0,0
          rof

          qfac   equ 7051 ; 1467 ; 6371 ;  369
          qdec   equ 4452 ; 2804 ; 3532 ; 3730

          qa     equ (qfac*(qtab0-1-qptr)+1)
          qb     equ (qfac*(qtab0-qptr)+1)
          qc     equ (qfac*(qtab1-1-qptr)+1)
          qd     equ (qfac*(qtab1-qptr)+1)
          qe     equ (qfac*(qtab1+1-qptr)+1)
          qf     equ (qfac*(qtab2-qptr)+1)

          qtime  equ 18
          qstep  equ -7
          qgap   equ 87

  qdecode mul.b  *q1,          qptr
  q0      sne    <qtab0,       @qptr
  q1      add.b  qtab1,        qptr
  q2      mov    qtab2,        @qptr
  qptr    mov    qtab2,        *qdec
          add    #qstep,       qptr
          djn    q2,           #qtime
          jmp    warr,         qc
  qtab1   dat    4000,         qd
          dat    4000,         qe

  qscan   sne    qptr+qdec*qe, qptr+qdec*qe+qe
          seq    <qtab1+1,     qptr+qdec*(qe-1)+qe-1
          jmp    qdecode,      }q1
          sne    qptr+qdec*qb, qptr+qdec*qb+qd
          seq    <qtab0,       qptr+qdec*(qb-1)+qd
          jmp    qdecode,      {qdecode
          sne    qptr+qdec*qa, qptr+qdec*qa+qd
          seq    <qtab0-1,     qptr+qdec*(qa-1)+qd
          djn.a  qdecode,      {qdecode
          sne    qptr+qdec*qf, qptr+qdec*qf+qd
          seq    <qtab2,       qptr+qdec*(qf-1)+qd
          jmp    qdecode,      }qdecode
          sne    qptr+qdec*qc, qptr+qdec*qc+qc
          seq    <qtab1-1,     qptr+qdec*(qc-1)+qc-1
          jmp    qdecode,      {q1
          sne    qptr+qdec*qd, qptr+qdec*qd+qd
          seq    <qtab1,       qptr+qdec*(qd-1)+qd-1
          jmp    qdecode,      <qa
  qtab0   jmp    warr,         <qb
  qtab2   dat    qgap,         qf
  end
  ```
- I tried the above code mutiple times may be 40 times and then got the flag. I don't know what is happening in the code and I am not good enough for anything. So sorry.
- Just copy the code in imp.red file and then run the nc command. You might get the flag.
- flag: picoCTF{d3m0n_3xpung3r_9a074a57}
</details>

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
- Again  calculated the ratios and had made mistake in the previous attempt. The correct ratio came to be 9359.
- Again launched the instance and got the input rpm to be 22039 so the final output is going to be 9359 * 22039 = 206263001. This was correct and got the flag.
- picoCTF{m0r3_g34r5_3g4d_2efa1d52}
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
- Found articles on [petya attack](https://www.vsec.infinigate.co.uk/blog/worlds-most-famous-bitcoin-wallets-petya-wannacry-ransomware).
- Google the name of the malware no success.
- Tried entering petya in the flag format. Got the flag.
- flag: picoCTF{Petya}
</details>

--------------------------------------------------------------------------------------------------------
<details>
<summary>babygame01</summary>

### Description
Get the flag and reach the exit.
Welcome to BabyGame! Navigate around the map and see what you can find! The game is available to download [here](https://artifacts.picoctf.net/c/227/game). There is no source available, so you'll have to figure your way around the map. You can connect with it using nc saturn.picoctf.net 49813.
**Hints-1** Use 'w','a','s','d' to move around.
**Hints-2** There may be secret commands to make your life easy.

### Steps taken to solve the problem.
- Wget the file in the webshell which is a elf file and then cat it to see if there is flag in plain text.
- Opened the file in nano. I has bunch of gibberish but some string like player has flag etc.
- Ran the net cat command. It wrote some gibberish then player position, endtile postion and the player flag.
- I entered move nothing happened it printed the same thing again. Then I enterd the player position: 4, 8 it printed things bunch of time and the printed you win but no flag.
- I started the program again. This time entered Player Postion 5, 9 it changed the position to 5, 4.
- I started the program again. This time entered Player Postion 6, 9 it changed the position to 6, 4.
- Tried Player Postion 3, 3 it made the Player Postion to 7, 4.
- Entered Player had flag: 2. Made the player postion to 8,3.
- Looked at the hints. 
- We can move multiple times by entering w a s d multiple times
- I made it reach the X and then it said you won.
- I looked at hint and it said there are some secret commands. So typed run or jump and walk.
- When entered walk the player changed from @ to k. So typed again wala. It changed to a.
- Typed lk it change to k. So thought(before this thought I typed many other characters thinking it might reveal the flag. So it is all hit and try and method.) of typing lX changed to X. 
- Now the end tile positon also updated to the position of the player.
- Moved that X around with the w a s d and took it to first postion and the then beyond the scrren. At this point I was just typing the a key and did not stop to see the result. 
- The program said suddenly that I have 46 flag but did not showed me the flag and stopped.
- Now with the same approach but see the result more carefully.
- Type lX then enter then type wwww then enter aaaa to take the player to starting postion of the board(0,0).
- Now enter a(your player will go beyond the boundaries of the board) and press enter till you see the change in the player has flag value which will become 88.
- Now start bringing back the player to the visible part of the board using a. Once you can see the player take it to the end postion that is to the place where the X is present at the last row and last column.
- When you reach there you will get the flag.
- flag: picoCTF{gamer_m0d3_enabled_0a880baf}
</details>

--------------------------------------------------------------------------------------------------------
<details>
<summary>SOAP</summary>

### Description
The web project was rushed and no security assessment was done. Can you read the /etc/passwd file?
[Web Portal](http://saturn.picoctf.net:51531/)
**Hint** XML external entity Injection
### Steps taken to solve the problem.
- Opened the website. Used the inspect element thing nothing there.
- Tried to nc the website nothing there too.
- Tried to wget the website, it got stuck at connecting the sever.
- Looked at the hint. Google the hint.
- Looked at [this site](https://portswigger.net/web-security/xxe#exploiting-xxe-to-retrieve-files). The site mentioned to install **Burp Suite** community  edition.
- Installed the community edition.
- Then launched the burp selected next and did not play with any settings and went to proxy tab and clicked on open browser and turned intercept on.
- Restared the problem instance and then pasted the link the opened browser window and clicked on the button in the card Open Details.
- Then the burp caught the request and I pasted this in the xml portion. ```<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>``` and replace the id number with ```&xxe;```. Then forwarded the request and then the page loaded with the picoCTF flag.
- I had to try and google a lot to get this solution and I did not understand most things and did as the things says. This solution does not cover all the tries that I did to get the flag.
- flag: picoCTF{XML_3xtern@l_3nt1t1ty_55662c16}
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
- I tried to extract each of the MSB from each color channel thinking there might be a message stored in them but it was just 1.
- Then I noticed that the border of the image in close to white so it's rgb value should be close to white. 
- The I examined the pixels in the 0th row and saw a pattern in the values it had some similar looking rgb value appearing again and again like so. 
```[103, 240, 111], [231, 112, 239], [103, 112, 111], [231, 240, 111], [231, 112, 111], [103, 112, 239] ```
- Then I went pixel peeping in the image a saw that there is a white pixel in the first row at index 27. I printed it's pixel value which was (233, 239, 239).
- Then I realized that the most significant bits in some of these pixels is 1 since they may have only 7 bits in them so I made sure that I am converting the decimal to 8 bit binary.
- So we have to take the MSB of the each color of each pixel and then using those bits we can get the entire message which has the flag.
- I tried storing all the bits in the variable but as the bits increased the program slowed down a lot. So I had to make sure that as soon as 8 bits are stored I convert those into their ascii counter parts and then remove them form the variable.
- This the [program](/solutions/msb.py) to solve the problem. I have tried to explain the program using comments.
- To run this program make sure that you have pillow module installed and make sure that the progrma is stored in a folder named "solutions".
- Then run the program to get the text stored in the image. The program will generate a message.txt file in the same folder. 
- Search for the pico string in the file and you will get the flag.
- flag: picoCTF{15_y0ur_que57_qu1x071c_0r_h3r01c_b5e03bc5}
</details>

--------------------------------------------------------------------------------------------------------
<details>
<summary>tic-tac</summary>

### Description
Someone created a program to read text files; we think the program reads files with root privileges but apparently it only accepts to read files that are owned by the user running it.
ssh to saturn.picoctf.net:49798, and run the binary named "txtreader" once connected. Login as ctf-player with the password, d137d16e

### Steps taken to solve the problem.
- Ssh into the server and run the binary txtreader. It gave an error and asked me to enter a filename after the command.
- I entered the flag.txt file name and then it gave a error that I don't own the file.
- I then entered the src.cpp and it printed the file. It was program which was checking id to see if I own the file or not.
- I saw the tag of toctou in the problem so I googled it and landed on this [wikipedia page](https://en.wikipedia.org/wiki/Time-of-check_to_time-of-use).
- Read the page the thing it exploit the race conditions. This is something that I read when dealing with promises in javascript. Race conditions are bad as they make code unpredictalbe. This is all I remember about them.
- Then I googled how to exploit the toctou and got this [article](https://en.wikipedia.org/wiki/Time-of-check_to_time-of-use). This guide explains things and I followed it do the thing but it did not work.
- The I found this [video](https://www.youtube.com/watch?v=5g137gsB9Wk) and did what it explained. Make sure to run the program in the background. To do this you just have to type & at the end of the command.
- But the problem was that when ever I tried to read the flag.txt file it sometime gave error but rest of time it just closed without displaying anything.
- So I just started bashing it with up arrow key and enter to run the last command which was the ./txtreader flag.txt. And then it in more than 20 tries it gave the flag.
- flag: picoCTF{ToctoU_!s_3a5y_f482a247}
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
- Opened burpsuite and then used it to capture the request after entering the password and username.
- In one of the request there was this weird looking text ```A¤¥€!Ur[v[Œú„=OªS€Òž’~Ùýë¹ñY'
Ÿ u¨T>```
- Again returned to this challenge and google redirections + web exploitation and got this [site](https://infosecwriteups.com/url-redirection-exploitation-and-mitigation-8eed73007375). Read it and thought to run the burp to see if we have some thing like this in the challenge.
- Was looking and saw this id things thought to run from start again and base64 decode this id text.
- I again went to the login page and ran the burp suite and looked at the things in the each interaction captured by burp.
- I the top line there was url with id in it. The id had a text value with base64 encoded text. So I copied that text and decoded it online
- Base64 encode text: cGljb0NURntwcm94aWVzX2Fs | plain text: picoCTF{proxies_al
- Then again I forwareded the request and again looked for the id things and found one again.
- Base64 encode text: bF90aGVfd2F5XzAxZTc0OGRifQ== | plain text: l_the_way_01e748db}
- flag: picoCTF{proxies_all_the_way_01e748db}
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
- Googled the atbash term. Found this [wikipedia article](https://en.wikipedia.org/wiki/Atbash#:~:text=Atbash%20Hebrew%3A%20%D7%90%D7%AA%D7%91%D7%A9%3B%20also,with%20a%20standard%20collating%20order.).
- Tried to decipher the string mentioned above using the cipher in the wikipedia article. No success.
- Again looked at the file format and checked for any error but everything is fine.
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
Connect to the program on our server: nc saturn.picoctf.net 54297

### Steps taken to solve the problem.
- Wget the file and opened it in nano.
- I think it is normal RSA.
- We need to find the pride string which is getting encoded.
- Googled crypto thing that is being imported to learn about the inverse function.
  ### Program Description
  - We are creating a variable pride and storing random alphabets and digits in it. The length of the word is 16.
  - We are then storing 2 prime numbers of 128 bits in the varialbes gluttony and greed.
  - Then we are storing the product of prime numbers in lust variable which is N in rsa.
  - Sloth is 65537 which is e in the rsa.
  - In the variable envy we are basically storing the private key which is d.
  - We are then converting out plain text to binary string and then converting it to base 256 number.
  - Let pride encoded string be byte string b'ab' then 256^1*97 + 256^0*98 = 29430 is what the base 256.
  - Then we raise this number it to power of sloth which is e and then mod it by lust which is N.
  - So anger variable stores the encrypted text.
  - It then prints the encrypted text and the private key.
  - We then have to enter the plain text to get the flag.
- So for the problem we know d, e and the encrypted text we have to find the plain text.
- 
</details>







--------------------------------------------------------------------------------------------------------
## Currently Working On









--------------------------------------------------------------------------------------------------------
<details>
<summary>hijacking</summary>

### Description
Getting root access can allow you to read the flag. Luckily there is a python file that you might like to play with.
Through Social engineering, we've got the credentials to use on the server. SSH is running on the server.
saturn.picoctf.net 51709
Username: picoctf
Password: rZSsB--vJK  
**Hints-1** Check for Hidden files
**Hints-2** No place like Home:

### Steps taken to solve the problem.
- SSH in the sever using the given credentials. 
- Cd ../.. . Cd to the challenge. Gave error that permission is denied.
- So we need to get the admin privilages. Enterd the su to get the root access. It asked for the password entered the one given above thing failed.
- Tried the su picoctf it asked for the password and I don't know the password.
- Looked at the hints. 
- Cd home/picoctf and the run ls -a as hint mentions to check for the hidden files.
- There bunch of file like .bash_logout, .bashrd, .cache, .profile, .server.py
- The problem mentions about the py file. So we open the server py file in nano.
- There is no nano is ssh server so we cat the file. No python to run the file too.
- So we copy the file contents.
- I made the new server.py file on the webshell and then ran it there. I printed a base64 encoded string and then I base64 decoded it is a IP address.
- Now I tried to deconstruct the code line by line.
  ```
  import base64
  import os
  import socket
  ip = 'picoctf.org'

  # this is a way to ping server using python
  # 
  response = os.system("ping -c 1 " + ip) 
  #saving ping details to a variable
  host_info = socket.gethostbyaddr(ip) 
  #getting IP from a domaine
  host_info_to_str = str(host_info[2])
  host_info = base64.b64encode(host_info_to_str.encode('ascii'))
  print("Hello, this is a part of information gathering",'Host: ', host_info)  
  ```
- I googled what is pinging and then read this [wikipedia article](https://en.wikipedia.org/wiki/Ping_(networking_utility)).
- Then I tried running the code on my system and got the error that option -c requires admin privileges. Then I ran the thing with admin privileges and got thing like this
 ```
 Pinging picoctf.org [18.164.217.38] with 32 bytes of data:
  Reply from 18.164.217.38: bytes=32 time=86ms TTL=247
  Reply from 18.164.217.38: bytes=32 time=51ms TTL=247
  Reply from 18.164.217.38: bytes=32 time=59ms TTL=247
  Reply from 18.164.217.38: bytes=32 time=89ms TTL=247

  Ping statistics for 18.164.217.38:
      Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
  Approximate round trip times in milli-seconds:
      Minimum = 51ms, Maximum = 89ms, Average = 71ms
  Hello, this is a part of information gathering Host:  b'WycxOC4xNjQuMjE3LjM4J10='
 ```
- The base 64 encoded string is ['18.164.217.38'].
- Then I thought of running the ping without the admin privileges. I googled how to run the ping command in python without the admin privileges and found this s[tack overflow thing](https://stackoverflow.com/questions/29952676/simple-ping-function-returns-access-denied-option-c-requires-administrative-p) which suggested to use -n in place of -c.
- I ran the thing server.py on my machine with option n and the thing ran with same output. So I thought of donig this on the webshell. It gave error not ping found.
- And we cannot run the file on the ssh sever too.
</details>


--------------------------------------------------------------------------------------------------------
<details>
<summary>UnforgottenBits</summary>

### Description
Download this disk image and find the flag.
Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.
[Download compressed disk image](https://artifacts.picoctf.net/c/491/disk.flag.img.gz)

### Steps taken to solve the problem.
- content

</details>




--------------------------------------------------------------------------------------------------------
<details>
<summary>Java Code Analysis!?!</summary>

### Description
BookShelf Pico, my premium online book-reading service.
I believe that my website is super secure. I challenge you to prove me wrong by reading the 'Flag' book!
Here are the credentials to get you started:
Username: "user"
Password: "user"
Source code can be downloaded [here](https://artifacts.picoctf.net/c/478/bookshelf-pico.zip).
Website can be accessed [here](http://saturn.picoctf.net:55420/)!.
**Hint-1** Maybe try to find the JWT Signing Key ("secret key") in the source code? Maybe it's hardcoded somewhere? Or maybe try to crack it?
**Hint-2** The 'role' and 'userId' fields in the JWT can be of interest to you!
**Hint-3** The 'controllers', 'services' and 'security' java packages in the given source code might need your attention. We've provided a README.md file that contains some documentation.
**Hint-4** Upgrade your 'role' with the new (cracked) JWT. And re-login for the new role to get reflected in browser's localStorage.

### Steps taken to solve the problem.
- Wget the source and unzip it and then go into src > main > java > io > github > nandandesai > pico.
- Opened the java file in nano. No flag there.
- Looked in the repositories. No flag in there too.
- Looked in few more folder. Nothing useful found. Since there are too many files I looked at the hints.
- Downloaded the zip on my computer and opened the folder. Went into the user folder then into books and found the flag.pdf opened it had a flag but it was not a correct flag.
- Opened the src > main > java\io\github\nandandesai\pico > configs > BookShelfCongig.java got the place where the admin user is initialized but the password was redacted.
- Looking through the files came upon the file named JWTService.java in security folder in main.
- There is this variable named SECRET_KEY a
</details>


--------------------------------------------------------------------------------------------------------
<details>
<summary>babygame02</summary>

### Description
Break the game and get the flag.
Welcome to BabyGame 02! Navigate around the map and see what you can find! The game is available to download here. There is no source available, so you'll have to figure your way around the map. You can connect with it using nc saturn.picoctf.net 55756.

### Steps taken to solve the problem.
- Ran the nc command in the webshell.
- Same game as the babygame01. I have not solve that one so.
- Solved the babygame 01 so have I idea of what should I do.
- Typed lX and enter.
- Typed wwwwaaaa and enter to take the player to the start postion of the board.
- Then typed aaa and and did same as in babygame01. 
- This time as I reached the final postion the end disappeared and no win thing and no flag and I was able to bring the player back.
- So the thing failed. So now what Don't know.
- Did the same thing as above but before reaching the end postion change the player symbol to what was originally there and this time got the win thing but not the flag.
- Typed l made some changes to the dot lines and the looking at the player postion I tried taking the player to the X.
- We can make the player symbol to be a dot and then player postion doesn't update at all. 
</details>


--------------------------------------------------------------------------------------------------------
<details>
<summary>MORE SQLi</summary>

### Description
Can you find the flag on this website.
Try to find the flag [here](http://saturn.picoctf.net:54912/).
**Hint** SQLiLite

### Steps taken to solve the problem.
- Opened the site and just entered gibberish.
- This has something to do with the ways people use to modify data using queries. I have watched it in some videos but don't know how to do it.
- So I looked at hint.
- Then googled about SQL injection. Looked at few sites. Did not understand anything.
- Then I was on the picoctf discord and saw that we could do the previous solved ctf problems under same category to get better understanding of how to do the things.
- So I went to the picogym and searced for sql and it gave me 2 problems. I looked up the SQLite porblem from 2022.
- Then I watched this [video](https://www.youtube.com/watch?v=3tIXN9X7-6E) on it.
- Did as the video did and logged in using ' OR 1=1 -- as password and name. 
- Got a lot of entries with city phone and address and a search bar for city
- Entered flag to search it removed all entries.
- Then I entered the same login value it gave back all the entries into table.
</details>

--------------------------------------------------------------------------------------------------------
<details>
<summary>cancri-sp</summary>

### Description
Life is short; opportunity fleeting; the experiment perilous; judgment flawed.
Website is [here](http://saturn.picoctf.net:55507/).
Download [source.tar.gz](https://artifacts.picoctf.net/c/368/source.tar.gz).

### Steps taken to solve the problem.
- Used the link to open the website.
- Wget the source file on the webshell and try to explore it.
- Could not download the source.tar.gz since the zip was 1 gb not have that much data.
</details>



--------------------------------------------------------------------------------------------------------
<details>
<summary>PowerAnalysis: Warmup</summary>

### Description
This encryption algorithm leaks a "bit" of data every time it does a computation. Use this to figure out the encryption key.
Download the encryption program here [encrypt.py](https://artifacts.picoctf.net/c/433/encrypt.py). Access the running server with nc saturn.picoctf.net 59900.
The flag will be of the format picoCTF{<encryption key>} where <encryption key> is 32 lowercase hex characters comprising the 16-byte encryption key being used by the program.

### Steps taken to solve the problem.
- Wget the encryptpy file.
- Nc into the server we get a propmpt the 16 bytes text encoded as hex. So I look at the py file in nano.
- Looking at the encryption file we see that we have to enter a hex encoded plain text of 16 bytes.
- Program also has a key which is encoded in the hex format.
- Each byte of the plain text and the secret key is then XOR which give out a value.
- The value from the XOR operation is then used to get the element in the Sbox tuple.
- The value from the Sbox is then AND with the 1 which is stored in the array leak_buf.
- The program then counts the number of 1 in the leak_Buf array an output is to the screen.
- I tried to reverse the problem by my failed attempts below.
- Since we are loosing some info about the key ascii value when we do the AND operation I don't know how to reverse the problem.
- The reason is that doing AND operation with 1 will give 1 if the value from Sbox is odd which there are many and 0 which also there are many in Sbox.
- So to determine the ascii value we need to have a the leak value to be 0 at start that I figured out using the input below.
- ffffffffffffffffffffffffffffffff 4
- 00ffffffffffffffffffffffffffffff 3 é
- ff00ffffffffffffffffffffffffffff 5
- ffff00ffffffffffffffffffffffffff 4 
- ffffff00ffffffffffffffffffffffff 4 
- ffffffff00ffffffffffffffffffffff 4 
- ffffffffff00ffffffffffffffffffff 5
- ffffffffffff00ffffffffffffffffff 3 é
- ffffffffffffff00ffffffffffffffff 3 é
- ffffffffffffffff00ffffffffffffff 4 
- ffffffffffffffffff00ffffffffffff 5
- ffffffffffffffffffff00ffffffffff 4
- ffffffffffffffffffffff00ffffffff 4
- ffffffffffffffffffffffff00ffffff 4
- ffffffffffffffffffffffffff00ffff 3 é
- ffffffffffffffffffffffffffff00ff 4 
- ffffffffffffffffffffffffffffff00 4
- The hex encoded plain text at which the leak_value is 0 is 00ffffffffff0000ffffffffff00ffff which mean at this point all the even value are being selected from the Sbox tuple.
- But there are many even value with even ascii value in the Sbox tuple so it is not easy to get the value of the each byte.
- May be I am missing something. I don't know.
- We can automate some process using the python pwntools.
- For first byte all the index for which the lek_vlaue is 1.
- [1, 3, 4, 5, 6, 8, 10, 12, 14, 15, 16, 19, 30, 31, 37, 40, 44, 45, 46, 49, 50, 51, 52, 53, 54, 61, 67, 72, 74, 76, 77, 79, 83, 84, 88, 89, 90, 91, 92, 95, 97, 98, 100, 101, 105, 106, 107, 108, 110, 112, 114, 115, 117, 120, 121, 122, 123, 127, 129, 130, 131, 132, 134, 135, 136, 138, 139, 140, 143, 146, 147, 148, 151, 153, 154, 160, 161, 163, 164, 167, 168, 170, 171, 173, 174, 175, 176, 178, 179, 183, 185, 188, 189, 190, 192, 193, 197, 200, 202, 204, 205, 207, 208, 209, 210, 214, 215, 216, 218, 222, 224, 226, 228, 229, 230, 231, 232, 233, 234, 239, 240, 241, 242, 244, 246, 250, 252, 255]
- For second byte all the index for which the lek_vlaue is 1.
- [0, 1, 3, 4, 7, 8, 9, 10, 12, 13, 15, 17, 18, 24, 25, 28, 31, 32, 33, 35, 36, 37, 38, 40, 42, 43, 44, 47, 50, 53, 54, 55, 56, 57, 59, 60, 65, 67, 68, 70, 71, 74, 75, 78, 81, 83, 85, 89, 90, 91, 92, 93, 97, 98, 99, 100, 105, 107, 108, 109, 110, 111, 113, 116, 119, 121, 122, 123, 125, 127, 129, 131, 132, 133, 135, 136, 138, 141, 142, 143, 148, 149, 152, 155, 163, 165, 166, 167, 174, 182, 184, 185, 186, 189, 190, 191, 193, 195, 196, 198, 199, 200, 208, 209, 210, 211, 212, 215, 216, 223, 224, 225, 226, 229, 231, 233, 234, 238, 239, 240, 241, 242, 243, 244, 248, 249, 251, 254]
- For 3 byte all the index for which the lek_vlaue is 1.
- [5, 8, 12, 13, 14, 17, 18, 19, 20, 21, 22, 29, 33, 35, 36, 37, 38, 40, 42, 44, 46, 47, 48, 51, 62, 63, 65, 66, 68, 69, 73, 74, 75, 76, 78, 80, 82, 83, 85, 88, 89, 90, 91, 95, 99, 104, 106, 108, 109, 111, 115, 116, 120, 121, 122, 123, 124, 127, 128, 129, 131, 132, 135, 136, 138, 139, 141, 142, 143, 144, 146, 147, 151, 153, 156, 157, 158, 161, 162, 163, 164, 166, 167, 168, 170, 171, 172, 175, 178, 179, 180, 183, 185, 186, 192, 194, 196, 197, 198, 199, 200, 201, 202, 207, 208, 209, 210, 212, 214, 218, 220, 223, 224, 225, 229, 232, 234, 236, 237, 239, 240, 241, 242, 246, 247, 248, 250, 254]
- For 4 byte all the index for which the lek_vlaue is 1.
- [2, 3, 4, 7, 9, 10, 17, 18, 19, 20, 22, 23, 24, 26, 27, 28, 31, 32, 34, 35, 39, 41, 44, 45, 46, 48, 49, 51, 52, 55, 56, 58, 59, 61, 62, 63, 64, 65, 66, 70, 71, 72, 74, 78, 80, 81, 85, 88, 90, 92, 93, 95, 96, 97, 98, 100, 102, 106, 108, 111, 112, 114, 116, 117, 118, 119, 120, 121, 122, 127, 128, 131, 142, 143, 145, 147, 148, 149, 150, 152, 154, 156, 158, 159, 161, 162, 163, 164, 165, 166, 173, 181, 184, 188, 189, 190, 195, 196, 200, 201, 202, 203, 204, 207, 211, 216, 218, 220, 221, 223, 224, 226, 227, 229, 232, 233, 234, 235, 239, 241, 242, 244, 245, 249, 250, 251, 252, 254]
</details>


--------------------------------------------------------------------------------------------------------
<details>
<summary>Horsetrack</summary>

### Description
I'm starting to write a game about horse racing, would you mind testing it out? Maybe you can find some of my easter eggs... Hopefully it's a heap of fun!
[vuln](https://artifacts.picoctf.net/c/459/vuln), [libc.so.6](), [ld-linux-x86-64.so.2](https://artifacts.picoctf.net/c/459/ld-linux-x86-64.so.2), nc saturn.picoctf.net 59143

### Steps taken to solve the problem.
- Ran the nc command first to see what is this game. Looked like a command line thing where we are prompted to enter the instructions and things happen.
- Wget the vuln file and it is a elf file.
- Wget the second file which is also a elf file.
- Wget the third file and it is also a elf file.
- Elf file problems are difficult and I really don't under stand them.
- I opened the file in the nano and most of the content in them is gibberish. So according to me we might have to find the flag using just interaction with the program.
- Ran the nc command and interacted with the thing.
- We need to add horse with stable index, name length and name.
- Added 3 horses and then wanted to race them gave an error that not enough horses.
- I entered it again to add horses this time I entered names with space in between something weird happend that after I entered hourse it did not give me a prompt that a horse has been added.
- Then I entered the horse name only space and it accepted it.
- 
</details>

--------------------------------------------------------------------------------------------------------
<details>
<summary>Special</summary>

### Description
Don't power users get tired of making spelling mistakes in the shell? Not anymore! Enter Special, the Spell Checked Interface for Affecting Linux. Now, every word is properly spelled and capitalized... automatically and behind-the-scenes! Be the first to test Special in beta, and feel free to tell us all about how Special streamlines every development process that you face. When your co-workers see your amazing shell interface, just tell them: That's Special (TM)
Start your instance to see connection details.
ssh -p 63865 ctf-player@saturn.picoctf.net
The password is af86add3
**Hint** Experiment with different shell syntax.

### Steps taken to solve the problem.
- Ssh in to the thing.
- Typed ls noticed it said that Is not found.
- Then typed cd got Ad not found. So I thought is doing some rot on first character.
- Typed in ed gave back ed not found and when typed fd gave Fed not found.
- So no idea what it is doing.
- Typed ssh gave Why go back to inferior shell?. Still no idea why it gave that.
- Read the problem and entered That's Special (TM) gave syntax error unquoted string. Still I don't understand what we have to do here. Looked at the hint.
- If you enter any word that has sh in it it says why go to inferior shell.

</details>

--------------------------------------------------------------------------------------------------------
<details>
<summary>No way out</summary>

### Description
Put this flag in standard picoCTF format before submitting. If the flag was h1_1m_7h3_f14g submit picoCTF{h1_1m_7h3_f14g} to the platform.
[Windows game](https://artifacts.picoctf.net/c/285/win.zip), [Mac game](https://artifacts.picoctf.net/c/285/mac.app.zip)

### Steps taken to solve the problem.
- Downloaded and unziped the file and opened the pico.exe file.
- It is a game. Played it. Saw a big flag out of the compound so climed the ladder to see if there is any flag there and there was not.
- I could also not jump down from the platform or outside the walls.
- 
</details>

--------------------------------------------------------------------------------------------------------
<details>
<summary>VNE</summary>

### Description
We've got a binary that can list directories as root, try it out !!
ssh to saturn.picoctf.net:61401, and run the binary named "bin" once connected. Login as ctf-player with the password, 3f39b042

### Steps taken to solve the problem.
- Ssh into the thing and then googled how to run binary in linux.
- Ran using ./bin_name. Got a error saying secret_dir environment variable is not set.
- cd ../.. and the ls. I saw the challenge file but could not open it since permission denied.
</details>


--------------------------------------------------------------------------------------------------------
<details>
<summary>Template</summary>

### Description


### Steps taken to solve the problem.
- content
</details>










