import os
import time
from datetime import datetime

hour1 = datetime.now()

for i in range(0, 5):
    os.system("node tester.js")

hour2 = datetime.now()

print(f"\nHeure de début : {hour1.hour}h {hour1.minute}min {hour1.second}sec")
print(f"Heure de fin : {hour2.hour}h {hour2.minute}min {hour2.second}sec")
