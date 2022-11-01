# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 15:59:26 2020

@author: Dallin
"""

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from tkinter import filedialog
# from PIL import ImageTk, ImageTk


def convert ():
    
    print("Starting conversion")
    df = UploadAction() # call the UploadAction function load it in the dataframe
    print("Return from UploadAction")
    print(df)
    datarowcount = df.shape[0]  
    a = np.zeros(shape=(datarowcount,2))
    df2 = pd.DataFrame(a)    
    for n in range(0,datarowcount):
        
        df2.iloc[n,1] = df.iloc[n,0] + df.iloc[n,1] + df.iloc[n,2] + df.iloc[n,3] + df.iloc[n,4] + df.iloc[n,5] + df.iloc[n,6] + df.iloc[n,7]
        df2.iloc[n,0] = df.iloc[n,8]
        
    print(df2)
    plt.plot(df2.iloc[:,0],df2.iloc[:,1])
    exportCSV(df2) #Call the export function 
    #end of function


def exportCSV (df2):

    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    df2.to_csv (export_file_path, index = False, header=True)
    print("File Saved")
    #end of function


def NormPlot (event = None):
    print("Accessed NormPlot")
    top = Toplevel()
    top.title("XRD Plotter")
    appwindow = tk.Tk()
    answer = simpledialog.askinteger("Input", "How many files?",
    parent=appwindow,
    minvalue=0, maxvalue=100)
    print("Number of Files is:", answer)
    
    #end of function


def QuitButton():
    global root
    root.quit()
    #end of function
    

def UploadAction(event = None):
    print("Starting Upload Action")    
    global filename
    filename = filedialog.askopenfilename()
    print('Selected file:', filename)
    
    df = pd.read_csv(
      filename,
      sep = '\s+',
      skiprows=1,
      # header="none"
    )
    print (df)
    print ("Uploading done")
    return df
    #end of function
    
    
#start main run

root = tk.Tk()
#Make the buttons
buttonquit = tk.Button(root, text="Quit", command=root.destroy)
buttonconvert = tk.Button(root, text='Convert', command=convert)
buttonplot = tk.Button(root, text='Normalize and Vertical Stack Plot', command=NormPlot)
#Pack the buttons
buttonquit.pack()
buttonconvert.pack()
buttonplot.pack()
#Run the loops
root.mainloop()

