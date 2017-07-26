# adventure-0.py


#==========================================================
class Room(object):
    """A describeable place which connects to other rooms."""

    def __init__(self, name):
        # Should assign something to each variable you want to exist on an
        # object during its initialization.
        self.name = name
        self.description = 'An indescribable room.'

    def describe(self):
        """Prints out what the player sees here."""
        print 'You see: {}'.format(self.description)


#==========================================================
# lose room
pit = Room('Pit of No Escape')

# entry room for the game
entry = Room('Cave Entrance')
entry.description = 'Curved walls leading into darkness.'

#==========================================================
pit.describe()
entry.describe()

