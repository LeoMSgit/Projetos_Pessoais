from datetime import datetime
from dateutil.relativedelta import relativedelta

dataInicial = datetime(2019,10,21)
dataAtual = datetime.now()

dif = relativedelta(dataAtual, dataInicial)

anos = dif.years
meses = dif.months
dias = dif.days


print("❤️  Feliz {} anos, {} meses e {} dias de namoro❤️  ".format(anos,meses,dias))
