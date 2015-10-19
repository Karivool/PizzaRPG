import random


class Spells(object):
    def __init__(self, id_num, name, mp_cost, base_damage, healing, mp_str):
        self.id_num = id_num
        self.name = name
        self.mp_cost = mp_cost
        self.base_damage = base_damage
        self.healing = healing
        self.mp_str = mp_str

    def __str__(self):
        return "%s" % self.name

    def mag_one(self, stats, stats2):
        return (self.base_damage + stats.mag_ttl * random.uniform(.7, 1.1)) - \
               (stats2.res_ttl * random.uniform(.95, 1.3))

    def mag_two(self, stats, stats2):
        return (self.base_damage + stats.mag_ttl * random.uniform(.85, 1.50)) - \
               (stats2.res_ttl * random.uniform(.8, 1.2))

    def mag_three(self, stats, stats2):
        return (self.base_damage + stats.mag_ttl * random.uniform(.9, 2.25)) - \
               (stats2.res_ttl * random.uniform(.7, 1.1))

    def cure_one(self, stats, stats2):
        return self.base_damage + stats.mag_ttl * .5 * random.uniform(.7, 1.25) + stats2

    def cure_two(self, stats, stats2):
        return self.base_damage + stats.mag_ttl * .75 * random.uniform(.8, 1.7) + stats2

    def cure_three(self, stats, stats2):
        return self.base_damage + stats.mag_ttl * .95 * random.uniform(.9, 2.1) + stats2


def spell_effects(hero, enemy1, enemy2, enemy3, attacker, enemy_target, sp_choice):
    if attacker == "hero":
        stats = hero
        if enemy_target == "1":
            stats2 = enemy1
        elif enemy_target == "2":
            stats2 = enemy2
        elif enemy_target == "3":
            stats2 = enemy3
        else:
            stats2 = 0
    elif attacker == "enemy1":
        stats = enemy1
        stats2 = hero
    elif attacker == "enemy2":
        stats = enemy2
        stats2 = hero
    else:
        stats = enemy3
        stats2 = hero
    damage = spell_atk[sp_choice](stats, stats2)
    if damage < 0 and not hero.spells[sp_choice].healing:
            damage = 0
    return damage


sp_empty = Spells(0, "           ", 0, 0, False, "       ")
sp_magic_shot = Spells(1, "Magic Shot ", 3, 25, False, "3 MP   ")
sp_magic_blast = Spells(2, "Magic Blast", 9, 65, False, "9 MP  ")
sp_magic_crush = Spells(3, "Magic Crush", 17, 150, False, "17 MP  ")
sp_cure_one = Spells(4, "Cure Weak  ", 3, 15, True, "3 MP   ")
sp_cure_two = Spells(5, "Cure Mid   ", 9, 50, True, "9 MP   ")
sp_cure_three = Spells(6, "Cure High  ", 18, 120, True, "18 MP  ")

spell_list = {0: sp_empty, 1: sp_magic_shot, 2: sp_magic_blast, 3: sp_magic_crush,
              4: sp_cure_one, 5: sp_cure_two, 6: sp_cure_three}

spell_atk = {0: sp_empty, 1: sp_magic_shot.mag_one, 2: sp_magic_blast.mag_two,
             3: sp_magic_crush.mag_three, 4: sp_cure_one.cure_one, 5: sp_cure_two.cure_two,
             6: sp_cure_three.cure_three}
