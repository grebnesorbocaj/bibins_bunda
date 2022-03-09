import time
import random
# Put other functions here
def slot_init():
    return 1, False, 100, ["Cherry", "Banana", "Grapes"]

def get_bet(cur_tokens):
    bet_tokens = int(input("Wagwan tokens yana bet my broda? "))
    if bet_tokens > cur_tokens:
        print("Yana got dem tokens my broda!")
    else:
        return bet_tokens

def play(img):
    return [random.choice(img), random.choice(img), random.choice(img)]

def settle_bet(result, bet, token):
    # 1. Three-in-a-row: three identical fruits (win twice the bet)
    if len(set(result)) == 1:
        print(f"Congrats broda you done got dem 3 identicals. You win {2*bet} tokens.  Up to {token+2*bet}.")
        token = token + 2*bet
    # 2. Three-of-a-kind: three distinct fruits (win the bet)
    elif len(set(result)) == 3:
        print(f"Congrats broda you done got dem 3 distincts. You win {bet} tokens. Up to {token+bet}.")
        token = token + bet
    # 3. Bummer: all other combinations (lose the bet)
    else:
        print(f"Damn nibba. You lose {bet} tokens. Down to {token-bet}.")
        token = token - bet
    return token


# Estimated lines of code is about 40 here
# Main
round, quit, cur_tokens, img = slot_init()
while not quit:
    print(f"\n******** Round: {round} ******** Tokens Left: {cur_tokens} ********")
    bet = get_bet(cur_tokens)
    result = play(img)
    cur_tokens = settle_bet(result, bet, cur_tokens)
    if cur_tokens==0:
        break
    else:
        quit = input("Quit the game (Y/N): ").upper()=='Y'
        round += 1
print(f"\n*** Game Over. Tokens left: {cur_tokens}. ***") 