# temperature_converter.py

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9


def main():
    """Main program to handle user input and conversion."""
    try:
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "C":
            converted = celsius_to_fahrenheit(temp)
            print(f"{temp:.1f}°C is {converted:.1f}°F")
        elif unit == "F":
            converted = fahrenheit_to_celsius(temp)
            print(f"{temp:.1f}°F is {converted:.1f}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature input. Please enter a number.")


if __name__ == "__main__":
    main()
