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


Thanks
---
Python-Boilerpipe : https://github.com/misja/python-boilerpipe
