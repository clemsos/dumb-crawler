Dumb crawler
----
A simple crawler to retrieve keywords from all links contained in a webpage

HOW TO USE IT
----
To extract keywords from a file : 
     python termtopia.py file.html
 

HOW IT WORKS
---
  1. retrieve all urls from a page (using beautiful soup)
  2. retrieve content from each page (using boilerpipe java-python)
  3. extract keywords from content (using topia.termextract)
  4. match all keywords (using difflib) 
  5. using (simple json)



Installation
---
This script reauires JAVA HOME configured and jdk7 to run Boilerpipe
''''bash
    on Ubuntu : 

    $ sudo apt-get install python-jpype
    $ find /usr/lib/jvm/ | grep jni.h
    $ export JAVA_HOME=/usr/lib/jvm/java-6-sun-1.6.0.xx
''''
More here http://blog.notmyidea.org/using-jpype-to-bridge-python-and-java.html

Thanks
---
Python-Boilerpipe : https://github.com/misja/python-boilerpipe
Onnno for topia use : http://goo.gl/0BMHr
