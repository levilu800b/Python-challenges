from replit import clear

# HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
print("Welcome to the secret auction program.")

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Angela": 123, "James": 321}
    for bidder in bidding_record:
        # print(bidder) # Angela, James
        # print(bidding_record[bidder]) # 123, 321
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
    elif should_continue == "yes":
        clear()