def count_alpha(sentence):
    count = {}
    for i in sentence:
        if i in count:
            count[i.lower()] = count[i.lower()] + 1
        else:
            count[i.lower()] = 1
    print(count)
    return count

def main():
    sentence = "Mary had a little lamb."
    count_alpha(sentence)

if __name__ == '__main__':
    main()