celsius = float(input('Informe a temperatura do local que você está nesse momento em °C: '))
fahrenheit = float((1.8 * celsius) + 32)
kelvin = float(celsius + 273)
print('A temperatua {}°C, corresponde a {}°F e {} na escala Kelvin.'.format(celsius, fahrenheit, kelvin))
