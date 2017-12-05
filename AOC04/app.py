def read_passphrases(filepath):
    with open(filepath) as f:
        content = f.read()
        return map(lambda line: line.split(),content.split("\n"))

def passphrase_has_no_duplicates(passphrase):
        return len(passphrase) == len(set(passphrase))

if __name__ == "__main__":
    input = read_passphrases('./AOC04/input.txt')
    result = reduce(lambda x,y: x+y, map(lambda p: 1 if passphrase_has_no_duplicates(p) == True else 0, input))
    print 'Valid passphrases without duplicates: {0}'.format(result)