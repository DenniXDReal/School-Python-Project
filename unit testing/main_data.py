import numpy as np
import pandas as pd
class VisitorsAnalyticsUtils:

    def loadDataFile(): #To load data files
        df = pd.read_csv("Data/Int_Monthly_Visitor.csv")
        df = pd.DataFrame(df)
        df.columns.values[0] = "Years" #To Remove column 0 with "Years"
        df = df.replace(" na ", "0") #To replace all NA str into int 0
        df = df.replace(',','', regex=True) #To replace all , with empty
        return df



