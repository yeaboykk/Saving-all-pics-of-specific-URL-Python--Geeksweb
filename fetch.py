import urllib, re
source = urllib.urlopen('http://www.cbssports.com/nba/draft/mock-draft').read()
f = open('out.txt', 'w')
for link in re.findall('http://sports.cbsimg.net/images/nba/logos/30x30/[A-Z]*.png', source):
    print >> f, link   # or f.write('...\n')
    actually_download = True
    if actually_download:
        filename = link.split('/')[-1]
        urllib.urlretrieve(link, filename)
f.close()
