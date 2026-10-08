from pyscript import document  # pyright: ignore[reportMissingImports]

# list of ICT club members
club_members = ["Alex Cruz", "Rose Garcia", "Leo Ramos", "Mia Santos", "Sam Reyes"]

# check if the candidate is a club member
def check_member(event):

    # get the names
    first_name = document.querySelector("#first").value.strip()
    last_name = document.querySelector("#last").value.strip()

    # combine the names
    full_name = first_name + " " + last_name

    # check the list
    result = full_name in club_members

    # messages
    messages = [
        f"Sorry {full_name}, your name is not on the list.",
        f"Congratulations {full_name}! You are now part of the ICT club."
    ]

    # show result
    document.querySelector("#result").innerText = messages[result]