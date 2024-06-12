def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def temperature_converter(celsius):
    fahrenheit = celsius_to_fahrenheit(celsius)
    kelvin = celsius_to_kelvin(celsius)
    return (f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit and "
            f"{kelvin} degrees Kelvin.")

# Example usage
print(temperature_converter(20))
