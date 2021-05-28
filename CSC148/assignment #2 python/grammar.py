import random
import sys


class InvalidSymbolError(LookupError):
    pass


class GrammarSolver(object):
    """A grammar solver, capable of generating sentences when provided with
    sufficent grammatical rules and an existing symbol inside the inserted
    rules."""
    def __init__(self, grammar):
        """(GrammarSolver, list(int)) -> NoneType

        Initialize a GrammarSolver object with creating a list of non-terminals
        from grammar and also a dictionary of grammatical rules also from
        grammar.

        """
        self._non_terminal_list = []
        self._grammar_dict = {}
        for grammar_line in grammar:
            if "::=" in grammar_line:
                grammar_line = grammar_line.rstrip("\n")
                grammar_line_separated = grammar_line.split('::=')
                non_terminal = grammar_line_separated[0]
                self._non_terminal_list.append(non_terminal)
                rules_str = grammar_line_separated[1]
                rules_str_list = rules_str.split("|")
                rules_of_non_terminal = []
                for rule_with_space in rules_str_list:
                    rule_list = rule_with_space.split()
                    rules_of_non_terminal.append(rule_list)
                self._grammar_dict[non_terminal] = rules_of_non_terminal

    def __contains__(self, symbol):
        """(GrammarSolver, str) -> bool

        Return True if symbol is inside GrammarSolver. False otherwise.

        """
        return symbol in self._non_terminal_list

    def generate(self, symbol, n):
        """(GrammarSolver, str, int) -> list(str)

        Return a list of n string(s) following the grammatical rules outlined
        by symbol. Raise InvalidSymbolError if symbol is not present in
        GrammarSolver or Raise ValueError if n is lesser than 0.

        """
        if symbol not in self._non_terminal_list:
            raise InvalidSymbolError('Error: Symbol %s not in grammar'
                                     % (symbol))
        elif n < 0:
            raise ValueError('Number of times must be >= 0')
        else:
            list_of_generated_sentences = []
            for index in range(n):
                sentence = self._recursive(self._grammar_dict[symbol], "")
                list_of_generated_sentences.append(sentence)
            return list_of_generated_sentences

    def _recursive(self, rules_list_of_non_terminal,
                                     sentence_piece):
        """(GrammarSolver, list(list(str)), str) -> str

        Return a string following the grammatical rules outlined in
        rules_list_of_non_terminal.

        """
        random_index = random.randint(0, len(rules_list_of_non_terminal) - 1)
        rule_list = rules_list_of_non_terminal[random_index]
        for rule in rule_list:
            if rule in self._grammar_dict:
                sentence_piece = self._recursive(self._grammar_dict[rule],
                                                 sentence_piece)
            else:
                sentence_piece = " ".join([sentence_piece, rule])
        return sentence_piece.strip()

    def __str__(self):
        """GrammarSolver -> str

        Return a string representation of GrammarSolver. The string
        representation creates a sorted list of all avaliable non-terminals.

        """
        self._non_terminal_list.sort()
        return str(self._non_terminal_list)


if __name__ == "__main__":
    # Comment out the line below to get random output
    # random.seed(0)
    grammar = []  # Dummy value to enter loop
    while not grammar:
        filename = raw_input("Grammar file to load: ").strip()
        try:
            # Read file into string
            with open(filename) as ifp:
                grammar = ifp.readlines()
        except IOError:
            print >>sys.stderr, "Could not load file: %r" % filename

    # You should complete the rest of these lines based upon the
    # following pseudocode (for comparison, my solution is 9 lines):
    # ==========================================================
    #
    # Create a new GrammarSolver from the grammar list.
    solver = GrammarSolver(grammar)
    #
    # while True:
    while True:
    # - Print the list of available symbols to the user.
    #   hint: print "\nAvailable symbols to generate are:"
    #         print the string representation of your GrammarSolver object
        print "\nAvailable symbols to generate are:\n%s" % solver
    #
    # - Prompt the user for the desired symbol (if empty, break).
    #   hint: raw_input("Symbol to generate (ENTER to exit): ").strip()
        symbol = raw_input("Symbol to generate (ENTER to exit): ").strip()
        if not symbol:
            break
    #
    # - If the symbol is not a non-terminal in the grammar,
    #   Print the appropriate error to the user and "continue" the loop
        if symbol not in solver:
            print >>sys.stderr, "Error: symbol %r not in grammar" % symbol
            continue
    #
    # - Prompt the user for n, the number of times to generate the
    #   desired symbol from the grammar.
    #   You may assume that the user enters an integer.
    #   hint: raw_input("Number to generate: ")
        n_times = int(raw_input("Number to generate: "))
    #
    # - Try to generate n elements from the GrammarSolver object.
    #   hint: solver.generate
        try:
            sentences = solver.generate(symbol, n_times)
    #
    # - Catch any appropriate exception, printing errors.
    #   You can catch multiple kinds of exceptions by putting parentheses
    #   around them (e.g. "except (IndexError, KeyError) as e").
    #   hint: print >>sys.stderr, "Error: %s" % e
        except (InvalidSymbolError, ValueError) as e:
            print >>sys.stderr, "Error: %s" % e
        else:
    #
    # - If no errors: print the generated strings, numbered 1 through n.
    #   hint: enumerate
            for i, sentence in enumerate(sentences):
                print "%d: %s" % (i + 1, sentence)
