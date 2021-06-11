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
        sheet1.write(0, 16, 'HHPM',style)
        sheet1.write(0, 17, 'AAPM',style)
        sheet1.write(0, 18, 'AGF',style)
        sheet1.write(0, 19, 'AGA',style)
        sheet1.write(0, 20, 'ATG',style)
        sheet1.write(0, 21, 'SR',style)
        sheet1.write(0, 22, 'CR',style)
        sheet1.write(0, 23, 'CS',style)
        sheet1.write(0, 24, 'FS',style)
        sheet1.write(0, 25,'SBH',style)
        sheet1.write(0, 26, 'CBH',style)
        sheet1.write(0, 27, 'LAGM',style)
        sheet1.write(0, 28, 'O95C',style)
        sheet1.write(0, 29, 'O105C',style)
        sheet1.write(0, 30, 'HG',style)
        sheet1.write(0, 31, 'AG',style)
        sheet1.write(0, 32, 'WPL',style)
        

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
        try:
            data1=self.field1.get_text()
            data1=data1.split(" ")
    
            #column 0
            sheet1.write(row,0,row)
            #column 1 
            sheet1.write(row,1,data1[1]+data1[2])
    
            #column 2
            sheet1.write(row,2,data1[3])
        except Exception :
            logging.warning("for row {row} the coulum 1 and 2 is not present")

        try:
            data2=self.field2.get_text()
            data2=data2.split("-")

            #column 3
            sheet1.write(row,3,data2[0])

            #column 4
            sheet1.write(row,4,data2[1])
        except Exception :
            logging.warning("for row {row} the coulum 3 and 4 is not present")
        
        try:
            data=self.field3.get_text()
            data=data.split(" ")

            #column 5
            sheet1.write(row,5,data[0])

            #column 6
            sheet1.write(row,6,data[2])
        except Exception :
            logging.warning("for row {row} the coulum 5 and 6 is not present")

        
        try:
            #column 7
            custom_locator=self.createCustomLocator("//font[@style='font-size:14px;']",14)
            data=custom_locator.get_text()
            sheet1.write(row,7,data)
        except Exception :
            logging.warning("for row {row} the coulum 7 is not present")
        
        try:
            #column 8
            custom_locator=self.createCustomLocator("//font[@style='font-size:14px;']",15)
            data=custom_locator.get_text()
            sheet1.write(row,8,data)
        except Exception :
            logging.warning("for row {row} the coulum 8 is not present")

        try:
            #column 9
            custom_locator=self.createCustomLocator("//font[@style='font-size:14px;']",16)
            data=custom_locator.get_text()
            sheet1.write(row,9,data)
        except Exception :
            logging.warning("for row {row} the coulum 9 is not present")

        try:
            #column 10
            custom_locator=self.createCustomLocator("//font[@style='font-size:14px;']",17)
            data=custom_locator.get_text()
            sheet1.write(row,10,data)
        except Exception :
            logging.warning("for row {row} the coulum 10 is not present")

        try:
            #column 11
            custom_locator=self.createCustomLocator("//font[@style='font-size:14px;']",18)
            data=custom_locator.get_text()
            sheet1.write(row,11,data)
        except Exception :
            logging.warning("for row {row} the coulum 11 is not present")

        try:
            #column 12
            custom_locator=self.createCustomLocator("//font[@style='font-size:14px;']",19)
            data=custom_locator.get_text()
            sheet1.write(row,12,data)
        except Exception :
            logging.warning("for row {row} the coulum 12 is not present")

        try:
            #column 13
            custom_locator=self.createCustomLocator("//font[@style='font-size:14px;']",20)
            data=custom_locator.get_text()
            sheet1.write(row,13,data)
        except Exception :
            logging.warning("for row {row} the coulum 13 is not present")
        
        try:
            #column 14
            custom_locator=self.createCustomLocator("//font[@style='font-size:14px;']",21)
            data=custom_locator.get_text()
            sheet1.write(row,14,data)
        except Exception :
            logging.warning("for row {row} the coulum 14 is not present")

        try:
            #column 15
            custom_locator=self.createCustomLocator("//font[@style='font-size:14px;']",22)
            data=custom_locator.get_text()
            sheet1.write(row,15,data)
        except Exception :
            logging.warning("for row {row} the coulum 15 is not present")

        try:
            #column 16
            custom_locator=self.createCustomLocator("//table[@cellspacing='0']//tr[@class='trow3']/td[@align='center']/b",3)
            data=custom_locator.get_text()
            sheet1.write(row,16,data)
        except Exception :
            logging.warning("for row {row} the coulum 16 is not present")

        try:
            #column 17
            custom_locator=self.createCustomLocator("//table[@cellspacing='0']//tr[@class='trow3']/td[@align='center']/b",4)
            data=custom_locator.get_text()
            sheet1.write(row,17,data)
        except Exception :
            logging.warning("for row {row} the coulum 17 is not present")

        try:
            #column 18
            custom_locator=self.createCustomLocator("//font[@style='font-size:14px;']",1)
            data=custom_locator.get_text()
            sheet1.write(row,18,data)
        except Exception :
            logging.warning("for row {row} the coulum 18 is not present")

        try:
            #column 19
            custom_locator=self.createCustomLocator("//font[@style='font-size:14px;']",2)
            data=custom_locator.get_text()
            sheet1.write(row,19,data)
        except Exception :
            logging.warning("for row {row} the coulum 19 is not present")

        try:
            #column 20
            custom_locator=self.createCustomLocator("//font[@style='font-size:14px;']",3)
            data=custom_locator.get_text()
            sheet1.write(row,20,data)
        except Exception :
            logging.warning("for row {row} the coulum 20 is not present")

        try:
            #column 21
            custom_locator=self.createCustomLocator("//font[@style='font-size:14px;']",4)
            data=custom_locator.get_text()
            sheet1.write(row,21,data)
        except Exception :
            logging.warning("for row {row} the coulum 21 is not present")

        try:
            #column 22
            custom_locator=self.createCustomLocator("//font[@style='font-size:14px;']",5)
            data=custom_locator.get_text()
            sheet1.write(row,22,data)
        except Exception :
            logging.warning("for row {row} the coulum 22 is not present")

        try:
            #column 23
            custom_locator=self.createCustomLocator("//font[@style='font-size:14px;']",6)
            data=custom_locator.get_text()
            sheet1.write(row,23,data)
        except Exception :
            logging.warning("for row {row} the coulum 23 is not present")

        try:
            #column 24
            custom_locator=self.createCustomLocator("//font[@style='font-size:14px;']",7)
            data=custom_locator.get_text()
            sheet1.write(row,24,data)
        except Exception :
            logging.warning("for row {row} the coulum 24 is not present")
        
        try:
            #column 25
            custom_locator=self.createCustomLocator("//font[@style='font-size:14px;']",8)
            data=custom_locator.get_text()
            sheet1.write(row,25,data)
        except Exception :
            logging.warning("for row {row} the coulum 25 is not present")

        try:
            #column 26
            custom_locator=self.createCustomLocator("//font[@style='font-size:14px;']",9)
            data=custom_locator.get_text()
            sheet1.write(row,26,data)
        except Exception :
            logging.warning("for row {row} the coulum 26 is not present")

        try:
            #column 27
            data=self.field4.get_text()
            sheet1.write(row,27,data)
        except Exception :
            logging.warning("for row {row} the coulum 27 is not present")

        try:
            #column 28
            custom_locator=self.createCustomLocator("//font[@style='font-size:14px;']",26)
            data=custom_locator.get_text()
            sheet1.write(row,28,data)
        except Exception :
            logging.warning("for row {row} the coulum 28 is not present")

        try:
            #column 29
            custom_locator=self.createCustomLocator("//font[@style='font-size:14px;']",27)
            data=custom_locator.get_text()
            sheet1.write(row,29,data)
        except Exception :
            logging.warning("for row {row} the coulum 29 is not present")

        try:
            #column 32
            data=self.driver.current_url()
            sheet1.write(row,32,data)
        except Exception :
            logging.warning("for row {row} the coulum 32 is not present")
        





    def createCustomLocator(self,locator_name,index=1):
        _locator = ["XPATH"]
        _locator.append(f"({locator_name})[{index}]")
        self.locators.update({"custom_locator":[_locator]})
        if(selenium_helper.is_element_present(self.locators["custom_locator"][0],0)):
            self.custom_locator.scroll_to_element()
        return self.custom_locator





