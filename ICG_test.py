from basic import Lexer, Parser, TACGenerator

def run_tac_tests():
    test_cases = [
        ("20-1*(4/3)+2+(2+4)", [
            't1 = 20',
            't2 = 1',
            't3 = 4',
            't4 = 3',
            't5 = t3 / t4',
            't6 = t2 * t5',
            't7 = t1 - t6',
            't8 = 2',
            't9 = t7 + t8',
            't10 = 2',
            't11 = 4',
            't12 = t10 + t11',
            't13 = t9 + t12'
        ]),
        ("print(hello)", [
            'print hello'
        ]),
        ("var x = 5", [
            'x = 5'
        ]),
        ("let y = 10", [
            'y = 10'
        ]),
        ('print("Hello, World!")', [
            't1 = "Hello, World!"',
            'print t1'
        ]),
        ('while x=5: print(x)', [
            'label t1',
            't2 = 5',
            'if not t2 goto t3',
            'print x',
            'goto t1',
            'label t3'
        ])
    ]

    for i, (input_text, expected_tac) in enumerate(test_cases):
        lexer = Lexer("<stdin>", input_text)
        tokens, error = lexer.make_tokens()
        if error:
            print(f"Test {i + 1} failed: Lexer error: {error.as_string()}")
            continue

        parser = Parser(tokens)
        ast = parser.parse()

        if ast.error:
            print(f"Test {i + 1} failed: Parser error: {ast.error.as_string()}")
            continue

        tac_generator = TACGenerator()
        tac_instructions = tac_generator.generate(ast.node)
        tac_instructions_str = [str(instr) for instr in tac_instructions]

        if tac_instructions_str == expected_tac:
            print(f"Test {i + 1} passed")
        else:
            print(f"Test {i + 1} failed: expected {expected_tac}, got {tac_instructions_str}")

run_tac_tests()
