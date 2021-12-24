#Dette programmet faar inn tempratur i fahrenheit fra bruker og printer det
#Deretter blir tempraturen omgjort til celsius og saa printet

#bruker skriver inn tempratur i fahrenheit, blir lagret i variabel og videre printet
tempFahrenheit = int(input('Oppgi tempratur i fahrenheit: '))
print(f'Tempraturen i fahrenheit er: {tempFahrenheit}')

#Fahrenheit tempratur blir konvertert til celsius og lagret i en ny variabel, deretter blir celcius tempratur printet
tempTilCelsius = (tempFahrenheit - 32) * 5/9
print(f'Tempraturen i fahrenheit omgjort til celsius er: {tempTilCelsius:.2f}')