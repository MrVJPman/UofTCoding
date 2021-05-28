from critter import Critter
import random


class Wolf(Critter):
    """A Wolf that is capable of adapting to many situations. It is capable of
    communciating with each other to perform certain functionalities, and can
    hide as an ant or a parrot."""
    opponents_to_avoid = ["!", "%"]
    anti_parrot_as_mouse_mode = False
    anti_parrot_as_turtle_mode = False
    number_of_wolves = 0
    hunter_list = []
    unknown_critter_dict = {}
    ant_mode = False
    parrot_mode = False
    desperation_mode = False

    def __init__(self):
        """Wolf -> NoneType

        Initialize a Wolf object.

        """
        self.turns_passed = 0
        self.have_moved = False
        self.turtle_move = "scissors"
        self.hunted_animal = ''
        self.next_opponent_is_parrot = False
        self.next_step = None
        self.this_step = None
        self.wait = 0
        Wolf.number_of_wolves += 1

    def get_color(self):
        """Wolf -> str

        Return the string to draw the Wolf object random in colour.

        """
        return random.choice(["blue", "cyan", "gray", "green", "yellow",
                              "magenta", "red", "white"])

    def __str__(self):
        """Wolf -> str

        Return the string representation of the Wolf object based on whether
        it has a hiding mode. Can appear as an ant(%), a parrot(?) or itself(!)
        .

        """
        self.have_moved = False
        if Wolf.ant_mode:
            return "%"
        elif Wolf.parrot_mode:
            return "?"
        return "!"

    def _mode_control(self):
        """Wolf -> NoneType

        Adjusts the Wolf's modes depending on total numbers of moves made and
        number of Wolf objects remaining.

        """
        if self.turns_passed >= 250:
            Wolf.anti_parrot_as_mouse_mode = False
            Wolf.anti_parrot_as_turtle_mode = False
            Wolf.hunter_list = []
        if Wolf.number_of_wolves <= 15 and Wolf.number_of_wolves > 10:
            Wolf.ant_mode = True
        elif Wolf.number_of_wolves <= 10 and Wolf.number_of_wolves > 5:
            Wolf.ant_mode = False
            Wolf.parrot_mode = True
            Wolf.opponents_to_avoid.append('?')
        elif Wolf.number_of_wolves <= 5:
            Wolf.ant_mode = False
            Wolf.parrot_mode = False
            Wolf.desperation_mode = True

    def _update_variables_and_decide_hunt(self):
        """Wolf -> NoneType

        Resets and prepare the Wolf object's functionalities for its current
        turn.

        """
        self.turns_passed += 1
        if self.turns_passed % 24 == 15:
            self.turtle_move = "rock"
        elif self.turns_passed % 24 == 3:
            self.turtle_move = "scissors"
        self._mode_control()
        self.have_moved = True
        self.direction_list = ["north", "east", "west", "south", "center"]
        self.bird_and_parrot_list = []
        if not Wolf.parrot_mode:
            self._check_for_birds_and_parrots()
        self._check_for_hunter()

    def _check_for_hunter(self):
        """Wolf -> NoneType

        Decides the Wolf object's hunted critter, wait and kill it accordingly.
        Can only hunt parrot as mouse or parrot as turtle.

        """
        if self.turns_passed % 15 <= 10 or Wolf.hunter_list == []:
            self.this_step = None
            self.next_step = None
            self.wait = 0
            self.hunted_animal = ''
        elif self.next_step == None:
            hunted_animal = random.choice(Wolf.hunter_list)
            if hunted_animal == "Q":
                for direction in ["north", "east", "west", "south"]:
                    if self.get_neighbor(direction) == "Q":
                        self.next_step = direction
                        self.this_step = "center"
                        self.hunted_animal = "Q"
            elif hunted_animal == "@":
                for direction in ["north", "east", "west", "south"]:
                    if self.get_neighbor(direction) == "@":
                        self.next_step = direction
                        self.this_step = "center"
                        self.hunted_animal = "@"
        elif self.get_neighbor(self.next_step) == self.hunted_animal and \
             self.wait < 2:
                self.wait += 1
                self.this_step = "center"
        elif self.get_neighbor(self.next_step) == self.hunted_animal and \
             self.wait == 2:
                self.next_opponent_is_parrot = True
                self.this_step = self.next_step
                self.next_step = None
        else:
            self.wait = 0
            self.next_step = None
            self.this_step = None
            self.hunted_animal = ''

    def _duel_against_turtle(self):
        """Wolf -> str

        Return the weapons required to defeat a Turtle object.

        """
        if self.turns_passed % 24 in [2, 14] and self.turns_passed > 3 and \
           not self.have_moved:
            if self.turtle_move == "rock":
                return "rock"
            elif self.turtle_move == "scissors":
                return "paper"
        else:
            if self.turtle_move == "rock":
                return "paper"
            elif self.turtle_move == "scissors":
                return "rock"

    def _duel_against_stone_mouse_ant_other(self, opponent):
        """(Wolf, str) -> str

        Return the weapons required to defeat a Mouse, Stone object, else
        return paper against Ant, return a likely victorious weapon against
        an identified enemy Wolf or return a randomized weapon.

        """
        if opponent in "*%":
            return "paper"
        elif opponent == "Q":
            return "scissors"
        elif opponent in Wolf.unknown_critter_dict:
            weapons_list = Wolf.unknown_critter_dict[opponent]
            most_frequent_weapon = max(weapons_list)
            weapon_index = weapons_list.index(most_frequent_weapon)
            return ["rock", "paper", "scissors"][weapon_index]
        else:
            return random.choice(["rock", "paper", "scissors"])

    def duel(self, opponent):
        """(Wolf, str)-> str

        Return the Wolf critter's attack when given an string representation
        of opponent. Chooses from a variety of option depending on its hidden
        mode, opponent, and its latest movement.

        """
        self.opponent = opponent
        if Wolf.parrot_mode:
            self.recorded_attack = 'scissors'
            return "scissors"
        if opponent in '?!&^<>v' or self.next_opponent_is_parrot:
            self.next_opponent_is_parrot = False
            self.recorded_attack = "paper"
        elif opponent == "@":
            self.recorded_attack = self._duel_against_turtle()
        else:
            self.recorded_attack = \
                self._duel_against_stone_mouse_ant_other(opponent)

        return self.recorded_attack

    def _check_for_birds_and_parrots(self):
        """Wolf -> NoneType

        Check the Wolf object's surrounding for Bird and Parrot objects.

        """
        for direction in ["north", "east", "west", "south"]:
            if self.get_neighbor(direction) in "?><v^&":
                self.bird_and_parrot_list.append(direction)

    def _avoid_everything(self):
        """Wolf -> NoneType

        Check the Wolf object's surrounding for any critter.

        """
        for direction in ["north", "east", "west", "south"]:
            if self.get_neighbor(direction) != ' ':
                self.direction_list.remove(direction)

    def _avoid_enemies_when_needed(self):
        """Wolf -> NoneType

        Check the Wolf object's surrounding for any dangerous critter in
        invasive situations.

        """
        for direction in ["north", "east", "west", "south"]:
            if self.get_neighbor(direction) == '@' and \
               (self.turns_passed % 24 in [3, 15] or \
                Wolf.anti_parrot_as_turtle_mode):
                self.direction_list.remove(direction)
            elif self.get_neighbor(direction) in Wolf.opponents_to_avoid:
                self.direction_list.remove(direction)
            elif self.get_neighbor(direction) == "Q" and \
                 Wolf.anti_parrot_as_mouse_mode:
                self.direction_list.remove(direction)

    def get_move(self):
        """(Wolf, str)-> str

        Return the next move of the Wolf critter, its move is determined by
        the circumstances of the current gameplay, its surroundings critters,
        and the mode its on.

        """
        self._update_variables_and_decide_hunt()

        if Wolf.desperation_mode:
            self._avoid_everything()
            if self.direction_list == ["north", "east", "west", "south",
                                       "center"]:
                return "center"
            else:
                return random.choice(self.direction_list)

        if self.hunted_animal == "Q" or self.hunted_animal == "@":
            return self.this_step
        elif self.bird_and_parrot_list:
            return random.choice(self.bird_and_parrot_list)
        else:
            self._avoid_enemies_when_needed()
            return random.choice(self.direction_list)

    def _update_winning_attack_of_critter(self, weapon):
        """Wolf -> NoneType

        Updates the likely victorious weapon against identified enemy Wolf
        objects.

        """
        if weapon == "rock":
            Wolf.unknown_critter_dict[self.opponent][0] += 1
        elif weapon == "paper":
            Wolf.unknown_critter_dict[self.opponent][1] += 1
        elif weapon == "scissors":
            Wolf.unknown_critter_dict[self.opponent][2] += 1

    def won(self):
        """Wolf -> NoneType

        Called on a Wolf critter after it wins a duel.

        """
        if self.opponent not in "!*Q%@^v><&?":
            Wolf.unknown_critter_dict[self.opponent] = [1, 1, 1]
        if self.opponent in Wolf.unknown_critter_dict:
            self._update_winning_attack_of_critter(self.recorded_attack)

    def lost(self):
        """Wolf -> NoneType

        Called on a Wolf critter after it loses a duel.

        """
        Wolf.number_of_wolves -= 1
        if self.opponent not in "!*Q%@^v><&?":
            Wolf.unknown_critter_dict[self.opponent] = [1, 1, 1]
        elif self.opponent == "Q":
            Wolf.anti_parrot_as_mouse_mode = True
            Wolf.hunter_list.append("Q")
        elif self.opponent == "@":
            Wolf.anti_parrot_as_turtle_mode = True
            Wolf.hunter_list.append("@")

        if self.opponent in Wolf.unknown_critter_dict:
            if self.recorded_attack == "rock":
                self._update_winning_attack_of_critter("scissors")
            elif self.recorded_attack == "scissors":
                self._update_winning_attack_of_critter("paper")
            elif self.recorded_attack == "paper":
                self._update_winning_attack_of_critter("rock")
