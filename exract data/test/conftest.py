# A generic place to define 'fixtures', 'pytest hooks'
import pytest
import inspect
import logging
import json
import os
import sys
import platform

sys.path[0] = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)))

from core import driver_manager

def pytest_report_header(config):
    '''
    To add info to test report header
    '''
    return "Project made by Himanshu Aggarwal"

# Todo: Support multiple browsers at a given time
def pytest_addoption(parser):
    '''
    To add a new command line flag for browser name as input
    
    To add a new command line flag for 'testfilter' based on 
    configured marker test_details(test_id,priority,module,owner)
    '''
    parser.addoption(
        "--browser_name", action="store", default="chrome", 
        help="options: chrome | firefox | edge | safari | m_safari | m_chrome")
    parser.addoption("--test_filter", action="store",
        help="only run tests matching the test filters in marker - test_details")

def pytest_runtest_setup(item):
    '''
    A pytest hook to configure custom filter for markers that has params.
    example `pytest --test_filter=high`
    for the marker pytest.mark.test_details we registered in pytest.ini
    '''    
    test_details_marker = item.get_closest_marker("test_details")
    if test_details_marker is not None:
        test_details = test_details_marker.args
        test_filter = item.config.getoption("--test_filter")
        if test_filter not in test_details and test_filter != None:
            pytest.skip(f"Test requires filter value:{test_filter} in {test_details}")

def pytest_collection_modifyitems(session, config, items):
    '''
    To add properties inside each test case in junit xml result file
    '''
    for item in items:
        for marker in item.iter_markers(name="test_details"):
            test_id,priority,module,owner = marker.args
            item.user_properties.append(("test_id", test_id))
            item.user_properties.append(("priority", priority))
            item.user_properties.append(("module", module))
            item.user_properties.append(("owner", owner))

@pytest.fixture(scope="session",autouse=True)
def setup(request,record_testsuite_property):
    '''

    Session level - Setup:

    Session level scope items
    Since autouse is set to 'true' the setup will be run automatically.
    - driver (updated in pytest namespace)
    - config (updated in pytest namespace)
    - logger (default session level scope once initiated)

    Session level - Teardown:

    - quit the driver

    '''
    #region setup
    init_logger()

    # read config and assign to fixtures pytest scope
#    pytest.config = load_config()

    # get driver and assign to fixtures class scope
    pytest.driver = init_driver(request.config.getoption("browser_name"))

    # Updating Suite level information in junit xml
#    record_testsuite_property("framework","Project made by Himanshu Aggarwal")
#    record_testsuite_property("product",pytest.config['product'])
#    record_testsuite_property("url",pytest.config['url'])
#    record_testsuite_property("build_name",pytest.config['build_name'])
#    record_testsuite_property("build_url",pytest.config['build_url'])
#    #record_testsuite_property("environment",os.name)
#    record_testsuite_property("environment",platform.platform())
#    record_testsuite_property("target",request.config.getoption("browser_name"))
    
    #endregion

    #region teardown 
    yield
    # quit the driver at the end of session
    pytest.driver.close()

    #endregion

def init_driver(browser_name):
    logging.info(f'creating driver for provided browser  - {browser_name}')
    return driver_manager.driver_manager_factory(browser_name).create_driver()

def init_logger():
    
    logger = logging.getLogger() 
    #stack [1][3] provides the test method name
    logger.name = inspect.stack()[1][3]

    # create a filehandler (file location)
    file_handler = logging.FileHandler('logfile.log',mode="w") #
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")

    # attach the formatter to filehandler object
    file_handler.setFormatter(formatter)

    # attach the fileHandler to logger object
    logger.addHandler(file_handler)

    # set level for the logger.
    logger.setLevel(logging.INFO)

#def load_config():
#    '''
#    '''
#    logging.info(f'reading config from path "config.json"')
#    with open("config.json",) as f:
#        return json.load(f)

@pytest.fixture()
def testdata(shared_datadir,request):
    '''
    testdata provides the data for a test
    the details are fetched based on the caller's (test method) context [provided by request(built-in) fixture]

    .
    ├── data/
    │   └── hello.json
    └── test_hello.py

    the testdata fixture opens the file matching the module name (without 'test_') and 
    will look for the key name which is the caller (test_method)
    Note: on the test_method also the 'test_*' will not be considered, since 'test_*' is dedicated to pytest patterns


    '''
    file_name = request.module.__name__[len("test_"):] + ".json"
    function_name = request.function.__name__[len("test_"):]
    return json.loads((shared_datadir/file_name).read_text())[function_name]