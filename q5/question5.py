sample1 = "Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth"
sample2 = "Then took the other, as just as fair, And having perhaps the better claim, Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same,"


def reverse_words(str):
    print("input :")
    print(str)
    result = ""
    value = str.split()
    value.reverse()
    for i in value:
        result += i + " "
    print("output :")
    print(result)


def main():
    reverse_words(sample1)
    print()
    reverse_words(sample2)


if __name__== "__main__":
    main()
