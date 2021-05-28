class EmptyStackError(Exception):
    pass

class Stack(object):
    def __init__(self):
        self._data = []

    def push(self, elt):
        """ (Stack, object) -> NoneType

        Add elt to the top of the stack
        """
        # If we use the end of a list:
        self._data.append(elt)
        # If we use the beginning of a list:
        # self._data.insert(0, elt)

    def pop(self):
        """ Stack -> object

        Remove and return the top elt on the stack
        """
        # If we use the end of a list:
        if self.is_empty():
            raise EmptyStackError()

        return self._data.pop()
        # If we use the beginning of a list:
        # return self._data.pop(0)

    def is_empty(self):
        """ Stack -> bool

        Return if the stack is empty
        """
        # is self._data empty?
        # return not len(self._data)
        # return self._data == []

        # return bool(self._data)
        # This didn't end up working because our boolean was flipped
        # Instead we needed:
        # return not self._data

        # This will work just fine, though, and is arguably clearer
        return len(self._data) == 0

if __name__ == "__main__":
    cards = Stack()
    assert cards.is_empty()
    cards.push("Jack of hearts")
    cards.push("S2")  # 2 of spades
    assert cards.pop() == "S2"
    assert cards.pop() == "Jack of hearts"
    assert cards.is_empty()

    try:
        cards.pop()
        assert False, "Stack let us pop an empty stack"
    except EmptyStackError:
        pass
