def get_user_weather_input():
    try:
        temperature = float(input("Enter the current temperature: "))
        return temperature
    except ValueError:
        print("Invalid input. Please enter a numerical value for the temperature.")
        return None

def suggest_outfit(temperature):
    if temperature > 80:
        return "It's hot! How about shorts and a t-shirt, or a dress?"
    elif 60 <= temperature <= 80:
        return "Not too hot, not too cold. Jeans and a jacket would be fine."
    else:
        return "It's cold! Stay inside or perish with the snowmen!"

def main():
    temperature = get_user_weather_input()

    if temperature is not None:
        outfit_suggestion = suggest_outfit(temperature)
        print(f"Suggested outfit: {outfit_suggestion}")

if __name__ == "__main__":
    main()

