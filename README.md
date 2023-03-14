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
<summary>Template</summary>

### Description


### Steps taken to solve the problem.
- content
</details>


