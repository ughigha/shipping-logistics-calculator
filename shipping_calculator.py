# shipping_calculator.py

def calculate_shipping_rate(weight, distance, speed):
    """
    Calculates the shipping rate based on weight, distance, and shipping speed.
    """
    rate = 0.5 * weight + 0.1 * distance

    if speed == "express":
        rate *= 1.5
    elif speed == "standard":
        rate *= 1.0
    else:
        return "Invalid shipping speed."

    return f"The calculated shipping rate is: ${rate:.2f}"

# Example usage
print(calculate_shipping_rate(10, 100, "express")) # Weight: 10kg, Distance: 100km
