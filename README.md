# afw-version-grabber
Grabs version string of latest firmware for ASUS products.

## Requirements:
* Python 3
* Selenium (and Geckodriver)
* urllib3
* argparse

Installing python3-selenium via Debian (or similar) and geckodriver will satisfy script requirements.

## Usage:  
./get-asus-fwver.py [-h] asuscategory asusproduct  

positional arguments:   
  asuscategory  Category of Asus product, like 'Motherboards'  
  asusproduct   Name of Asus product, like 'A88XMA'  

Names must match corresponding ASUS urls.  
