from urllib import request
import sys

#if(len(sys.argv) < 3):
#    print("Missing arguments!")
#    exit(1)

#targe_tprocessing_time = int(sys.argv[1])
#receive_time_window = int(sys.argv[2])
#print(targe_tprocessing_time)
#-----------------------------------------------------


myLogFile = "https://s3.ap-south-1.amazonaws.com/kipkent/145683419925_elasticloadbalancing_us-east-1_awseb-e-a-AWSEBLoa-FVX6CNXZW....log"
myLocalFile = "logs.txt"
request.urlretrieve(myLogFile, myLocalFile)
#-----------------------------------------------------

inputfile = myLocalFile
outputfile = "Result.txt"

ipaddress = "0.000115"

myfile1 = open(inputfile, mode='r', encoding='latin_1')
#print(myfile1.read().replace(' ', ', '))
lines = myfile1.readlines()
myfile1.close()
myfile2 = open(outputfile, mode='w', encoding='latin_1')

count_time = 0
for line in lines:
    line = line.strip()
    if line.find(ipaddress)!= -1:
        count_time = count_time + 1

print( count_time )

for line in lines:
    if ipaddress in line:
        print(line.strip())
        myfile2.write(line.strip())
