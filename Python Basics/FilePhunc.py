base_dir = "C:/Users/shrip/Pictures/url_downloads/"
fileName = base_dir+"sampleText.txt"
fileWrite = open(fileName, 'w')
fileWrite.write('First File write \n')
fileWrite.write('ever')
fileWrite.close()

fileRead = open(fileName, 'r')
contents = fileRead.read()
print(contents)
fileRead.close()


n = 3
nfirstlines = []

with open("bigFile.txt") as f, open("bigfiletmp.txt", "w") as out:
    for x in xrange(n):
        nfirstlines.append(next(f))
    for line in f:
        out.write(line)