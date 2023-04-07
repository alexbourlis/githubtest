import asyncio

async def main():   #creates a wrapper around this object(coroutine object)
    print('tim')
    #await foo('text')
    task = asyncio.create_task(foo('text'))
    print('finished')


async def foo(text):
	
	await asyncio.sleep(1)  #await required to run a coroutine
	print(text)

asyncio.run(main()) #we need to define an event loop(lower level, async takes care of that)