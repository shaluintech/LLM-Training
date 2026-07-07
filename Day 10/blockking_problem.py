import time

def fake_api_call(name,seconds):
    print(f"start {name}")
    time.sleep(seconds)
    print(f"done {name}")
    return f"{name}result"

start = time.perf_counter()
r1= fake_api_call("model-A",1.0)
r2= fake_api_call("model-B",1.0)
r3= fake_api_call("model-C",1.0)
elapsed = time.perf_counter() - start
print("Results",[r1,r2,r3])
print(f"Three 1-second calls took{elapsed}")