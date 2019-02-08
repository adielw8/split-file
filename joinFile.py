import sys
import os
import random
import string
import ast

class joinFile:
    def __init__(self):
        self.parse_args(sys.argv)
        self.file_base_name = self.dict.get("file_base_name")
        self.file_ext = self.dict.get("file_ext")
    @staticmethod
    def run():
        splitter = joinFile()
        splitter.join()

    def join(self):
        join_file = open(self.file_base_name+self.file_ext,"wb")
        for i in range(1,len(self.dict)-1):
            split_file = open(self.dict.get(self.file_base_name+"."+str(i)+self.file_ext),"rb")
            for row in split_file:
                join_file.write(row)
        join_file.close()

    def get_new_file(self):
        """return a new file object ready to write to"""
        new_file_name = randomString()
        mappingFile = "%s%s" % (self.file_base_name, self.file_ext)
        new_file_path = os.path.join(self.working_dir, new_file_name)
        print("creating file %s" % (new_file_path))
        self.dict.update({mappingFile:new_file_name})
        return open(new_file_path, 'wb')

    def parse_args(self,argv):
        try:
            """parse args and set up instance variables"""
            if len(argv) == 2:
                mappingFile = argv[1]
            with open(mappingFile, "r") as f:
                self.dict = ast.literal_eval(f.read())
        except:
            print(self.usage())
            sys.exit(1)


        
    def usage(self):
        return """
        join files.
        Usage:
            $ python3 joinFile.py <mapping_file_name>
        """

    
if __name__ == "__main__":
    joinFile.run()