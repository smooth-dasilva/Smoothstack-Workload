import os
from classes.FileExpertClass import FileExpert
from classes.Logger import setup_logger


def main():    

    #set up loggers
    error_logger = setup_logger('error_logger', 'error.log')
    app_logger = setup_logger('app_logger', 'app.log')
    
    #for log use separator
    logSeparator ='++++++++++++++++++++++++++++'

    # On app load create logs
    app_logger.info(f"Begin app log from {__name__}\n{logSeparator}")
    error_logger.info(f"Begin error handler log from {__name__}\n{logSeparator}")

    #get files we wish to examine
    #reg expression to match *_*_YYYYMMDD.csv
    fileExpert = FileExpert(app_logger, error_logger, r'[A-Z]+_[a-zA-Z]+_[12][09]\d{2}[01]\d[0123]\d\.csv', '../datasets/')
    


    if not fileExpert.NameTimeMap:
        return error_logger.error("No files with given pattern match in the given directory. Terminating the program...")
    
    dictI = dict(sorted(fileExpert.NameTimeMap.items(), key=lambda item: item[1]))
    print(dictI)
if __name__ =="__main__":
     main()