on trouve un fichier .pcap qui est un "packet capture", donc une capture de paquets qui transitent sur un réseau

on l'ouvre sur Wireshark et en faisant une analyse TCP on trouve un mot de passe : "ft_wandr...NDRel.L0L" qui ne marche pas comme réponse

on affiche le flux TCP en hexadécimal et on voit que les '.' sont des 7F donc des DEL en ascii, ce qui donne réellement : "ft_waNDReL0L"

```
level02@SnowCrash:~$ su flag02
Password:
Don't forget to launch getflag !
flag02@SnowCrash:~$ getflag
Check flag.Here is your token : kooda2puivaav1idi4f57q8iq
```
