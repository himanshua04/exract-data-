import pytest
from pages.tomorrow_page import TomorrowPage
from helper import selenium_helper
import time
import os
import xlwt
from xlwt import Workbook
import datetime 
from selenium.webdriver.chrome.options import Options



class TestTomorrow():


        @pytest.fixture
        def initialize_pages(self,scope='class'):
            self.pg_tomorrow = TomorrowPage(pytest.driver)
        
        def test_get_details_of_tomorrow_match(self,initialize_pages,testdata):
            
            # Workbook is created
            wb = Workbook()

            # add_sheet is used to create sheet.
            sheet1 = wb.add_sheet('Sheet 1')

            # inisiazie the first coulum of sheet
            self.pg_tomorrow.inisilizeSheetDetails(sheet1)

            self.pg_tomorrow.goToUrl(testdata['tomorrow_url'])
            
            self.pg_tomorrow.clickOnStats(self.pg_tomorrow.btn_stats)
            
            self.pg_tomorrow.goToUrl(testdata['tomorrow_url'])
            self.pg_tomorrow.startProcessing("//a[@class='myButton']",sheet1,testdata['tomorrow_url'])    
           
            self.pg_tomorrow.saveExcelFile(wb)

            '''
            self.pg_tomorrow.goToYesterdayUrl(testdata['yesterday_url'])
            self.pg_tomorrow.readExcelFile()
            '''

            
            
