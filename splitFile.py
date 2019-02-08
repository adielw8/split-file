import sys
import os
import random
import string
import argparse

class splitFile:
    def __init__(self):
        self.parse_args(sys.argv)
        self.dict = {}
    @staticmethod
    def run():
        splitter = splitFile()
        splitter.split()



    def split(self):
        file_number = 1
        line_number = 1
        part_number = 1
        entry = 1

        randRow = True if self.split_parts != 0 else False
        out_file = self.get_new_file(file_number)
        self.dict.update({"file_base_name":self.file_base_name,"file_ext":self.file_ext})


        if randRow:
            self.split_size = int(self.line_numbers/self.split_parts) +50
            print("Splitting {} into multiple files with {} parts".format(self.file_base_name+self.file_ext,self.split_parts))
        else:
            print("Splitting {} into multiple files with random parts".format(self.file_base_name+self.file_ext))
        
        
        for line in self.in_file:
            out_file.write(line)
            line_number += 1
            if file_number == entry and not randRow:
                self.split_size = random.randint(int(self.line_numbers/50),int(self.line_numbers/4))
                entry +=1
            if line_number == self.split_size:
                if self.random_blocks:
                    if random.randint(0,5) > 2 : createing_random_blocks(line_number) 
                out_file.close()
                file_number += 1
                line_number = 1
                out_file = self.get_new_file(file_number)
                


                        

        out_file.close()
        with open(self.file_base_name+self.file_ext +".txt","w") as f:
            f.write(str(self.dict))
        print("Created %s files." % (str(file_number)))


    def get_new_file(self,file_number):
        """return a new file object ready to write to"""
        new_file_name = randomString()
        mappingFile = "%s.%s%s" % (self.file_base_name, str(file_number), self.file_ext)
        new_file_path = os.path.join(self.working_dir, new_file_name)
        #print("creating file %s" % (new_file_path))
        self.dict.update({mappingFile:new_file_name})
        return open(new_file_path, 'wb')

    def parse_args(self,argv):
        """parse args and set up instance variables"""
        try:
            if len(argv) >= 3:
                self.file_name = argv[1]
                self.split_parts = int(argv[2])
                if len(argv) == 4 and argv[3] == "-rb":   
                    self.random_blocks = True
                else:
                    self.random_blocks = False
            self.line_numbers = file_len(self.file_name)
            self.in_file = open(self.file_name, "rb")
            self.working_dir = os.getcwd()
            self.file_base_name, self.file_ext = os.path.splitext(self.file_name)
        except:
            print(self.usage())
            sys.exit(1)
        
    def usage(self):
        return """
        Split a large file into many smaller files with set number of parts.
        Usage:
            $ python3 fileSplitter.py <file_name> <parts> -rb
        if you enter 0 in parts  - the script pick the parts randomly and create the blocks in random size
        -rb is optional (use -rb if you want to create random blocks)
        """

        
def randomString():
    startR = 5
    endR = 10

    ranString = ""
    ranRange = random.randint(startR,endR)
    for i in range(ranRange):
        ranString += random.choice(string.ascii_letters)

    return ranString


def file_len(full_path):
  """ Count number of lines in a file."""

  return sum(1 for line in open(full_path,"rb"))

def split_to_random_parts(line_numbers,split_parts):
    line_len = 0
    part_list = []
    if split_parts == 0:
        while(line_numbers>0):
            row_size = random.randint(int(line_numbers/20),line_numbers)
            line_numbers = line_numbers - row_size
            part_list.append(row_size)
    else:
        row_size = int(line_numbers/split_parts)

        for i in range(split_parts):
            part_list.append(row_size)
    
    return part_list

def createing_random_blocks(block_size):    
    fileName = randomString()
    f= open(fileName,"wb")
    fileSize = random.randint(block_size,block_size*2)*10
    print("file size: "+str(fileSize/1000)+"kb")
    f.write(os.urandom(fileSize))

    #f.write(str.encode(fileText))
    print("file name: "+fileName)
    #for i in range(10):
     #   f.write( +"\n")
    f.close() 
    



if __name__ == "__main__":
    splitFile.run()