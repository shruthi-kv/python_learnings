import math
import myModule
import requests

print(math.sqrt(4))
myModule.printHello()

r =  requests.get("https://www.google.com/?zx=1792418125676")
print(r.text)