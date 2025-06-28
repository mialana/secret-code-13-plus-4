import questionary

response = questionary.confirm("Do you like apples?").ask()

print(response)

# response is either True or False
if response: 
    favorite_friend = questionary.select(
        "Who is your favorite friend?", choices=["sam", "tom"]
    ).ask()

    print("My favorite friend is " + favorite_friend)
else:
    print("WHY DON'T YOU LIKE APPLES???")