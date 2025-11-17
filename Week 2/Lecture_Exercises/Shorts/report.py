# Main function to initialize spacecraft data and print the report
def main():
    # Create a dictionary with the spacecraft's name
    spacecraft = {"name": "James Webb Space Telescope"}

    # Add distance and orbit information to the dictionary
    spacecraft.update({"distance": 0.01, "orbit": "Sun"})

    # Generate and print the formatted report
    print(create_report(spacecraft))

# Function to create a formatted report from the spacecraft dictionary
def create_report(spacecraft):
    return f"""
    ========= REPORT =========

    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} AU
    Orbit: {spacecraft.get("orbit", "Unknown")}

    ==========================
    """

# Run the main function
main()
