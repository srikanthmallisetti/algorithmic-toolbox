"""
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters,
return true if sentence is a pangram, or false otherwise.

"""


def is_pangram(sen: str) -> bool:
    return len(set(sen)) >= 26


if __name__ == "__main__":
    print(is_pangram("thequickbrownfoxjumpsoverthelazydog"))
