argparse import

# Funções para conversão de escalas

# celcius para fahrenheit
def celsius_to_fahrenheit(tc):
    return c * 9/5 + 32

# celcius para kelvin
def celsius_to_kelvin(tc):
    return c + 273.15

# fahrenheit para kelvin
def fahrenheit_to_kelvin(tf):
    return (5/9)*(tf-32) + 273.15

# fahrenheit para kelvin
def fahreingeit_to_celcius(tf):
    return (5/9) * (tf-32)
    
# kelvin para fahrenheit 
def kelvin_to_fahreinheit(tk):
    return 9/5 * (tk-273) + 32
    
# kelvin para fahrenheit
def kelvin_to_celcius(tk):
    return tk - 273.15
    


# Cria um parser de argumentos
parser = argparse.ArgumentParser(description="Conversor de Escalas Termométricas")

# Argumentos para a conversão
parser.add_argument("--temp", type=float, required=True, help="Temperatura em Celsius")
parser.add_argument("--scale", choices=["fahrenheit", "kelvin"], required=True, help="Escala para conversão")

# Analisa os argumentos da linha de comando
args = parser.parse_args()

# Executar ação com base na escala fornecida
if args.scale == "fahrenheit":
    temp_converted = celsius_to_fahrenheit(args.temp)
    print(f"Temperatura convertida para Fahrenheit: {temp_converted} °F")
elif args.scale == "kelvin":
    temp_converted = celsius_to_kelvin(args.temp)
    print(f"Temperatura convertida para Kelvin: {temp_converted} K")

