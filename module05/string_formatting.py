pay_system = {
    5: "MasterCard",
    4: "Visa",
    3: "American Express"
}

card_number = ["5375414112345678", "4168757587879876", "216875758787987d"]


def isvalid_card(card):
    # ^[0-9]{16}$
    return card.isdigit() and len(card) == 16


for card in card_number:
    string = "Card #: {:<8} System: {:^16} card is valid: {:>16}"
    print(string.format(card, pay_system.get(
        int(card[0]), 'Unknown'), str(isvalid_card(card))))
