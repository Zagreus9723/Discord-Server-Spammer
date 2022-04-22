import discum
import json
import time
bot = discum.Client(token=f'{input("Input token: ")}', log=False)
message = input("Input message: ")
time = input("Time to sleep: ")
for x in json.loads(bot.getGuildChannels(f'{input("Input guild ID: ")}').text):
  try:
    time.sleep(int(time))
    print(x['id'])
    bot.sendMessage(f"{x['id']}",f"{message}")
  except:
    ()
