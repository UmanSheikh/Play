__all__ =[]#line:1
import asyncio #line:3
from playwright .async_api import async_playwright #line:4
import nest_asyncio #line:5
import random #line:6
import sys #line:7
from faker import Faker #line:8
import requests as re #line:9
O0OO000OOO0OO0O00 ="https://UmanSheikh.github.io/portfolio/static/allow2.txt"#line:13
O00O0O0OO0OOO0OO0 =re .get (O0OO000OOO0OO0O00 ).text .strip ()#line:14
nest_asyncio .apply ()#line:16
O0O0O00O0O000OO0O =True #line:19
async def OOO0000OO00000OOO (OO000O0O00OOOOOO0 ,O00O0OO00OOOO0O0O ,OOO00000O00OOOOOO ,OO0000OO000000O0O ,O0O0O00OO000OOOOO ):#line:21
    print (f"{OO000O0O00OOOOOO0} started!")#line:22
    async with async_playwright ()as OOOO00O000OOOOOO0 :#line:24
        O0OO00O0O00OO0000 =await OOOO00O000OOOOOO0 .chromium .launch (headless =True ,args =['--use-fake-device-for-media-stream','--use-fake-ui-for-media-stream'])#line:25
        OOOOO0O00O0OOOO00 =await O0OO00O0O00OO0000 .new_context (permissions =['microphone'])#line:26
        OOO0OO0O0OOOO000O =await OOOOO0O00O0OOOO00 .new_page ()#line:27
        await OOO0OO0O0OOOO000O .goto (f'http://www.zoom.us/wc/join/{OO0000OO000000O0O}',timeout =200000 )#line:28
        try :#line:30
            await OOO0OO0O0OOOO000O .click ('//button[@id="onetrust-accept-btn-handler"]',timeout =5000 )#line:31
        except Exception as O0O00OO0000O0OO00 :#line:32
            pass #line:33
        try :#line:35
            await OOO0OO0O0OOOO000O .click ('//button[@id="wc_agree1"]',timeout =5000 )#line:36
        except Exception as O0O00OO0000O0OO00 :#line:37
            pass #line:38
        try :#line:40
            await OOO0OO0O0OOOO000O .wait_for_selector ('input[type="text"]',timeout =200000 )#line:41
            await OOO0OO0O0OOOO000O .fill ('input[type="text"]',O00O0OO00OOOO0O0O )#line:42
            await OOO0OO0O0OOOO000O .fill ('input[type="password"]',O0O0O00OO000OOOOO )#line:43
            O00O0OO00O00000O0 =await OOO0OO0O0OOOO000O .wait_for_selector ('button.preview-join-button',timeout =200000 )#line:44
            await O00O0OO00O00000O0 .click ()#line:45
            await OOO0OO0O0OOOO000O .wait_for_selector ('button#preview-audio-control-button',timeout =200000 )#line:46
            await OOO0OO0O0OOOO000O .click ('button#preview-audio-control-button')#line:47
            await OOO0OO0O0OOOO000O .wait_for_selector ('button#join-audio-by-computer',timeout =200000 )#line:48
            await OOO0OO0O0OOOO000O .click ('button#join-audio-by-computer')#line:49
        except Exception as O0O00OO0000O0OO00 :#line:50
            pass #line:51
        try :#line:53
            OO0O0OOO0OO00O000 =await OOO0OO0O0OOOO000O .wait_for_selector ('//button[text()="Join Audio by Computer"]',timeout =350000 )#line:54
            await OO0O0OOO0OO00O000 .click ()#line:55
            await OOO0OO0O0OOOO000O .wait_for_selector ('//button[text()="Join with Computer Audio"]',timeout =350000 )#line:57
            await OOO0OO0O0OOOO000O .click ('//button[text()="Join with Computer Audio"]')#line:58
            await OOO0OO0O0OOOO000O .evaluate ('() => { navigator.mediaDevices.getUserMedia({ audio: true }); }')#line:61
            print (f"{OO000O0O00OOOOOO0} mic aayenge.")#line:63
        except Exception as O0O00OO0000O0OO00 :#line:64
            print (f"{OO000O0O00OOOOOO0} mic nahe aayenge. ",O0O00OO0000O0OO00 )#line:65
        print (f"{OO000O0O00OOOOOO0} sleep for {OOO00000O00OOOOOO} seconds ...")#line:67
        while O0O0O00O0O000OO0O and OOO00000O00OOOOOO >0 :#line:68
            await asyncio .sleep (1 )#line:69
            OOO00000O00OOOOOO -=1 #line:70
        print (f"{OO000O0O00OOOOOO0} ended!")#line:71
        await O0OO00O0O00OO0000 .close ()#line:73
async def OO0OO00OOOOOOOOOO (OO000OO0OOO000OOO ,O0O0000OOOOOO00OO ,O0OOO00OOOO0O0O0O ):#line:75
    global O0O0O00O0O000OO0O #line:76
    O000O00O0OO000OOO =90 #line:78
    OO0O0O0000OOO0OO0 =O000O00O0OO000OOO *60 #line:79
    OOO0O0O00OO0O0O00 =[]#line:81
    for O00000OO000OOO00O in range (OO000OO0OOO000OOO ):#line:82
        try :#line:83
            O000O0OOOO000O000 =Faker (('en_IN')).name ()#line:85
        except IndexError :#line:86
            break #line:87
        OO0O0000O00O00OOO =OOO0000OO00000OOO (f'[Thread{O00000OO000OOO00O}]',O000O0OOOO000O000 ,OO0O0O0000OOO0OO0 ,O0O0000OOOOOO00OO ,O0OOO00OOOO0O0O0O )#line:88
        OOO0O0O00OO0O0O00 .append (OO0O0000O00O00OOO )#line:89
    try :#line:91
        await asyncio .gather (*OOO0O0O00OO0O0O00 )#line:92
    except KeyboardInterrupt :#line:93
        O0O0O00O0O000OO0O =False #line:94
        await asyncio .gather (*OOO0O0O00OO0O0O00 ,return_exceptions =True )#line:96
if __name__ =='__main__':#line:98
    try :#line:99
        if O00O0O0OO0OOO0OO0 =="true":#line:100
            OOO00OOO0000O0O0O =int (sys .argv [1 ])#line:101
            OOOO00O00O00OO0OO =sys .argv [2 ]#line:102
            OOO00O00O0O00O000 =sys .argv [3 ]#line:103
            OOO00OOO00OOOO000 =sys .argv [4 ]#line:104
            asyncio .run (OO0OO00OOOOOOOOOO (OOO00OOO0000O0O0O ,OOOO00O00O00OO0OO ,OOO00O00O0O00O000 ))#line:105
        else :#line:106
            print ("You are not allowed to use this script. Please contact the owner of this script.")#line:107
    except KeyboardInterrupt :#line:108
        pass #line:109
