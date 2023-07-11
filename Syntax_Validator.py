class SyntaxValidator:
    def __init__(self):
        # Initialize the valid keywords, operators, and punctuation
        self.valid_keywords = ["if", "else",
                               "while", "for", "int", "float", "string"]
        self.valid_operators = ["+", "-", "*", "/"]
        self.valid_punctuation = ["(", ")", "{", "}", ";"]

    def validate_syntax(self, code):
        """
        Validates the syntax of the given code.

        Args:
            code (str): The code to be validated.

        Returns:
            None
        """
        try:
            # Compile the code to check for syntax errors
            compile(code, "<string>", "exec")
            print("No syntax errors found.")
        except SyntaxError as e:
            print(f"Syntax error: {e}")

    def tokenize(self, code):
        """
        Tokenizes the code into individual tokens.

        Args:
            code (str): The code to be tokenized.

        Returns:
            list: A list of tokens.
        """
        tokens = []
        current_token = ""
        is_within_string = False

        for char in code:
            if char.isspace() and not is_within_string:
                if current_token:
                    tokens.append(current_token)
                    current_token = ""
            elif char in self.valid_punctuation:
                if current_token:
                    tokens.append(current_token)
                    current_token = ""
                tokens.append(char)
            elif char == '"':
                current_token += char
                is_within_string = not is_within_string
            else:
                current_token += char

        if current_token:
            tokens.append(current_token)

        return tokens

    def parse_tokens(self, tokens):
        """
        Parses the tokens and checks their validity.

        Args:
            tokens (list): A list of tokens.

        Returns:
            None
        """
        line_number = 1
        index = 0

        while index < len(tokens):
            token = tokens[index]

            if token in self.valid_keywords:
                self.handle_keyword(token)
            elif token in self.valid_operators:
                self.handle_operator(token)
            elif token in self.valid_punctuation:
                self.handle_punctuation(token)
            elif token.isdigit():
                self.handle_number(token)
            elif token.startswith('"') and token.endswith('"'):
                self.handle_string(token[1:-1])
            else:
                self.handle_invalid_token(token, line_number)

                # Attempt error recovery by skipping to the next semicolon
                while index < len(tokens) - 1 and tokens[index] != ";" and tokens[index] != "\n":
                    index += 1

            if token == "\n":
                line_number += 1

            index += 1

        if tokens[-1] != ";":
            print("Missing semicolon at the end of the code.")

    def handle_keyword(self, keyword):
        """
        Handles a valid keyword.

        Args:
            keyword (str): The valid keyword.

        Returns:
            None
        """
        print(f"Valid keyword: {keyword}")

    def handle_operator(self, operator):
        """
        Handles a valid operator.

        Args:
            operator (str): The valid operator.

        Returns:
            None
        """
        print(f"Valid operator: {operator}")

    def handle_punctuation(self, punctuation):
        """
        Handles a valid punctuation.

        Args:
            punctuation (str): The valid punctuation.

        Returns:
            None
        """
        print(f"Valid punctuation: {punctuation}")

    def handle_number(self, number):
        """
        Handles a valid number.

        Args:
            number (str): The valid number.

        Returns:
            None
        """
        print(f"Valid number: {number}")

    def handle_string(self, string):
        """
        Handles a valid string.

        Args:
            string (str): The valid string.

        Returns:
            None
        """
        print(f"Valid string: {string}")

    def handle_invalid_token(self, token, line_number):
        """
        Handles an invalid token.

        Args:
            token (str): The invalid token.
            line_number (int): The line number where the invalid token is found.

        Returns:
            None
        """
        print(f"Invalid token '{token}' at line {line_number}.")


# Example usage
validator = SyntaxValidator()

# Paste your code below to validate its syntax
code = """
is_magician = True
is_expert = True

if (is_magician and is_expert):
    print('You are a Magician !!')
elif (is_magician and not (is_expert)):
    print('At least you are getting there...')
elif (not (is_magician)):
    print('You need magic powers...')
else:
    print('Find yourself..')
"""

validator.validate_syntax(code)
