# rpg-complete.py

TEAM_UNDEFINED = 0
TEAM_PLAYER = 1
TEAM_ENEMY = 2


class Character(object):
    name = 'UNNAMED'
    hp = 0
    hp_max = 0
    team = TEAM_UNDEFINED
    attacks = {}

    def __init__(self, name, hp, team, attacks):
        self.name = name
        self.hp = hp
        self.hp_max = hp
        self.team = team
        self.attacks = attacks

    def __str__(self):
        return '{} ({}/{} hp)'.format(self.name, self.hp, self.hp_max)

    def format_attacks_list(self):
        result = ''
        for attack in self.attacks.items():
            result += '{}\n'.format(str(attack))
        return result


class Attack(object):
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __str__(self):
        return '{} ({} dmg)'.format(self.name, self.damage)


#====================================================================
characters = []

characters.append(Character('Alice', 20, TEAM_PLAYER, {}))
characters.append(Character('Bob', 12, TEAM_PLAYER, {}))
characters.append(Character('Slime 0', 5, TEAM_ENEMY, {}))

for ch in characters:
    print ch
    print ch.format_attacks_list()
    print ''

