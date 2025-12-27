#-------------------------------------------
# IMPORTING REQUIRED LIBRARIES & CSV FILES
#-------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pathlib 
pd.set_option ('display.max_columns',500) #Output Setting For Display Columns
pd.set_option('display.width', 1000)

csv_path = pathlib.Path(__file__).with_name("crime_csv.csv")
df_crimes=pd.read_csv(csv_path) #Importing For Driven Program To Access CSV File
print(df_crimes)
#-------------------------
#FUNCTIONS
#-------------------------
def menudrive():
    while True:
        print()          #ADDING SPACE AFTER ONE MENU GETS DRIVED
        print()
        print("\t\t\tCRIME CASES ANALYSIS SYSTEM")
        print("\t\t", "_"*40)
        print()
        print("~"*40)
        print("1-Read csv/excel file")
        print("2-Attributes of Csv/excel DataFrame")
        print("3-Analyse the Data")
        print("4-Manipulation of Dataset")
        print("5-Visual Representation of CSV file")
        print("6-EXIT")
        print("~"*40)
        print ()
        #---------------------------------
        #MAIN PREFERENCES FOR DEF ANALYSIS
        #---------------------------------
        Preference=int (input("➥Enter Your Preference (1-6): "))
        if Preference ==1:
             readcsv()
        elif Preference ==2:
             attribute_df ()
        elif Preference ==3:
             func_Analyse ()
        elif Preference ==4:
             Data_update()
        elif Preference ==5:
             Visualize()
        elif Preference ==6:
            x=input("Do you really want to exit?" "YES / NO ")
            if x =="YES":
                print ("Thanks for using menu driven program!!")
                print ("NOW EXITING.....")
                break
            else:
                continue
        else:
                 print("Please print the appropriate number")
                 continue
#--------------------------------------------------
# FUNCTION TO READ AND CREATE CSV FILE TO DATAFRAME
#--------------------------------------------------
def readcsv():
    df_crimes=pd.read_csv("crime_csv.csv")
    print (df_crimes)

#-------------------------------------    
#FUNCTIONS FOR ATTRIBUTES OF DATAFRAME
#-------------------------------------
def attribute_df() :
    while True:
        print()
        print()
        print("\t\t\tATTRIBUTES MENU")
        print("\t\t", "-"*30)
        print("1-indexes in DataFrame")
        print("2-Columns in DataFrame")
        print("3-Axes in DataFrame")
        print("4-size of DataFrame (Row * Column)")
        print("5-shape of DataFrame (Row, Column)")
        print()
        #---------------------------------
        #PREFERENCES CODE FOR ATTRIBUTES
        #---------------------------------
        Preference = int(input("Enter your Preference (1-5):"))
        print()
        if Preference ==1:
            print("The Range of The Indexes Are:-")
            print (df_crimes.index)
        elif Preference ==2:
            ("The Names of The Columns Are:-")
            print (df_crimes.columns)
        elif Preference ==3:
            print("The Axes of DataFrame Is:-")
            print (df_crimes.axes)
        elif Preference ==4:
            print("The Size of The DataFrame Is:-")
            print(df_crimes.size)
        elif Preference ==5:
            print("The Shape Of The DataFrame Is:-")
            print(df_crimes.shape)
            break
        else:
            print("-->please enter appropriate number")
            continue
#----------------------------       
# FUNCTION FOR DATA ANALYSIS
#----------------------------
def func_Analyse() :
        while True:
            print()
            print()
            print("\t\t\tDATA ANALYSIS MENU")
            print("\t\t", "_"*35)
            print("1-Display The Top Crimes")
            print("2-Display The Bottom Crimes")
            print("3-Display Specific COLUMNS Details")
            print("4-Display Specific ROWS Details")
            print("5-Display Crimes In Desending Order")
            print("6-Display Crimes In Ascending order")
            print("7-Display Data Crime Wise")
            print("8-Display Top N Crimes Commited")
            print("9-Display Lowest N Crimes Commited")
            print("10-Back To Main Menu")
            print()
            
            #----------------------------------            
            #PREFERENCES CODE FOR DATA ANALYSIS
            #----------------------------------
            Preference = int (input("Enter your Preference: "))
            print ()
            if Preference ==1:
                n=int(input("How many Top Rows To Be Displayed?:"))
                print (df_crimes.head (n))
                
            elif Preference ==2:
                nx=int (input("How many Bottom Rows To Be Displayed?:"))
                print (df_crimes.tail (nx))
        
            elif Preference ==3:
                print (df_crimes.columns)
                column_name = input("Enter the column name you want to display: ")
                if column_name in df_crimes.columns:
                        print (df_crimes [column_name])
                        
            elif Preference ==4:
                 row_index = int(input("Enter the row index (0 to 50): "))
                 if 0 <= row_index < len(df_crimes):
                      print (f"\nData In Row (row_index) :")
                      print (df_crimes.iloc[row_index])
                      
            elif Preference ==5:
                print (df_crimes.sort_values (by="CRIMES", ascending=False))
            
            elif Preference ==6:
                print (df_crimes.sort_values (by="CRIMES"))
            
            elif Preference ==7:
                for (row, rowseries) in df_crimes.iterrows():
                    print ("Row INDEX", row)
                    print ("Containing:")
                    print (rowseries)
                    
            elif Preference ==8:
                N_Crimes=int (input ("How Manu Top Crimes In INDIA You Want To Display? "))
                cases=df_crimes.sort_values (by='ALL_INDIA', ascending=False)
                Highest_cs=cases.head (N_Crimes)
                print ("HIGHEST CASES ARE :-")
                print (Highest_cs)
                
            elif Preference ==9:
                N_Crimes=int (input ("How Many Bottom Crimes In INDIA You Want To Display? "))
                cases=df_crimes.sort_values (by='ALL_INDIA', ascending = False)
                Highest_cs=cases.tail(N_Crimes)
                print("HIGHEST CASES ARE :- ")
                print (Highest_cs)
                
            elif Preference == 10:
                 break
                
            else:
                 print("Please Enter Appropriate Number !!!")
                 continue
#---------------------------
#FUNCTION FOR DATA UPDATION
#---------------------------
def Data_update():
        while True:
            print()
            print()
            print("\t\t\tUPDATION OF DATA")
            print("\t\t", "-"*30)
            print()
            print("1-To Add A New Crime")
            print("2-To Add A New Column")
            print("3-To Delete A Crime")
            print("4-To Remove A Column")
            print("5-Back To Main Menu")
            print()

            #-----------------------------------
            #PREFERENCES CODE FOR DATA UPDATION
            #-----------------------------------
            Preference= int (input("Enter Your Preference:- "))
            if Preference ==1:
                crime=input ("Enter The Name Of The Crime:")
                Ind_case=int (input ("Enter The Number Of The Cases in India:"))
                cs_py=int(input("Enter The Number Of Cases in Previous Year:"))
                St_high=input ("Enter The Name Of State which Has Highest Cases: ")
                Wrld_no=input ("Enter The Name Of Country which Has Highest Cases: ")
                ttl_cs=int(input ("Enter The Total Number of Cases Are:"))
                df_crimes.loc [len (df_crimes)+1]=[crime, Ind_case, cs_py, St_high, Wrld_no, ttl_cs]
                print (df_crimes)
                print ("One CRIME has Been SUCCESSFULLY Added !!")
                
            elif Preference ==2:
                print (df_crimes.axes)
                col=eval (input("Enter Values For The Column To Be Added (use:'[] ') : -") )
                nm=input ("Enter Name of NEW Column:- ")
                df_crimes [nm]=col
                print (df_crimes)
            
            elif Preference ==3:
                print (df_crimes ['CRIMES'])
                NM=input("Enter Crime Name You Want To Delete:")
                response=input ("Do you really want to remove this crime from Dataset (YES/NO) ?")
                if response == "YES":
                    df_crimes.drop (df_crimes [df_crimes ['CRIMES']==NM].index, inplace=True)
                    print ("Crime", NM, "Has Been SUCCESSFULLY DELETED....")
                    print(df_crimes)
                else:
                    print ("Crime is not found....")
            elif Preference ==4:
                print (df_crimes.columns)
                d=input("Enter Column Name: ")
                r=input ("Do you really want to remove this column? (YES/NO) ")
                if r =="YES":
                    df_crimes.drop (d, axis=1, inplace=True)
                    print ("Column", d, "Has Been SUCCESSFULLY DELETED...")
            elif Preference == 5:
                break
                     
            else:
                 print("-->please enter appropriate number")
                 continue
#---------------------------------------
#FUNCTION FOR DATA VISUAL REPRESENTATION
#---------------------------------------
def Visualize():
    while True:
        print()
        print()
        print("\t\t\tGRAPHING AND CHARTING MENU")
        print("\t\t", "_"*35)
        print("1-Line Chart")
        print("2-Bar Chart")
        print("3-Histogram")
        print("4-Back to Main Menu")
        print()
        #-----------------------------------------
        #PREFERENCES CODE FOR DATA VISUALTIZATION
        #-----------------------------------------
        Preference= int(input("Enter Your Preference:-"))
        if Preference==1:
            df_crimes.plot (kind='line')
            plt.title("LINE GRAPH ON CRIME CASE ANALYSIS SYSTEM")
            plt.legend ()
            plt.show()
        elif Preference==2:
            df_crimes.plot (kind='bar')
            plt.title("BAR GRAPH ON CRIME CASE ANALYSIS SYSTEM")
            plt.legend ()
            plt.show()

        elif Preference==3:
            df_crimes.plot (kind='hist')
            plt.title("GRAPH ON CRIME CASE ANALYSIS SYSTEM")
            plt.legend ()
            plt.show()

        elif Preference == 4:
            break
        
        else:
            print("Please Enter Appropriate Number:")
            continue
        break
    
        
menudrive ()
