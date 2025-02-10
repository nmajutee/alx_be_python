def safe_divide(numerator, denominator):
    try:
        # Convert to float and store the values
        numerator = float(numerator)
        denominator = float(denominator)

        if denominator == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")

        return f"The result of the division is {numerator / denominator}"
    
    except ZeroDivisionError as e:
        return str(e)
    
    except ValueError:
        return "Error: Please enter numeric values only."
