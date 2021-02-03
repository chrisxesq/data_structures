# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append([i,next])    
        elif next in ")]}":
            if len(opening_brackets_stack)==0:
                return i+1
            else:
                top = opening_brackets_stack.pop(-1)
                if (next == ')' and top[1] == '(') or (next == ']' and top[1] == '[') or (next == '}' and top[1] == '{'):
                    continue
                else:
                    return i + 1
    if len(opening_brackets_stack)==0:
        return 'Success'
    
    return opening_brackets_stack[0][0]+1

def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()

