from lib.temperature import Temperature

# be able to Temprature(celcius=value, fahrenheit=value, kelvin=value)
temp = Temperature(celcius=50)

# default celcius is 50
cel_to_fah_default = temp.celcius().toFahrenheit(True)

# convert celcius to fahrenheit
# celcius change or overwritten to 30, below
cel_to_fah = temp.celcius(30).toFahrenheit(True)
# convert celcius to kelvin
cel_to_kel = temp.celcius(20).toKelvin(True)
# convert fahrenheit to celcius
fah_to_cel = temp.fahrenheit(50).toCelcius(True)

print('50' + temp.symbol('c') + ' = ' + cel_to_fah_default)
print('30' + temp.symbol('C') + ' = ' + cel_to_fah)
print('30' + temp.symbol('C') + ' = ' + cel_to_kel)
print('30' + temp.symbol('F') + ' = ' + fah_to_cel)
