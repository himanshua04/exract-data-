from selenium import webdriver
from core.page_factory import PageFactory
import time
from datetime import datetime, timedelta
import os
import xlwt
import xlrd
from xlutils.copy import copy
import logging
from helper import selenium_helper
row_number=1
from xlrd import open_workbook


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
        if(selenium_helper.is_element_present(self.locators["btn_agree"][0],1)):
            self.btn_agree.click_button()
        self.show_all_matches.scroll_to_element()
        self.show_all_matches.click_button()

    def clickOnStats(self,stats_locator,):
        stats_locator.scroll_to_element()
        stats_locator.click_button()
        if(selenium_helper.is_element_present(self.locators["cross_add"][0],0)):
            self.cross_add.click_button()
        if(selenium_helper.is_element_present(self.locators["ad_close"][0],0)):
            self.ad_close.click_button()
    
    def startProcessing(self,stats_locator,sheet1,tomorrow_url):

        number_of_stats=self.btn_stats.get_all_elements()
        loop_run=len(number_of_stats)+1
        logging.warning(loop_run)
        for row in range (1,loop_run):
            #coustomize locator
            self.goToUrl(tomorrow_url)
            _locator = ["XPATH"]
            _locator.append(f"({stats_locator})[{row}]")
            self.locators.update({"dynamic_locator":[_locator]})
            self.clickOnStats(self.dynamic_locator)
            self.extractDataTomorrow(sheet1)
            
    
    def extractDataTomorrow(self,sheet1):
        global row_number
        
        try:
            data1=self.field1.get_text()
            data1=data1.split(" ")  
            #column 0
            sheet1.write(row_number,0,row_number)
            #column 1 
            sheet1.write(row_number,1,data1[1]+data1[2])
    
            #column 2
            sheet1.write(row_number,2,data1[3])
        except Exception :
            logging.warning(f"for row {row_number} the coulum 1 and 2 is not present")
            return 

        try:
            data2=self.field2.get_text()
            data2=data2.split(" - ")

            #column 3
            sheet1.write(row_number,3,data2[0])

            #column 4
            sheet1.write(row_number,4,data2[1])
        except Exception :
            logging.warning(f"for row_number {row_number} the coulum 3 and 4 is not present")
        
        try:
            data=self.field3.get_text()
            data=data.split(" vs ")

            #column 5
            sheet1.write(row_number,5,data[0])

            #column 6
            sheet1.write(row_number,6,data[1])
        except Exception :
            logging.warning(f"for row_number {row_number} the coulum 5 and 6 is not present")

        
        try:
            #column 7
            custom_locator=self.createCustomLocator("//td[text()='Over 1.5 goals']/parent::tr/td/font[@style='font-size:14px;']")
            data=custom_locator.get_text()
            sheet1.write(row_number,7,data)
        except Exception :
            logging.warning(f"for row_number {row_number} the coulum 7 is not present")
        
        try:
            #column 8
            custom_locator=self.createCustomLocator("//td[text()='Over 2.5 goals']/parent::tr/td/font[@style='font-size:14px;']")
            data=custom_locator.get_text()
            sheet1.write(row_number,8,data)
        except Exception :
            logging.warning(f"for row_number {row_number} the coulum 8 is not present")

        try:
            #column 9
            custom_locator=self.createCustomLocator("//td[text()='Over 3.5 goals']/parent::tr/td/font[@style='font-size:14px;']")
            data=custom_locator.get_text()
            sheet1.write(row_number,9,data)
        except Exception :
            logging.warning(f"for row_number {row_number} the coulum 9 is not present")

        try:
            #column 10
            custom_locator=self.createCustomLocator("//td[text()='Over 4.5 goals']/parent::tr/td/font[@style='font-size:14px;']")
            data=custom_locator.get_text()
            sheet1.write(row_number,10,data)
        except Exception :
            logging.warning(f"for row_number {row_number} the coulum 10 is not present")

        try:
            #column 11
            custom_locator=self.createCustomLocator("//td[text()='Over 5.5 goals']/parent::tr/td/font[@style='font-size:14px;']")
            data=custom_locator.get_text()
            sheet1.write(row_number,11,data)
        except Exception :
            logging.warning(f"for row_number {row_number} the coulum 11 is not present")

        try:
            #column 12
            custom_locator=self.createCustomLocator("//td[text()='Both teams scored']/parent::tr/td/font[@style='font-size:14px;']")
            data=custom_locator.get_text()
            sheet1.write(row_number,12,data)
        except Exception :
            logging.warning(f"for row_number {row_number} the coulum 12 is not present")

        try:
            #column 13
            custom_locator=self.createCustomLocator("//td[text()='Over 0.5 g. at halftime']/parent::tr/td/font[@style='font-size:14px;']")
            data=custom_locator.get_text()
            sheet1.write(row_number,13,data)
        except Exception :
            logging.warning(f"for row_number {row_number} the coulum 13 is not present")
        
        try:
            #column 14
            custom_locator=self.createCustomLocator("//td[text()='Over 1.5 g. at halftime']/parent::tr/td/font[@style='font-size:14px;']")
            data=custom_locator.get_text()
            sheet1.write(row_number,14,data)
        except Exception :
            logging.warning(f"for row_number {row_number} the coulum 14 is not present")

        try:
            #column 15
            custom_locator=self.createCustomLocator("//td[text()='Over 2.5 g. at halftime']/parent::tr/td/font[@style='font-size:14px;']")
            data=custom_locator.get_text()
            sheet1.write(row_number,15,data)
        except Exception :
            logging.warning(f"for row_number {row_number} the coulum 15 is not present")

        try:
            #column 16
            custom_locator=self.createCustomLocator("//table[@cellspacing='0']//tr[@class='trow3']/td[@align='center']/b",3)
            data=custom_locator.get_text()
            sheet1.write(row_number,16,data)
        except Exception :
            logging.warning(f"for row_number {row_number} the coulum 16 is not present")

        try:
            #column 17
            custom_locator=self.createCustomLocator("//table[@cellspacing='0']//tr[@class='trow3']/td[@align='center']/b",4)
            data=custom_locator.get_text()
            sheet1.write(row_number,17,data)
        except Exception :
            logging.warning(f"for row_number {row_number} the coulum 17 is not present")

        try:
            #column 18
            custom_locator=self.createCustomLocator("//td[text()='Avg Goals For']/parent::tr/td/font[@style='font-size:14px;']",1)
            data=custom_locator.get_text()
            sheet1.write(row_number,18,data)
        except Exception :
            logging.warning(f"for row_number {row_number} the coulum 18 is not present")

        try:
            #column 19
            custom_locator=self.createCustomLocator("//td[text()='Avg Goals For']/parent::tr/td/font[@style='font-size:14px;']",2)
            data=custom_locator.get_text()
            sheet1.write(row_number,19,data)
        except Exception :
            logging.warning(f"for row_number {row_number} the coulum 19 is not present")

        try:
            #column 20
            custom_locator=self.createCustomLocator("//td[text()='Avg Total Goals (GF+GA)']/parent::tr/td/font[@style='font-size:14px;']")
            data=custom_locator.get_text()
            sheet1.write(row_number,20,data)
        except Exception :
            logging.warning(f"for row_number {row_number} the coulum 20 is not present")

        try:
            #column 21
            custom_locator=self.createCustomLocator("//td[text()='Scoring rate']/parent::tr/td/font[@style='font-size:14px;']",1)
            data=custom_locator.get_text()
            sheet1.write(row_number,21,data)
        except Exception :
            logging.warning(f"for row_number {row_number} the coulum 21 is not present")

        try:
            #column 22
            custom_locator=self.createCustomLocator("//td[text()='Scoring rate']/parent::tr/td/font[@style='font-size:14px;']",2)
            data=custom_locator.get_text()
            sheet1.write(row_number,22,data)
        except Exception :
            logging.warning(f"for row_number {row_number} the coulum 22 is not present")

        try:
            #column 23
            custom_locator=self.createCustomLocator("//td[text()='Clean Sheets']/parent::tr/td/font[@style='font-size:14px;']",1)
            data=custom_locator.get_text()
            sheet1.write(row_number,23,data)
        except Exception :
            logging.warning(f"for row_number {row_number} the coulum 23 is not present")

        try:
            #column 24
            custom_locator=self.createCustomLocator("//td[text()='Clean Sheets']/parent::tr/td/font[@style='font-size:14px;']",2)
            data=custom_locator.get_text()
            sheet1.write(row_number,24,data)
        except Exception :
            logging.warning(f"for row_number {row_number} the coulum 24 is not present")
        
        try:
            #column 25
            custom_locator=self.createCustomLocator("//td[text()='Scored in both halves']/parent::tr/td/font[@style='font-size:14px;']",1)
            data=custom_locator.get_text()
            sheet1.write(row_number,25,data)
        except Exception :
            logging.warning(f"for row_number {row_number} the coulum 25 is not present")

        try:
            #column 26
            custom_locator=self.createCustomLocator("//td[text()='Scored in both halves']/parent::tr/td/font[@style='font-size:14px;']",2)
            data=custom_locator.get_text()
            sheet1.write(row_number,26,data)
        except Exception :
            logging.warning(f"for row_number {row_number} the coulum 26 is not present")

        try:
            #column 27
            custom_locator=self.createCustomLocator("//font[text()='Total goals averages']/parent::td/parent::tr/parent::tbody/tr[@class='trow3']/td/font[@color='#555555']",2)
            data=custom_locator.get_text()
            sheet1.write(row_number,27,data)
        except Exception :
            logging.warning(f"for row_number {row_number} the coulum 27 is not present")

        try:
            #column 28
            custom_locator=self.createCustomLocator("//td[text()='Over 9.5 corners']/parent::tr/td/font[@style='font-size:14px;']")
            data=custom_locator.get_text()
            sheet1.write(row_number,28,data)
        except Exception :
            logging.warning(f"for row_number {row_number} the coulum 28 is not present")

        try:
            #column 29
            custom_locator=self.createCustomLocator("//td[text()='Over 10.5 corners']/parent::tr/td/font[@style='font-size:14px;']")
            data=custom_locator.get_text()
            sheet1.write(row_number,29,data)
        except Exception :
            logging.warning(f"for row_number {row_number} the coulum 29 is not present")

        try:
            #column 32
            data=self.driver.current_url
            sheet1.write(row_number,32,data)
        except Exception :
            logging.warning("for row_number {row_number} the coulum 32 is not present")
        
        row_number=row_number+1
        





    def createCustomLocator(self,locator_name,index=1):
        _locator = ["XPATH"]
        _locator.append(f"({locator_name})[{index}]")
        self.locators.update({"custom_locator":[_locator]})
        if(selenium_helper.is_element_present(self.locators["custom_locator"][0],0)):
            self.custom_locator.scroll_to_element()
        return self.custom_locator

    def goToYesterdayUrl(self,url):
        self.driver.get(url)
        if(selenium_helper.is_element_present(self.locators["btn_agree"][0],5)):
            self.btn_agree.click_button()
        
        

    def readExcelFile(self):
        # Get today's date
        presentday = datetime.now() # or presentday = datetime.today()

        # Get Yesterday
        yesterday = presentday - timedelta(1)
        file_name=yesterday.strftime('%d-%m-%Y')
        
        original_path=os.getcwd()
        new_path="test/excel sheet/"
        try:
            wb = xlrd.open_workbook(new_path+file_name+'.xls')
            wbwrite=copy(wb)
            sheet = wb.sheet_by_index(0)

            #os.chdir(new_path)

            x1 = wbwrite.get_sheet(0)


            # For row 0 and column 0
            self.insertValue(sheet,x1)
            os.chdir(new_path)
            os.remove(file_name+'.xls')
            wbwrite.save(file_name+'.xls')
        
            
        except Exception :
            logging.warning("no file found")
    
    def insertValue(self,sheet,x1):
        
            all_team_name=self.yesterday_team_name.get_all_elements()
            logging.warning(len(all_team_name))
            #for i in range (1,len(all_team_name)+1):
            i=1
            while (i <len(all_team_name)):
                flag=0
                try:
                    custom_locator=self.createCustomLocator("//td[@class='steam']",i)
                    custom_locator.scroll_to_element()
                    home_team_name=custom_locator.get_text()
                    custom_locator=self.createCustomLocator("//td[@class='steam']/parent::tr/td/b",i)
                    home_team_score=custom_locator.get_text()
                    i=i+1
                except Exception :
                    logging.warning("data missing for home team ")
                    i=i+1
                    flag=1
                try:
                    if(flag==1):
                        i=i+1
                        continue
                    else:
                        custom_locator=self.createCustomLocator("//td[@class='steam']",i)
                        custom_locator.scroll_to_element()
                        away_team_name=custom_locator.get_text()
                        custom_locator=self.createCustomLocator("//td[@class='steam']/parent::tr/td/b",i)
                        away_team_score=custom_locator.get_text()
                        row=self.matching(home_team_name,away_team_name,sheet)
                        i=i+1
                        if(row>-1):
                            x1.write(row,30,home_team_score)
                            x1.write(row,31,away_team_score)
                except Exception :
                    logging.warning("data missing for away team")
                    i=i+1

    def matching(self,home_team_name,away_team_name,sheet):
        
        column=5
        try:
            size=sheet.nrows
            for row in range (1,size):
                if( (sheet.cell_value(row,column ) in home_team_name and sheet.cell_value(row,column+1 ) in away_team_name) or ( home_team_name in sheet.cell_value(row,column ) and  away_team_name in sheet.cell_value(row,column+1 ) ) ):
                    logging.warning(row)
                    return row



            return -1
        except Exception :
            logging.warning("error in reading from file")
        
        


        




