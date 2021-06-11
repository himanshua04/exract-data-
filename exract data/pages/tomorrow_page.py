from selenium import webdriver
from core.page_factory import PageFactory
import time
from datetime import datetime, timedelta
import os
import xlwt
from xlwt import Workbook
import logging
from helper import selenium_helper


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
        style = xlwt.easyxf('font: bold 1')
        sheet1.write(0, 0, '#',style)
        sheet1.write(0, 1, 'Date',style)
        sheet1.write(0, 2, 'Time',style)
        sheet1.write(0, 3, 'Country',style)
        sheet1.write(0, 4, 'League',style)
        sheet1.write(0, 5, 'Home',style)
        sheet1.write(0, 6, 'Away',style)
        sheet1.write(0, 7, 'O15FT',style)
        sheet1.write(0, 8, 'O25FT',style)
        sheet1.write(0, 9, 'O35FT',style)
        sheet1.write(0, 10,'O45FT',style)
        sheet1.write(0, 11, 'O55FT',style)
        sheet1.write(0, 12, 'BTTS',style)
        sheet1.write(0, 13, 'O05HT',style)
        sheet1.write(0, 14, 'O15HT',style)
        sheet1.write(0, 15, 'O25HT',style)
        sheet1.write(0, 16, 'HLT',style)
        sheet1.write(0, 17, 'ALT',style)
        sheet1.write(0, 18, 'HFT',style)
        sheet1.write(0, 19, 'AFT',style)
        sheet1.write(0, 20, 'HHT',style) 
        sheet1.write(0, 21, 'AAT',style)
        sheet1.write(0, 22, 'HHPM',style)
        sheet1.write(0, 23, 'AAPM',style)
        sheet1.write(0, 24, 'AGF',style)
        sheet1.write(0, 25, 'AGA',style)
        sheet1.write(0, 26, 'ATG',style)
        sheet1.write(0, 27, 'SR',style)
        sheet1.write(0, 28, 'CS',style)
        sheet1.write(0, 29, 'FS',style)
        sheet1.write(0, 30,'SBH',style)
        sheet1.write(0, 31, 'CBH',style)
        sheet1.write(0, 32, 'LAGM',style)
        sheet1.write(0, 33, 'HG',style)
        sheet1.write(0, 34, 'AG',style)
        sheet1.write(0, 35, 'WPL',style)
        

    def goToUrl(self,url):
        self.driver.get(url)
        if(selenium_helper.is_element_present(self.locators["btn_agree"][0],5)):
            self.btn_agree.click_button()
        self.show_all_matches.click_button()

    def clickOnStats(self,stats_locator,):
        stats_locator.scroll_to_element()
        stats_locator.click_button()
        if(selenium_helper.is_element_present(self.locators["cross_add"][0],2)):
            self.cross_add.click_button()
        if(selenium_helper.is_element_present(self.locators["ad_close"][0],2)):
            self.ad_close.click_button()
    
    def startProcessing(self,stats_locator,sheet1):

        number_of_stats=self.btn_stats.get_all_elements()
        logging.warning(len(number_of_stats))
        #coustomize locator
        _locator = ["XPATH"]
        _locator.append(f"({stats_locator})[5]")
        self.locators.update({"dynamic_locator":[_locator]})
        self.clickOnStats(self.dynamic_locator)
        i=1
        self.extractDataTomorrow(i,sheet1)
    
    def extractDataTomorrow(self,row,sheet1):
        data1=self.field1.get_text()
        data1=data1.split(" ")

        #column 0
        sheet1.write(row,0,row)
        #column 1 
        sheet1.write(row,1,data1[1]+data1[2])

        #column 2
        sheet1.write(row,2,data1[3])




