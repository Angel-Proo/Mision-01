rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')

# Salida:
# october: 3.5cm
# november: 4.2cm
# december: 2.1cm

# El valor de december: 2.1cm

# Si, 'december' existe en rainfall
if 'december' in rainfall:
    # rainfall [en la posición december] es igual a
    # rainfall [en la posición december] + 1 (2.1+1)
    rainfall['december'] = rainfall['december'] + 1

# Si no:
else:

    # rainfall [en la posición december] es igual a 1
    rainfall['december'] = 1

print(rainfall['december'])
# Como december si existe, el valor será 3.1

#Total de precipitaciones 0
total_rainfall = 0

# Para cada valor en los valores de rainfall
for value in rainfall.values():
    
    # El total de las precipitaciones será igual a ese mismo + el valor que se está iterando

    total_rainfall = total_rainfall + value

# Muestra 'Hay un total de precipitaciones (el valor total) en centímetros en el último cuarto (haciendo referencia al cuarto del año)

print(f'There was {total_rainfall}cm in the last quarter')

# Salida:
# There was 10.8cm in the last quarter