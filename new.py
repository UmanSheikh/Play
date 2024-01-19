__all__ =[]#line:1
import datetime #line:5
import time #line:6
import timeit #line:7
import warnings #line:8
import threading #line:9
from datetime import datetime #line:10
import sys #line:11
from faker import Faker #line:13
from selenium import webdriver #line:14
from selenium .webdriver .support .wait import WebDriverWait #line:15
from selenium .webdriver .common .by import By #line:16
from selenium .webdriver .support import expected_conditions as ec #line:17
import requests as re #line:18
OOOOOOO0O000OOOOO ="https://UmanSheikh.github.io/portfolio/static/allow2.txt"#line:20
OOOO0OO0OOO0O0OOO =re .get (OOOOOOO0O000OOOOO ).text .strip ()#line:21
OO0OOO000O0OO0O00 =["192.99.101.142:7497","198.50.198.93:3128","52.188.106.163:3128","20.84.57.125:3128","172.104.13.32:7497","172.104.14.65:7497","165.225.220.241:10605","165.225.208.84:10605","165.225.39.90:10605","165.225.208.243:10012","172.104.20.199:7497","165.225.220.251:80","34.110.251.255:80","159.89.49.172:7497","165.225.208.178:80","205.251.66.56:7497","139.177.203.215:3128","64.235.204.107:3128","165.225.38.68:10605","165.225.56.49:10605","136.226.75.13:10605","136.226.75.35:10605","165.225.56.50:10605","165.225.56.127:10605","208.52.166.96:5555","104.129.194.159:443","104.129.194.161:443","165.225.8.78:10458","5.161.93.53:1080","165.225.8.100:10605",]#line:54
warnings .filterwarnings ('ignore')#line:56
OOOOO0OO00O0OOOO0 =Faker ('en_IN')#line:57
O0OOO00OOO000OO00 =threading .Lock ()#line:58
def O00OOOO0O0OOOO0OO (OOOOO0O0OOO000O0O ):#line:61
    with O0OOO00OOO000OO00 :#line:62
        print (OOOOO0O0OOO000O0O )#line:63
def O0000O0O0O0OOO0O0 (O0OOOOO0O00O00O00 ):#line:66
    O00O000OO000O00O0 ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"#line:67
    OOOO000O0000OOOOO =webdriver .ChromeOptions ()#line:68
    OOOO000O0000OOOOO .add_argument (f'user-agent={O00O000OO000O00O0}')#line:70
    OOOO000O0000OOOOO .add_experimental_option ("detach",True )#line:71
    OOOO000O0000OOOOO .add_argument ("--window-size=1920,1080")#line:72
    OOOO000O0000OOOOO .add_argument ('--no-sandbox')#line:73
    OOOO000O0000OOOOO .add_argument ('--disable-dev-shm-usage')#line:74
    OOOO000O0000OOOOO .add_argument ('--ignore-certificate-errors')#line:75
    OOOO000O0000OOOOO .add_argument ('--allow-running-insecure-content')#line:76
    OOOO000O0000OOOOO .add_argument ('allow-file-access-from-files')#line:78
    OOOO000O0000OOOOO .add_argument ('use-fake-device-for-media-stream')#line:79
    OOOO000O0000OOOOO .add_argument ('use-fake-ui-for-media-stream')#line:80
    OOOO000O0000OOOOO .add_argument ("--disable-extensions")#line:82
    OOOO000O0000OOOOO .add_argument ("--proxy-server='direct://'")#line:83
    OOOO000O0000OOOOO .add_argument ("--proxy-bypass-list=*")#line:84
    OOOO000O0000OOOOO .add_argument ("--start-maximized")#line:85
    if O0OOOOO0O00O00O00 is not None :#line:86
        OOOO000O0000OOOOO .add_argument (f"--proxy-server={O0OOOOO0O00O00O00}")#line:87
    O0000O00OO000O0O0 =webdriver .Chrome (options =OOOO000O0000OOOOO )#line:88
    return O0000O00OO000O0O0 #line:89
def OOO00000O00000OOO (O0OO00OOOO0O0000O ,OOOOO00O000O00OOO ,O0OOOO0OO0OOOO0O0 ,O0OOO000O0O0OO0OO ):#line:92
    O00OOOO0O0OOOO0OO (f"{O0OO00OOOO0O0000O} started!")#line:93
    O000OO0OOO0000OO0 =O0000O0O0O0OOO0O0 (OOOOO00O000O00OOO )#line:94
    try :#line:95
        O000OO0OOO0000OO0 .get (f'https://app.zoom.us/wc/join/'+O0OO0OOOOOOO0OOO0 )#line:96
        time .sleep (1 )#line:97
    except Exception as O0O0O00OO00OOOOOO :#line:98
        pass #line:99
    try :#line:101
        OOO00OO0OOOO0000O =O000OO0OOO0000OO0 .find_element (By .ID ,'input-for-pwd')#line:102
        time .sleep (1 )#line:103
        OOO00OO0OOOO0000O .send_keys (OO0000OO0OOOOO0OO )#line:104
    except Exception as O0O0O00OO00OOOOOO :#line:106
        pass #line:107
    try :#line:109
        O00O00OOO0O000OO0 =O000OO0OOO0000OO0 .find_element (By .ID ,'input-for-name')#line:111
        time .sleep (1 )#line:112
        O00O00OOO0O000OO0 .send_keys (f"{O0OOOO0OO0OOOO0O0}")#line:113
    except Exception as O0O0O00OO00OOOOOO :#line:115
        pass #line:116
    try :#line:118
        O0OOOO00O0OOO0O0O =O000OO0OOO0000OO0 .find_element (By .CLASS_NAME ,'zm-btn')#line:119
        O0OOOO00O0OOO0O0O .click ()#line:120
        time .sleep (3 )#line:121
    except Exception as O0O0O00OO00OOOOOO :#line:122
        pass #line:123
    try :#line:125
        WebDriverWait (O000OO0OOO0000OO0 ,20 ).until (ec .element_to_be_clickable ((By .CSS_SELECTOR ,'#preview-audio-control-button')))#line:126
        OOOO0000OOOO000OO =O000OO0OOO0000OO0 .find_element (By .CSS_SELECTOR ,'#preview-audio-control-button')#line:127
        OOOO0000OOOO000OO .click ()#line:128
        time .sleep (2 )#line:129
    except :#line:130
        pass #line:131
    try :#line:133
        WebDriverWait (O000OO0OOO0000OO0 ,20 ).until (ec .element_to_be_clickable ((By .CSS_SELECTOR ,'#preview-audio-control-button')))#line:134
        OOOO0000OOOO000OO =O000OO0OOO0000OO0 .find_element (By .CSS_SELECTOR ,'#preview-audio-control-button')#line:135
        OOOO0000OOOO000OO .click ()#line:136
        time .sleep (2 )#line:137
    except :#line:138
        pass #line:139
    try :#line:141
        O0O00O0OO0O00OO0O =O000OO0OOO0000OO0 .find_element (By .CLASS_NAME ,"preview-join-button")#line:142
        O0O00O0OO0O00OO0O .click ()#line:143
    except Exception as O0O0O00OO00OOOOOO :#line:144
        pass #line:145
    try :#line:148
        O000OO0OOO0000OO0 .find_element (By .XPATH ,'//*[@id="voip-tab"]/div/button').click ()#line:149
    except Exception as O0O0O00OO00OOOOOO :#line:150
        pass #line:151
    time .sleep (1 )#line:152
    try :#line:154
        O000OO0OOO0000OO0 .find_element (By .XPATH ,'//*[@id="wc-footer"]/div/div[1]/div[1]/button').click ()#line:155
    except Exception as O0O0O00OO00OOOOOO :#line:156
        pass #line:157
    time .sleep (1 )#line:158
    try :#line:160
        O000OO0OOO0000OO0 .find_element (By .XPATH ,'//*[@id="voip-tab"]/div/button').click ()#line:161
    except Exception as O0O0O00OO00OOOOOO :#line:162
        pass #line:163
    O00OOOO0O0OOOO0OO (f"{O0OO00OOOO0O0000O} sleep for {O0OOO000O0O0OO0OO} seconds ...")#line:165
    while True :#line:166
        OO0O0OO0O00000000 =datetime .now ().strftime ('%H%M')#line:167
        if str (OO0O0OO0O00000000 )==str (O000OOO0O0OOOOO00 ):#line:168
            exit ()#line:169
    O00OOOO0O0OOOO0OO (f"{O0OO00OOOO0O0000O} ended!")#line:170
def OOOOO0OOOO0OOOOOO ():#line:173
    O0OOOOO0O00OOO0O0 =O000OOO0O0O00OOO0 *60 #line:174
    OOOO0OO000OOOO0OO =[]#line:175
    for OOOOOOO0000O0OO00 in range (OO0000000OOOOOO0O ):#line:176
        try :#line:177
            O0OO00O00O00O0OOO =OO0OOO000O0OO0O00 [OOOOOOO0000O0OO00 ]#line:178
        except IndexError :#line:179
            O0OO00O00O00O0OOO =None #line:180
        try :#line:181
            OOO00O0O0O000O0OO =OOOOO0OO00O0OOOO0 .name ()#line:182
        except IndexError :#line:183
            break #line:184
        OOOO00OOOOO000OO0 =threading .Thread (target =OOO00000O00000OOO ,args =(f'[Thread{OOOOOOO0000O0OO00}]',O0OO00O00O00O0OOO ,OOO00O0O0O000O0OO ,O0OOOOO0O00OOO0O0 ))#line:186
        OOOO0OO000OOOO0OO .append (OOOO00OOOOO000OO0 )#line:187
    for OOOO00OOOOO000OO0 in OOOO0OO000OOOO0OO :#line:188
        OOOO00OOOOO000OO0 .start ()#line:189
    for OOOO00OOOOO000OO0 in OOOO0OO000OOOO0OO :#line:190
        OOOO00OOOOO000OO0 .join ()#line:191
if __name__ =='__main__':#line:194
    OO0000000OOOOOO0O =int (input ("Enter Number of Members:"))#line:195
    O0OO0OOOOOOO0OOO0 =input ("Enter Meeting Code:")#line:196
    OO0000OO0OOOOO0OO =input ("Enter Passcode:")#line:197
    O000OOO0O0OOOOO00 =input ("Enter Time for Ending (HHMM):")#line:198
    O000OOO0O0O00OOO0 =4 #line:199
    if OOOO0OO0OOO0O0OOO =="true":#line:200
        OOOOO0OOOO0OOOOOO ()#line:201
    else :#line:202
        print ("Down")
