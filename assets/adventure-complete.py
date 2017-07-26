# adventure-complete.py


#==========================================================
class Room(object):
    """A describeable place which connects to other rooms."""

    def __init__(self, name, connections={}):
        # Should assign something to each variable you want to exist on an
        # object during its initialization.
        self.name = name
        self.description = 'An indescribable room.'
        self.connections = connections
        self.visits = 0

    def enter(self):
        """Called when the player enters the room."""
        print 'You enter the {}.'.format(self.name)
        print "You've been here {} time(s) before.".format(self.visits)
        self.visits += 1
        self.describe()

    def describe(self):
        """Prints out what the player sees here."""
        print 'You see: {}'.format(self.description)
        self.show_connections()

    def show_connections(self):
        """Prints the available connections to other rooms."""
        print 'Paths: {}'.format(self.connections.keys())


#==========================================================
# Our Room objects are created in a sort of reversed order, to make it
#   easy to initialize connections to future rooms (since those objects
#   need to exist at that time).
# Alternatively, you could create them in forward order without connections
#   to later rooms, then add the connections later.

# lose room
pit = Room('Pit of No Escape')

# win room
bakery = Room('Bakery')
bakery.description = 'A bright bakery full of delicious cupcakes.'

# modified hallway room
hallway_plate = Room('Hallway (Pressure Plate)', connections={'left': pit, 'right': bakery})
hallway_plate.description = 'A long way forward with another path to the left.  A new way has opened.'

# hallway room (first interesting room after entrance)
hallway = Room('Hallway', connections={'left': pit, 'pressure-plate': hallway_plate})
hallway.description = 'A long way forward with another path to the left.'

# entry room for the game
entry = Room('Cave Entrance', connections={'trapdoor': pit, 'forward': hallway})
entry.description = 'Curved walls leading into darkness.'

# Now that the 'entry' object exists, we can add it to the hallway room(s).
# Note, however, that entry's "forward" will always be to 'hallway'.
hallway_plate.connections['back'] = entry
hallway.connections['back'] = entry


#==========================================================
current_room = entry  # refers to the room object (above) that we're currently in

while True:  # loop until 'quit' or a dead-end room; logic below
    current_room.enter()
    # if in a dead-end room, stop the game
    if len(current_room.connections) <= 0:
        print 'Game Over!'
        break  # leave the loop
    path = ''
    # get from the player a choice of connection available in the current room
    # (or 'quit' to stop playing)
    while path not in current_room.connections.keys() and path != 'quit':
        path = raw_input('Choose your path: ')
    if path == 'quit':
        break
    # move to the chosen room, referred to by the connection in this one
    current_room = current_room.connections[path]
    print ''  # just give a little breathing room for the text

