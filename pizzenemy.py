import random


class Enemy(object):
    def __init__(self, name, hp, hp_ttl, mp, mp_ttl, pwr_ttl, mag_ttl, skl_ttl, spd_ttl, lck_ttl, blck_ttl, res_ttl,
                 gold, exp, used):
        self.name = name
        self.hp = hp
        self.hp_ttl = hp_ttl
        self.mp = mp
        self.mp_ttl = mp_ttl
        self.pwr_ttl = pwr_ttl
        self.mag_ttl = mag_ttl
        self.skl_ttl = skl_ttl
        self.spd_ttl = spd_ttl
        self.lck_ttl = lck_ttl
        self.blck_ttl = blck_ttl
        self.res_ttl = res_ttl
        self.gold = gold
        self.exp = exp
        self.used = used

    def attack(self):
        return self.pwr_ttl * random.uniform(.8, 1.2)

    def magic_atk(self):
        return self.mag_ttl * random.uniform(.8, 1.2)

    def atk_spd(self):
        return (self.spd_ttl * 2) * random.uniform(.65, 1.15)

    def atk_aim(self):
        return ((self.skl_ttl * 2) + self.spd_ttl + (self.lck_ttl * .5)) * random.uniform(.7, 1.2)

    def atk_dodge(self):
        return ((self.skl_ttl * .5) + (self.spd_ttl * 2) + (self.lck_ttl * .25)) * random.uniform(.6, 1.1)

    def crit_chance(self):
        return ((self.skl_ttl * .2) + (self.lck_ttl * .2)) * random.uniform(.3, 1)


# foe_enemy_name (             Name                  HP        MP    St  Mg Sk  Spd Lck De  Re  Go  EXP
foe_choco_boar = Enemy("Choco Boar",                 40,  40,  0, 0, 26, 0, 8,  16, 7,  9,  2,  7,  19,  True)
foe_dice_gumbler = Enemy("Dice Gumbler",             30,  30,  0, 0, 17, 0, 16, 11, 14, 7,  5,  16, 17,  True)
foe_candied_canemra = Enemy("Candied Canemra",       25,  25,  0, 0, 19, 0, 11, 7,  6,  4,  6,  6,  14,  True)
foe_marshy_bug = Enemy("Marshy Bug",                 15,  15,  0, 0, 14, 0, 5,  20, 3,  2,  1,  4,  11,  True)
foe_twinkie_star = Enemy("Twinkie Big Star Candy",   99,  99,  0, 0, 36, 0, 26, 10, 5,  12, 9,  35, 56,  True)
foe_boulder_den_heifer = Enemy("Boulder Den Heifer", 85,  85,  0, 0, 58, 0, 20, 14, 12, 27, 21, 13, 39,  True)
foe_earthly_moleling = Enemy("Earthly Moleling",     52,  52,  0, 0, 44, 0, 23, 16, 14, 15, 9,  11, 28,  True)
foe_intercom_bat = Enemy("Intercom Bat",             46,  46,  0, 0, 42, 0, 22, 18, 13, 14, 13, 12, 27,  True)
foe_eagle_two_please = Enemy("Eagle Two Please",     77,  77,  0, 0, 51, 0, 25, 24, 17, 19, 16, 14, 43,  True)
foe_cave_drweller = Enemy("Cave Digging Drweller",   220, 220, 0, 0, 72, 0, 40, 9,  9,  36, 27, 80, 98,  True)
foe_mr_fedorable = Enemy("Mister Fedorable",         124, 124, 0, 0, 64, 0, 46, 15, 25, 33, 37, 24, 56,  True)
foe_nacho_knife = Enemy("Nacho Knife Guy",           90,  90,  0, 0, 69, 0, 51, 49, 5,  19, 15, 35, 64,  True)
foe_sir_nick = Enemy("Sir Nick Bird",                149, 149, 0, 0, 68, 0, 40, 12, 30, 42, 43, 27, 68,  True)
foe_sam_of_rye = Enemy("Sam Of Rye",                 133, 133, 0, 0, 74, 0, 64, 30, 22, 37, 49, 21, 84,  True)
foe_trilbyous_pursuit = Enemy("Trilbyous Pursuit",   394, 394, 0, 0, 99, 0, 69, 20, 45, 50, 69, 90, 180, True)

# ("", hp, hp_max, mp, mp_max, pwr, mag, skl, spd, lck, blck, res, gold, exp, True)


enemy_list = {0: {0: foe_choco_boar, 1: foe_dice_gumbler, 2: foe_candied_canemra, 3: foe_marshy_bug},
              1: {0: foe_boulder_den_heifer, 1: foe_earthly_moleling, 2: foe_intercom_bat, 3: foe_eagle_two_please},
              2: {0: foe_mr_fedorable, 1: foe_nacho_knife, 2: foe_sir_nick, 3: foe_sam_of_rye}}

# 0: uncandy_valley, 1: molehill_mountain, 2: tipping_complex
