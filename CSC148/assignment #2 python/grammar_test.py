import unittest
from grammar import GrammarSolver, InvalidSymbolError


def error_message(expected, produced):
    """ (anything, anything) -> str
    Return a message stating what was expected in a unitTest and
    what was produced in the actual code in the same test. Only
    runs if expected is not the same as produced.
    """
    return "Expected:\n%s\ngot:\n%s\ninstead." % (str(expected), str(produced))


class EmptyGrammarCase(unittest.TestCase):
    """Tests the behaviour of an empty Grammar input."""
    def setUp(self):
        """Sets up a GrammarSolver object with an empty Grammar."""
        grammar = []
        self.solver = GrammarSolver(grammar)

    def tearDown(self):
        """Clean up."""
        self.solver = None

    def testPrivateMethodContains(self):
        """Test __contains__ method on the GrammarSolver object."""
        self.assertFalse('' in self.solver,
                         error_message(False, 'a' in self.solver))

    def testPublicMethodGenerate(self):
        """Test generate method on the GrammarSolver object."""
        self.assertRaises(InvalidSymbolError, self.solver.generate, 'Not', 10)

    def testPrivateMethodStr(self):
        """Test __str__ method on the GrammarSolver object."""
        result_str = str([])
        self.assertEqual(result_str, str(self.solver),
                         error_message(result_str, str(self.solver)))


class EmptyStringGrammarCase(unittest.TestCase):
    """Tests the behaviour of Grammar input with blank lines and an empty
    string non-terminal."""
    def setUp(self):
        """Sets up a GrammarSolver object with Grammar that contains blank
        lines and an empty string non-terminal."""
        grammar = ['\n', '\n', "::=A\n", '\n', '\n']
        self.solver = GrammarSolver(grammar)

    def tearDown(self):
        """Clean up."""
        self.solver = None

    def testPrivateMethodContains(self):
        """Test __contains__ method on the GrammarSolver object."""
        self.assertTrue('' in self.solver,
                         error_message(True, '' in self.solver))
        self.assertFalse('\n' in self.solver,
                         error_message(False, '\n' in self.solver))

    def testPublicMethodGenerate(self):
        """Test generate method on the GrammarSolver object."""
        self.assertRaises(InvalidSymbolError, self.solver.generate, 'Not', 10)
        self.assertRaises(ValueError, self.solver.generate, '', -1)
        self.assertEqual(['A'], self.solver.generate('', 1),
                         error_message(['A'], self.solver.generate('', 1)))

    def testPrivateMethodStr(self):
        """Test __str__ method on the GrammarSolver object."""
        result_str = str([''])
        self.assertEqual(result_str, str(self.solver),
                         error_message(result_str, str(self.solver)))


class SingleBlankTerminalGrammarCase(unittest.TestCase):
    """Tests the behaviour of Grammar input with blank terminals."""
    def setUp(self):
        """Sets up a GrammarSolver object with Grammar that contains a blank
        terminal for each non-terminal."""
        grammar = ['C::=\n', 'B::=\n', 'A::=\n', '3::=\n', '2::=\n', '1::=\n']
        self.solver = GrammarSolver(grammar)

    def tearDown(self):
        """Clean up."""
        self.solver = None

    def testPrivateMethodContains(self):
        """Test __contains__ method on the GrammarSolver object."""
        self.assertTrue('A' in self.solver, error_message(True,
                                                          'A' in self.solver))
        self.assertTrue('B' in self.solver, error_message(True,
                                                          'B' in self.solver))
        self.assertTrue('C' in self.solver, error_message(True,
                                                          'D' in self.solver))
        self.assertTrue('1' in self.solver, error_message(True,
                                                          '1' in self.solver))
        self.assertTrue('2' in self.solver, error_message(True,
                                                          '2' in self.solver))
        self.assertTrue('3' in self.solver, error_message(True,
                                                          '3' in self.solver))
        self.assertFalse('a' in self.solver, error_message(False,
                                                          'a' in self.solver))
        self.assertFalse('b' in self.solver, error_message(False,
                                                          'b' in self.solver))
        self.assertFalse('c' in self.solver, error_message(False,
                                                          'c' in self.solver))

    def testPublicMethodGenerate(self):
        """Test generate method on the GrammarSolver object."""
        self.assertRaises(InvalidSymbolError, self.solver.generate, 'Not', 10)
        self.assertRaises(ValueError, self.solver.generate, 'A', -1)
        self.assertEqual([''], self.solver.generate('A', 1),
                         error_message([''], self.solver.generate('A', 1)))
        self.assertEqual([''], self.solver.generate('B', 1),
                         error_message([''], self.solver.generate('B', 1)))
        self.assertEqual([''], self.solver.generate('C', 1),
                         error_message([''], self.solver.generate('C', 1)))
        self.assertEqual([''], self.solver.generate('1', 1),
                         error_message([''], self.solver.generate('1', 1)))
        self.assertEqual([''], self.solver.generate('2', 1),
                         error_message([''], self.solver.generate('2', 1)))
        self.assertEqual([''], self.solver.generate('3', 1),
                         error_message([''], self.solver.generate('3', 1)))

    def testPrivateMethodStr(self):
        """Test __str__ method on the GrammarSolver object."""
        result_str = str(['1', '2', '3', 'A', 'B', 'C'])
        self.assertEqual(result_str, str(self.solver),
                         error_message(result_str, str(self.solver)))


class ManyBlankTerminalsGrammarCase(unittest.TestCase):
    """Tests the behaviour of Grammar input with many blank terminals for each
    non-terminal."""
    def setUp(self):
        """Sets up a GrammarSolver object with Grammar that contains many blank
        terminals for each non-terminal."""
        grammar = ['E::=||\n', 'D::= | | \n', 'C::=\t|\t|\t\n',
                   'B::=\t| |\t\n', 'A::= |\t| \n']
        self.solver = GrammarSolver(grammar)

    def tearDown(self):
        """Clean up."""
        self.solver = None

    def testPrivateMethodContains(self):
        """Test __contains__ method on the GrammarSolver object."""
        self.assertTrue('A' in self.solver, error_message(True,
                                                          'A' in self.solver))
        self.assertTrue('B' in self.solver, error_message(True,
                                                          'B' in self.solver))
        self.assertTrue('C' in self.solver, error_message(True,
                                                          'C' in self.solver))
        self.assertTrue('D' in self.solver, error_message(True,
                                                          'D' in self.solver))
        self.assertTrue('E' in self.solver, error_message(True,
                                                          'E' in self.solver))

    def testPublicMethodGenerate(self):
        """Test generate method on the GrammarSolver object."""
        self.assertRaises(InvalidSymbolError, self.solver.generate, 'Not', 10)
        self.assertRaises(ValueError, self.solver.generate, 'A', -1)
        self.assertEqual([''], self.solver.generate('A', 1),
                         error_message([''], self.solver.generate('A', 1)))
        self.assertEqual([''], self.solver.generate('B', 1),
                         error_message([''], self.solver.generate('B', 1)))
        self.assertEqual([''], self.solver.generate('C', 1),
                         error_message([''], self.solver.generate('C', 1)))
        self.assertEqual([''], self.solver.generate('D', 1),
                         error_message([''], self.solver.generate('D', 1)))
        self.assertEqual([''], self.solver.generate('E', 1),
                         error_message([''], self.solver.generate('E', 1)))

    def testPrivateMethodStr(self):
        """Test __str__ method on the GrammarSolver object."""
        result_str = str(['A', 'B', 'C', 'D', 'E'])
        self.assertEqual(result_str, str(self.solver),
                         error_message(result_str, str(self.solver)))


class SpaceAndTabSingleTerminalGrammarCase(unittest.TestCase):
    """Tests the behaviour of Grammar input with non-terminals having only one
    terminal surrounded by many variation of blankspace."""
    def setUp(self):
        """Sets up a GrammarSolver object with Grammar that contains
        non-terminals having only one terminal surrounded by many variation of
        blankspace."""
        grammar = ['space_terminal::=     ~1~     \n',
                   'tab_terminal::=\t\t\t\t\t~2~\t\t\t\t\t\n',
                   'space_then_tab_terminal::=     ~3~\t\t\t\t\t\n',
                   'tab_then_space_terminal::=\t\t\t\t\t~4~     \n',
                   'alternate_tab_space::=\t \t \t~5~ \t \t \n',
                   'alternate_space_tab::= \t \t ~6~\t \t \t\n']
        self.solver = GrammarSolver(grammar)

    def tearDown(self):
        """Clean up."""
        self.solver = None

    def testPrivateMethodContains(self):
        """Test __contains__ method on the GrammarSolver object."""
        self.assertTrue('space_terminal' in self.solver,
                        error_message(True, 'space_terminal' in self.solver))
        self.assertTrue('tab_terminal' in self.solver,
                        error_message(True, 'tab_terminal' in self.solver))
        self.assertTrue('space_then_tab_terminal' in self.solver,
                        error_message(True, 'space_then_tab_terminal'
                                      in self.solver))
        self.assertTrue('tab_then_space_terminal' in self.solver,
                        error_message(True, 'space_then_tab_terminal'
                                      in self.solver))
        self.assertTrue('alternate_tab_space' in self.solver,
                        error_message(True, 'alternate_tab_space'
                                      in self.solver))
        self.assertTrue('alternate_space_tab' in self.solver,
                        error_message(True, 'alternate_space_tab'
                                      in self.solver))

    def testPublicMethodGenerate(self):
        """Test generate method on the GrammarSolver object."""
        self.assertRaises(InvalidSymbolError, self.solver.generate, 'Not', 10)
        self.assertRaises(ValueError, self.solver.generate, 'space_terminal',
                          -1)
        self.assertEqual(
            ['~1~'],
            self.solver.generate('space_terminal', 1),
            error_message(['~1~'], self.solver.generate('space_terminal', 1)))
        self.assertEqual(
            ['~2~'],
            self.solver.generate('tab_terminal', 1),
            error_message(['~2~'], self.solver.generate('tab_terminal', 1)))
        self.assertEqual(
            ['~3~'],
            self.solver.generate('space_then_tab_terminal', 1),
            error_message(['~3~'],
                          self.solver.generate('space_then_tab_terminal', 1)))
        self.assertEqual(
            ['~4~'],
            self.solver.generate('tab_then_space_terminal', 1),
            error_message(['~4~'],
                          self.solver.generate('tab_then_space_terminal', 1)))
        self.assertEqual(
            ['~5~'],
            self.solver.generate('alternate_tab_space', 1),
            error_message(['~5~'],
                          self.solver.generate('alternate_tab_space', 1)))
        self.assertEqual(
            ['~6~'],
            self.solver.generate('alternate_space_tab', 1),
            error_message(['~6~'],
                          self.solver.generate('alternate_space_tab', 1)))

    def testPrivateMethodStr(self):
        """Test __str__ method on the GrammarSolver object."""
        result_str = str(['alternate_space_tab', 'alternate_tab_space',
                          'space_terminal', 'space_then_tab_terminal',
                          'tab_terminal', 'tab_then_space_terminal'])
        self.assertEqual(result_str, str(self.solver),
                         error_message(result_str, str(self.solver)))


class SpaceAndTabMultiTerminalGrammarCase(unittest.TestCase):
    """Tests the behaviour of Grammar input with non-terminals having only many
    terminal surrounded by many variation of blankspace."""
    def setUp(self):
        """Sets up a GrammarSolver object with Grammar that contains
        non-terminals having only many terminal surrounded by many variation of
        blankspace."""
        grammar = [
            'space_terminal::=     ~1~     |     ~a~     |     ~A~     \n',
            'tab_terminal::=\t\t~2~\t\t|\t\t~b~\t\t|\t\t~B~\t\t\n',
            'space_then_tab_terminal::=    ~3~\t\t|    ~c~\t\t|    ~C~\t\t\n',
            'tab_then_space_terminal::=\t\t~4~   |\t\t~d~   |\t\t~D~   \n',
            'alternate_tab_space::=\t \t~5~ \t |\t \t~e~ \t |\t \t~E~ \t \n',
            'alternate_space_tab::= \t ~6~\t \t| \t ~f~\t \t| \t ~F~\t \t\n']
        self.solver = GrammarSolver(grammar)

    def tearDown(self):
        """Clean up."""
        self.solver = None

    def testPrivateMethodContains(self):
        """Test __contains__ method on the GrammarSolver object."""
        self.assertTrue('space_terminal' in self.solver,
                        error_message(True, 'space_terminal' in self.solver))
        self.assertTrue('tab_terminal' in self.solver,
                        error_message(True, 'tab_terminal' in self.solver))
        self.assertTrue('space_then_tab_terminal' in self.solver,
                        error_message(True, 'space_then_tab_terminal'
                                      in self.solver))
        self.assertTrue('tab_then_space_terminal' in self.solver,
                        error_message(True, 'space_then_tab_terminal'
                                      in self.solver))
        self.assertTrue('alternate_tab_space' in self.solver,
                        error_message(True, 'alternate_tab_space'
                                      in self.solver))
        self.assertTrue('alternate_space_tab' in self.solver,
                        error_message(True, 'alternate_space_tab'
                                      in self.solver))

    def testPublicMethodGenerate(self):
        """Test generate method on the GrammarSolver object."""
        self.assertRaises(InvalidSymbolError, self.solver.generate, 'Not', 10)
        self.assertRaises(ValueError, self.solver.generate, 'space_terminal',
                          -1)
        random_list = self.solver.generate('space_terminal', 1)
        self.assertTrue(random_list in [['~1~'], ['~a~'], ['~A~']],
                        error_message("['~1~'] OR ['~a~'] OR ['~A~']",
                                      random_list))
        random_list = self.solver.generate('tab_terminal', 1)
        self.assertTrue(random_list in [['~2~'], ['~b~'], ['~B~']],
                        error_message("['~2~'] OR ['~b~'] OR ['~B~']",
                                      random_list))
        random_list = self.solver.generate('space_then_tab_terminal', 1)
        self.assertTrue(random_list in [['~3~'], ['~c~'], ['~C~']],
                        error_message("['~3~'] OR ['~c~'] OR ['~C~']",
                                      random_list))
        random_list = self.solver.generate('tab_then_space_terminal', 1)
        self.assertTrue(random_list in [['~4~'], ['~d~'], ['~D~']],
                        error_message("['~4~'] OR ['~d~'] OR ['~D~']",
                                      random_list))
        random_list = self.solver.generate('alternate_tab_space', 1)
        self.assertTrue(random_list in [['~5~'], ['~e~'], ['~E~']],
                        error_message("['~5~'] OR ['~e~'] OR ['~E~']",
                                      random_list))
        random_list = self.solver.generate('alternate_space_tab', 1)
        self.assertTrue(random_list in [['~6~'], ['~f~'], ['~F~']],
                        error_message("['~6~'] OR ['~f~'] OR ['~F~']",
                                      random_list))

    def testPrivateMethodStr(self):
        result_str = str(['alternate_space_tab', 'alternate_tab_space',
                          'space_terminal', 'space_then_tab_terminal',
                          'tab_terminal', 'tab_then_space_terminal'])
        self.assertEqual(result_str, str(self.solver),
                         error_message(result_str, str(self.solver)))


class SinglePathGrammarGenerationCase(unittest.TestCase):
    """Tests the behaviour of Grammar input that the private method
    generate will traverse along a single path of non-terminals and terminals.
    """
    def setUp(self):
        """Sets up a GrammarSolver object with Grammar in which the private
        method generate will traverse along a single path of non-terminals and
        terminals."""
        grammar = ['<Start>::=<Node1>\n', '<Node1>::=<Node2>\n',
                   '<Node2>::=<Node3>\n', '<Node3>::=<End>\n']
        self.solver = GrammarSolver(grammar)

    def tearDown(self):
        """Clean up."""
        self.solver = None

    def testPrivateMethodContains(self):
        """Test __contains__ method on the GrammarSolver object."""
        self.assertTrue('<Start>' in self.solver,
                        error_message(True, '<Start>' in self.solver))
        self.assertTrue('<Node1>' in self.solver,
                        error_message(True, '<Node1>' in self.solver))
        self.assertTrue('<Node2>' in self.solver,
                        error_message(True, '<Node2>' in self.solver))
        self.assertTrue('<Node3>' in self.solver,
                        error_message(True, '<Node3>' in self.solver))
        self.assertFalse('<End>' in self.solver,
                        error_message(False, '<End>' not in self.solver))

    def testPublicMethodGenerate(self):
        """Test generate method on the GrammarSolver object."""
        self.assertRaises(InvalidSymbolError, self.solver.generate, 'Not', 10)
        self.assertRaises(ValueError, self.solver.generate, '<Start>', -1)
        self.assertEqual(['<End>'], self.solver.generate('<Start>', 1),
                         error_message(['<End>'],
                                       self.solver.generate('<Start>', 1)))
        self.assertEqual(['<End>'], self.solver.generate('<Node1>', 1),
                         error_message(['<End>'],
                                       self.solver.generate('<Node1>', 1)))
        self.assertEqual(['<End>'], self.solver.generate('<Node2>', 1),
                         error_message(['<End>'],
                                       self.solver.generate('<Node2>', 1)))
        self.assertEqual(['<End>'], self.solver.generate('<Node3>', 1),
                         error_message(['<End>'],
                                       self.solver.generate('<Node3>', 1)))

    def testPrivateMethodStr(self):
        """Test __str__ method on the GrammarSolver object."""
        result_str = str(['<Node1>', '<Node2>', '<Node3>', '<Start>'])
        self.assertEqual(result_str, str(self.solver),
                         error_message(result_str, str(self.solver)))


class MultiPathGrammarGenerationCase(unittest.TestCase):
    """Tests the behaviour of Grammar input that the private method
    generate will traverse along all paths of non-terminals and terminals."""
    def setUp(self):
        """Sets up a GrammarSolver object with Grammar in which the private
        method generate will traverse along all paths of non-terminals and
        terminals."""
        grammar = ['<Start>::=<Path1> <Path2> <Path3>\n',
         '<Path1>::=<Path1Node1> <Path1Node2> <Path1Node3>\n',
         '<Path2>::=<Path2Node1> <Path2Node2> <Path2Node3>\n',
         '<Path3>::=<Path3Node1> <Path3Node2> <Path3Node3>\n',
         '<Path1Node1>::= C\n', '<Path1Node2>::= S\n', '<Path1Node3>::= C\n',
         '<Path2Node1>::= 1\n', '<Path2Node2>::= 4\n', '<Path2Node3>::= 8\n',
         '<Path3Node1>::= H \n', '<Path3Node2>::= 1\n', '<Path3Node3>::= Y\n']
        self.solver = GrammarSolver(grammar)

    def tearDown(self):
        """Clean up."""
        self.solver = None

    def testPrivateMethodContains(self):
        """Test __contains__ method on the GrammarSolver object."""
        self.assertTrue('<Start>' in self.solver,
                        error_message(True, '<Start>' in self.solver))
        self.assertTrue('<Path1>' in self.solver,
                        error_message(True, '<Path1>' in self.solver))
        self.assertTrue('<Path2>' in self.solver,
                        error_message(True, '<Path2>' in self.solver))
        self.assertTrue('<Path3>' in self.solver,
                        error_message(True, '<Path3>' in self.solver))
        self.assertTrue('<Path1Node1>' in self.solver,
                        error_message(True, '<Path1Node1>' in self.solver))
        self.assertTrue('<Path2Node1>' in self.solver,
                        error_message(True, '<Path2Node1>' in self.solver))
        self.assertTrue('<Path3Node1>' in self.solver,
                        error_message(True, '<Path3Node1>' in self.solver))
        self.assertTrue('<Path1Node2>' in self.solver,
                        error_message(True, '<Path1Node2>' in self.solver))
        self.assertTrue('<Path2Node2>' in self.solver,
                        error_message(True, '<Path2Node2>' in self.solver))
        self.assertTrue('<Path3Node2>' in self.solver,
                        error_message(True, '<Path3Node2>' in self.solver))
        self.assertTrue('<Path1Node3>' in self.solver,
                        error_message(True, '<Path1Node3>' in self.solver))
        self.assertTrue('<Path2Node3>' in self.solver,
                        error_message(True, '<Path2Node3>' in self.solver))
        self.assertTrue('<Path3Node3>' in self.solver,
                        error_message(True, '<Path3Node3>' in self.solver))

    def testPublicMethodGenerate(self):
        """Test generate method on the GrammarSolver object."""
        self.assertRaises(InvalidSymbolError, self.solver.generate, 'Not', 10)
        self.assertRaises(ValueError, self.solver.generate, '<Start>', -1)
        self.assertEqual(['C S C 1 4 8 H 1 Y'],
                         self.solver.generate('<Start>', 1),
                         error_message(['C S C 1 4 8 H 1 Y'],
                                       self.solver.generate('<Start>', 1)))
        self.assertEqual(['C S C'], self.solver.generate('<Path1>', 1),
                         error_message(['C S C'],
                                       self.solver.generate('<Path1>', 1)))
        self.assertEqual(['1 4 8'], self.solver.generate('<Path2>', 1),
                         error_message(['1 4 8'],
                                       self.solver.generate('<Path2>', 1)))
        self.assertEqual(['H 1 Y'], self.solver.generate('<Path3>', 1),
                         error_message(['H 1 Y'],
                                       self.solver.generate('<Path3>', 1)))

    def testPrivateMethodStr(self):
        """Test __str__ method on the GrammarSolver object."""
        result_str = str(['<Path1>', '<Path1Node1>', '<Path1Node2>',
                          '<Path1Node3>', '<Path2>', '<Path2Node1>',
                          '<Path2Node2>', '<Path2Node3>', '<Path3>',
                          '<Path3Node1>', '<Path3Node2>', '<Path3Node3>',
                          '<Start>'])
        self.assertEqual(result_str, str(self.solver),
                         error_message(result_str, str(self.solver)))


class ManyPathRandomSingleResultGrammarGenerationCase(unittest.TestCase):
    """Tests the behaviour of Grammar input that the private method
    generate will randomly traverse one of many paths of non-terminals and
    terminals."""
    def setUp(self):
        """Sets up a GrammarSolver object with Grammar in which the private
        method generate will randomly traverse one of many paths of
        non-terminals and terminals."""
        grammar = ['<Start>::= <Path1>\t|\t<Path2> |<Path3>\n',
        '<Path1>::= <Path1Node1>|<Path1Node2>|<Path1Node3> \n',
        '<Path2>::= <Path2Node1>|<Path2Node2>|<Path2Node3> \n',
        '<Path3>::= <Path3Node1>|<Path3Node2>|<Path3Node3> \n',
        '<Path1Node1>::= 1 \n', '<Path1Node2>::= 2 \n',
        '<Path1Node3>::= 3 \n', '<Path2Node1>::= 4 \n',
        '<Path2Node2>::= 5 \n', '<Path2Node3>::= 6 \n',
        '<Path3Node1>::= 7 \n', '<Path3Node2>::= 8 \n', '<Path3Node3>::= 9 \n']
        self.solver = GrammarSolver(grammar)

    def tearDown(self):
        """Clean up."""
        self.solver = None

    def testPrivateMethodContains(self):
        """Test __contains__ method on the GrammarSolver object."""
        self.assertTrue('<Start>' in self.solver,
                        error_message(True, '<Start>' in self.solver))
        self.assertTrue('<Path1>' in self.solver,
                        error_message(True, '<Path1>' in self.solver))
        self.assertTrue('<Path2>' in self.solver,
                        error_message(True, '<Path2>' in self.solver))
        self.assertTrue('<Path3>' in self.solver,
                        error_message(True, '<Path3>' in self.solver))
        self.assertTrue('<Path1Node1>' in self.solver,
                        error_message(True, '<Path1Node1>' in self.solver))
        self.assertTrue('<Path2Node1>' in self.solver,
                        error_message(True, '<Path2Node1>' in self.solver))
        self.assertTrue('<Path3Node1>' in self.solver,
                        error_message(True, '<Path3Node1>' in self.solver))
        self.assertTrue('<Path1Node2>' in self.solver,
                        error_message(True, '<Path1Node2>' in self.solver))
        self.assertTrue('<Path2Node2>' in self.solver,
                        error_message(True, '<Path2Node2>' in self.solver))
        self.assertTrue('<Path3Node2>' in self.solver,
                        error_message(True, '<Path3Node2>' in self.solver))
        self.assertTrue('<Path1Node3>' in self.solver,
                        error_message(True, '<Path1Node3>' in self.solver))
        self.assertTrue('<Path2Node3>' in self.solver,
                        error_message(True, '<Path2Node3>' in self.solver))
        self.assertTrue('<Path3Node3>' in self.solver,
                        error_message(True, '<Path3Node3>' in self.solver))

    def testPublicMethodGenerate(self):
        """Test generate method on the GrammarSolver object."""
        self.assertRaises(InvalidSymbolError, self.solver.generate, 'Not', 10)
        self.assertRaises(ValueError, self.solver.generate, '<Start>', -1)
        self.assertTrue(
            self.solver.generate('<Start>', 1)[0] in '123456789',
            error_message(True,
                          self.solver.generate('<Start>',
                                               1)[0] in '123456789'))

    def testPrivateMethodStr(self):
        """Test __str__ method on the GrammarSolver object."""
        result_str = str(['<Path1>', '<Path1Node1>', '<Path1Node2>',
                          '<Path1Node3>', '<Path2>', '<Path2Node1>',
                          '<Path2Node2>', '<Path2Node3>', '<Path3>',
                          '<Path3Node1>', '<Path3Node2>', '<Path3Node3>',
                          '<Start>'])
        self.assertEqual(result_str, str(self.solver),
                         error_message(result_str, str(self.solver)))


class EndlessRecursiveGrammarGenerationCase(unittest.TestCase):
    """Tests the behaviour of Grammar input that the private method
    generate will definately traverse forever along its non-terminal/terminal
    path and hit recursion depth."""
    def setUp(self):
        """Sets up a GrammarSolver object with Grammar in which the private
        method generate will definately traverse forever along its non-terminal
        /terminal path and hit recursion depth."""
        grammar = ['<Start>::= <Node1> | <Node2> | <Node3>\n',
                   '<Node1>::= <Node1A> | <Node1B> | <Node1C>\n',
                   '<Node2>::= <Node2A> | <Node2B> | <Node2C>\n',
                   '<Node3>::= <Node3A> | <Node3B> | <Node3C>\n',
                   '<Node1A>::= <Start>\n', '<Node1B>::= <Start>\n',
                   '<Node1C>::= <Start>\n', '<Node2A>::= <Start>\n',
                   '<Node2B>::= <Start>\n', '<Node2C>::= <Start>\n',
                   '<Node3A>::= <Start>\n', '<Node3B>::= <Start>\n',
                   '<Node3C>::= <Start>\n']
        self.solver = GrammarSolver(grammar)

    def tearDown(self):
        """Clean up."""
        self.solver = None

    def testPrivateMethodContains(self):
        """Test __contains__ method on the GrammarSolver object."""
        self.assertTrue('<Start>' in self.solver,
                        error_message(True, '<Start>' in self.solver))
        self.assertTrue('<Node1>' in self.solver,
                        error_message(True, '<Node1>' in self.solver))
        self.assertTrue('<Node2>' in self.solver,
                        error_message(True, '<Node2>' in self.solver))
        self.assertTrue('<Node3>' in self.solver,
                        error_message(True, '<Node3>' in self.solver))
        self.assertTrue('<Node1A>' in self.solver,
                        error_message(True, '<Node1A>' in self.solver))
        self.assertTrue('<Node2A>' in self.solver,
                        error_message(True, '<Node2A>' in self.solver))
        self.assertTrue('<Node3A>' in self.solver,
                        error_message(True, '<Node3A>' in self.solver))
        self.assertTrue('<Node1B>' in self.solver,
                        error_message(True, '<Node1B>' in self.solver))
        self.assertTrue('<Node2B>' in self.solver,
                        error_message(True, '<Node2B>' in self.solver))
        self.assertTrue('<Node3B>' in self.solver,
                        error_message(True, '<Node3B>' in self.solver))
        self.assertTrue('<Node1C>' in self.solver,
                        error_message(True, '<Node1C>' in self.solver))
        self.assertTrue('<Node2C>' in self.solver,
                        error_message(True, '<Node2C>' in self.solver))
        self.assertTrue('<Node3C>' in self.solver,
                        error_message(True, '<Node3C>' in self.solver))

    def testPublicMethodGenerate(self):
        """Test generate method on the GrammarSolver object."""
        self.assertRaises(InvalidSymbolError, self.solver.generate, 'Not', 10)
        self.assertRaises(ValueError, self.solver.generate, '<Start>', -1)
        self.assertRaises(RuntimeError, self.solver.generate, '<Start>', 1)

    def testPrivateMethodStr(self):
        """Test __str__ method on the GrammarSolver object."""
        result_str = str(['<Node1>', '<Node1A>', '<Node1B>',
                          '<Node1C>', '<Node2>', '<Node2A>',
                          '<Node2B>', '<Node2C>', '<Node3>',
                          '<Node3A>', '<Node3B>', '<Node3C>', '<Start>'])
        self.assertEqual(result_str, str(self.solver),
                         error_message(result_str, str(self.solver)))


class ComplexGenerationCase(unittest.TestCase):
    """Tests the behaviour of a complex Grammar input that involves
    recursing along different paths randomly, concatenation of word pieces,
    and some terminals being non-terminals."""
    def setUp(self):
        """Sets up a complex GrammarSolver object with Grammar in which the
        private method generate will recurse along different paths randomly,
        concatenate word pieces, and some terminals being non-terminals."""
        grammar = ['<Start>::= <Path1> |<Path2>\n',
                   '<Path1>::= <Path1Continued>\n',
                   '<Path2>::= <Path2Continued>\n',
                   '<Path1Continued>::= <string1> <string2> H 1 Y\n',
                   '<Path2Continued>::= <Start>\n',
                   '<string1>::= C S C \n',
                   '<string2>::= 1 4 8\n']

        self.solver = GrammarSolver(grammar)

    def tearDown(self):
        """Clean up."""
        self.solver = None

    def testPrivateMethodContains(self):
        """Test __contains__ method on the GrammarSolver object."""
        self.assertTrue('<Start>' in self.solver,
                        error_message(True, '<Start>' in self.solver))
        self.assertTrue('<Path1>' in self.solver,
                        error_message(True, '<Path1>' in self.solver))
        self.assertTrue('<Path2>' in self.solver,
                        error_message(True, '<Path2>' in self.solver))
        self.assertTrue('<Path1Continued>' in self.solver,
                        error_message(True, '<Path1Continued>' in self.solver))
        self.assertTrue('<Path2Continued>' in self.solver,
                        error_message(True, '<Path2Continued>' in self.solver))
        self.assertTrue('<string1>' in self.solver,
                        error_message(True, '<string1>' in self.solver))
        self.assertTrue('<string2>' in self.solver,
                        error_message(True, '<string2>' in self.solver))

    def testPublicMethodGenerate(self):
        """Test generate method on the GrammarSolver object."""
        self.assertRaises(InvalidSymbolError, self.solver.generate, 'Not', 10)
        self.assertRaises(ValueError, self.solver.generate, '<Start>', -1)
        generated_list = self.solver.generate('<Start>', 1)
        self.assertEqual(['C S C 1 4 8 H 1 Y'], generated_list,
                         error_message(['C S C 1 4 8 H 1 Y'], generated_list))

    def testPrivateMethodStr(self):
        """Test __str__ method on the GrammarSolver object."""
        result_str = str(['<Path1>', '<Path1Continued>', '<Path2>',
                          '<Path2Continued>', '<Start>', '<string1>',
                          '<string2>'])
        self.assertEqual(result_str, str(self.solver),
                         error_message(result_str, str(self.solver)))


if __name__ == '__main__':
    unittest.main()
