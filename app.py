from google import genai
import time

client = genai.Client(api_key="AQ.Ab8RN6KPfnJtVhd4Z8R-OIyvsmZT6SXeabDCjiXE1bxnuEWQbg")

while True:
    user_input = input("user: ")

    if user_input == "end":
        break

    try:
        interaction = client.interactions.create(
            model="gemini-3.6-flash",
            input=user_input
        )

        print("bot:", interaction.output_text)

    except Exception as e:
        print("error आया, retry हो रहा है...")
        time.sleep(2)