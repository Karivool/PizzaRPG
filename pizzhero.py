import random
import os
import pizzitems
import pizzspells


class Protagonist(object):
    def __init__(self, name, sex, gender, he, his, him,
                 hp, hp_max, mp, mp_max,
                 pwr, mag, skl, spd, lck,
                 blck, res,
                 gold, exp, exp_ttl, lvl, items,
                 weapon, head, body, legs, accs,
                 hp_ttl, mp_ttl, atk_ttl, mag_ttl,
                 skl_ttl, spd_ttl, lck_ttl, def_ttl,
                 res_ttl,
                 is_alive, location, in_battle, bad_key,
                 mbti, spells, inv, saved):
        self.name = name
        self.sex = sex
        self.gender = gender
        self.he = he
        self.his = his
        self.him = him
        self.hp = hp
        self.hp_max = hp_max
        self.mp = mp
        self.mp_max = mp_max
        self.pwr = pwr
        self.mag = mag
        self.skl = skl
        self.spd = spd
        self.lck = lck
        self.blck = blck
        self.res = res
        self.gold = gold
        self.exp = exp
        self.exp_ttl = exp_ttl
        self.lvl = lvl
        self.items = items
        self.weapon = weapon
        self.head = head
        self.body = body
        self.legs = legs
        self.accs = accs
        self.hp_ttl = hp_ttl
        self.mp_ttl = mp_ttl
        self.atk_ttl = atk_ttl
        self.mag_ttl = mag_ttl
        self.skl_ttl = skl_ttl
        self.spd_ttl = spd_ttl
        self.lck_ttl = lck_ttl
        self.def_ttl = def_ttl
        self.res_ttl = res_ttl
        self.is_alive = is_alive
        self.location = location
        self.in_battle = in_battle
        self.bad_key = bad_key
        self.mbti = mbti
        self.spells = spells
        self.inv = inv
        self.saved = saved

    def inventory_menu(self, menuing):
        print "%s's Items" % self.name
        print " "
        if menuing:
            print "(1) %s%s  . (2) %s%s  . (3) %s%s" % (self.inv[0], (self.inv[0].leng * " "),
                                                        self.inv[1], (self.inv[1].leng * " "),
                                                        self.inv[2], (self.inv[2].leng * " "))
            print "(4) %s%s  . (5) %s%s  . (6) %s%s" % (self.inv[3], (self.inv[3].leng * " "),
                                                        self.inv[4], (self.inv[4].leng * " "),
                                                        self.inv[5], (self.inv[5].leng * " "))
            print "(7) %s%s  . (8) %s%s  . (9) %s%s" % (self.inv[6], (self.inv[6].leng * " "),
                                                        self.inv[7], (self.inv[7].leng * " "),
                                                        self.inv[8], (self.inv[8].leng * " "))
            print "(10) %s%s . (11) %s%s . (12) %s%s" % (self.inv[9], (self.inv[9].leng * " "),
                                                         self.inv[10], (self.inv[10].leng * " "),
                                                         self.inv[11], (self.inv[11].leng * " "))
            print "(13) %s%s . (14) %s%s . (15) %s%s" % (self.inv[12], (self.inv[12].leng * " "),
                                                         self.inv[13], (self.inv[13].leng * " "),
                                                         self.inv[14], (self.inv[14].leng * " "))
            print "(16) %s%s" % (self.inv[15], (self.inv[15].leng * " "))

            print "(B) Back"
        else:
            print "%s%s . %s%s . %s%s" % (self.inv[0], (self.inv[0].leng * " "),
                                          self.inv[1], (self.inv[1].leng * " "),
                                          self.inv[2], (self.inv[2].leng * " "))
            print "%s%s . %s%s . %s%s" % (self.inv[3], (self.inv[3].leng * " "),
                                          self.inv[4], (self.inv[4].leng * " "),
                                          self.inv[5], (self.inv[5].leng * " "))
            print "%s%s . %s%s . %s%s" % (self.inv[6], (self.inv[6].leng * " "),
                                          self.inv[7], (self.inv[7].leng * " "),
                                          self.inv[8], (self.inv[8].leng * " "))
            print "%s%s . %s%s . %s%s" % (self.inv[9], (self.inv[9].leng * " "),
                                          self.inv[10], (self.inv[10].leng * " "),
                                          self.inv[11], (self.inv[11].leng * " "))
            print "%s%s . %s%s . %s%s" % (self.inv[12], (self.inv[12].leng * " "),
                                          self.inv[13], (self.inv[13].leng * " "),
                                          self.inv[14], (self.inv[14].leng * " "))
            print "%s%s" % (self.inv[15], (self.inv[15].leng * " "))

    def spell_menu(self):
        print "%s's Spells" % self.name
        print "%s / %s MP" % (self.mp, self.mp_ttl)
        print " "
        print "(1) %s %s . (2) %s %s . (3) %s %s" % (self.spells[0], self.spells[0].mp_str,
                                                     self.spells[1], self.spells[1].mp_str,
                                                     self.spells[2], self.spells[2].mp_str)
        print "(4) %s %s . (5) %s %s . (6) %s %s" % (self.spells[3], self.spells[3].mp_str,
                                                     self.spells[4], self.spells[4].mp_str,
                                                     self.spells[5], self.spells[5].mp_str)
        print "(7) %s %s . (8) %s %s . (9) %s %s" % (self.spells[6], self.spells[6].mp_str,
                                                     self.spells[7], self.spells[7].mp_str,
                                                     self.spells[8], self.spells[8].mp_str,)
        print "(10) %s %s. (11) %s %s. (12) %s %s" % (self.spells[9], self.spells[9].mp_str,
                                                      self.spells[10], self.spells[10].mp_str,
                                                      self.spells[11], self.spells[11].mp_str,)
        print "(B) Back"

    def item_use(self, in_batt):
        command = 0
        item_list = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "b", 1)
        while command not in item_list:
            os.system('cls')
            self.inventory_menu(menuing=True)
            print "Use which item?"
            if self.bad_key:
                print "That's not an item!"
            print " "
            command = raw_input()
            if command in item_list:
                self.bad_key = False
                if command == "b":
                    command = 1
                else:
                    if self.inv[int(command) - 1] == "Empty":
                        print "There's nothing in that slot!"
                    else:
                        delete_item = self.inv[int(command) - 1].use_item(self)
                        if delete_item:
                            self.inv[int(command) - 1] = pizzitems.item_empty
                            if in_batt:
                                return True
                    raw_input()
                    command = 0
            else:
                self.bad_key = True
        return

    def inventory_sys(self, in_batt):
        command = 0
        comm_list = ("1", "2", "b")
        item_list = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "b", 1)
        while command not in comm_list:
            os.system('cls')
            menuing = False
            self.inventory_menu(menuing)
            print " "
            print "(1) Use   (2) Discard"
            print "(B) Return"
            if self.bad_key:
                print "Invalid command!"
            command = raw_input()
            if command in comm_list:
                self.bad_key = False
                menuing = True
            if command == "1":
                used_item = self.item_use(in_batt)
                if in_batt and used_item:
                    return True
            elif command == "2":
                command = 0
                while command not in item_list:
                    os.system('cls')
                    self.inventory_menu(menuing)
                    print "Discard which item?"
                    if self.bad_key:
                        print "That's not an item!"
                    print " "
                    command = raw_input()
                    if command in item_list:
                        self.bad_key = False
                        if command == "b":
                            command = 1
                        else:
                            if self.inv[int(command) - 1] == "Empty":
                                print "There's nothing to discard in that slot!"
                            else:
                                print "%s discarded." % self.inv[int(command) - 1]
                                self.inv[(int(command) - 1)] = "Empty"
                            raw_input()
                            command = 0
                    else:
                        self.bad_key = True
            elif command == "b":
                return False
            else:
                self.bad_key = True

    def str_atk(self, enemy1, enemy2, enemy3, enemy_target):
        damage = 0
        hero_atk = self.atk_ttl * random.uniform(.85, 1.3)
        if enemy_target == "1":
            damage = hero_atk - (enemy1.blck_ttl * random.uniform(.7, 1.1))
        if enemy_target == "2":
            damage = hero_atk - (enemy2.blck_ttl * random.uniform(.7, 1.1))
        if enemy_target == "3":
            damage = hero_atk - (enemy3.blck_ttl * random.uniform(.7, 1.1))
        if damage < 0:
            damage = 0
        return damage

    def spell(self):
        command = 0
        choices = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12")
        while command not in choices:
            os.system('cls')
            self.spell_menu()
            if self.bad_key:
                "That's no spell I ever heard!"
            print " "
            command = raw_input().lower()
            if command in choices:
                if self.spells[int(command) - 1] == pizzspells.sp_empty:
                    command = 0
                    print "Your mind draws a blank on that 'spell' choice!"
                    raw_input()
                else:
                    self.bad_key = False
                    spell_cost = self.spells[int(command) - 1].mp_cost
                    if spell_cost <= self.mp:
                        self.mp -= spell_cost
                        command = self.spells[int(command) - 1].id_num
                        return command
                    else:
                        print "You don't have enough MP to cast that spell!"
                        raw_input()
                        command = 0
            elif command == "b":
                return "Cancelled"
            else:
                self.bad_key = True

    def atk_spd(self):
        return (self.spd_ttl * 2) * random.uniform(.7, 1.25)

    def atk_aim(self):
        return ((self.skl_ttl * 2) + self.spd_ttl + (self.lck_ttl * .5)) * random.uniform(.8, 1.3)

    def atk_dodge(self):
        return ((self.skl_ttl * .5) + (self.spd_ttl * 2) + (self.lck_ttl * .25)) * random.uniform(.7, 1.1)

    def crit_chance(self):
        return ((self.skl_ttl * .2) + (self.lck_ttl * .2)) * random.uniform(.3, 1)

    def level_up(self):
        start_lvl = self.lvl
        hp_add_ttl = 0
        mp_add_ttl = 0
        pwr_add_ttl = 0
        mag_add_ttl = 0
        skl_add_ttl = 0
        spd_add_ttl = 0
        lck_add_ttl = 0
        blck_add_ttl = 0
        res_add_ttl = 0
        while self.exp >= self.exp_ttl:
            self.lvl += 1
            self.exp_ttl = int(((self.lvl + 1) * (self.lvl * self.lvl) * 1.5 * 3.6))
            hp_add = int((self.hp_max + 1.9) * 1.08) - self.hp_max
            hp_add_ttl += hp_add
            self.hp_max += hp_add
            mp_add = int((self.mp_max + 1.7) * 1.04) - self.mp_max
            self.mp_max += mp_add
            mp_add_ttl += mp_add
            pwr_add = int((self.pwr + 1.2) * 1.05) - self.pwr
            self.pwr += pwr_add
            pwr_add_ttl += pwr_add
            mag_add = int((self.mag + 1.1) * 1.06) - self.mag
            self.mag += mag_add
            mag_add_ttl += mag_add
            skl_add = int((self.skl + 1.14) * 1.06) - self.skl
            self.skl += skl_add
            skl_add_ttl += skl_add
            spd_add = int((self.spd + 1.15) * 1.05) - self.spd
            self.spd += spd_add
            spd_add_ttl += spd_add
            lck_add = int((self.lck + 1.03) * 1.03) - self.lck
            self.lck += lck_add
            lck_add_ttl += lck_add
            blck_add = int((self.blck + 1.25) * 1.04) - self.blck
            self.blck += blck_add
            blck_add_ttl += blck_add
            res_add = int((self.res + 1.25) * 1.04) - self.res
            self.res += res_add
            res_add_ttl += res_add
            if self.lvl == 2:
                print "%s learned Cure Weak!" % self.name
                self.spells[3] = pizzspells.sp_cure_one
                raw_input()
            if self.lvl == 5:
                print "%s learned Magic Blast!" % self.name
                self.spells[1] = pizzspells.sp_magic_blast
                raw_input()
            if self.lvl == 9:
                print "%s learned Cure Mid!" % self.name
                self.spells[4] = pizzspells.sp_cure_two
                raw_input()
            if self.lvl == 12:
                print "%s learned Magic Crush!" % self.name
                self.spells[2] = pizzspells.sp_magic_crush
                raw_input()
            if self.lvl == 15:
                print "%s learned Cure High!" % self.name
                self.spells[5] = pizzspells.sp_cure_three
                raw_input()
        if start_lvl != self.lvl:
            print "You leveled up from Level %s to Level %s!" % (start_lvl, self.lvl)
            print " "
            print "HP + %s" % hp_add_ttl
            print "MP + %s" % mp_add_ttl
            print "Str + %s" % pwr_add_ttl
            print "Mag + %s" % mag_add_ttl
            print "Skl + %s" % skl_add_ttl
            print "Spd + %s" % spd_add_ttl
            print "Lck + %s" % lck_add_ttl
            print "Def + %s" % blck_add_ttl
            print "Res + %s" % res_add_ttl
            raw_input()
            self.stats_total()
        return

    def stats_total(self):
        self.hp_ttl = self.hp_max + self.weapon.hp_max + self.head.hp_max + self.body.hp_max + self.legs.hp_max + \
                      self.accs.hp_max
        self.mp_ttl = self.mp_max + self.weapon.mp_max + self.head.mp_max + self.body.mp_max + self.legs.mp_max + \
                      self.accs.mp_max
        self.atk_ttl = self.pwr + self.weapon.pwr + self.head.pwr + self.body.pwr + self.legs.pwr + self.accs.pwr
        self.mag_ttl = self.mag + self.weapon.mag + self.head.mag + self.body.mag + self.legs.mag + self.accs.mag
        self.skl_ttl = self.skl + self.weapon.skl + self.head.skl + self.body.skl + self.legs.skl + self.accs.skl
        self.spd_ttl = self.spd + self.weapon.spd + self.head.spd + self.body.spd + self.legs.spd + self.accs.spd
        self.lck_ttl = self.lck + self.weapon.lck + self.head.lck + self.body.lck + self.legs.lck + self.accs.lck
        self.def_ttl = self.blck + self.weapon.blck + self.head.blck + self.body.blck + self.legs.blck + self.accs.blck
        self.res_ttl = self.res + self.weapon.res + self.head.res + self.body.res + self.legs.res + self.accs.res
        return


# hp, mp, str, mag, skl, spd, lck, def, res


def mbti_stats(hero):
    typed_choice = "invalid"
    infj = (0, 20, 0, 15, 10, 0, 2, 6, 0)
    intj = (15, 5, 5, 4, 17, 1, 0, 2, 4)
    infp = (12, 8, 1, 9, 5, 5, 0, 13, 0)
    intp = (11, 9, 4, 5, 6, 12, 1, 1, 4)
    isfj = (13, 7, 6, 5, 9, 0, 0, 12, 1)
    istj = (9, 11, 12, 1, 12, 0, 1, 2, 5)
    isfp = (14, 6, 12, 4, 5, 6, 0, 6, 0)
    istp = (6, 14, 7, 0, 6, 5, 1, 2, 12)
    enfj = (4, 16, 1, 7, 5, 1, 12, 5, 2)
    entj = (3, 17, 5, 12, 6, 0, 4, 1, 5)
    enfp = (2, 18, 1, 14, 0, 6, 5, 5, 2)
    entp = (1, 19, 5, 4, 2, 3, 6, 0, 13)
    esfj = (16, 4, 6, 2, 5, 0, 13, 5, 2)
    estj = (17, 3, 7, 0, 7, 1, 5, 0, 13)
    esfp = (18, 2, 5, 3, 0, 13, 5, 5, 2)
    estp = (20, 0, 15, 0, 1, 6, 5, 0, 6)
    iass = (1, 1, 0, 0, 0, 0, 0, 0, 0)
    mbti = {"infj": infj, "intj": intj, "infp": infp, "intp": intp,
            "isfj": isfj, "istj": istj, "isfp": isfp, "istp": istp,
            "enfj": enfj, "entj": entj, "enfp": enfp, "entp": entp,
            "esfj": esfj, "estj": estj, "esfp": esfp, "estp": estp, }
    raw_input()
    while typed_choice == "invalid":
        choice = 0
        answer = 0
        answer_choices = ("yes", "y", "no", "n")
        os.system('cls')
        print "Now %s, we need you to tell us your Myers Briggs personality type." % hero.name
        print "If you don't know your personality type, that's okay, you can guess or have one"
        print "randomly assigned to you by typing 'random'."
        print " "
        print "(I)ntrovert vs (E)xtrovert"
        print "i(N)tuition vs (S)ensing"
        print "(F)eeling vs (T)hinking"
        print "(J)udging vs (P)erceiving"
        print "Enter a four letter personality type combination (eg. INTJ):"
        typed_choice = raw_input().lower()
        if typed_choice != "random":
            try:
                choice = mbti[typed_choice]
            except KeyError:
                typed_choice = "invalid"
        if typed_choice == "invalid":
            while answer not in answer_choices:
                print " "
                os.system('cls')
                print "Hey, that's not a valid personality type! It has to be a combination like"
                print "'ESTP' or 'INFP'."
                print "Or is it that you don't want to put in a personality type? (Y) or (N)"
                print " "
                if hero.bad_key:
                    print "Sorry, that's not a valid answer."
                answer = raw_input().lower()
                if answer in answer_choices:
                    hero.bad_key = False
                if answer == "yes" or answer == "y":
                    answer = 0
                    while answer not in answer_choices:
                        print " "
                        os.system('cls')
                        print "Oh come on, it's just for fun!"
                        print "Don't you want to be cool and put in your type? :) (Y) or (N)"
                        print " "
                        if hero.bad_key:
                            print "That's not yes or no!"
                        answer = raw_input().lower()
                        if answer in answer_choices:
                            hero.bad_key = False
                        if answer == "yes" or answer == "y":
                            print "Good! Let's get with it then."
                            typed_choice = "invalid"
                            raw_input()
                        elif answer == "no" or answer == "n":
                            print "Oh fine, is that how you want to be? Fine! You can get a special"
                            print "personality type: IASS: I'm A Spoil Sport. "
                            print " "
                            print "I hope you're happy now, %s. Oh look, IASS even works as I ASS." % hero.name
                            print "So fitting for you."
                            print " "
                            print "No, I'm not salty that you didn't go along, why do you ask?"
                            typed_choice = "IASS"
                            raw_input()
                            choice = iass
                            hero.hp_max += 1
                            hero.mp_max += 1
                        else:
                            hero.bad_key = True
                elif answer == "no" or answer == "n":
                    print "Oh, okay! Let's try this again then."
                    typed_choice = "invalid"
                    raw_input()
                else:
                    hero.bad_key = True
        if typed_choice == "random":
            typed_choice = random.choice(mbti.keys())
            choice = mbti[typed_choice]
        if typed_choice in mbti.keys() or choice == iass:
            hero.hp += choice[0]
            hero.hp_max = hero.hp
            hero.mp += choice[1]
            hero.mp_max = hero.mp
            hero.pwr += choice[2]
            hero.mag += choice[3]
            hero.skl += choice[4]
            hero.spd += choice[5]
            hero.lck += choice[6]
            hero.blck += choice[7]
            hero.res += choice[8]
            hero.mbti = typed_choice.upper()
            return
