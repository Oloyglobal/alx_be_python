# Global conversion factors
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def main():
    try:
        choice = input("Choose conversion: (C/F): ").strip().upper()
        if choice == "C":
            celsius = float(input("Enter temperature in Celsius: "))
            print("In Fahrenheit:", celsius_to_fahrenheit(celsius))
        elif choice == "F":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print("In Celsius:", fahrenheit_to_celsius(fahrenheit))
        else:
            print("Invalid choice")
    except ValueError:
        print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
