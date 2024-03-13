# %%
import numpy as np
import pandas as pd
import statistics

class VisitorsAnalyticsUtils:
    def __init__(self):
        self.years = yearlist
        self.regions = worldlist
        self.timeperiod = timeperiod

    def loadDataFile(): #To load data files
        df = pd.read_csv("Data/Int_Monthly_Visitor.csv")
        df = pd.DataFrame(df)
        df.columns.values[0] = "Years" #To Remove column 0 with "Years"
        df = df.replace(" na ", "0") #To replace all NA str into int 0
        df = df.replace(',','', regex=True) #To replace all , with empty
        return df
    
    
    def parseData(self, yearlist, worldlist,timeperiod):
        #This is to calculate the min max etc.
        def minval():
            dfsplit = df.iloc[rows,0].to_string(index = False).split() #This is to convert all into str, removing index and splitting all
            s = [int(x) for x in dfsplit if x.isdigit()] #This is to check if its digit
            dfmin = min(s)
            return dfmin
        def maxval():
            dfsplit = df.iloc[rows,0].to_string(index = False).split()
            s = [int(x) for x in dfsplit if x.isdigit()]
            dfmax = max(s)
            return dfmax
        def countval():
            dfsplit = df.iloc[rows,0].to_string(index = False).split()
            s = [int(x) for x in dfsplit if x.isdigit()]
            dfcount = len(s)
            return dfcount
        def stdval():
            dfsplit = df.iloc[rows,0].to_string(index = False).split()
            s = [int(x) for x in dfsplit if x.isdigit()]
            dfstd = statistics.stdev(s)
            return dfstd
        def meanval():
            dfsplit = df.iloc[rows,0].to_string(index = False).split()
            s = [int(x) for x in dfsplit if x.isdigit()]
            dfmean = statistics.mean(s)
            return dfmean
        def quanval(p):
            dfsplit = df.iloc[rows,0].to_string(index = False).split()
            s = [int(x) for x in dfsplit if x.isdigit()]
            dfquan = np.percentile(s, p)   #
            return dfquan
        x=0
        while x != numofrows: #To get check for years
            df_filter = df.iloc[x, 0]
            if any(year in df_filter for year in yearlist): #This is to get the exact location of the rows that contains in yearlists
                rows.append(x) #This is to append all rows which contains inside yearlist here to use for the other codes
            x += 1
        #This is to filtered both the years and countries together.
        countryfilted = df.loc[rows, worldlist]

        print("""
       _________________________________________________ 
      |           First 5 row of data loaded            |
      |_________________________________________________|          
        """)
        print(countryfilted.head(5)) #Print first 5 of filtered data
        print("""
       _________________________________________________ 
      |            Last 5 row of data loaded            |
      |_________________________________________________|          
        """)
        print(countryfilted.tail(5)) #Print last 5 of filtered Data

        print("""
       _________________________________________________ 
      |               Parse Data (Region)               |
      |_________________________________________________|       
        """)
        print(countryfilted.info()) #To get the informations of the countries
        

        print(f"""
       _________________________________________________ 
      |                Parse Data (Years)               |
      |_________________________________________________|              
       count: {countval()}                              
       mean: {meanval()}                                
       std:  {stdval()}                                 
       min: {minval()}                                  
       25%: {quanval(25)}                               
       50%: {quanval(50)}                                
       75%: {quanval(75)}                               
       max: {maxval()}                                  
       Name: year, dtype: {df.Years.dtypes}
                                                            """)
        return countryfilted                                                                                                                      

    def getTop3Countries(self, x):
        res = []
        x=0
        q=0
        while q!=len(worldlist): #First loops is for the countries
            x=0
            while x!= len(rows): #Second loops is to append the numbers from the rows into a list
                num = (df.loc[rows[x],worldlist[q]])
                res.append(num)
                x+=1
            s = [int(p) for p in res if p.isdigit()] #This is to check if its digit
            total = sum(s)
            datalist[(q)] = { #This is to make it into a nested dictionary
            "Country":worldlist[q],
            "Total":total
            }
            q+=1
        df_result = pd.DataFrame.from_dict(datalist, orient='index') #This is to convert it into a DataFrame
        df_result = pd.DataFrame(df_result)
        df_result = df_result.sort_values(by="Total",ascending=False).head(3) #This is to get the top 3 countries
        df_result = df_result.to_string(index=False, header=False) #This is to print out only top 3 countries without header and indexs
        
        print(f"""
       _________________________________________________
      |                 Top 3 countries                 |
      |_________________________________________________|
        """)
        print(df_result)
def countriesmenu():
    print("""
       _________________________________________________ 
      |                   Enter Region                  |
      |_________________________________________________|
      |             Enter 1 for Year: Asia              | 
      |            Enter 2 for Year: Europe             |
      |            Enter 3 for Year: Others             | 
      |_________________________________________________|  
""")

df = VisitorsAnalyticsUtils.loadDataFile() #To load data files
datalist = {} #To make a dictionary
yearlist = [] #This is to store the year periods after users input
worldlist = [] #This is to store the regions after users input
timeperiod = 0 #This is to store the string text of time period after user input
rows = []
col = []
numofrows = len(df) #To get number of rows before filtered
numofcol = len(df.columns) #To get number of columns before filtered

#Region List
asialist = ['Years',' Brunei Darussalam ', ' Indonesia ', ' Malaysia ', ' Philippines ',' Thailand ', ' Viet Nam ', ' Myanmar ', ' Japan ',\
            ' Hong Kong ', ' China ', ' Taiwan ', ' Korea, Republic Of ',\
            ' India ', ' Pakistan ', ' Sri Lanka ', ' Saudi Arabia ', ' Kuwait ', ' UAE ']
europelist = ['Years',' United Kingdom ', ' Germany ', ' France ', ' Italy ', ' Netherlands ', ' Greece ', ' Belgium & Luxembourg ',\
              ' Switzerland ', ' Austria ', ' Scandinavia ', ' CIS & Eastern Europe ']
otherlist = ['Years',' USA ', ' Canada ', ' Australia ', ' New Zealand ', ' Africa ']
#Year List
yearlist1 = ['1978', '1979' ,'1980', '1981', '1982', '1983','1984','1985', '1986', '1987']
yearlist2 = ['1988', '1989' ,'1990', '1991', '1992', '1993','1994','1995', '1996', '1997']
yearlist3 = ['1998', '1999' ,'2000', '2001', '2002', '2003','2004','2005', '2006', '2007']
yearlist4 = ['2008', '2009' ,'2010', '2011', '2012', '2013','2014','2015', '2016', '2017']

#Starting Page Menu
print(""" 
       _________________________________________________
      |                                                 | 
      | ***********Welcome to Group 1 Project********** | 
      |                                                 | 
      |-------------------------------------------------|
      |                                                 |
      |_________________________________________________| 
      |                Enter Year Period                | 
      |_________________________________________________|
      |          Enter 1 for Year: 1978 - 1987          | 
      |          Enter 2 for Year: 1988 - 1997          | 
      |          Enter 3 for Year: 1998 - 2007          | 
      |          Enter 4 for Year: 2008 - 2017          |
      |                                                 | 
      |_________________________________________________| """)
yearperiod = input("")
if yearperiod == "1":
    yearlist = yearlist1 #This is to copy  yearlist1 over into yearlist for the other codes line above to work.
    timeperiod = "1978 Jan to 1987 Dec" #This is to copy string over into timeperiod for the other codes line above to work.
    countriesmenu()
    countries = input("")
elif yearperiod == "2":
    yearlist = yearlist2
    timeperiod = "1988 Jan to 1997 Dec"
    countriesmenu()
    countries = input("")
elif yearperiod == "3":
    yearlist = yearlist3
    timeperiod = "1998 Jan to 2007 Dec"
    countriesmenu()
    countries = input("")
elif yearperiod == "4":
    yearlist = yearlist4
    timeperiod = "2008 Jan to 2017 Dec"
    countriesmenu()
    countries = input("")
else:
    print("Invalid Value Entered.")  

while yearperiod == "1" or yearperiod =="2"or yearperiod =="3"or yearperiod =="4": #This is to check for invalid input before and after years and countries input.
    if countries == "1":
        worldlist = asialist #This is to copy asialist over into yearlist for the other codes line above to work.
        output = VisitorsAnalyticsUtils()
        countryfiltered = output.parseData(yearlist, worldlist,timeperiod) #To save country filtered output
        output.getTop3Countries(0)
        break
    elif countries == "2":
        worldlist = europelist
        output = VisitorsAnalyticsUtils()
        countryfiltered = output.parseData(yearlist, worldlist,timeperiod)
        output.getTop3Countries(0)
        break
    elif countries == "3":
        worldlist = otherlist
        output = VisitorsAnalyticsUtils()
        countryfiltered = output.parseData(yearlist, worldlist,timeperiod) 
        output.getTop3Countries(0)
        break
    else:
        print("Invalid Value Entered.")
        break 
      





