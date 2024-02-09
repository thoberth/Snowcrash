commande pour rechercher tous les fichiers appartenant à l'user "level00" et on ne lit pas les sorties d'erreurs

```
level00@SnowCrash:~$ find / -user flag00 2> /dev/null
/usr/sbin/john
/rofs/usr/sbin/john
```

on trouve deux fichiers ; /usr/sbin/john et /rofs/usr/sbin/john qui contiennent la même chose : "cdiiddwpgswtgt"

```
level00@SnowCrash:~$ cat /usr/sbin/john /rofs/usr/sbin/john
cdiiddwpgswtgt
cdiiddwpgswtgt
```

avec le chiffrement césar on trouve une phrase : "nottoohardhere", qui fonctionne comme mot de passe

```
level00@SnowCrash:~$ su flag00
Password: 
Don't forget to launch getflag !
flag00@SnowCrash:~$ getflag
Check flag.Here is your token : x24ti5gi3x0ol2eh4esiuxias
```