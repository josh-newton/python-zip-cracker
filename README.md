Zip File Password Cracker
=========================
Nothing fancy. Attempts to brute force the password of a zip file.

Taken and adapted from the book [Violent Python](http://store.elsevier.com/product.jsp?isbn=9781597499576&pagename=search).

Password.txt Sources:
[http://contest-2010.korelogic.com/wordlists/password.dic](http://contest-2010.korelogic.com/wordlists/password.dic)
[http://downloads.skullsecurity.org/passwords/cain.txt.bz2](http://downloads.skullsecurity.org/passwords/cain.txt.bz2)
and the british-english dictionary file living in /usr/share/dict on an Ubuntu machine.

### Usage
```bash
python cracker.py -f <zip file> -d <dictionary>
```
If no dictionary file is passed, it will use the passwords.txt file instead. 