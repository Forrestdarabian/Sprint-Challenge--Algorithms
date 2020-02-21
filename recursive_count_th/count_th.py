'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # TBC

    i = word.find("th")
    if i == -1:
        return 0
    return 1 + count_th(word[i + 2:])


print(count_th("thereisnothinglefttosay"))
