from urllib import request
import sys

if(len(sys.argv) < 2):
    print("Missing arguments!")
    exit(1)

targe_tprocessing_time = sys.argv[1]
#targe_tprocessing_time = int(sys.argv[1])
#receive_time_window = int(sys.argv[2])
#print(targe_tprocessing_time)
#targe_tprocessing_time = ipaddress
x = targe_tprocessing_time

#-----------------------------------------------------


myLogFile = "https://s3.ap-south-1.amazonaws.com/kipkent/145683419925_elasticloadbalancing_us-east-1_awseb-e-a-AWSEBLoa-FVX6CNXZW....log"
myLocalFile = "logs.txt"
request.urlretrieve(myLogFile, myLocalFile)
#-----------------------------------------------------

inputfile = myLocalFile
outputfile = "Result.txt"


#targe_tprocessing_time = '0.09'

myfile1 = open(inputfile, mode='r', encoding='latin_1')
#print(myfile1.read().replace(' ', ', '))
lines = myfile1.readlines()
myfile1.close()
myfile2 = open(outputfile, mode='w', encoding='latin_1')

count_time = 0
last_time = 0

for line in lines:
    line = line.strip()
    parts = line.strip().split(' ')
    float(parts[5])

    if parts[5].find(x)!= -1:
        count_time = count_time + 1
        print(line.strip())
        myfile2.write(line.strip())
    if parts[5].find('.')!= -1:
        last_time = last_time + 1
        #если нет то +1

print("There are <x> delayed requests :", count_time )
print("There is no delayed request : ", last_time - count_time )
#print(parts[6])
#print(line.strip().split(' '))
#for line in lines:
#    if ipaddress in line:
#        print(line.strip())
#        myfile2.write(line.strip())
