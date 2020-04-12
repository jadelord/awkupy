from awkupy import Awk

awk = Awk()
awk.PATTERN = '/gold/'
awk.ACTION = 'country[$4]++'
awk.END = 'for (i in country) print "Country: " i," count: ", country[i]'
awk.INPUT = 'coins.txt'

print(awk.code)

awk()
