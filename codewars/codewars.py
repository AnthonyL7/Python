def number(lines):
    if isinstance(lines, list):
      print([F'{i+1}: {line}' for i, line in enumerate(lines)])
    else:
        print([])

number(['9', '8', 'L', 'z', 'c', 'q', 'd', 'U', 'm', 'H', ']', 'f', 'D', 'w', 'w', 'v', 'K', 'a', '4', '1', '0', 'P', 'a', 'N', '4', 'C', '=', '`', 'C', 'n', 'v', 'V', 'U', 'I', 'l', '6', '9', 'M', 'f', 'A', 'K', 'V', '>', 'H', '?', 'b', 'q', '0', 'C', '\\', 'c', 'h', 'm', 'Y', 'k', 'E', 'x', 'v', 'e', 'O', 'E', 'M', '2', 'f', 'w', 'O', 'M', 'K', ':', 'L', 'y', '?', 'u', 'Z', '2', 'J', 'y', 'h', 'F', 'Y', 'Z', 'r', 'R', 'U', 'D', 'd', '^', '[', '0', 'z', 'Y', 'V', '`', 'U', 'r', ']', '\\', '>', 'v', 'h'])