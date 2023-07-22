import datetime

hora = datetime.datetime.now().time()

if hora >= datetime.time(6, 0) and hora <= datetime.time(12, 0):
    print("Bom dia")
elif hora >= datetime.time(12, 1) and hora <= datetime.time(18, 0):
    print("Boa tarde")
else:
    print("Boa noite")
