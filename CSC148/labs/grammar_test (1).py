import unittest
from grammar import GrammarSolver

class SimplestCase(unittest.TestCase):
    def setUp(self):
        grammar = ["<a>::=1|2"]
        self.gs = GrammarSolver(grammar)

    def test_str(self):
        self.assertEqual(str(self.gs).replace("'", ""), "[<a>]")

    def test_contains(self):
        self.assertTrue("<a>" in self.gs)
        self.assertFalse("<b>" in self.gs)
        self.assertFalse("1" in self.gs)

    def test_value_error_lenient(self):
        try:
            from grammar import ValueError
        except:
            from exceptions import ValueError

        self.assertRaises(ValueError, self.gs.generate, '<a>', -1)

    def test_bultin_value_error(self):
        try:
            from grammar import ValueError as v
        except:
            from exceptions import ValueError as v

        try:
            self.gs.generate('<a>', -1)
            self.assertTrue(False, "generate() did not fail appropriately")
        except StandardError as e:
            pass
        except v:
            self.assertTrue(False, "Raised custom exception rather than"
                            " built-in ValueError")

    def test_value_error_message(self):
        try:
            from grammar import ValueError
        except:
            from exceptions import ValueError

        try:
            self.gs.generate('<a>', -1)
            self.assertTrue(False, "generate('<a>', -1) did not fail"
                            " appropriately")
        except ValueError as e:
            self.assertEqual(e.message.lower(), "Number of times must be >= 0".lower())

    def test_symbol_case_sensitivity(self):
        from grammar import InvalidSymbolError
        self.assertRaises(InvalidSymbolError, self.gs.generate, '<A>', 1)

    def test_symbol_error(self):
        from grammar import InvalidSymbolError
        self.assertRaises(InvalidSymbolError, self.gs.generate, '<b>', 1)

    def test_symbol_error_inheritance(self):
        from grammar import InvalidSymbolError
        try:
            self.gs.generate('<b>', 1)
            self.assertTrue(False, "generate() with invalid symbol did not"
                            " fail appropriately")
        except LookupError:
            pass
        except InvalidSymbolError:
            self.assertTrue(False, "InvalidSymbolError did not inherit from"
                            " LookupError")

    def test_both_errors(self):
        from grammar import InvalidSymbolError
        try:
            self.gs.generate('<b>', -1)
            self.assertTrue(False, "generate('<b>', -1) did not fail"
                            " appropriately")
        except (InvalidSymbolError, ValueError):
            pass
            
    def test_generate_0(self):
        self.assertEqual(self.gs.generate('<a>', 0), [])

    def test_generate_several(self):
        n = 10
        lines = self.gs.generate('<a>', n)
        self.assertEqual(len(lines), n)

    def test_generate_many(self):
        n = 1000
        lines = self.gs.generate('<a>', n)
        self.assertEqual(len(lines), n)

    def test_generate_random(self):
        counts = {1: 0, 2: 0}
        n = 1000
        for i in xrange(n):
            lines = self.gs.generate('<a>', 1)
            self.assertEqual(len(lines), 1)
            counts[int(lines[0])] += 1

        min_ = 0.6 * n / len(counts)
        max_ = 1.3 * n / len(counts)
        for count in counts.values():
            self.assertTrue(min_ < count < max_, 
                            "Found unreasonable balance of outputted"
                            " terminals: %s" % counts.values())

class OneRuleCase(unittest.TestCase):
    def setUp(self):
        grammar = ["<a>::=1"]
        self.gs = GrammarSolver(grammar)

    def test_generate_one(self):
        lines = self.gs.generate('<a>', 1)
        self.assertEqual(len(lines), 1)
        self.assertEqual(lines[0].strip(), "1")

    def test_generate_ten(self):
        for i in xrange(10):
            lines = self.gs.generate('<a>', 1)
            self.assertEqual(len(lines), 1)
            self.assertEqual(lines[0].strip(), "1")

class BracketlessNonterminalCase(unittest.TestCase):
    def setUp(self):
        grammar = ["a::=1|2"]
        self.gs = GrammarSolver(grammar)

    def test_str(self):
        self.assertEqual(str(self.gs).replace("'", ""), "[a]")
            
    def test_generate_one(self):
        self.assertIn(self.gs.generate('a', 1)[0].strip(), "12")

class StrangeSymbolCase(unittest.TestCase):
    def setUp(self):
        grammar = ["=::=-"]
        self.gs = GrammarSolver(grammar)

    def test_contains(self):
        self.assertTrue("=" in self.gs)
        self.assertFalse("-" in self.gs)

    def test_str(self):
        self.assertEqual(str(self.gs).replace("'", ""), "[=]")
            
    def test_generate_one(self):
        self.assertEqual(self.gs.generate('=', 1), ["-"])

class WhitespaceCase(unittest.TestCase):
    def setUp(self):
        grammar = ["<a>::=4|             3	|		1  	2 "]
        self.gs = GrammarSolver(grammar)

    def test_str(self):
        self.assertEqual(str(self.gs).replace("'", ""), "[<a>]")
            
    def test_generate_lenient(self):
        possible = set(["1 2", "3", "4"])
        for i in xrange(50):
            lines = self.gs.generate('<a>', 1)
            self.assertEqual(len(lines), 1)
            self.assertIn(lines[0].strip(), possible)

    def test_generate_strict(self):
        possible = set(["1 2", "3", "4"])
        for i in xrange(50):
            lines = self.gs.generate('<a>', 1)
            self.assertEqual(len(lines), 1)
            self.assertIn(lines[0], possible)


class NestedCase(unittest.TestCase):
    def setUp(self):
        grammar = ["<c>::=<a>|<b>", "<a>::=1|2", "<b>::=3|4"]
        self.gs = GrammarSolver(grammar)

    def test_contains(self):
        self.assertTrue("<a>" in self.gs)
        self.assertTrue("<b>" in self.gs)
        self.assertTrue("<c>" in self.gs)
        self.assertFalse("1" in self.gs)

    def test_str(self):
        self.assertEqual(str(self.gs).replace("'", ""), "[<a>, <b>, <c>]")
            
    def test_generate_0(self):
        self.assertEqual(self.gs.generate('<c>', 0), [])

    def test_generate_random(self):
        counts = {1: 0, 2: 0, 3: 0, 4: 0}
        n = 1000
        lines = self.gs.generate('<c>', n)
        self.assertEqual(len(lines), n)
        for line in lines:
            counts[int(line)] += 1

        min_ = 0.6 * n / len(counts)
        max_ = 1.3 * n / len(counts)
        for count in counts.values():
            self.assertTrue(min_ < count < max_, 
                            "Found unreasonable balance of outputted"
                            " terminals: %s" % counts.values())

class MultipleTokenCase(unittest.TestCase):
    def setUp(self):
        grammar = ["<c>::=( <a> : <b> , <a> : <b> )", "<a>::=1|2", "<b>::=3|4"]
        self.gs = GrammarSolver(grammar)

    def test_contains(self):
        self.assertTrue("<a>" in self.gs)
        self.assertTrue("<b>" in self.gs)
        self.assertTrue("<c>" in self.gs)
        self.assertFalse("(" in self.gs)
        self.assertFalse(")" in self.gs)
        self.assertFalse("," in self.gs)

    def test_str(self):
        self.assertEqual(str(self.gs).replace("'", ""), "[<a>, <b>, <c>]")
            
    def test_generate_random(self):
        possible = []
        for a1 in "12":
            for b1 in "34":
                for a2 in "12":
                    for b2 in "34":
                        possible.append("( %s : %s , %s : %s )" % 
                                        (a1, b1, a2, b2))

        counts = dict([(val, 0) for val in possible])
        n = 5000
        lines = self.gs.generate('<c>', n)
        self.assertEqual(len(lines), n)
        for line in lines:
            counts[line.strip()] += 1

        min_ = 0.5 * n / len(counts)
        max_ = 1.5 * n / len(counts)
        for count in counts.values():
            self.assertTrue(min_ < count < max_, 
                            "Found unreasonable balance of outputted"
                            " terminals: %s" % counts.values())

class RecursiveCase(unittest.TestCase):
    def setUp(self):
        grammar = ["<b>::=<b>|2", "<a>::=<a>|1", "<c>::=<a> <b>"]
        self.gs = GrammarSolver(grammar)

    def test_str(self):
        self.assertEqual(str(self.gs).replace("'", ""), "[<a>, <b>, <c>]")
            
    def test_generate_random(self):
        lines = self.gs.generate("<c>", 10)
        for line in lines:
            tokens = line.split()
            self.assertEqual(set(tokens), set("12"))


if __name__ == '__main__':
    unittest.main()
