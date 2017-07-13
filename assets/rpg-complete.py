# rpg-complete.py

import random


class Character:
    def __init__(self, name, hp, attacks):
        self.name = name
        self.hp = hp
        self.hp_max = hp
        self.attacks = {}
        for attack in attacks:
            self.attacks[attack.name.lower()] = attack

    def __str__(self):
        return '{} ({}/{} hp)'.format(self.name, self.hp, self.hp_max)

    def attack_something(self, target, attack=None):
        if attack is None:
            attack = random.choice(self.attacks.values())
        elif type(attack) == str:
            attack = self.attacks[attack]
        attack.perform(self, target)


class CharSlime(Character):
    def __init__(self, name, hp, can_disintegrate):
        attacks = [AttackAcid()]
        if can_disintegrate:
            attacks.append(AttackDisintegrate())
        Character.__init__(self, name, hp, attacks)


class Attack:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __str__(self):
        return '{} ({} dmg)'.format(self.name, self.damage)

    def perform(self, source, target):
        target.hp = min(max(0, target.hp - self.damage), target.hp_max)
        print '{} used {} on {}'.format(source.name, self, target)


class AttackAcid(Attack):
    def __init__(self):
        Attack.__init__(self, 'Acid', 2)

    def perform(self, source, target):
        Attack.perform(self, source, target)
        self.damage += 1


class AttackHeal(Attack):
    def __init__(self):
        Attack.__init__(self, 'Heal', -8)

    def __str__(self):
        return '{} ({} healing)'.format(self.name, -self.damage)


class AttackDisintegrate(Attack):
    def __init__(self):
        Attack.__init__(self, 'Disintegrate', 9)

    def perform(self, source, target):
        Attack.perform(self, source, target)
        Attack.perform(self, source, source)


#==================================================================
player = Character('Hiro', 20, [Attack('Slash', 4), AttackHeal()])
monsters = {}

monsters['slimea'] = CharSlime('SlimeA', 5, False)
monsters['slimeb'] = CharSlime('SlimeB', 5, True)

while player.hp > 0 and len(monsters) > 0:
    # player attacks a monster
    print 'Your attacks: {}'.format(sorted(player.attacks.keys()))
    print 'Remaining monsters: {}'.format(sorted(monsters.keys()))
    atk_name = ''
    monster_name = ''
    while atk_name not in player.attacks.keys() or (monster_name not in monsters.keys() and monster_name != 'self'):
        atk_name, monster_name = raw_input('<attack> <<monster>|self>: ').split(' ')
    if monster_name == 'self':
        player.attack_something(player, atk_name)
    else:
        player.attack_something(monsters[monster_name], atk_name)

    # monsters attack player
    for monster in monsters.values():
        monster.attack_something(player)

    # clean up dead monsters
    dead_monsters = []
    for key, monster in monsters.iteritems():
        if monster.hp <= 0:
            dead_monsters.append(key)
    for key in dead_monsters:
        del monsters[key]

if player.hp <= 0:
    print 'You have died.'
else:
    print 'Cleared!'

