class File:
    def __init__(self, filepath):
        self.filepath = filepath

    @property
    def name(self):
        index= 0
        while (index < len(self.filepath)-1):
            if(self.filepath[index] == '.'):
            #print(filepath[:index-1])
                return self.filepath[:index-1]
            index+=1
        return None
    
    @property   ##this makes it so that these functions can act as getter methods
    def extension(self):
        index= 0
        while(index < len(self.filepath)-1):
            if(self.filepath[index] == '.'):
            #print(filepath[:index-1])
                return self.filepath[index:len(filepath)-1]
            index+=1
        return None

    @property
    def classCode(self):
        classCode = ""
        num = 0
        index = 0
        while(index < len(self.filepath)):
            if '0' <= self.filepath[index] <= '9':
                num+=1
                if(num == 3):
                    classCode = self.filepath[:index+1]
                    return classCode     
            index+=1
        return None    
