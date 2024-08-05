import os
import time
import asyncio
import sys
if len(sys.argv) > 1:
    i = int(sys.argv[1])
    async def fun(a, b):
        sum = a + b
        pid = os.getpid()
        print(f"2nd pid fun: {pid}")
        print(a,b)
        print(sum)
        print("Hello World")
        await asyncio.sleep(10)
        try:
            f=open("file2.txt",'w')
            f.write(str(pid))
            f.close()
        except Exception as e:
            print(e)
        await asyncio.sleep(20)
        print("Last")
        for i in range(0, 10):
            print(i)
            time.sleep(5)
        
        print("#######")
    async def fun2(a,b):
        await asyncio.sleep(10)
        sub=a-b
        print(f"sub : {sub}")
        print("fun2 End")
    async def main(x,y):
        L=await asyncio.gather(fun(x,y),
                                fun2(x,y),) 
    asyncio.run(main(i,i+1))
else:
    print('No value received.')