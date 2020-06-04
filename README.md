# Collect Salt Water Disposal Permits in Texas

This script queries the Texas Rail Road Commission(RRC) Underground Injection Control (UIC)
database for permitted wells in District 10, the district can be changed. It will create two files. File one is the 
query results generated by the RRC, and is generated in the first minute. File two is 
the permit detail for every UIC number, and will take longer depending on results.

## Installation / Set-Up / Usage / How to 
Script was written and designed to be ran from Spyder on Windows. Script is based on codes in Texas_RRC_well_log_scraper repository. The code uses selenium library to scrape data. More about selenium [here](https://www.selenium.dev). Firefox must be installed on the machine to run the code. The code will open an automated Firefox window, closing the 
window will cause the code to crash, minimizing the window is fine. In future versions of this 
code, the window may be hidden, but I have left it visible as a quick way to monitor the code's 
progress. 

## License
No License - Please contact if you would like to use part of this code
