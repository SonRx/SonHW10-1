# Richard Son

import sys
# print sys.argv[0] # prints reconstruct.py
# print sys.argv[1] # prints 1st argument
# print sys.argv[2] # prints 2nd argument

def readAsManyFiles(): # algorithm to read as many files as user inputs
    for i in range(1, len(sys.argv)):
        with open(sys.argv[i],'r') as myfile:
            textFile = sys.argv[i]
            print
            print "Reading file: ", textFile
            
            list = []
            for line in myfile:
                strip_lines = line.strip()
                listli = strip_lines.split()
              #  print(listli)
                m = list.append(listli)
            print "Length of text: ", len(listli)
            print(list)
    
def readFile(file):
    with open(file,'r') as myfile:
        textFile = file
        print
        print "Reading file: ", textFile
        
        line = myfile.read()
        lines = line.split()
    
        print(line)
        return lines

def combineBackwardsSentence(l1,l2):
    list1Length = len(l1)
    list2Length = len(l2)
    maxLength = 0    

    if list2Length > list1Length:
        maxLength = list2Length
    else:
        maxLength = list1Length
    
    print "max length is: ", maxLength
    outList = []
    
    for i in range(0, maxLength):
        if(l1 != []): # if l1 is not empty
            outList.append(l1.pop()) # append out list with the latest word
        if(l2 != []):
            outList.append(l2.pop())
    print "out list is: ", outList

    
def main():
    list1 = readFile(sys.argv[1])
    print "length of list 1 is: ", len(list1)
    list2 = readFile(sys.argv[2])
    print "length of list 2 is: ", len(list2)    
    print
    combineBackwardsSentence(list1,list2)

if __name__ == "__main__":
    main() 
