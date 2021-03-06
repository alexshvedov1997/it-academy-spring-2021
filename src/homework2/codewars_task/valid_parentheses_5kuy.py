"""
                 Valid Parentheses - 5kuy

Write a function that takes a string of parentheses,
and determines if the order of the parentheses is valid.
The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
"" => true

Constraints

0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis,
input may contain any valid ASCII characters. Furthermore, the input
string may be empty and/or not contain any parentheses at all.
Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).
"""


def delete_other_symb(symb):
    if symb == "(" or symb == ")":
        return True
    else:
        return False


def valid_parentheses(string):
    l = list(filter(delete_other_symb, string))
    if not l:
        return True
    if len(l) % 2:
        return False
    state = True
    while True:
        i = 0
        parent = l.pop(0)
        if parent == ")":
            return False
        while i < len(l):
            if l[i] == ")":
                del l[i]
                break
            i += 1
            if i == len(l):
                return False
        if not l:
            return True
        elif not state:
            return False


def print_valid_parentheses():
    print("\n","-" * 20)
    print("\t\tTask: Valid Parentheses - 5kuy")
    print("gfhfgh)(fghgj())3423)gfh", "=>", valid_parentheses("gfhfgh)(fghgj())3423)gfh"))
    print("rhiccn(bem(qkedw(nmhnf(skcwov))eowlcfyaeih", "=>",
          valid_parentheses("rhiccn(bem(qkedw(nmhnf(skcwov))eowlcfyaeih"))
    print("(()", "=>", valid_parentheses("(()"))
    print("(sdgdsfg(dfs)(45)())", "=>", valid_parentheses("(sdgdsfg(dfs)(45)())"))
    print("()", "=>", valid_parentheses("()"))
    print("-" * 20)
