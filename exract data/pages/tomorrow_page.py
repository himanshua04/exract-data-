from selenium import webdriver
from core.page_factory import PageFactory
import time
from datetime import datetime, timedelta
import os
import logging


class TomorrowPage(PageFactory):

    def __init__(self,driver):
        # It is necessary to to initialise driver as page class member to implement Page Factory
        self.driver = driver
        self.driver.maximize_window()
        self.locators = self.load_locators()
        self.timeout = 5

    def saveExcelFile(self,wb):
        # Get today's date
        presentday = datetime.now() # or presentday = datetime.today()

        # Get Yesterday
        yesterday = presentday - timedelta(1)

        # Get Tomorrow
        tomorrow = presentday + timedelta(1)
        file_name=tomorrow.strftime('%d-%m-%Y')
        #os.chdir(cwd)
        original_path=os.getcwd()
        new_path="test/excel sheet"
        os.chdir(new_path)
        wb.save(file_name+'.xls')
        os.chdir(original_path)
    
    def inisilizeSheetDetails(self,sheet1):
        sheet1.write(0, 0, '#')
        sheet1.write(0, 1, 'Date')
        sheet1.write(0, 2, 'Time')
        sheet1.write(0, 3, 'Country')
        sheet1.write(0, 4, 'League')
        sheet1.write(0, 5, 'Home')
        sheet1.write(0, 6, 'Away')
        sheet1.write(0, 7, 'O15FT')
        sheet1.write(0, 8, 'O25FT')
        sheet1.write(0, 9, 'O35FT')
        sheet1.write(0, 10,'O45FT')
        sheet1.write(0, 11, 'O55FT')
        sheet1.write(0, 12, 'BTTS')
        sheet1.write(0, 13, 'O05HT')
        sheet1.write(0, 14, 'O15HT')
        sheet1.write(0, 15, 'O25HT')
        sheet1.write(0, 16, 'HLT')
        sheet1.write(0, 17, 'ALT')
        sheet1.write(0, 18, 'HFT')
        sheet1.write(0, 19, 'AFT')
        sheet1.write(0, 20, 'HHT') 
        sheet1.write(0, 21, 'AAT')
        sheet1.write(0, 22, 'HHPM')
        sheet1.write(0, 23, 'AAPM')
        sheet1.write(0, 24, 'AGF')
        sheet1.write(0, 25, 'AGA')
        sheet1.write(0, 26, 'ATG')
        sheet1.write(0, 27, 'SR')
        sheet1.write(0, 28, 'CS')
        sheet1.write(0, 29, 'FS')
        sheet1.write(0, 30,'SBH')
        sheet1.write(0, 31, 'CBH')
        sheet1.write(0, 32, 'LAGM')
        sheet1.write(0, 33, 'HG')
        sheet1.write(0, 34, 'AG')
        sheet1.write(0, 35, 'WPL')
        




