import webbrowser
import requests
import time
#Open File

File = open("Lists.txt","r")
List = str(File.read()).split('\n')
NewList = []

#Find Links Here:
for i in List:
    if i.find('https://osu.ppy.sh/')!=-1:
        NewList.append(str(i[i.find('https://osu.ppy.sh/'):]).split(' ')[0])

#Gets the Proper URL for downloading
lastlist = []
for i in NewList: 
    lastlist.append(requests.get(i).url)

#Opens Links.txt to parse
# File = open("Links.txt","r")
# List = str(File.read()).split('\n')

#Appends the Download Links
DownloadList = []
for i in lastlist:
    m = i.split("/#")
    DownloadNewList.append(str(m[0])+'/download')
#Download List is containing the Links that can be downloaded.

for i in DownloadList:
    webbrowser.open(i)
    time.sleep(120)
