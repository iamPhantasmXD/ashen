import os
import telethon
import re
import time
from random import sample
import asyncio
import json
import requests
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon import events

SESSION = '1AZWarzsBuzdzzTIURzytGT7wj-zIXpIn_AmVodmxmwhoLi9ZvjXq_V4BLnOJB_72ubwE99RJtltnEZX6t9NePdklvpg_aEUlJhGU20EvRDhplkotYam_owQRMlDBDFNmHV6bAawb5Dti5KlJld5BQwursgKn2agUEOg9OvMJ82F7ZpmBRBNG2VI2L294JZbPsmE6zd7b9cVqu7nCeenwLax-KXVzmVW3Yz990uHqdG-RK8e47UiL086dndC0ywfOqCjc8W5Ae4TLMqcE-6vKFixxh3xYdk0vBKkA09V_u9xHNoWXdks73Lg1_g3ACnJkHJClX-5fvNhEMXGoTOViR23W9-AFsxI='
API_ID = '5367566'
API_HASH = '641c80fcd5206311afd85bf78580ca4f'
LOG_GROUP = -1001274630529
list1 = [510491, 510484, 512085, 512104, 512173, 512940, 513096, 513364, 513859, 514346, 515685, 516402, 516615, 516659, 516582, 517270, 517210, 517402, 517355, 517580, 517661, 517708, 517964, 518256, 519479, 520202, 521079, 521085, 521597, 521794, 522141, 523670, 523981, 524051, 524118, 524522, 524615, 526155, 526158, 526511, 526910, 526927, 527370, 529305, 530091, 531191, 531432, 532016, 532169, 532726, 532796, 533140, 534178, 534274, 535330, 535331, 535927, 538147, 538391, 539138, 539157, 539921, 539986, 540331, 540630, 541134, 541374, 541902, 541973, 542127, 542190, 542937, 542949, 543202, 545017, 545935, 545936, 546523, 547165, 548485, 548806, 548807, 548804, 548805, 549406, 549405, 550489, 550490, 550598, 552419, 552474, 552773, 552805, 553806, 554214, 554642, 557583, 557676, 558339, 559316, 559574, 559576, 559729, 559728, 563774, 571722, 575672, 581335, 581840, 581880, 589461] 
bot = TelegramClient(StringSession(SESSION), API_ID, API_HASH)
bot.start()

@bot.on(events.NewMessage(pattern='/go'))
async def runner(event):
    print('hi sessy')
    bin = 0
    l_bin = 99999
    while bin <= l_bin:
        bb=(sample(list1,1))
        def slicetext(text, start, end):
          try:
            return text.split(start)[1].split(end)[0]
          except:
            return ""
            
        bb=(slicetext(f"{bb}", "[", "]"))
        #print(bb)
        response = requests.get(f'https://rezothcc.herokuapp.com/cc.php?format={bb}xxxxxxxxxx|xx|2xxx|xxx&count=1&json')
        #print(response.text)
        if json.loads(response.content)["ok"]:
            card = json.loads(response.content)["data"]
            #print(card)
            def slicetext(text, start, end):
              try:
                return text.split(start)[1].split(end)[0]
              except:
                return ""
                
            card=(slicetext(f"{card}", "['", "']"))
            #print(card)
            data = {
              'data': f'{card}'
            }
            response = requests.post('https://www.mrchecker.net/card-checker/ccn2/api.php', data=data)
            bb= (response.text)
            #print(bb)
            #print(bb)
            def slicetext(text, start, end):
              try:
                return text.split(start)[1].split(end)[0]
              except:
                return ""
            bbbb=(slicetext(f"{bb}", "</b> | ", " "))
            #print(bbbb)
            def slicetext(text, start, end):
              try:
                return text.split(start)[1].split(end)[0]
              except:
                return ""
            bbb=(slicetext(f"{bb}", ";'>", "</b>"))
            print(bbb, bbbb)
            
            if bbb=='Unknown':
                print('Miss')
            if bbb=='Die':
                print('Miss')
            if bbb=='Live':
                #print(bbbb)
                print('----------------------------------------')
                print(bbbb)
                final_card = f'''/ch {bbbb}'''
                await bot.send_message(LOG_GROUP, final_card)
                time.sleep(20)
print('bot start')
bot.run_until_disconnected()