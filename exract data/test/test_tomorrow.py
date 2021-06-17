import pytest
from pages.tomorrow_page import TomorrowPage
from xlwt import Workbook
from selenium.webdriver.chrome.options import Options



class TestTomorrow():


        @pytest.fixture
        def initialize_pages(self,scope='class'):
            self.pg_tomorrow = TomorrowPage(pytest.driver)
        
        def test_get_details_of_tomorrow_match(self,initialize_pages):
        
            # Workbook is created
            wb = Workbook()

            # add_sheet is used to create sheet.
            sheet1 = wb.add_sheet('Sheet 1')

            # inisiazie the first coulum of sheet
            self.pg_tomorrow.inisilizeSheetDetails(sheet1)

            self.pg_tomorrow.goToUrl("https://www.soccerstats.com/matches.asp?matchday=2&daym=tomorrow")
            
            self.pg_tomorrow.clickOnStats(self.pg_tomorrow.btn_stats)
            
            self.pg_tomorrow.goToUrl("https://www.soccerstats.com/matches.asp?matchday=2&daym=tomorrow")
            self.pg_tomorrow.startProcessing("//a[@class='myButton']",sheet1,"https://www.soccerstats.com/matches.asp?matchday=2&daym=tomorrow")    
           
            self.pg_tomorrow.saveExcelFile(wb)
            
            
            self.pg_tomorrow.goToYesterdayUrl("https://www.soccerstats.com/matches.asp?matchday=0&daym-yesterday")
            self.pg_tomorrow.readExcelFile()
            

            
            
