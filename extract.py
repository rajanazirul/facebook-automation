import os
import glob
import re


filename = 'C:/Users/rajan/Desktop/facebook-automation/comment2.html'

fh = open(filename)
s =" "
while (s):
    s = fh.readline()

    if "https://www.facebook.com" in s:
        start = s.find('href="https://www.facebook.com') + len("href=")
        end = s.find(">")
        substring = s[start:end]
        res = substring.split(None, 8)
        link = res[0]
        if "eziakaunxls" not in link:
            link = link
            print(link)

            out_file = open("outfile.txt", "a+")
            out_file.write("%s\n" %res[0])
fh.close()
out_file.close()