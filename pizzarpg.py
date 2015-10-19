import os
import pizzhero
import pizztown
import pizzitems
import pizzspells
import pizzdungeon

__author__ = 'Evelyn Lee'


def has_num(name):
    return any(char.isdigit() for char in name)


def intro(hero):
    hero_sex = "blank"
    hero_gen = "blank"
    hero_he = "blank"
    hero_his = "blank"
    hero_him = "blank"
    hero.bad_key = False
    game_loaded = False
    comm_key = 0
    while comm_key not in ("n", "l", "q"):
        os.system('cls')
        print "\n"
        print "Welcome to Pizza Lady's RPG!"
        print " " * 2
        print "Choose an option:"
        print " "
        print "(N) New Game"
        print "(L) Load Game"
        print "(Q) Quit Game"
        print " "
        if hero.bad_key:
            print "Umm, that's not going to get this game started!!"
        comm_key = raw_input().lower()
        if comm_key in ("n", "l", "q"):
            hero.bad_key = False
        if comm_key == "n":
            pass
        elif comm_key == "l":
            load_success = pizztown.load_game(hero)
            if load_success:
                game_loaded = True
            else:
                comm_key = 0
        elif comm_key == "q":
            exit()
        else:
            hero.bad_key = True
    while not game_loaded:
        os.system('cls')
        print "Enter your hero's name:"
        hero.name = raw_input()
        while len(hero.name) > 12 or len(hero.name) == 0:
            os.system('cls')
            print " "
            if len(hero.name) == 0:
                print "Uh... everyone has a name, friend. If you don't have one,"
                print "just come up with one, geez..."
            else:
                print "Whoa whoa, we're kinda short with people who have names THAT long."
                print "I suggest you give your name a trim... if you want to play."
            print "Enter your hero's name:"
            hero.name = raw_input()
        print " "
        print "Ah, I see, your name is", hero.name + "!"
        if has_num(hero.name):
            print "What kind of weirdo has numbers in their name though? Lma0."
        raw_input()
        while hero_sex not in ("male", "female", "pizza", "Bungh0"):
            os.system('cls')
            print "Now", hero.name + ", we need to know your sex."
            print "Do you consider yourself male, female, or pizza?"
            hero_sex = raw_input().lower()
            print " "
            if hero_sex in ("male", "man", "m", "dude", "d00d", "guy", "bro", "brah"):
                if hero_sex in ("bro", "brah"):
                    print "Okay, BRO, you're a man who is into his BRO identity, okay."
                else:
                    print "I see, you consider yourself a man!"
                hero_sex = "male"
                hero_gen = "man"
                hero_he = "he"
                hero_his = "his"
                hero_him = "him"
            elif hero_sex in ("female", "woman", "f", "dudette", "d00dette", "girl", "gal", "lady", "chick"):
                if hero_sex == "chick":
                    print "Uhh... what woman identifies her sex as a CHICK? Seriously? Okay... whatever."
                else:
                    print "I see, you consider yourself a woman!"
                hero_sex = "female"
                hero_gen = "woman"
                hero_he = "she"
                hero_his = "her"
                hero_him = "her"
            elif hero_sex == "pizza":
                print "Ahh, you're a pizza! It's rare to see your kind uneaten."
                hero_sex = "pizza"
                hero_gen = "pizza"
                hero_he = "pie"
                hero_his = "pies"
                hero_him = "pizz"
            elif hero_sex == "bungh0":
                print "I see, y0u're a Bungh0. Th0se are a very rare type 0f male. Pleased to meet y0u."
                hero_sex = "Bungh0"
                hero_gen = "Bungh0"
                hero_he = "bun"
                hero_his = "bung"
                hero_him = "bungh"
            else:
                print "Dear me, I'm sorry, but we've never heard of", hero_sex + "!"
                print "I apologize, but please try again."
                raw_input()
        hero = pizzhero.Protagonist(hero.name, hero_sex, hero_gen, hero_he, hero_his, hero_him,
                                    95, 95, 16, 16, 5, 5, 6, 6, 4, 3, 3, 120, 0,
                                    int((2 * 1.5 * 3.6)),
                                    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                    True, "town", False, False, "",
                                    {0: pizzspells.sp_magic_shot, 1: pizzspells.sp_empty, 2: pizzspells.sp_empty,
                                     3: pizzspells.sp_empty, 4: pizzspells.sp_empty, 5: pizzspells.sp_empty,
                                     6: pizzspells.sp_empty, 7: pizzspells.sp_empty, 8: pizzspells.sp_empty,
                                     9: pizzspells.sp_empty, 10: pizzspells.sp_empty, 11: pizzspells.sp_empty},
                                    {0: pizzitems.item_empty, 1: pizzitems.item_empty, 2: pizzitems.item_empty,
                                     3: pizzitems.item_empty, 4: pizzitems.item_empty, 5: pizzitems.item_empty,
                                     6: pizzitems.item_empty, 7: pizzitems.item_empty, 8: pizzitems.item_empty,
                                     9: pizzitems.item_empty, 10: pizzitems.item_empty, 11: pizzitems.item_empty,
                                     12: pizzitems.item_empty, 13: pizzitems.item_empty, 14: pizzitems.item_empty,
                                     15: pizzitems.item_empty},
                                    False)
        pizzhero.mbti_stats(hero)
        if hero.name == "Pizza Lady" and hero.sex == "pizza" and hero.mbti == "INFJ":
            hero.weapon = pizzitems.we_st_heart
            hero.head = pizzitems.ar_chef_sh
            hero.body = pizzitems.ar_chef_to
            hero.legs = pizzitems.ar_chef_ap
            hero.accs = pizzitems.ar_hrt_nck
        elif hero.name == "Bungh0" and hero.sex == "Bungh0" and hero.mbti == "ISFJ":
            hero.weapon = pizzitems.we_fk_sword
            hero.head = pizzitems.ar_fedora
            hero.body = pizzitems.ar_trench
            hero.legs = pizzitems.ar_pants
            hero.accs = pizzitems.ar_bu_char
        elif hero.name == "Lulu" and hero.sex == "female" and hero.mbti == "INFP":
            hero.weapon = pizzitems.we_ir_sword
            hero.head = pizzitems.ar_hat
            hero.body = pizzitems.ar_sun_fun
            hero.legs = pizzitems.ar_broo_sh
            hero.accs = pizzitems.ar_pu_charm
        else:
            hero.weapon = pizzitems.we_stick
            hero.head = pizzitems.ar_none
            hero.body = pizzitems.ar_cloth
            hero.legs = pizzitems.ar_pants
            hero.accs = pizzitems.ar_none
        hero.stats_total()
        hero.hp = hero.hp_ttl
        hero.mp = hero.mp_ttl
        print "With that, we will begin,", hero_sex, hero.name + "."
        raw_input()
        os.system('cls')
        print " "
        print "You are a young", hero_gen + ", seeking", hero_his, "fortune after a disastrous run at your"
        print "village's local school."
        raw_input()
        if hero_sex == "pizza":
            print "Due to the fact that you were a pizza, you were treated as lesser due to your"
            print "low IQ, and constantly under the threat of being eaten."
            raw_input()
            print "As a result, you had no choice but to flee to find a place that wouldn't"
            print "discriminate against you, on account of having grain DNA."
        elif hero_sex == "Bungh0":
            print "You found yourself academically excelling over every one of your peers,"
            print "to the point none of them could keep you engaged in conversation with them."
            raw_input()
            print "The last straw was losing the contest for Best Village Banner. A f00l with"
            print "abysmal design sense won, and you quickly packed y0ur bags t0 leave."
        else:
            print "You did not excel, nor fall behind in your studies, but you had absolutely"
            print "no interest in your studies and wished for something grander."
            raw_input()
            print "One day, you bent over to pick your pencil up and ripped your jeans at the"
            print "seams, resulting in you using that as an excuse to flee the village."
        raw_input()
        print "You soon arrive at the town of Central Point, and decide here, you will"
        print "make something of yourself and be an adventurer."
        raw_input()
        print "Go forth,", hero.name + ", and discover what lies ahead!"
        raw_input()
        os.system('cls')
        return hero
    return hero


def main():
    hero = pizzhero.Protagonist("Error", "error", "error", "error", "error", "error",
                                1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, True, "none", False, False, "",
                                {0: pizzspells.sp_empty, 1: pizzspells.sp_empty, 2: pizzspells.sp_empty,
                                 3: pizzspells.sp_empty, 4: pizzspells.sp_empty, 5: pizzspells.sp_empty,
                                 6: pizzspells.sp_empty, 7: pizzspells.sp_empty, 8: pizzspells.sp_empty,
                                 9: pizzspells.sp_empty, 10: pizzspells.sp_empty, 11: pizzspells.sp_empty},
                                {0: pizzitems.item_empty, 1: pizzitems.item_empty, 2: pizzitems.item_empty,
                                 3: pizzitems.item_empty, 4: pizzitems.item_empty, 5: pizzitems.item_empty,
                                 6: pizzitems.item_empty, 7: pizzitems.item_empty, 8: pizzitems.item_empty,
                                 9: pizzitems.item_empty, 10: pizzitems.item_empty, 11: pizzitems.item_empty,
                                 12: pizzitems.item_empty, 13: pizzitems.item_empty, 14: pizzitems.item_empty,
                                 15: pizzitems.item_empty},
                                False)
    hero = intro(hero)
    while hero.is_alive:
        while hero.location == "town":
            pizztown.town(hero)
        while hero.location == "dungeon":
            pizzdungeon.dungeon(hero)
    print "Game over, you died!"
    print "R.I.P."


main()
