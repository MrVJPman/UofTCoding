import sys
import unittest

from random import shuffle
from StringIO import StringIO

ATTACKS = ('rock', 'paper', 'scissors')
MOVES = ('north', 'south', 'east', 'west', 'center')
OPPONENTS = ".*Q%@^><v& W"

stdout_log = []
def no_stdout(test):
    def wrapped(self):
        stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            test(self)
            output = sys.stdout.getvalue()
            if output:
                stdout_log.append((self.__class__.__name__, test.__name__, output))
        finally:
            sys.stdout = stdout

    return wrapped


class NoPrinting(unittest.TestCase):
    def test_no_stdout(self):
        if stdout_log:
            msgs = []
            for cls, func, msg in stdout_log:
                msgs.append("%s.%s: %r" % (cls, func, msg))
        
            self.assertFalse(stdout_log, "Writing to stdout was not allowed, but found:\n%s" % '\n'.join(msgs))



class BasicCase():
    @no_stdout
    def test_duel(self):
        """Duel attack is correct"""
        for opponent in OPPONENTS:
            for critter in self.critters:
                self.assertEqual(critter.duel(opponent), self.attack)

    @no_stdout
    def test_color(self):
        """Color is correct"""
        for critter in self.critters:
            self.assertEqual(critter.get_color(), self.color)

    @no_stdout
    def test_str(self):
        """String is correct"""
        for critter in self.critters:
            self.assertEqual(str(critter), self.str)
        

class MouseCase(BasicCase, unittest.TestCase):
    @no_stdout
    def setUp(self):
        from mouse import Mouse
        self.critters = [Mouse() for i in range(20)]
        self.color = 'white'
        self.str = 'Q'
        self.attack = 'paper'

    @no_stdout
    def test_move_strict(self):
        """Move alternates north and west, starting north"""
        for move in ['north', 'west'] * 5:
            for critter in self.critters:
                self.assertEqual(critter.get_move(), move)

    @no_stdout
    def test_move_lenient(self):
        """Move alternates north and west"""
        move = None
        last_move = None
        for i in range(20):
            for critter in self.critters:
                if move is None:
                    move = critter.get_move()
                    # Make sure moves alternate
                    self.assertNotEqual(move, last_move)
                else:
                    self.assertEqual(critter.get_move(), move)

            last_move = move
            move = None


class AntCase(BasicCase, unittest.TestCase):
    @no_stdout
    def setUp(self):
        from ant import Ant
        self.n = 1000
        self.critters = [Ant() for i in range(self.n)]
        self.color = 'red'
        self.str = '%'

    @no_stdout
    def test_duel(self):
        """Make sure duels look random"""
        for opponent in OPPONENTS:
            counts = dict([(attack, 0) for attack in ATTACKS])
            for critter in self.critters:
                counts[critter.duel(opponent)] += 1

            for count in counts.values():
                self.assertTrue(self.n / 5 < count < self.n / 2, 
                                "Distribution of attacks against opponent (%r)"
                                " does not look random: R:%d, P:%d, S:%d" 
                                % (opponent, counts['rock'], 
                                   counts['paper'], counts['scissors']))

    @no_stdout
    def test_move(self):
        """Make sure the first 10 moves look random"""
        for i in range(10):
            counts = dict([(move, 0) for move in MOVES])
            for critter in self.critters:
                counts[critter.get_move()] += 1

            for count in counts.values():
                self.assertTrue(self.n / 8 < count < self.n / 2, 
                                "Distribution of moves does not look random:"
                                " N:%d, E:%d, S:%d, W:%d, C:%d" 
                                % (counts['north'], counts['east'],
                                   counts['south'], counts['west'], 
                                   counts['center']))




class TurtleCase(BasicCase, unittest.TestCase):
    @no_stdout
    def setUp(self):
        from turtle import Turtle
        self.n = 20
        self.critters = [Turtle() for i in range(self.n)]
        self.color = 'green'
        self.str = '@'

    @no_stdout
    def test_duel(self):
        """Make sure duel is correct based upon moves"""
        duel = {'east': 'scissors', 'west': 'scissors', 
                'north': 'rock', 'south': 'rock'}
        for critter in self.critters:
            self.assertEqual(critter.duel(' '), 'scissors')
            # Test first duels/moves
            last_move = 'east'
            for opponent in OPPONENTS * 5:
                move = critter.get_move()
                if move != 'center':
                    last_move = move

                self.assertEqual(critter.duel(opponent), duel[last_move])

    @no_stdout
    def test_move_strict(self):
        """Make sure the first three cycles of moves are correct"""
        moves = []
        for dir in ('west', 'north', 'east', 'south'):
            for i in range(4):
                moves.extend(['center'] * 2)
                moves.append(dir)

        for move in moves * 3:
            for critter in self.critters:
                self.assertEqual(critter.get_move(), move)

    @no_stdout
    def test_move_lenient(self):
        """Make sure moves are correct, ignoring centers"""
        moves = ['west'] * 4 + ['north'] * 4 + ['east'] * 4 + ['south'] * 4
        for move in moves * 3:
            for critter in self.critters:
                # Up to 10 chances to get next move
                found = False
                for i in range(10):
                    observed_move = critter.get_move()
                    if observed_move != 'center':
                        self.assertEqual(observed_move, move)
                        found = True
                        break

                self.assertTrue(found, "Expected next move was not returned"
                                " within 10 moves")




class BirdCase(BasicCase, unittest.TestCase):
    @no_stdout
    def setUp(self):
        from bird import Bird
        self.n = 200
        self.critters = [Bird() for i in range(self.n)]
        self.color = 'blue'

    @no_stdout
    def test_str(self):
        """Test string based upon last move"""
        strs = {'east': '>', 'west': '<', 
                'north': '^', 'south': 'v', 'center': '&'}
        for critter in self.critters:
            # Test first 50 move/strs
            for i in range(50):
                move = critter.get_move()
                self.assertEqual(str(critter), strs[move])
        

    @no_stdout
    def test_duel(self):
        """Make sure duel is correct"""
        duels = {'Q': 'scissors', '*': 'paper'}
        for critter in self.critters:
            for opponent in OPPONENTS:
                attack = critter.duel(opponent)
                if opponent in duels:
                    self.assertEqual(attack, duels[opponent])
                else:
                    self.assertEqual(attack, 'rock')

    @no_stdout
    def test_move_random_first(self):
        """Make sure the first move is random north or south"""
        counts = dict([(move, 0) for move in MOVES])
        for critter in self.critters:
            counts[critter.get_move()] += 1

        self.assertTrue(counts['east'] == counts['west'] == \
                            counts['center'] == 0)
        for count in (counts['north'], counts['south']):
            self.assertTrue(self.n / 4 < count < 3 * self.n / 4, 
                            "Distribution of moves does not look random:"
                            " N:%d, S:%d" 
                            % (counts['north'], counts['south']))

    @no_stdout
    def test_move_random_second(self):
        """Make sure the sixth move is random east or west"""
        counts = dict([(move, 0) for move in MOVES])
        for critter in self.critters:
            for _ in range(5):
                critter.get_move()

            # Measure the 6th move
            counts[critter.get_move()] += 1

        self.assertTrue(counts['north'] == counts['south'] == \
                            counts['center'] == 0)
        for count in (counts['east'], counts['west']):
            self.assertTrue(self.n / 4 < count < 3 * self.n / 4, 
                            "Distribution of moves does not look random:"
                            " E:%d, W:%d" 
                            % (counts['east'], counts['west']))


    @no_stdout
    def test_move_strict(self):
        """Make sure full move behavior is correct"""
        for i in range(7):
            expected = {0: set(['north', 'south']),
                        1: set(['east', 'west'])}
            moves = dict([(critter, critter.get_move()) 
                          for critter in self.critters])
            for _ in range(4):
                counts = dict([(move, 0) for move in MOVES])
                for move in moves.values():
                    counts[move] += 1

                if i % 3 == 2:
                    self.assertEqual(counts['center'], self.n,
                                     "Expected all 'center' at steps 10-14")
                else:
                    for dir in set(MOVES) - expected[i % 3]:
                        self.assertEqual(counts[dir], 0)
                        
                    for dir in expected[i % 3]:
                        self.assertTrue(self.n / 4 < counts[dir] \
                                            < 3 * self.n / 4, 
                                        "Expected 50/50: %s (found: %s)" 
                                        % (expected[i % 3], counts))

                new_moves = dict([(critter, critter.get_move()) 
                                  for critter in self.critters])
                self.assertEqual(moves, new_moves, 
                                 "Same direction not followed for five steps")

    @no_stdout
    def test_dir_preserved(self):
        """Make sure each direction is continued for 5 steps"""
        for critter in self.critters:
            # Do 7 sets of 5
            for _ in range(7):
                for _ in range(5):
                    moves = set()
                    moves.add(critter.get_move())
                    self.assertTrue(len(moves) == 1, 
                                    "Expected only one direction for 5 steps,"
                                    " but found: %s" % moves)
    

class ParrotCase(BirdCase, unittest.TestCase):
    @no_stdout
    def setUp(self):
        from parrot import Parrot
        self.n = 200
        self.critters = [Parrot() for i in range(self.n)]
        self.color = 'yellow'

    @no_stdout
    def test_inheritance(self):
        from bird import Bird
        self.assertTrue(isinstance(self.critters[0], Bird))
        
    @no_stdout
    def test_str(self):
        """Test string based upon last opponent"""
        opponents = list(OPPONENTS * 3)
        shuffle(opponents)
        for critter in self.critters:
            self.assertEqual(str(critter), '?')
            for opponent in opponents:
                critter.duel(opponent)
                self.assertEqual(str(critter), opponent)

class WolfCase(unittest.TestCase):
    @no_stdout
    def setUp(self):
        from wolf import Wolf
        self.n = 200
        self.critters = []
        for i in range(self.n):
            w = Wolf()
            w.neighbors = dict([(move, ' ') for move in MOVES])
            w.x = i
            w.y = i
            w.world_height = self.n
            w.world_width = self.n
            self.critters.append(w)

    @no_stdout
    def test_duel(self):
        """Duel attack is valid"""
        for opponent in OPPONENTS:
            for critter in self.critters:
                self.assertIn(critter.duel(opponent), ATTACKS)

    @no_stdout
    def test_color(self):
        """Color is valid"""
        for critter in self.critters:
            self.assertTrue(isinstance(critter.get_color(), str))

    @no_stdout
    def test_str(self):
        """String is valid"""
        for critter in self.critters:
            str(critter)  # will crash if not a string

    @no_stdout
    def test_move(self):
        """Movement is valid"""
        for i in range(50):
            for critter in self.critters:
                self.assertIn(critter.get_move(), MOVES)
        


if __name__ == '__main__':
    unittest.main()
