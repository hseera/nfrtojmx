# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 15:35:47 2020

@author: harinder
"""
import xlrd

def convert_to_yaml(fileName):
    wb = xlrd.open_workbook(fileName)
    sheet = wb.sheet_by_index(0)
    sheet_names = wb.sheet_names()
    
    with open('jmeter.yml', 'w') as outfile:
        outfile.write("---\nName: "+ sheet_names[0] +"\n")
        outfile.write("TestConcurrency: 10\n")
        outfile.write("Threads: \n")
        for i in range(sheet.nrows):
            if (i==(sheet.nrows - 1) or i==0 or i ==1):
                if (i==(sheet.nrows - 1)):
                   outfile.write("TestThroughput: "+ str(sheet.cell_value(i,4)) +"\n")
                else:
                    print("Ignore the row")
            else:
                outfile.write("- Thread:\n")
                ThreadName="   ThreadName: "+ str(sheet.cell_value(i,0)) +"\n"
                outfile.write(ThreadName)
                Throughput="   Throughput: "+ str(sheet.cell_value(i,1)) +"\n"
                outfile.write(Throughput)
    outfile.close()
