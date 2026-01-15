score = 0

country = {
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "France": "Paris",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Germany": "Berlin",
    "Bulgaria": "Sofia",
    "Turkey": "Ankara",
    "Greece": "Athens",
    "Hungary": "Budapest",
    "Romania": "Bucharest",
    "Japan": "Tokyo",
    "South Korea": "Seoul",
    "North Korea": "Pyongyang",
    "Mexico": "Mexico City",
    "Russia": "Moscow",
    "Ukrane": "Kyev",
    "Italy": "Rome",
    "Albania": "Tirana",
    "Poland": "Warsaw"
}
while True:
    user_country = input("Enter a country: ")

    if user_country in country:
        user_capital = input(f"Enter the capital of {user_country}: ")

        if user_capital.lower() == country[user_country].lower():
            print("Correct!")
            score += 1

        else:
            print("Incorrect.")
            print(f"The correct capital is {country[user_country]}.")
    else:
        print("Country not found in the dictionary.")
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print(score)
        break
