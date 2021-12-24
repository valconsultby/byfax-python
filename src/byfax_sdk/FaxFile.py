import os
import hashlib

class FaxFile:
    @staticmethod
    def CreateFile( filePath):
        in_file = open(filePath, "rb")
        data = in_file.read()
        in_file.close()
        faxFile = {
            'fileCheck': FaxFile.__md5(filePath),
            'fileName': os.path.basename(filePath),
            'fileSize': len(data),
            'fileData': data}
        return faxFile #{'documentFile': faxFile}
    
    @staticmethod
    def CreateDocumentFile( filePath):
        in_file = open(filePath, "rb")
        data = in_file.read()
        in_file.close()
        faxFile = {
            'fileCheck': FaxFile.__md5(filePath),
            'fileName': os.path.basename(filePath),
            'fileSize': len(data),
            'fileData': data}
        return {'documentFile': faxFile}
    
    def __md5(fname):
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
