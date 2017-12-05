def read_passphrases(filepath):
    with open(filepath) as f:
        content = f.read()
        return map(lambda line: line.split(),content.split("\n"))

def passphrase_has_no_duplicates(passphrase):
        return len(passphrase) == len(set(passphrase))

def passphrase_has_no_anagrams(passphrase):
    lenght = len(passphrase)
    for i in range(0, lenght - 1):
        sorted_a = sorted(passphrase[i])

        for j in range(i + 1, lenght):
            sorted_b = sorted(passphrase[j])
            if sorted_a == sorted_b:
                return False

    return True


if __name__ == "__main__":
    input = read_passphrases('./AOC04/input.txt')
    no_duplicates_count = reduce(lambda x,y: x+y, map(lambda p: 1 if passphrase_has_no_duplicates(p) == True else 0, input))
    print 'Valid passphrases without duplicates: {0}'.format(no_duplicates_count)

    no_anagrams_count = reduce(lambda x,y: x+y, map(lambda p: 1 if passphrase_has_no_anagrams(p) == True else 0, input))
    print 'Valid passphrases without anagrams: {0}'.format(no_anagrams_count)