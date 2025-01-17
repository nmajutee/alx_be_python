# Global Variables - conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to Convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to Convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

# Main Script Execution
if __name__ == "__main__":
    print('Welcome to the Temperature Conversion Tool!')
    
    # Prompt user for input
    temperature = input('Enter the temperature to convert: ')
    temperature_unit = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').upper()
    
    # Validate input
    try:
        temperature = float(temperature)
    except ValueError:
        print('Invalid temperature. Please enter a numeric value.')
        exit()  # Exit if the input is invalid
        
    # Perform conversion based on the unit
    
    if temperature_unit == 'C':
        converted_temperature = convert_to_celsius(temperature)
        print(f'{temperature}°C is {converted_temperature:.1f}°F.')
    elif temperature_unit == 'F':
        converted_temperature = convert_to_fahrenheit(temperature)
        print(f'{temperature}°F is {converted_temperature:.1f}°C.')
    else: 
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")