# adventure-complete.py

class Room(object):
    def __init__(self, name, connections={}):
        self.name = name
        self.description = 'An indescribable room.'
        self.connections = connections

    def enter(self):
        print 'You enter the {}.'.format(self.name)
        self.describe()
        if len(self.connections) <= 0:
            print 'Game Over!'
            exit()

    def describe(self):
        print 'You see: {}'.format(self.description)
        self.show_connections()

    def show_connections(self):
        print 'Paths: {}'.format(self.connections.keys())


#==========================================================
pit = Room('Pit of No Escape')

bakery = Room('Bakery')
bakery.description = 'A bright bakery full of delicious cupcakes.'

hallway_plate = Room('Hallway (Pressure Plate)', connections={'left': pit, 'right': bakery})
hallway_plate.description = 'A long way forward with another path to the left.  A new way has opened.'

hallway = Room('Hallway', connections={'left': pit, 'forward': pit, 'pressure-plate': hallway_plate})
hallway.description = 'A long way forward with another path to the left.'

entry = Room('Cave Entrance', connections={'trapdoor': pit, 'forward': hallway})
entry.description = 'Curved walls leading into darkness.'

current_room = entry
while True:
    current_room.enter()
    path = ''
    while path not in current_room.connections.keys():
        path = raw_input('Choose your path: ')
    current_room = current_room.connections[path]

