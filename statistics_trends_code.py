# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 18:44:29 2023

@author: sware
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 21:00:33 2023

@author: sware
"""
#import all the necessary python modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#define a fucntion to read the csv files containing world bank data
def readfile(filename): #accept filename as the argument
    df = pd.read_csv(filename) #read the data from csv file into df
    return df #return the data read to the function call

#define a function to find the transpose of the data to plot the graphs in a meaningful format
def transpose(df): #accept the filename as argument
    df_transpose = df.set_index('Country Name').transpose() #call predefined transpose function and store the result into df_transpose
    return df_transpose #return the resultant data to the function call

#define a function to filter the data ie to select only the 5 countries
def filter_data(df):
    df =df[['Country Name','2000','2003','2006','2009','2012','2015']] #select the column names including years that needs to be processed
    df =df[(df['Country Name']=='Afghanistan') |  #select the country names that needs to be processed
           (df['Country Name']=='Brazil') |
           (df['Country Name']=='Jamaica') |
           (df['Country Name']=='Germany') |
           (df['Country Name']=='Spain') ]     
    return df

#define a function barchart for representing the data in multiple barchart format for comparison
def barplot(db, ylab, title): #accept the data file, ylabel and title of the graph as arguments
    plt.figure(figsize =(25, 18)) #set the size of the graph
    width = 0.1 #set the width of each bar
    ax = plt.subplot(1,1,1)
    x = np.arange(5) 
    #call the function bar and assign the required values to the arguments ie value for the X axis, Y axis, label, the thickness of each bar, the width
    bar1 = ax.bar(x, db["2000"], width, label ='2000')
    bar2 = ax.bar(x+width, db["2003"], width, label ='2003')
    bar3 = ax.bar(x+width*2, db["2006"], width, label ='2006')
    bar4 = ax.bar(x+width*3, db["2009"], width, label ='2009')
    bar5 = ax.bar(x+width*4, db["2012"], width, label ='2012')
    bar6 = ax.bar(x+width*5, db["2015"], width, label ='2015')
    
    ax.set_xlabel("Countries",fontsize=50)#set the label to be displayed on x axis with fontsize 
    ax.set_ylabel(ylab,fontsize=50)#set the label to be displayed on y axis with fontsize 
    ax.set_title(title,fontsize=50)#set the title of the graph to be displayed with fontsize 
    ax.set_xticks(x, Countries,fontsize=50,rotation=90)#set the xtick value with fontsize and degree of rotation
    ax.legend(fontsize=50, bbox_to_anchor=(1.3, 1), loc="upper right")#call the legedn function to represent the labels
    plt.show() #call the show function to display the bar chart

#define a function for representing data in the form of a line graph
def lineplot(df,ylab,title): #accept the data file, ylabel and title as arguments
    for i in range(len(Countries)): #initiate for loop to read all the 5 countries and to display their corresponding line graphs
        plt.plot(df.index, df[Countries[i]], label = Countries[i])
    plt.title(title,fontsize=10) #set the title of the graph to be displayed with fontsize
    plt.xlabel("Year", fontsize =10) #set the label to be displayed on the x-axis with fontsize
    plt.ylabel(ylab, fontsize =10) #set the label to be displayed on the y-axis with fontsize
    plt.xticks(rotation = 90) #set the xtick value with fontsize and degree of rotation
    plt.legend(bbox_to_anchor=(1.3, 1), loc ="upper right") #call the legedn function to represent the labels
    plt.show() #call the show function to display the bar chart
    
#define a statistical function to calculate the mean value
def mean_val(data): #accept data as argument 
    data = data.fillna(0) #replace the NaN values with 0 for getting proper result
    mean = data.mean() #call predefined mean() to calculate the mean
    return mean #return the result back to the function call
    
Countries = ['Afghanistan', 'Brazil','Jamaica','Germany','Spain'] #initialize array with the desired 5 country names 

#read the data set of Access to clean fuels
fuel_data =readfile(r"C:\Users\sware\OneDrive\Desktop\Data Science\ADS-ASSIGNMENT 2-REWORK\Access to clean fuels.csv")
fuel_filt = filter_data(fuel_data) #call the filter function to filter out only the datas of the desired countries 

#read the data set of Access to electricity
electricity_data =readfile(r"C:\Users\sware\OneDrive\Desktop\Data Science\ADS-ASSIGNMENT 2-REWORK\Access to electricity.csv")
electricity_filt = filter_data(electricity_data) #call the filter function to filter out only the datas of the desired countries 

#read the data set of Annual freshwater withdrawal
water_data =readfile(r"C:\Users\sware\OneDrive\Desktop\Data Science\ADS-ASSIGNMENT 2-REWORK\Annual freshwater withdrawal.csv")
water_filt = filter_data(water_data) #call the filter function to filter out only the datas of the desired countries 

#read the dataset of land area
land =readfile(r"C:\Users\sware\OneDrive\Desktop\Data Science\ADS-ASSIGNMENT 2-REWORK\land area.csv")
land_filt = filter_data(land) #call the filter function to filter out only the datas of the desired countries 

#call the barplot function to print bar graphs of access to electricity and fuels data
barplot(electricity_filt,"% of population ","Access to electricity")
barplot(fuel_filt,"% of population ","Access to clean fuels and technologies for cooking")

#call he transpose and lineplot functions to find the transpose of the data file and to print the line graph
water_trans = transpose(water_filt)
lineplot(dwt,"% of water ","Freshwater withdrawal")
land_trans = transpose(land_filt)
lineplot(land_trans,"land area(sq.km) ","Land area available")

#call the mean function to calculate and write the result into a csv file
mean = mean_val(water_trans)
mean = mean.to_csv(r"C:\Users\sware\OneDrive\Desktop\Data Science\ADS-ASSIGNMENT 2-REWORK\Mean Values.csv")

    

    
    
