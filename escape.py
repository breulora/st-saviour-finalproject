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

    response = input('What has hands but cannot clap? ')
    if response.lower() == 'clock' or response.lower() == 'a clock':
        print_dramatic_text('correct!')
    else:
        print_dramatic_text('incorrect ...')