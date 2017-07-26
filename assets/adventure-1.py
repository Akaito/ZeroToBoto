# adventure-1.py


#==========================================================
class Room(object):
    """A describeable place which connects to other rooms."""

    def __init__(self, name, connections={}):
        # Should assign something to each variable you want to exist on an
        # object during its initialization.
        self.name = name
        self.description = 'An indescribable room.'
        self.connections = connections

    def describe(self):
        """Prints out what the player sees here."""
        print 'You see: {}'.format(self.description)
        self.show_connections()

    def show_connections(self):
        """Prints the available connections to other rooms."""
        print 'Paths: {}'.format(self.connections.keys())


#==========================================================
# lose room
pit = Room('Pit of No Escape')

# hallway room (first interesting room after entrance)
hallway = Room('Hallway', connections={'left': pit, 'right': pit})
hallway.description = 'A long way forward with another path to the left.'

# entry room for the game
entry = Room('Cave Entrance', connections={'trapdoor': pit, 'forward': hallway})
entry.description = 'Curved walls leading into darkness.'

# Now that the 'entry' object exists, we can add it to the hallway room.
hallway.connections['back'] = entry

#==========================================================
entry.describe()
entry.connections['trapdoor'].describe()
entry.connections['forward'].describe()

