# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!
#
# 13. Balanced Symbols
# Check if the brackets in a string are balanced.
# Input: "{[()]}"
# Output: True
# Input: "{[(])}"
# Output: False

def balanced_symbols(s: str) -> bool:
    """
    Return True if all brackets in s are balanced; otherwise False.
    Supports (), {}, [] and ignores other characters.
    """
    if not isinstance(s, str):
        raise TypeError("s must be a string")
    pairs = {")": "(", "}": "{", "]": "["}
    stack = []
    for ch in s:
        if ch in pairs.values():
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack


def _run_tests():
    cases = [
        ("{[()]}", True, "balanced nested"),
        ("{[(])}", False, "crossed"),
        ("", True, "empty string"),
        ("()", True, "simple pair"),
        ("(", False, "single opener"),
        (")", False, "single closer"),
        ("([]){}", True, "multiple groups"),
        ("([{}])", True, "deep nesting"),
        ("([}{])", False, "mismatched order"),
        ("abc{[()]}xyz", True, "ignores other chars"),
        ("[", False, "single bracket"),
        ("[]][[]", False, "extra closer"),
    ]
    for s, expected, label in cases:
        result = balanced_symbols(s)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: {label} | input={s!r} | expected={expected} got={result}")

    bad_inputs = [None, 123, ["[", "]"], {"a": 1}]
    for value in bad_inputs:
        try:
            balanced_symbols(value) 
            print(f"FAIL: expected TypeError for input={value!r}")
        except TypeError:
            print(f"PASS: TypeError for input={value!r}")


if __name__ == "__main__":
    _run_tests()
