def expand_macros(code):
    macro_table = {}
    expanded_code = []

    # First pass: Collect macro definitions
    lines = code.strip().split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith('MACRO'):
            macro_name = line.split()[1]
            macro_definition = []
            i += 1
            while i < len(lines) and lines[i].strip() != 'MEND':
                macro_definition.append(lines[i].strip())
                i += 1
            macro_table[macro_name] = macro_definition
        else:
            expanded_code.append(line)
        i += 1

    # Second pass: Expand macros in the code
    final_code = []
    for line in expanded_code:
        tokens = line.split()
        if tokens and tokens[0] in macro_table:
            # Replace macro call with macro definition
            macro_name = tokens[0]
            macro_definition = macro_table[macro_name]
            final_code.extend(macro_definition)
        else:
            # Regular instruction, add to final code
            final_code.append(line)

    return final_code

def generate_intermediate_code(code):
    intermediate_code = []
    line_num = 1

    for line in code:
        intermediate_code.append(f"{line_num}: {line}")
        line_num += 1

    return intermediate_code

# Example Macro-Expanded Code
code = """
LOAD J
STORE M
MACRO EST
LOAD P
ADD V
MEND
LOAD S
MACRO ADD7 P4, P5, P6
LOAD P5
LOAD e
ADD d
MEND
LOAD S
MACRO SUB4 ABC
LOAD U
STORE ABC
MEND
SUB4 XYZ
SUB 8
SUB 2
STORE P4
STORE P6
MEND
EST
ADD7 C4, C5
SUB4 z
END
"""

# Expand macros in the code
expanded_code = expand_macros(code.strip().upper())

# Generate Intermediate code from expanded code
intermediate_code = generate_intermediate_code(expanded_code)

# Print Intermediate code
print("Intermediate Code:")
for line in intermediate_code:
    print(line)
