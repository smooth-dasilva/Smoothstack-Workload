import datetime
import os
import logging
import os.path, time 
import re

# use Expert to :
# Assign responsibility to class that has information required to fulfill responsibility.

class FileExpert:

    #use type hints for readability! they do nothing to enforce types
    NameTimeMap : dict

    app_logger : logging
    error_logger : logging

    pattern : str
    path :str


    def __init__(self,app_logger, error_logger,pattern, path) -> None:
        
        self.error_logger = error_logger
        self.app_logger = app_logger

        self.pattern =pattern
        self.path = path
        self.NameTimeMap = self.AddFilesNameTimeMap(self.CheckPathValidity())
    
    #Get List of all files in specified folder with specified pattern
    def AddFilesNameTimeMap(self, files):
        if files:
            NameTimeMapTemp = {}
            for el in files:
                if (self.MatchFilenameToPattern(el)):
                    NameTimeMapTemp[el] = self.GetTimeFromKey(el.split('_')[2])
            return NameTimeMapTemp

    #match filename with specified patter when creating File Expert
    def MatchFilenameToPattern(self,el):
        find = re.compile(self.pattern)
        match = find.finditer(el)
        if match:
            return True
        return False
    
    #get time from filename
    def GetTimeFromKey(self, date):
         # Remove .csv, pass through remaining string through date formatter
        date = date[:len(date)-4]
        format_str = '%Y%m%d' # The format
        return datetime.datetime.strptime(date, format_str)
    
    #check path validity
    def CheckPathValidity(self):
        try:
            return os.listdir(self.path)
        except FileNotFoundError:
            self.error_logger.error(f"Input error caught from {__name__}. Valid path not given. Returning empty string")
            return ""            