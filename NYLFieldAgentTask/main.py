
import os
import math
import pandas as pd
import smtplib, ssl
import matplotlib.pyplot as plt

from classes.FileExpertClass import FileExpert
from classes.Logger import setup_logger
from classes.ProcessingExpertClass import ProcessingExpert
from quickstart import SendMessage


# set up loggers
error_logger = setup_logger('error_logger', 'error.log')
app_logger = setup_logger('app_logger', 'app.log')

# for log session separator
logSeparator = '++++++++++++++++++++++++++++'

# On app load : create logs
app_logger.info(f"Begin app log from {__name__}\n{logSeparator}")
error_logger.info(f"Begin error handler log from {__name__}\n{logSeparator}")


def CompareFirstSecondLatestLen(path, firstLatest, secondLatest):
    input(f"I will compare csv lengths : {firstLatest} vs {secondLatest}")

    with open("ProcessedFilesListNYL.txt","a+") as f:
        f.seek(0)
        previousList= f.read().split('\n')

        with open(path+firstLatest, 'r') as first, open(path+secondLatest, 'r') as second:
            firstLen =sum(1 for line in first)
            secondLen =sum(1 for line in second)

            if abs(firstLen-secondLen)>500:
                error_logger.error("This latest fiile has a variance greater than 500 with the second latest file.\nTerminating program...")  
                return False

        if (firstLatest not in previousList) :
            f.flush()
            f.write(str(firstLatest)+'\n')
        else:
            error_logger.error(f"{firstLatest} has already been examined.")  
            return False
        return True

def GetNthKey(dictionary, n=0):
    if n < 0:
        n += len(dictionary)
    for i, key in enumerate(dictionary.keys()):
        if i == n:
            return key
    raise IndexError 

def main():    

    #pandas settings
    # Use 3 decimal places in output display
    pd.set_option("display.precision", 3)

    # Don't wrap repr(DataFrame) across additional lines
    pd.set_option("display.expand_frame_repr", False)

    # Set max rows displayed in output to 25
    pd.set_option("display.max_rows", 25)

    # get files we wish to examine
    # reg expression to match *_*_YYYYMMDD.csv

    
    fileExpert = FileExpert(app_logger, error_logger, r'[A-Z]+_[a-zA-Z]+_[12][09]\d{2}[01]\d[0123]\d\.csv', './datasets/')
    input(f"FileExpert created. Will get files from {fileExpert.path} matching regex pattern {fileExpert.pattern}")

    if fileExpert.path=="ERROR":
        return
    if not fileExpert.NameTimeMap:
        return error_logger.error(f"No files with regex pattern {fileExpert.pattern} match in the given {fileExpert.path}. \nTerminating the program...")
    
    # files ordered by date
    orderedByDateNameTimeMap = (dict(sorted(fileExpert.NameTimeMap.items(), key=lambda item: item[1])))

    # This is the final check... if we pass this block we process the file with ProcessingExpert 
    for index, (Name, Time) in enumerate(orderedByDateNameTimeMap.items()):
        continueBool = True
        try:
            continueBool = CompareFirstSecondLatestLen(fileExpert.path, GetNthKey(orderedByDateNameTimeMap,index), GetNthKey(orderedByDateNameTimeMap, index+1))
                
            if continueBool:
                #we are only now assigning the processing expert, so latest is not processed!
                app_logger.info(f"Processing file: {Name}")
                processingExpert = ProcessingExpert(app_logger, error_logger, Name, False)
            else:
                continueQuestion = input(f"Processing of {Name} failed (check error log). Would you like to process the next dated file? (y/n)")
                if continueQuestion=="y":
                    continueBool=False
                else:
                    return        
    
        except IndexError:
            return error_logger.error("Every file has a difference of greater than 500 lines compared to the previous date. Check csv records are correct. \nTerminating program...")
        
        if continueBool:
            #we break out of the loop if the input is anything other than y. else above already end program if false
            break
        
    #time for ProcessExpert to process!
    while(not processingExpert.LatestIsProcessed):
        df = pd.read_csv(fileExpert.path+processingExpert.LatestFile)
        
        #change header requirement
        processingExpert.ChangeHeaderName(df, "Agent Writing Contract Start Date (Carrier appointment start date)", "Agent Writing Contract Start Date")
        processingExpert.ChangeHeaderName(df, "Agent Writing Contract Status (actually active and cancelled\'s should come in two different files)", "Agent Writing Contract Status")

        #check phone number patterns
        phonePattern =r'\d{3}[^0-9]\d{3}[^0-9]\d{4}'
        processingExpert.CheckColumnsPattern(df, 'Agency Phone Number', phonePattern)
        #processingExpert.CheckPhoneNumbersFormat(df, 'Agent Phone Number', phonePattern)

        try:
            #check email
            emailPattern =r'[a-zA-Z0-9.]+[@][Ff]?[Tt]?[.]?[a-zA-Z]+[.][a-zA-Z]{3}'
            processingExpert.CheckColumnsPattern(df, 'Agent Email Address', emailPattern)


            #check US state
            statesPattern =r'[ACDFGHIKLMNOPRSTUVW][ACDEHIJKLMNORSTUVXYZ]'
            processingExpert.CheckColumnsPattern(df, 'Agency State', statesPattern)


            #data manipulation and visualization bit
            input("Adding Dataframe to app log:")
            app_logger.info(f"Dataframe head :\n\n{df.head(20).to_string()}")

            
            # input("Adding Dataframe [ Agent Name , Agent Writing Contract, Start Date ] filter")
            DfFiltered = df[['Agent Last Name', 'Agent First Name', 'Agency Name', 'Agent Writing Contract Start Date', 'Date when an agent became A2O']]
            app_logger.info(f"Dataframe filtered by [ Agent Name , Agent Writing Contract, Start Date:\n\n{DfFiltered.head(20).to_string} ]:")
            
            # seriesDfFiltered = DfFiltered.groupby('Agency Name')['Date when an agent became A2O'].min() 
   
            # plt.scatter(x=seriesDfFiltered.index, y=seriesDfFiltered)
            # plt.savefig('AgencyByMinDate.png')
            # plt.show()


            input("Adding Dataframe grouped by Agency State to app log:")
            seriesAgentsByState = df.groupby('Agency State')['Agent Id'].count()
            app_logger.info(f"Dataframe Count of Agents grouped by state :\n\n{seriesAgentsByState.to_string()}")
            seriesAgentsByState.plot(kind='bar', fontsize=4)
            plt.savefig('AgencyByState.png')

        except KeyError:
            return error_logger.error("You queueing an incorrect column key. \nPlease check your column names during manipulation")
        except FileNotFoundError:
            return error_logger.error("You are saving a plot to an incorrect path. \nPlease check your column names during manipulation")



        processingExpert.LatestIsProcessed = True

    #Send email of app log to self
    to = "luan.dasilva@smoothstack.com"
    sender = "luan.dasilva@smootstack.com"
    subject = "Automated Log File Email"
    msgHtml = "Log file from app run"
    msgPlain = "Log file from app run"
    
    SendMessage(sender, to, subject, msgHtml, msgPlain,'./app.log')


if __name__ =="__main__":
     main()



# loggers ending
app_logger.info(f"End app log from {__name__}\n{logSeparator}")
error_logger.info(f"End error handler log from {__name__}\n{logSeparator}")

