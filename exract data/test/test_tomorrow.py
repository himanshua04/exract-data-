import pytest
from pages.tomorrow_page import TomorrowPage
from helper import selenium_helper
import time
import os
import xlwt
from xlwt import Workbook
import datetime 



class TestTomorrow():


        @pytest.fixture
        def initialize_pages(self,scope='class'):
            self.pg_tomorrow = TomorrowPage(pytest.driver)
        
        def test_get_details_of_tomorrow_match(self,initialize_pages,testdata):

            pytest.driver.get(testdata['url'])
             
  
            # Workbook is created
            wb = Workbook()

            # add_sheet is used to create sheet.
            sheet1 = wb.add_sheet('Sheet 1')

            self.pg_tomorrow.inisilizeSheetDetails(sheet1)
            sheet1.write(1, 0, 'ISBT DEHRADUN')
            sheet1.write(2, 0, 'SHASTRADHARA')
            self.pg_tomorrow.saveExcelFile(wb)
            #wb.save('xlwt example.xls')
            #time.sleep(10)
