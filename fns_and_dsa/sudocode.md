# Define Global Variables
SET FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
SET CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Define Function to Convert Fahrenheit to Celsius
FUNCTION convert_to_celsius(fahrenheit)
    RETURN (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
END FUNCTION

# Define Function to Convert Celsius to Fahrenheit
FUNCTION convert_to_fahrenheit(celsius)
    RETURN (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
END FUNCTION

# Main Script Execution
FUNCTION main()
    DISPLAY "Welcome to the Temperature Conversion Tool!"

    # Prompt user for input
    INPUT temperature AS STRING
    INPUT unit AS STRING ("C" for Celsius, "F" for Fahrenheit)

    # Validate input
    TRY
        SET temperature = CONVERT temperature TO FLOAT
    CATCH EXCEPTION
        RAISE ERROR "Invalid temperature. Please enter a numeric value."
        EXIT PROGRAM
    END TRY

    # Perform conversion based on the unit
    IF unit IS "C"
        SET converted_temperature = CALL convert_to_fahrenheit(temperature)
        DISPLAY "Temperature in Fahrenheit: ", converted_temperature
    ELSE IF unit IS "F"
        SET converted_temperature = CALL convert_to_celsius(temperature)
        DISPLAY "Temperature in Celsius: ", converted_temperature
    ELSE
        DISPLAY "Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit."
    END IF
END FUNCTION

# Start the Program
CALL main()
