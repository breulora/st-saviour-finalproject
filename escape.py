import time

def print_dramatic_text(text: str, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

if __name__ == '__main__':
    print_dramatic_text('welcome to Breukelen\'s Escape Room!')

    response = input('You see a black box ... open it? (y/n) ')
    if response.lower() == 'y':
        print_dramatic_text('you opened the box!')

        # TODO add events for the open box ...
    else:
        print_dramatic_text('the box remains closed ... for now')

    score = 0

    response = input('What has hands but cannot clap? ')
    if response.lower() == 'clock' or response.lower() == 'a clock':
        print_dramatic_text('correct!')
        score += 1
    else:
        print_dramatic_text('incorrect ...')

    response = input('You see a lock ... crack the code? (y/n) ')
    if response.lower() == 'y':
        print_dramatic_text('you decided to crack the code!')

        # TODO add events for the lock ...
    else:
        print_dramatic_text('the code remains unkown ... for now')

    response = input('What number comes after 5?')
    if response.lower() == '6' or response.lower() == 'six':
        print_dramatic_text('correct!')
        score += 1
    else:
        print_dramatic_text('incorrect ...')

    response = input('You see a bigger box ... open it? (y/n) ')
    if response.lower() == 'y':
        print_dramatic_text('you opened the box!')

        # TODO add events for the open box ...
    else:
        print_dramatic_text('the box remains closed ... for now')

    response = input ('I am tall when I am young and short when I am old what am I?')
    if response.lower() == 'candle' or response.lower() == 'a candle':
        print_dramatic_text('correct!')
        score += 1
    else:
        print_dramatic_text('incorrect ...')

    response = input('You see a phone ... unlock it? (y/n) ')
    if response.lower() == 'y':
        print_dramatic_text('you unlocked it!')

        # TODO add events for the phone ...
    else:
        print_dramatic_text('the phone remains locked ... for now')

    response = input ('What has keys but can not open locks?')
    if response.lower()== 'piano' or response.lower() == 'a piano':
        print_dramatic_text('correct!')
        score += 1
    else:
        print_dramatic_text('incorrect ...')

    response = input('You see paints and brushes ... mix them? (y/n) ')
    if response.lower() == 'y':
        print_dramatic_text('you mixed the paints!')

        # TODO add events for the mix paints ...
    else:
        print_dramatic_text('the paints remain unmixed ... for now')

    response = input ('What color do you get when you mix red and white?')
    if response.lower ()== 'pink':
        print_dramatic_text('correct!')
        score += 1
    else:
        print_dramatic_text('icorrect ...')
        
    # at the end of the game
    if score >= 4:
        print_dramatic_text('congratulations you win!')
    else:
        print_dramatic_text('sorry you did not score enough points ...')