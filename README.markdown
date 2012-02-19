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
# reauire JAVA HOME and jdk7
# install jpype : sudo apt-get install python-jpype
# http://trucsdedev.com/2012/01/24/utiliser-des-librairies-java-en-python-avec-jpype/
# on Ubuntu : $ find /usr/lib/jvm/ | grep jni.h
# export JAVA_HOME=/usr/lib/jvm/java-6-sun-1.6.0.22
# git clone https://github.com/misja/python-boilerpipe
# http://blog.notmyidea.org/using-jpype-to-bridge-python-and-java.html
# http://pypi.python.org/pypi/topia.termextract
# http://www.peterbe.com/plog/uniqifiers-benchmark

Thanks
---
Python-Boilerpipe : https://github.com/misja/python-boilerpipe
Onnno for topia use : http://goo.gl/0BMHr
