logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

from os import system

bids = {}
bidding_finished = False
auction_name = ""

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder, bid_amount in bidding_record.items():
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is [{winner}] with a bid of [${highest_bid}]")

def print_logo_with_auction_name(auction_name):
  system('cls||clear')
  print(logo)
  if auction_name != "":
    print(f"[Auction/Bid name]: {auction_name}\n")

print_logo_with_auction_name(auction_name)
auction_name = input("[Please input the Auction/Bid name]: ")

while not bidding_finished:
  print_logo_with_auction_name(auction_name)
  name = input("[What is your name?]: ")
  price = int(input("[What is your bid?]: $"))
  bids[name] = price
  if should_continue := input("[Are there any other bidders?] Type 'yes or 'no'.\n").lower() == "no":
    bidding_finished = True
    print_logo_with_auction_name(auction_name)
    find_highest_bidder(bids)
