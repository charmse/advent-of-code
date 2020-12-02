import time

# --- Day 1: Report Repair ---

# Dumb solution
def findPair(input):
    for i in input:
        difference = 2020 - i
        if difference in input:
            return (i, difference)
            break

def main():
    # Read Input
    with open('./in.txt', 'r', encoding='utf-8') as f:
        input = list(map(int, f.readlines()))
    print(f'Input: {input}\n')
    
    # Find pair
    print('Finding pair...')
    begin = time.time()
    pair = findPair(input)
    time.sleep(1)
    t = time.time() - begin

    # Print results and solution
    print(f'Pair: {pair}')
    print(f'Solution: {pair[0]*pair[1]}')
    print(f'Time took: {t}')

if __name__ == "__main__":
    main()
