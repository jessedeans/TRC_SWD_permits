## -*- coding: utf-8 -*-
"""
This code queries the Texas Rail Road Commission(RRC) Underground Injection Control (UIC)
database for permitted wells in District 10. It will create two files. File one is the 
query results generated by the RRC, and is generated in the first minute. File two is 
the permit detail for every UIC number, and will take longer.
Firefox must be installed on the machine to run the code. The code will open an 
automated Firefox window, closing the window will cause the code to crash, 
minmizing the window is fine. In future versions of this code, the window will 
be hidden, but I have left it visible as a quick way to monitor the codes progress.   
 
@author: jshumway
"""
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import Select

############## OutPut Directory #################
outputDir = os.getcwd()

############### Set Firefox Profile #################
profile = webdriver.FirefoxProfile()
## do not use default downloads directory
profile.set_preference('browser.download.folderList', 2)
##Do not show download progress
profile.set_preference("browser.download.manager.showWhenStarting", False)
##Set directory for downloads
profile.set_preference('browser.download.dir', outputDir)
##automatically download file for selcted mime-type, do not create pop up window
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', "text/plain, application/vnd.ms-excel, text/csv, text/comma-separated-values, application/octet-stream")

############## Start Browswer go to database #################
driver = webdriver.Firefox(profile)
#go to the query page
driver.get("http://webapps2.rrc.texas.gov/EWA/uicQueryAction.do")

############## Input Query #################           
inputDistrict = Select(driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/select')) 
inputDistrict.select_by_value("10")
driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[4]/td/input[1]').click()

############## Download Search Results #################
driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input').click()

############## Change Search Results to 100 #################     
pageSize = Select(driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr/td[3]/label/select'))
pageSize.select_by_value('100')

############## Find number of pages returned  #################  
pages = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr/td[2]/a[12]').text
#pages = driver.find_element_by_xpath('/html/body/table[3]/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr/td[1]').text
#pages = pages.replace(' results', '')
pages = int(pages)

############## Select First Permit Detail #################     
driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[3]/td[1]/a').click()

############## Scrape Table Header #################
#get table headers
tableHeader = [driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td[1]").text,
               driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[3]/td[1]').text,
               driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[4]/td[1]').text,
               driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[5]/td[1]").text,
               driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[6]/td[1]').text,
               driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[7]/td[1]').text,
               driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[8]/td[1]').text,
               driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[9]/td[1]').text,
               driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[10]/td[1]').text,
               driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[11]/td[1]').text,
               driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[12]/td[1]').text,
               driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[13]/td[1]').text,
               driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[14]/td[1]').text,
               driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[15]/td[1]').text,
               driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[16]/td[1]').text,
               driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[17]/td[1]').text,
               driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[18]/td[1]').text,
               driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[19]/td[1]').text,
               driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[20]/td[1]').text,
               driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[21]/td[1]').text,
               driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[22]/td[1]').text,
               driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[23]/td[1]').text,
               driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[24]/td[1]').text,
               driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[25]/td[1]').text,
               driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[26]/td[1]').text,
               driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[27]/td[1]').text,
               driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[28]/td[1]').text,
               driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[29]/td[1]').text,
               driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[30]/td[1]').text,
               driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[31]/td[1]').text,
               driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[32]/td[1]').text,
               driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[33]/td[1]').text,
               driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[34]/td[1]').text,
               driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[35]/td[1]').text,
               driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[36]/td[1]').text,
               driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[37]/td[1]').text,
               ]  

#return to search results
driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/input').click()

#Create panda dataframe with headers
exportData_df=pd.DataFrame(columns=(tableHeader), index = [0])


############## Scrape Permit Details #################
for n in range (pages):
    for i in range(100):
        row = 3+i
        driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[%s]/td[1]/a' %row).click()
        tableData = [driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td[2]").text,
                   driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[3]/td[2]').text,
                   driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[4]/td[2]').text,
                   driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[5]/td[2]").text,
                   driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[6]/td[2]').text,
                   driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[7]/td[2]').text,
                   driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[8]/td[2]').text,
                   driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[9]/td[2]').text,
                   driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[10]/td[2]').text,
                   driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[11]/td[2]').text,
                   driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[12]/td[2]').text,
                   driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[13]/td[2]').text,
                   driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[14]/td[2]').text,
                   driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[15]/td[2]').text,
                   driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[16]/td[2]').text,
                   driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[17]/td[2]').text,
                   driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[18]/td[2]').text,
                   driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[19]/td[2]').text,
                   driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[20]/td[2]').text,
                   driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[21]/td[2]').text,
                   driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[22]/td[2]').text,
                   driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[23]/td[2]').text,
                   driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[24]/td[2]').text,
                   driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[25]/td[2]').text,
                   driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[26]/td[2]').text,
                   driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[27]/td[2]').text,
                   driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[28]/td[2]').text,
                   driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[29]/td[2]').text,
                   driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[30]/td[2]').text,
                   driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[31]/td[2]').text,
                   driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[32]/td[2]').text,
                   driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[33]/td[2]').text,
                   driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[34]/td[2]').text,
                   driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[35]/td[2]').text,
                   driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[36]/td[2]').text,
                   driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[37]/td[2]').text,
                   ]  
        
    # Append results data to panda dataframe
        dataSeries=pd.Series(tableData,index=exportData_df.columns)
        exportData_df.loc[exportData_df.index.max()+1] = dataSeries
   # Return to search results     
        driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/input').click()
  
    #go to next page
    try:
        driver.find_element_by_partial_link_text('[Next>]').click()
    except:
        pass

exportData_df.to_csv(os.path.join(outputDir, r'SWDPermits.csv'))
driver.quit()
print ("done")

