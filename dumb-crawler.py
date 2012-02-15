#buildkeywords.py
# -*- coding: utf-8 -*-#

"""Module Dumb-Crawler by Clement Renaud - 2012
Retrieve text and extract keywords from all links contained in a webpage
Return json format

     To extract keywords from a file : python termtopia.py file.html
 
"""
# reauire JAVA HOME and jdk7
# install jpype : sudo apt-get install python-jpype
# http://trucsdedev.com/2012/01/24/utiliser-des-librairies-java-en-python-avec-jpype/
# on Ubuntu : $ find /usr/lib/jvm/ | grep jni.h
# export JAVA_HOME=/usr/lib/jvm/java-6-sun-1.6.0.22
# git clone https://github.com/misja/python-boilerpipe
# http://blog.notmyidea.org/using-jpype-to-bridge-python-and-java.html
# Thanks to Onnno for topia use : http://goo.gl/0BMHr
#http://pypi.python.org/pypi/topia.termextract
#http://www.peterbe.com/plog/uniqifiers-benchmark


import simplejson as json
import sys
import getopt
from topia.termextract import tag
from topia.termextract import extract
import jpype 
from bs4 import BeautifulSoup 
import urllib


# **** Get all URLs from a webpage using BeautifulSoup ****

def extractlinks(html):
    soup = BeautifulSoup(html)
    anchors = soup.findAll('a')
    links = []
    for a in anchors:
        links.append(a['href'])
    print ('-- Links have been extracted from the webpage')
    return links

def exportLinks(links,filename):
    thefile = open(filename,"w")
    for link in links:
      thefile.write("%s\n" % link)
    print('-- Links has been saved to the following file :' + filename)

# **** Get page title using Boilerpipe  ****

def retrieveTitle(url):
    soup = BeautifulSoup(urllib.urlopen(url))
    return soup.title.string

# **** Get page content using Boilerpipe  ****


# start the JVM with the good classpaths using python-boilerpipe
classpath = '/home/clement/Sites/makesense/python-boilerpipe/src/boilerpipe/data/boilerpipe-1.2.0/boilerpipe-1.2.0.jar:/home/clement/Sites/makesense/python-boilerpipe/src/boilerpipe/data/boilerpipe-1.2.0/lib/nekohtml-1.9.13.jar:/home/clement/Sites/makesense/python-boilerpipe/src/boilerpipe/data/boilerpipe-1.2.0/lib/xerces-2.9.1.jar'

def startJava():
    jpype.startJVM(jpype.getDefaultJVMPath(), "-Djava.class.path=%s" % classpath)
    print('starting java')

def retrieveContent(url):
    print ('-- Retrieving content from : '+ url)
    DefaultExtractor = jpype.JPackage("de").l3s.boilerpipe.extractors.DefaultExtractor
    # call Java Classes to extract content !
    content = (url,DefaultExtractor.INSTANCE.getText(jpype.java.net.URL(url))) 
    print("     successfuly retrieved!")
    return content

def closeJava():
    jpype.shutdownJVM()


# **** Extract tags from text  ****

def uniqify(seq, idFun=None):
    # order preserving
    if idFun is None:
        def idFun(x): return x
    seen = {}
    result = []
    for item in seq:
        marker = idFun(item)
        if marker in seen: continue
        seen[marker] = 1
        result.append(item)
    return result
 
def extractKeywords(text,language='english'):
    print('-- Extracting keywords')
    # initialize the tagger with the required language
    tagger = tag.Tagger(language)
    tagger.initialize()
    # create the extractor with the tagger
    extractor = extract.TermExtractor(tagger=tagger)
    # invoke tagging the text
    extractor.tagger(text)
    # extract all the terms, even the &amp;quot;weak&amp;quot; ones
    extractor.filter = extract.DefaultFilter(singleStrengthMinOccur=3)
    # extract
    return extractor(text)

def formatJson(tags):
    resultList = []
    # or result = build('dutch')
    for t in tags:
        # discard the weights for now
        # not using them at this point and defaulting to lowercase keywords/tags
        tag = (t[0].lower(),t[1])
        resultList.append(tag)
    # dump to JSON output
    return json.dumps(sorted(uniqify(resultList)))

def saveFile(content,filename):
    f = open(filename, 'w')
    f.write(content)
    f.close()
    print('-- File has been saved :' + filename)


def main():
    # parse command line options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)
    # process options
    for o, a in opts:
        if o in ("-h", "--help"):
            print __doc__
            sys.exit(0)
    # process arguments
    for arg in args:
        print '==================================='
        print 'Extracting keywords from : '+arg
        print('=======================================')
        print 'Processing...'
        raw= open(arg).read()
        links = extractlinks(raw)
        exportLinks(links, 'links.txt')
        allInfo = []
        startJava() #to use boilerpipe
        for url in links:
            content = retrieveContent(url)
            title = retrieveTitle(url)
            myTags = []
            for string in content:
                # print(string)
                tags = extractKeywords(string, language='english')
                json = formatJson(tags)
                myTags.append(json)
            info = {"title" : title,"url" : url,"tags" : myTags}
            allInfo.append(info)
        closeJava()
        print('=======================================')
        print('Results formatted using jSon : ')
        print('---------------------------------------')
        # saveFile(json.dumps(allInfo), 'data.json')
        print(allInfo)
        data = json.dumps(allInfo)
        print(data)

if __name__ == "__main__":
    main()
