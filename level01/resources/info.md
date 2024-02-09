# First Search

```
$ id
uid=2001(level01) gid=2001(level01) groups=2001(level01),100(users)

$ find / -user level01 2> /dev/null | grep -v proc
(nothing)

$ find / -user flag01 2> /dev/null | grep -v proc
(nothing)
```

# /etc/passwd

## content of /etc/passwd file
`username:encrypted_password:id:gid:user_info:home_directory:default_shell`

nowadays encrypted password are no longer in /etc/passw they're replaced by a x or * and they are in /etc/shadow, but we dont have the rights

## Notes

There is a line where the encrypted password is present so we can decrypted it with John the reaper

`flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash`

Oh this is flag01 ... 

# Docker 

We have to build a container with a kali OS to download john and decrypted the passw

```
$ scp -P 4242 level01@127.0.0.1:/etc/passwd level01/resources
<!-- copy the passwd file to host -->
$ docker run -it --name snowcrash -v myvolsnowcrash:/Ressources kalilinux/kali-rolling
<!-- create the container -->
$ docker cp level01/resources/passwd snowcrash:/
<!-- copy passwd to container -->
<!-- NOW In the container :  -->
$ apt-get update && apt-get install john -y
$ john passwd
<!-- we decrypted the passwd in the file -->
$ john --show passwd
abcdefg          (flag01)
```

# We have the passwd of flag01

```
su flag01
abcdefg
```