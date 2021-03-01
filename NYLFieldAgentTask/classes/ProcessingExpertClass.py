from datetime import date
import logging

# use Expert to :
# Assign responsibility to class that has information required to fulfill responsibility.


class ProcessingExpert:
    LatestFile : str
    LatestIsProcessed: bool

    app_logger : logging
    error_logger : logging

    def __init__(self,  _app_logger, _error_logger, latestFile, latestsIsProcessed):
        self.error_logger = _error_logger
        self.app_logger = _app_logger
        
        self.LatestFile = latestFile
        self.LatestIsProcessed = latestsIsProcessed

    def ChangeHeaderName(self, df,  UndesiredHeader, DesiredHeader):
        if UndesiredHeader in  list(df.columns.values):
            df.rename(columns={UndesiredHeader: DesiredHeader}  , inplace=True)
            print(f"CSV column {UndesiredHeader} renamed to {DesiredHeader}")

    def CheckColumnsPattern(self, df, column, pattern):
        try:
            new_df = df[~df[column].str.contains(pattern)]
            self.app_logger.info(f"Logging from {__name__}: Getting all rows with invalid {column}:\n\nDataframe: \n\n{new_df.to_string()}")
        except KeyError:
            self.error_logger.error("There is no column with that specified name! We can't validate it if it doesn't exist!")
