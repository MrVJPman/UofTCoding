import unittest
from mouse import Mouse
from ant import Ant
from turtle import Turtle
from bird import Bird
from parrot import Parrot


class TestMouse(unittest.TestCase):
    """Tests the behaviour of the Mouse class."""
    def setUp(self):
        """Sets up a Mouse object."""
        self.mouse = Mouse()

    def tearDown(self):
        """Clean up."""
        self.mouse = None

    def testColor(self):
        """Test get_color() method on the Mouse object."""
        self.assertEqual('white', self.mouse.get_color())

    def testStr(self):
        """Test __str__ method on the Mouse object."""
        self.assertEqual('Q', str(self.mouse))

    def testDuel(self):
        """Test duel() method on the Mouse object."""
        for string in '*Q%@^><v&?':
            self.assertEqual('paper', self.mouse.duel(string))
        self.assertEqual('paper', self.mouse.duel(''))

    def testMovement(self):
        """Test get_move() method on the Mouse object."""
        for index in range(1, 1001):
            if index % 2 == 1:
                self.assertEqual('north', self.mouse.get_move())
            elif index % 2 == 0:
                self.assertEqual('west', self.mouse.get_move())


class TestAnt(unittest.TestCase):
    """Tests the behaviour of the Ant class."""
    def setUp(self):
        """Sets up an Ant object."""
        self.ant = Ant()

    def tearDown(self):
        """Clean up."""
        self.ant = None

    def testColor(self):
        """Test get_color() method on the Ant object."""
        self.assertEqual('red', self.ant.get_color())

    def testStr(self):
        """Test __str__ method on the Ant object."""
        self.assertEqual('%', str(self.ant))

    def testDuel(self):
        """Test duel() method on the Ant object."""
        duel_choices = ["rock", "paper", "scissors"]
        for index in range(1000):
            for string in '*Q%@^><v&?':
                self.assertTrue(self.ant.duel(string) in duel_choices)
        self.assertTrue(self.ant.duel('') in duel_choices)

    def testMovement(self):
        """Test get_move() method on the Ant object."""
        directions = ["north", "south", "east", "west", "center"]
        for index in range(10000):
            self.assertTrue(self.ant.get_move() in directions)


class TestTurtle(unittest.TestCase):
    """Tests the behaviour of the Turtle class."""
    def setUp(self):
        """Sets up a Turtle object."""
        self.turtle = Turtle()

    def tearDown(self):
        """Clean up."""
        self.turtle = None

    def testColor(self):
        """Test get_color() method on the Turtle object."""
        self.assertEqual('green', self.turtle.get_color())

    def testStr(self):
        """Test __str__ method on the Turtle object."""
        self.assertEqual('@', str(self.turtle))

    def testDuelForLoopOne(self):
        """Test duel() method on the Turtle object using a for loop."""
        last_move = 'scissors'
        for index in range(1, 1001):
            self.turtle.get_move()
            if index % 48 in [15, 39]:
                last_move = "rock"
            elif index % 48 in [3, 27]:
                last_move = "scissors"
            for string in '*Q%@^><v&?':
                self.assertEqual(last_move, self.turtle.duel(string))
            self.assertEqual(last_move, self.turtle.duel(''))

    def testDuelForLoopTwo(self):
        """Test duel() method on the Turtle object using a for loop."""
        last_move = 'scissors'
        for index in range(1, 1001):
            if index % 10 == 0:
                self.turtle.get_move()
            if index % 480 in [150, 390]:
                last_move = "rock"
            elif index % 480 in [30, 270]:
                last_move = "scissors"
            for string in '*Q%@^><v&?':
                self.assertEqual(last_move, self.turtle.duel(string))
            self.assertEqual(last_move, self.turtle.duel(''))

    def testDuelReg(self):
        """Test duel() method on the Turtle object by calling on it repeatedly.
        """
        self.turtle.get_move()  # C
        self.turtle.get_move()  # C
        self.assertEqual("scissors", self.turtle.duel(''))
        self.turtle.get_move()  # W
        self.assertEqual("scissors", self.turtle.duel(''))
        self.turtle.get_move()  # C
        self.turtle.get_move()  # C
        self.assertEqual("scissors", self.turtle.duel(''))
        self.turtle.get_move()  # W
        self.assertEqual("scissors", self.turtle.duel(''))
        self.turtle.get_move()  # C
        self.turtle.get_move()  # C
        self.assertEqual("scissors", self.turtle.duel(''))
        self.turtle.get_move()  # W
        self.assertEqual("scissors", self.turtle.duel(''))
        self.turtle.get_move()  # C
        self.turtle.get_move()  # C
        self.assertEqual("scissors", self.turtle.duel(''))
        self.turtle.get_move()  # W
        self.assertEqual("scissors", self.turtle.duel(''))

        self.turtle.get_move()  # C
        self.turtle.get_move()  # C
        self.assertEqual("scissors", self.turtle.duel(''))
        self.turtle.get_move()  # N
        self.assertEqual("rock", self.turtle.duel(''))
        self.turtle.get_move()  # C
        self.turtle.get_move()  # C
        self.assertEqual("rock", self.turtle.duel(''))
        self.turtle.get_move()  # N
        self.assertEqual("rock", self.turtle.duel(''))
        self.turtle.get_move()  # C
        self.turtle.get_move()  # C
        self.assertEqual("rock", self.turtle.duel(''))
        self.turtle.get_move()  # N
        self.assertEqual("rock", self.turtle.duel(''))
        self.turtle.get_move()  # C
        self.turtle.get_move()  # C
        self.assertEqual("rock", self.turtle.duel(''))
        self.turtle.get_move()  # N
        self.assertEqual("rock", self.turtle.duel(''))

        self.turtle.get_move()  # C
        self.turtle.get_move()  # C
        self.assertEqual("rock", self.turtle.duel(''))
        self.turtle.get_move()  # E
        self.assertEqual("scissors", self.turtle.duel(''))
        self.turtle.get_move()  # C
        self.turtle.get_move()  # C
        self.assertEqual("scissors", self.turtle.duel(''))
        self.turtle.get_move()  # E
        self.assertEqual("scissors", self.turtle.duel(''))
        self.turtle.get_move()  # C
        self.turtle.get_move()  # C
        self.assertEqual("scissors", self.turtle.duel(''))
        self.turtle.get_move()  # E
        self.assertEqual("scissors", self.turtle.duel(''))
        self.turtle.get_move()  # C
        self.turtle.get_move()  # C
        self.assertEqual("scissors", self.turtle.duel(''))
        self.turtle.get_move()  # E
        self.assertEqual("scissors", self.turtle.duel(''))

        self.turtle.get_move()  # C
        self.turtle.get_move()  # C
        self.assertEqual("scissors", self.turtle.duel(''))
        self.turtle.get_move()  # S
        self.assertEqual("rock", self.turtle.duel(''))
        self.turtle.get_move()  # C
        self.turtle.get_move()  # C
        self.assertEqual("rock", self.turtle.duel(''))
        self.turtle.get_move()  # S
        self.assertEqual("rock", self.turtle.duel(''))
        self.turtle.get_move()  # C
        self.turtle.get_move()  # C
        self.assertEqual("rock", self.turtle.duel(''))
        self.turtle.get_move()  # S
        self.assertEqual("rock", self.turtle.duel(''))
        self.turtle.get_move()  # C
        self.turtle.get_move()  # C
        self.assertEqual("rock", self.turtle.duel(''))
        self.turtle.get_move()  # S
        self.assertEqual("rock", self.turtle.duel(''))

        self.turtle.get_move()  # C
        self.turtle.get_move()  # C
        self.assertEqual("rock", self.turtle.duel(''))
        self.turtle.get_move()  # W
        self.assertEqual("scissors", self.turtle.duel(''))
        self.turtle.get_move()  # C
        self.turtle.get_move()  # C
        self.assertEqual("scissors", self.turtle.duel(''))
        self.turtle.get_move()  # W
        self.assertEqual("scissors", self.turtle.duel(''))
        self.turtle.get_move()  # C
        self.turtle.get_move()  # C
        self.assertEqual("scissors", self.turtle.duel(''))
        self.turtle.get_move()  # W
        self.assertEqual("scissors", self.turtle.duel(''))
        self.turtle.get_move()  # C
        self.turtle.get_move()  # C
        self.assertEqual("scissors", self.turtle.duel(''))
        self.turtle.get_move()  # W
        self.assertEqual("scissors", self.turtle.duel(''))

        self.turtle.get_move()  # C
        self.turtle.get_move()  # C
        self.assertEqual("scissors", self.turtle.duel(''))
        self.turtle.get_move()  # N
        self.assertEqual("rock", self.turtle.duel(''))
        self.turtle.get_move()  # C
        self.turtle.get_move()  # C
        self.assertEqual("rock", self.turtle.duel(''))
        self.turtle.get_move()  # N
        self.assertEqual("rock", self.turtle.duel(''))
        self.turtle.get_move()  # C
        self.turtle.get_move()  # C
        self.assertEqual("rock", self.turtle.duel(''))
        self.turtle.get_move()  # N
        self.assertEqual("rock", self.turtle.duel(''))
        self.turtle.get_move()  # C
        self.turtle.get_move()  # C
        self.assertEqual("rock", self.turtle.duel(''))
        self.turtle.get_move()  # N
        self.assertEqual("rock", self.turtle.duel(''))

        self.turtle.get_move()  # C
        self.turtle.get_move()  # C
        self.assertEqual("rock", self.turtle.duel(''))
        self.turtle.get_move()  # E
        self.assertEqual("scissors", self.turtle.duel(''))
        self.turtle.get_move()  # C
        self.turtle.get_move()  # C
        self.assertEqual("scissors", self.turtle.duel(''))
        self.turtle.get_move()  # E
        self.assertEqual("scissors", self.turtle.duel(''))
        self.turtle.get_move()  # C
        self.turtle.get_move()  # C
        self.assertEqual("scissors", self.turtle.duel(''))
        self.turtle.get_move()  # E
        self.assertEqual("scissors", self.turtle.duel(''))
        self.turtle.get_move()  # C
        self.turtle.get_move()  # C
        self.assertEqual("scissors", self.turtle.duel(''))
        self.turtle.get_move()  # E
        self.assertEqual("scissors", self.turtle.duel(''))

        self.turtle.get_move()  # C
        self.turtle.get_move()  # C
        self.assertEqual("scissors", self.turtle.duel(''))
        self.turtle.get_move()  # S
        self.assertEqual("rock", self.turtle.duel(''))
        self.turtle.get_move()  # C
        self.turtle.get_move()  # C
        self.assertEqual("rock", self.turtle.duel(''))
        self.turtle.get_move()  # S
        self.assertEqual("rock", self.turtle.duel(''))
        self.turtle.get_move()  # C
        self.turtle.get_move()  # C
        self.assertEqual("rock", self.turtle.duel(''))
        self.turtle.get_move()  # S
        self.assertEqual("rock", self.turtle.duel(''))
        self.turtle.get_move()  # C
        self.turtle.get_move()  # C
        self.assertEqual("rock", self.turtle.duel(''))
        self.turtle.get_move()  # S
        self.assertEqual("rock", self.turtle.duel(''))

    def testMovementForLoop(self):
        """Test get_move() method on the Turtle object using a for loop."""
        for index in range(1, 1000):
            direction = self.turtle.get_move()
            if index % 3 != 0:
                self.assertEqual('center', direction)
            else:
                if index % 48 in [3, 6, 9, 12]:
                    self.assertEqual('west', direction)
                elif index % 48 in [15, 18, 21, 24]:
                    self.assertEqual('north', direction)
                elif index % 48 in [27, 30, 33, 36]:
                    self.assertEqual('east', direction)
                elif index % 48 in [39, 42, 45, 0]:
                    self.assertEqual('south', direction)

    def testMovementReg(self):
        """Test get_move() method on the Turtle object by calling on it
        repeatedly."""
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('west', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('west', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('west', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('west', self.turtle.get_move())

        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('north', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('north', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('north', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('north', self.turtle.get_move())

        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('east', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('east', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('east', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('east', self.turtle.get_move())

        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('south', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('south', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('south', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('south', self.turtle.get_move())

        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('west', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('west', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('west', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('west', self.turtle.get_move())

        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('north', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('north', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('north', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('north', self.turtle.get_move())

        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('east', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('east', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('east', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('east', self.turtle.get_move())

        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('south', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('south', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('south', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('center', self.turtle.get_move())
        self.assertEqual('south', self.turtle.get_move())


class TestBird(unittest.TestCase):
    """Tests the behaviour of the Bird class."""
    def setUp(self):
        """Sets up a Bird object."""
        self.bird = Bird()

    def tearDown(self):
        """Clean up."""
        self.bird = None

    def testColor(self):
        """Test get_color() method on the Bird object."""
        self.assertEqual('blue', self.bird.get_color())

    def testStr(self):
        """Test __str__ method on the Bird object."""
        self.assertEqual('&', str(self.bird))
        for i in range(1000):
            last_move = self.bird.get_move()
            if last_move == "north":
                self.assertEqual('^', str(self.bird))
            if last_move == "east":
                self.assertEqual('>', str(self.bird))
            if last_move == "west":
                self.assertEqual('<', str(self.bird))
            if last_move == "south":
                self.assertEqual('v', str(self.bird))
            if last_move == "center":
                self.assertEqual('&', str(self.bird))

    def testDuel(self):
        """Test duel() method on the Bird object."""
        for string in '*Q%@^><v&?':
            if string == 'Q':
                self.assertEqual('scissors', self.bird.duel(string))
            elif string == '*':
                self.assertEqual('paper', self.bird.duel(string))
            else:
                self.assertEqual('rock', self.bird.duel(string))
        self.assertEqual('rock', self.bird.duel(''))

    def testMovementForLoop(self):
        """Test get_move() method on the Bird object using a for loop."""
        for index in range(1, 1001):
            if index % 15 == 1:
                direction = self.bird.get_move()
                self.assertTrue(direction in ["north", "south"])
            if index % 15 == 6:
                direction = self.bird.get_move()
                self.assertTrue(direction in ["east", "west"])
            if index % 15 in [2, 3, 4, 5, 7, 8, 9, 10]:
                self.assertEqual(direction, self.bird.get_move())
            if index % 15 in [11, 12, 13, 14, 0]:
                direction = 'center'
                self.assertEqual(direction, self.bird.get_move())

    def testMovementReg(self):
        """Test get_move() method on the Bird object by calling on it
        repeatedly."""
        direction = self.bird.get_move()
        self.assertTrue(direction in ["north", "south"])
        self.assertEqual(direction, self.bird.get_move())
        self.assertEqual(direction, self.bird.get_move())
        self.assertEqual(direction, self.bird.get_move())
        self.assertEqual(direction, self.bird.get_move())
        direction = self.bird.get_move()
        self.assertTrue(direction in ["east", "west"])
        self.assertEqual(direction, self.bird.get_move())
        self.assertEqual(direction, self.bird.get_move())
        self.assertEqual(direction, self.bird.get_move())
        self.assertEqual(direction, self.bird.get_move())
        self.assertEqual('center', self.bird.get_move())
        self.assertEqual('center', self.bird.get_move())
        self.assertEqual('center', self.bird.get_move())
        self.assertEqual('center', self.bird.get_move())
        self.assertEqual('center', self.bird.get_move())

        direction = self.bird.get_move()
        self.assertTrue(direction in ["north", "south"])
        self.assertEqual(direction, self.bird.get_move())
        self.assertEqual(direction, self.bird.get_move())
        self.assertEqual(direction, self.bird.get_move())
        self.assertEqual(direction, self.bird.get_move())
        direction = self.bird.get_move()
        self.assertTrue(direction in ["east", "west"])
        self.assertEqual(direction, self.bird.get_move())
        self.assertEqual(direction, self.bird.get_move())
        self.assertEqual(direction, self.bird.get_move())
        self.assertEqual(direction, self.bird.get_move())
        self.assertEqual('center', self.bird.get_move())
        self.assertEqual('center', self.bird.get_move())
        self.assertEqual('center', self.bird.get_move())
        self.assertEqual('center', self.bird.get_move())
        self.assertEqual('center', self.bird.get_move())


class TestParrot(unittest.TestCase):
    """Tests the behaviour of the Parrot class."""
    def setUp(self):
        """Sets up a Parrot object."""
        self.parrot = Parrot()

    def tearDown(self):
        """Clean up."""
        self.parrot = None

    def testColor(self):
        """Test get_color() method on the Parrot object."""
        self.assertEqual('yellow', self.parrot.get_color())

    def testStr(self):
        """Test __str__ method on the Parrot object."""
        self.assertEqual('?', str(self.parrot))
        for string in '*Q%@^><v&?':
            self.parrot.duel(string)
            self.assertEqual(string, str(self.parrot))

    def testDuel(self):
        """Test duel() method on the Parrot object."""
        for string in '*Q%@^><v&?':
            if string == 'Q':
                self.assertEqual('scissors', self.parrot.duel(string))
            elif string == '*':
                self.assertEqual('paper', self.parrot.duel(string))
            else:
                self.assertEqual('rock', self.parrot.duel(string))

    def testMovementForLoop(self):
        """Test get_move() method on the Parrot object using a for loop."""
        for index in range(1, 1001):
            if index % 15 == 1:
                direction = self.parrot.get_move()
                self.assertTrue(direction in ["north", "south"])
            if index % 15 == 6:
                direction = self.parrot.get_move()
                self.assertTrue(direction in ["east", "west"])
            if index % 15 in [2, 3, 4, 5, 7, 8, 9, 10]:
                self.assertEqual(direction, self.parrot.get_move())
            if index % 15 in [11, 12, 13, 14, 0]:
                direction = 'center'
                self.assertEqual(direction, self.parrot.get_move())

    def testMovementReg(self):
        """Test get_move() method on the Parrot object by calling on it
        repeatedly."""
        direction = self.parrot.get_move()
        self.assertTrue(direction in ["north", "south"])
        self.assertEqual(direction, self.parrot.get_move())
        self.assertEqual(direction, self.parrot.get_move())
        self.assertEqual(direction, self.parrot.get_move())
        self.assertEqual(direction, self.parrot.get_move())
        direction = self.parrot.get_move()
        self.assertTrue(direction in ["east", "west"])
        self.assertEqual(direction, self.parrot.get_move())
        self.assertEqual(direction, self.parrot.get_move())
        self.assertEqual(direction, self.parrot.get_move())
        self.assertEqual(direction, self.parrot.get_move())
        self.assertEqual('center', self.parrot.get_move())
        self.assertEqual('center', self.parrot.get_move())
        self.assertEqual('center', self.parrot.get_move())
        self.assertEqual('center', self.parrot.get_move())
        self.assertEqual('center', self.parrot.get_move())

        direction = self.parrot.get_move()
        self.assertTrue(direction in ["north", "south"])
        self.assertEqual(direction, self.parrot.get_move())
        self.assertEqual(direction, self.parrot.get_move())
        self.assertEqual(direction, self.parrot.get_move())
        self.assertEqual(direction, self.parrot.get_move())
        direction = self.parrot.get_move()
        self.assertTrue(direction in ["east", "west"])
        self.assertEqual(direction, self.parrot.get_move())
        self.assertEqual(direction, self.parrot.get_move())
        self.assertEqual(direction, self.parrot.get_move())
        self.assertEqual(direction, self.parrot.get_move())
        self.assertEqual('center', self.parrot.get_move())
        self.assertEqual('center', self.parrot.get_move())
        self.assertEqual('center', self.parrot.get_move())
        self.assertEqual('center', self.parrot.get_move())
        self.assertEqual('center', self.parrot.get_move())


if __name__ == '__main__':
    unittest.main()
