cards = input()

# Initialize variables to store the cards for each suit
current_card = ""
p = set()  # Use set to store P cards
k = set()  # Use set to store K cards
h = set()  # Use set to store H cards
t = set()  # Use set to store T cards
is_greska = False
# Loop through each character in the input string
for index in range(len(cards)):
    current_card += cards[index]

    # Ensure we do not try to access cards[index+1] if we are at the last card
    if index + 1 == len(cards) or (cards[index + 1] in "PKHT" and cards[index] in "0123456789"):
        # Check for duplicates and raise an error if found
        if current_card[0] == "P":
            if current_card[1] + current_card[2] in p:
                print("GRESKA")
                is_greska = True
            p.add(current_card[1] + current_card[2])
        
        elif current_card[0] == "K":
            if current_card in k:
                print("GRESKA")
                is_greska = True
            k.add(current_card)
        
        elif current_card[0] == "H":
            if current_card in h:
                print("GRESKA")
                is_greska = True
            h.add(current_card)
        
        elif current_card[0] == "T":
            if current_card in t:
                print("GRESKA")
                is_greska = True
            t.add(current_card)
        
        current_card = ""


if (is_greska == False):
    # Print the number of missing cards in each suit
    print(f"{13 - len(p)} {13 - len(k)} {13 - len(h)} {13 - len(t)}")