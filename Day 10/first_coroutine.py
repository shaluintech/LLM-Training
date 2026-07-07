import asyncio

async def greet(name):
    print(f"...waiting to greet {name}")
    await asyncio.sleep(1) #nonblocking
    return f"Hello {name}"
maybe = greet("Tushar")
print("greet(Tushar) gave us:",maybe)
print("Type:", type(maybe).__name__)
maybe.close()
result1 = asyncio.run(greet("Tushar"))
result2 = asyncio.run(greet("Tanya"))
print("result", result1)
print("result", result2)