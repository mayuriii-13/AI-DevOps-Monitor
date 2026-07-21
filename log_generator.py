import time
import random


errors=[

"Database connection failed",

"API timeout detected",

"Disk usage exceeded 95%",

"Service unavailable"

]


while True:


    error=random.choice(errors)


    log=f"""

2026-07-21 ERROR | {error}

"""


    with open(
        "logs/server.log",
        "a"
    ) as file:

        file.write(log)



    print(
        log
    )


    time.sleep(10)
