import re
#Opening the Html file
n= open("head.html","r")
k= n.read()

n.close()
urls = re.findall('https?://(?:[\w./])+', k)

index= 0
f = open("output.txt", "w")
for line in k.splitlines():
    if(line.find(urls[index])!=-1):

        tags= re.findall('<(?:[\w]*)',line)

        tags[0]=tags[0][1:]
        x = tags[0]+": "+ urls[index]+"\n"
        print(x)
        f.write(x)
        index+=1
        if(index>len(urls)-1):
            break
