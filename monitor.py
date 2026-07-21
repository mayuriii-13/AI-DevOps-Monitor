import time

from ai_helper import analyze_log
from alert import send_alert
from config import LOG_FILE



def monitor():

    print(
        "🚀 AI DevOps Monitor Started..."
    )

    print(
        f"📡 Watching: {LOG_FILE}"
    )


    with open(LOG_FILE,"r") as file:

        file.seek(0,2)


        while True:

            line=file.readline()


            if line:

                if (
                    "ERROR" in line
                    or
                    "CRITICAL" in line
                ):


                    print(
                        "\n🚨 ERROR DETECTED"
                    )

                    print(line)



                    analysis = analyze_log(
                        line
                    )


                    print(
                        "\n🤖 AI ROOT CAUSE ANALYSIS:"
                    )

                    print(
                        analysis
                    )


                    alert_message = f"""

🚨 DevOps Alert

Log:
{line}


AI Analysis:

{analysis}

"""


                    send_alert(
                        alert_message
                    )


            time.sleep(1)



if __name__=="__main__":

    monitor()
