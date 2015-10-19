class Item(object):
    def __init__(self, idnum, name, leng, cost):
        self.idnum = idnum
        self.name = name
        self.leng = leng
        self.cost = cost

    def __str__(self):
        return "%s" % self.name


class Healing(Item):
    def __init__(self, idnum, name, leng, cost, heal, stat):
        super(Healing, self).__init__(idnum, name, leng, cost)
        self.heal = heal
        self.stat = stat

    def use_item(self, hero):
        if self.stat == "HP":
            hero.hp += self.heal
            if hero.hp > hero.hp_ttl:
                hero.hp = hero.hp_ttl
        elif self.stat == "MP":
            hero.mp += self.heal
            if hero.mp > hero.mp_ttl:
                hero.mp = hero.mp_ttl
        print "%s restores %s %s!" % (self.name, self.heal, self.stat)
        print " "
        return True


class Equip(Item):
    def __init__(self, idnum, name, leng, cost, hp_max, mp_max, pwr, mag, skl, spd, lck, blck, res,
                 wep, head, body, legs, accs):
        super(Equip, self).__init__(idnum, name, cost, leng)
        self.idnum = idnum
        self.name = name
        self.leng = leng
        self.cost = cost
        self.hp_max = hp_max
        self.mp_max = mp_max
        self.pwr = pwr
        self.mag = mag
        self.skl = skl
        self.spd = spd
        self.lck = lck
        self.blck = blck
        self.res = res
        self.wep = wep
        self.head = head
        self.body = body
        self.legs = legs
        self.accs = accs

    def use_item(self):
        if self.wep:
            print "This is a weapon, you have to wield it!"
        else:
            print "You need to equip this on yourself to use it!"
        return False


# Item (self, idnum,           name,              ln, cost, heal, stat):
item_empty = Item(0,           "Empty",           10, 0)
item_potion = Healing(1,       "Life Drink",      5,  10,  100,  "HP")
item_potion_plus = Healing(2,  "Life Drink +",    3,  100, 300,  "HP")
item_potion_max = Healing(3,   "Life Drink X",    3,  250, 1100, "HP")
item_elixir = Healing(32,      "Magic Gulp",      5,  20,  35,   "MP")
item_elixir_plus = Healing(33, "Magic Gulp +",    3,  150, 75,   "MP")
item_elixir_max = Healing(34,  "Magic Gulp X",    3,  300, 300,  "MP")


#                       Name               Ln Cost HP   MP  Atk Mag Skl Sd Lck Def Res Wep,  Head   Body   Legs   Accs
we_none = Equip(4,      "Nothing",         8, 0,   0,   0,  0,  0,  0,  0, 0,  0,  0,  True, False, False, False, False)
we_stick = Equip(5,     "Travel Stick",    3, 10,  0,   0,  4,  0,  0,  0, 0,  1,  0,  True, False, False, False, False)
we_frying = Equip(6,    "Frying Pan",      5, 120, 0,   0,  5,  0,  0,  0, 0,  5,  0,  True, False, False, False, False)
we_fk_sword = Equip(7,  "Fake Sword",      5, 4,   0,   0,  3,  0,  1,  2, 0,  0,  0,  True, False, False, False, False)
we_st_heart = Equip(8,  "Staff of Hearts", 0, 999, 100, 50, 25, 50, 30, 0, 25, 10, 25, True, False, False, False, False)
we_br_sword = Equip(9,  "Bronze Sword",    3, 75,  0,   0,  11, 0,  2,  0, 0,  1,  0,  True, False, False, False, False)
we_ir_sword = Equip(10, "Iron Sword",      5, 240, 0,   0,  19, 0,  4,  0, 0,  2,  0,  True, False, False, False, False)
we_st_sword = Equip(11, "Steel Sword",     4, 500, 0,   0,  28, 0,  8,  0, 0,  3,  0,  True, False, False, False, False)
we_br_axe = Equip(35,   "Bronze Axe",      5, 95,  0,   0,  14, 0,  0,  0, 0,  2,  0,  True, False, False, False, False)
we_ir_lance = Equip(36, "Iron Lance",      5, 280, 0,   0,  16, 0,  8,  0, 0,  0,  0,  True, False, False, False, False)
we_st_knife = Equip(37, "Steel Knife",     4, 450, 0,   0,  20, 0,  6,  4, 0,  0,  0,  True, False, False, False, False)


#                        Name              Ln Cost HP  MP  Atk Mag Skl Spd Lck Def Res Wep,   Head  Body  Legs  Accs
ar_none = Equip(12,     "Nothing",         8, 0,   0,  0,  0,  0,  0,  0,  0,  0,  0,  False, True, True, True, True)
ar_hat = Equip(13,      "Kool Kap",        7, 75,  20, 12, 2,  4,  4,  4,  4,  2,  4,  False, True, False, False, False)
ar_cloth = Equip(14,    "Travel Garb",     4, 15,  0,  0,  0,  0,  0,  0,  0,  1,  0,  False, False, True, False, False)
ar_pants = Equip(15,    "Rugged Pants",    3, 10,  0,  0,  0,  0,  0,  0,  0,  1,  0,  False, False, False, True, False)
ar_fedora = Equip(16,   "Fedora",          9, 2,   0,  0,  0,  0,  -5, 0,  -5, 2,  2,  False, True, False, False, False)
ar_chef_sh = Equip(17,  "Chef's Hat",      5, 200, 50, 20, 20, 20, 20, 20, 50, 0,  0,  False, True, False, False, False)
ar_chef_to = Equip(18,  "Chef's Top",      5, 100, 0,  0,  0,  0,  0,  0,  5,  45, 45, False, False, True, False, False)
ar_chef_ap = Equip(19,  "Chef's Apron",    3, 100, 0,  0,  0,  0,  0,  0,  5,  40, 40, False, False, False, True, False)
ar_br_helm = Equip(20,  "Bronze Helm",     4, 45,  0,  0,  0,  0,  0,  0,  0,  5,  0,  False, True, False, False, False)
ar_br_plate = Equip(21, "Bronze Plate",    3, 150, 0,  0,  0,  0,  0,  0,  0,  15, 2,  False, False, True, False, False)
ar_br_legs = Equip(22,  "Bronze Legs",     4, 110, 0,  0,  0,  0,  0,  0,  0,  10, 1,  False, False, False, True, False)
ar_pu_charm = Equip(23, "Purple Charm",    3, 500, 15, 10, 10, 5,  10, 5,  15, 5,  5,  False, False, False, False, True)
ar_sun_fun = Equip(24,  "Sunday Funday",   2, 300, 25, 35, 15, 20, 10, 10, 15, 5,  10, False, False, True, False, False)
ar_broo_sh = Equip(25,  "Brooklyn Shorts", 0, 200, 0,  0,  0,  0,  10, 35, 10, 5,  5,  False, False, False, True, False)
ar_trench = Equip(26,   "Trenchcoat",      5, 0,   0,  0,  0,  0,  0,  0,  2,  5,  5,  False, False, True, False, False)
ar_hrt_nck = Equip(27,  "Heart Necklace",  1, 500, 50, 20, 0,  5,  0,  0,  15, 0,  12, False, False, False, False, True)
ar_ir_helm = Equip(28,  "Iron Helm",       6, 125, 0,  0,  0,  0,  0,  0,  0,  9,  2,  False, True, False, False, False)
ar_ir_plate = Equip(29, "Iron Plate",      5, 280, 0,  0,  0,  0,  0,  0,  0,  21, 4,  False, False, True, False, False)
ar_ir_legs = Equip(30,  "Iron Legs",       6, 230, 0,  0,  0,  0,  0,  0,  0,  15, 2,  False, False, False, True, False)
ar_bu_char = Equip(31,  "Bungh0's Charm",  1, 400, 25, 0,  0,  20, 25, 0,  10, 0,  0,  False, False, False, False, True)
ar_st_helm = Equip(38,  "Steel Helm",      5, 310, 0,  0,  0,  0,  0,  0,  0,  13, 3,  False, True, False, False, False)
ar_st_plate = Equip(39, "Steel Plate",     4, 560, 0,  0,  0,  0,  0,  0,  0,  32, 6,  False, False, True, False, False)
ar_st_legs = Equip(40,  "Steel Legs",      5, 425, 0,  0,  0,  0,  0,  0,  0,  19, 3,  False, False, False, True, False)
ar_ma_hat = Equip(41,   "Magic Hat",       6, 250, 0,  10, 0,  2,  0,  0,  0,  1,  4,  False, True, False, False, False)
ar_ma_robe = Equip(42,  "Magic Robes",     4, 480, 10, 15, 0,  5,  0,  0,  0,  3,  15, False, False, True, False, False)
ar_ma_scale = Equip(43, "Magic Scales",    3, 460, 10, 10, 0,  0,  0,  0,  0,  10, 12, False, False, False, True, False)

# Armor (idnum, name, cost, hp_max, mp_max, pwr, mag, skl, spd, lck, blck, res, head, body, legs, accs)

item_buy_list = {0: item_potion, 1: item_potion_plus, 2: item_potion_max, 3: item_elixir, 4: item_elixir_plus,
                 5: item_elixir_max}

item_list = {0: item_empty, 1: item_potion, 2: item_potion_plus, 3: item_potion_max, 32: item_elixir,
             33: item_elixir_plus, 34: item_elixir_max}

weapon_buy_list = {0: we_br_sword, 1: we_br_axe, 2: we_ir_sword, 3: we_ir_lance, 4: we_st_sword, 5: we_st_knife}

weapon_list = {4: we_none, 5: we_stick, 6: we_frying, 7: we_fk_sword, 8: we_st_heart,
               9: we_br_sword, 10: we_ir_sword, 11: we_st_sword, 35: we_br_axe, 36: we_ir_lance, 37: we_st_knife}

armor_buy_list = {0: ar_br_helm, 1: ar_br_plate, 2: ar_br_legs, 3: ar_ir_helm, 4: ar_ir_plate,
                  5: ar_ir_legs, 6: ar_st_helm, 7: ar_st_plate, 8: ar_st_legs, 9: ar_ma_hat,
                  10: ar_ma_robe, 11: ar_ma_scale}

armor_list = {12: ar_none, 13: ar_hat, 14: ar_cloth, 15: ar_pants, 16: ar_fedora, 17: ar_chef_sh,
              18: ar_chef_to, 19: ar_chef_ap, 20: ar_br_helm, 21: ar_br_plate, 22: ar_br_legs,
              23: ar_pu_charm, 24: ar_sun_fun, 25: ar_broo_sh, 26: ar_trench, 27: ar_hrt_nck,
              28: ar_ir_helm, 29: ar_ir_plate, 30: ar_ir_legs, 31: ar_bu_char, 38: ar_st_helm,
              39: ar_st_plate, 40: ar_st_legs, 41: ar_ma_hat, 42: ar_ma_robe, 43: ar_ma_scale}

inv_list = {0: item_empty, 1: item_potion, 2: item_potion_plus, 3: item_potion_max, 4: we_none, 5: we_stick,
            6: we_frying, 7: we_fk_sword, 8: we_st_heart, 9: we_br_sword, 10: we_ir_sword, 11: we_st_sword,
            12: ar_none, 13: ar_hat, 14: ar_cloth, 15: ar_pants, 16: ar_fedora, 17: ar_chef_sh,
            18: ar_chef_to, 19: ar_chef_ap, 20: ar_br_helm, 21: ar_br_plate, 22: ar_br_legs,
            23: ar_pu_charm, 24: ar_sun_fun, 25: ar_broo_sh, 26: ar_trench, 27: ar_hrt_nck,
            28: ar_ir_helm, 29: ar_ir_plate, 30: ar_ir_legs, 31: ar_bu_char, 32: item_elixir,
            33: item_elixir_plus, 34: item_elixir_max, 35: we_br_axe, 36: we_ir_lance, 37: we_st_knife,
            38: ar_st_helm, 39: ar_st_plate, 40: ar_st_legs, 41: ar_ma_hat, 42: ar_ma_robe, 43: ar_ma_scale}
