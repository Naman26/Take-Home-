import re
#----------------------------------File Processing------------------------------------------------
# Opening the Html file
n= open("head.html","r")
# Reading the file  
k= n.read()

n.close()
#---------------------------------Capturing URLs--------------------------------------------------
# Regular expression to catch URLs and save them into a list urls
urls = re.findall('https?://(?:[\w./])+', k)

index= 0
# Creating a file to save output
f = open("output.txt", "w")
#---------------------------------Capturing Tags--------------------------------------------------
# Reading file line by line
for line in k.splitlines():
    # If line contains a url
    if(line.find(urls[index])!=-1):
        # Save the tag into tags list including "<" 
        tags= re.findall('<(?:[\w]*)',line)
        # Remove "<" from the tag 
        tags[0]=tags[0][1:]
        x = tags[0]+": "+ urls[index]+"\n"
        print(x)
        # Writing output to ouput.txt
        f.write(x)
        index+=1
        # Break if index overflows
        if(index>len(urls)-1):
            break
