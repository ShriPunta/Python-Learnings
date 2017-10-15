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