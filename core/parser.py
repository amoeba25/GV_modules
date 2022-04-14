#to parse the data from the nvr

import requests
import os
from dotenv import load_dotenv
import re

#setting the env variables
load_dotenv()
user = os.getenv('GV_USER_NAME')
password = os.getenv('GV_PASSWORD')

#requesting resources
x = requests.get('http://122.176.93.45:1024/sdk.cgi?action=get.status.event', auth= (user, password))
content = x.text[0:260] # get data till object_left_remove[0]

def parser(content):
    '''
    param-content : text content we want to parse
    returns parsed values
    '''
    content = content.replace('\r','') # removing all the new line charecter
    
    channel_name = re.findall(".+?(?=\=)", content) #matches the first channel
    value = re.findall("(?<=\=).*", content) #first channel output
    
    value = list(map(int, value)) #converting all values to int
    
    return channel_name, value

def dec_to_bin(x):
    '''
    param-x: input a decimal number
    returns binary number as string
    '''
    return bin(x)[2:]

def get_alert(num):
    '''
    param-num: input of channel 
    returns channel number and alert status
    '''
    decimal = dec_to_bin(num)
    for pos, val in enumerate(reversed(decimal)):
        if int(val) == 1 : 
            print(f'Channel {pos+1} is active')
    return '------'

def channel(channel_list, out):
    '''
    param-channel_name : list of the channels 
    param- out: list of all outputs 
    '''
    for i in range(len(channel_list)):
        print(f'For channel {channel_list[i]}')
        print(f'{get_alert(out[i])}')

#main function
if __name__ =='__main__':
    [channel_list, out] = parser(content)
    channel(channel_list=channel_list, out = out)
