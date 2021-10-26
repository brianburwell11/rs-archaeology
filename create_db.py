from db import *

# materials
if False:
    tutorial_materials = [(49444,'Imperial iron'), (49445,'Purpleheart wood')]
    agnostic_materials = [(49460,'Third Age iron'), (49456,'Samite silk'), (49464,'White oak'), (49450,'Goldrune'), (49454,'Orthenglass'),
                          (49462,'Vellum'), (49452,'Leather scraps'), (49446,'Animal furs'), (49448,'Fossilised bone'), (49458,'Soapstone')]
    armadylean_materials = [(49472,'Stormguard steel'), (49474,'Wings of War'), (49468,'Armadylean yellow'), (49466,'Aetherium alloy'), (49470,'Quintessence')]
    bandosian_materials = [(49476,'Malachite green'), (49478,'Mark of the Kyzaj'), (49480,'Vulcanised rubber'), (49482,'Warforged bronze'), (49484,"Yu'biusk clay")]
    dragonkin_materials = [(50688,'Compass rose'), (50692,'Felt'), (50690,'Dragon metal'), (50686,'Carbon black'), (50694,'Orgone')]
    saradominist_materials = [(49490,'Keramos'), (49494,'White marble'), (49486,'Cobalt blue'), (49488,'Everlight silvthril'), (49492,'Star of Saradomin')]
    zamorakian_materials = [(49498,'Chaotic brimstone'), (49500,'Demonhide'), (49502,'Eye of Dagon'), (49504,'Hellfire metal'), (49496,'Cadmium red')]
    zarosian_materials = [(37104,'Zarosian insignia'), (49510,'Imperial steel'), (49506,'Ancient vis'), (49512,'Tyrian purple'), (49508,'Blood of Orcus')]
    misc_materials = [(1607, 'Sapphire'), (1605, 'Emerald'), (1603, 'Ruby'), (1601, 'Diamond'), (1615, 'Dragonstone'), (8792, 'Clockwork'), (954, 'Rope'),
                      (4621, 'Phoenix feather'), (25487, 'Weapon poison (3)'), (4622, 'Black mushroom ink'), (1775, 'Molten glass'), (560, 'Death rune'),
                      (2349, 'Bronze bar'), (2355, 'Silver bar'), (36, 'White candle')]

    materials = [
            [Material(id=id, name=name, alignment='Agnostic') for id,name in tutorial_materials]
            + [Material(id=id, name=name, alignment='Agnostic') for id,name in agnostic_materials]
            + [Material(id=id, name=name, alignment='Armadylean') for id,name in armadylean_materials]
            + [Material(id=id, name=name, alignment='Bandosian') for id,name in bandosian_materials]
            + [Material(id=id, name=name, alignment='Dragonkin') for id,name in dragonkin_materials]
            + [Material(id=id, name=name, alignment='Saradominist') for id,name in saradominist_materials]
            + [Material(id=id, name=name, alignment='Zamorakian') for id,name in zamorakian_materials]
            + [Material(id=id, name=name, alignment='Zarosian') for id,name in zarosian_materials]
            + [Material(id=id, name=name, alignment='Agnostic') for id,name in misc_materials]
    ][0]

# collectors
if False:
    collector_ids = {
        'Art Critic Jacques': 5930,
        'Chief Tess': 7088,
        'General Bentnoze': 27541,
        'General Wartface': 27542,
        'Isaura': 26920,
        'Lowse': 26921,
        'Sharrigan': 19098,
        'Sir Atcha': 26922,
        'Soran, Emissary of Zaros': 21102,
        'Velucia': 26924,
        'Wise Old Man': 8409,
        'Giles': 26406
    }
    collector_names = [
        'Art Critic Jacques',
        'Chief Tess',
        'General Bentnoze',
        'General Wartface',
        'Isaura',
        'Lowse',
        'Sharrigan',
        'Sir Atcha',
        'Soran, Emissary of Zaros',
        'Velucia',
        'Wise Old Man',
        'Giles'
    ]
    collectors = [Collector(id=collector_ids.get(name), name=name) for name in collector_names]

# collections
if False:
    collections = []

    names = ['Anarchic Abstraction', 'Radiant Renaissance', 'Imperial Impressionism']
    [collections.append(Collection(name=name, collector_id=collector_ids.get('Art Critic Jacques'))) for name in names]

    names = ['Blingy Fings', 'Smoky Fings', 'Hitty Fings', 'Showy Fings']
    [collections.append(Collection(name=name, collector_id=collector_ids.get('Chief Tess'))) for name in names]

    for collector,name in [ ('General Bentnoze', 'Red Rum Relics'),
                            ('General Wartface', 'Green Gobbo Goodies'),
                            ('Lowse', 'Armadylean'),
                            ('Velucia', 'Museum - Bandosian'),
                            ('Velucia', 'Museum - Armadylean')]:
        [collections.append(Collection(name=f'{name} {num}',collector_id=collector_ids.get(collector))) for num in ['I','II','III']]

    for collector,name in [ ('Isaura', 'Zamorakian'),
                            ('Sharrigan', 'Dragonkin'),
                            ('Sir Atcha', 'Saradominist'),
                            ('Soran, Emissary of Zaros', 'Zarosian')]:
        [collections.append(Collection(name=f'{name} {num}',collector_id=collector_ids.get(collector))) for num in ['I','II','III','IV']]
        [collections.append(Collection(name=f'Museum - {name} {num}',collector_id=collector_ids.get('Velucia'))) for num in ['I','II','III','IV']]
        
    names = ['Wise Am the Music Man', 'Hat Problem', 'Hat Hoarder', 'Magic Man', 'Knowledge is Power']
    [collections.append(Collection(name=name, collector_id=collector_ids.get('Wise Old Man'))) for name in names]
    
    # collection_levels = {
    #     'Anarchic Abstraction': 89,
    #     'Armadylean I': 81,
    #     'Armadylean II': 91,
    #     'Armadylean III': 118,
    #     'Blingy Fings': 69,
    #     'Dragonkin I': 99,
    #     'Dragonkin II': 102,
    #     'Dragonkin III': 108,
    #     'Dragonkin IV': 120,
    #     'Green Gobbo Goodies I': 83,
    #     'Green Gobbo Goodies II': 97,
    #     'Green Gobbo Goodies III': 119,
    #     'Hat Hoarder': 116,
    #     'Hat Problem': 114,
    #     'Hitty Fings': 89,
    #     'Imperial Impressionism': 118,
    #     'Knowledge is Power': 119,
    #     'Magic Man': 118,
    #     'Museum - Armadylean I': 81,
    #     'Museum - Armadylean II': 98,
    #     'Museum - Armadylean III': 118,
    #     'Museum - Bandosian I': 89,
    #     'Museum - Bandosian II': 100,
    #     'Museum - Bandosian III': 119,
    #     'Museum - Dragonkin I': 99,
    #     'Museum - Dragonkin II': 102,
    #     'Museum - Dragonkin III': 108,
    #     'Museum - Dragonkin IV': 120,
    #     'Museum - Saradominist I': 56,
    #     'Museum - Saradominist II': 72,
    #     'Museum - Saradominist III': 100,
    #     'Museum - Saradominist IV': 117,
    #     'Museum - Zamorakian I': 36,
    #     'Museum - Zamorakian II': 81,
    #     'Museum - Zamorakian III': 104,
    #     'Museum - Zamorakian IV': 116,
    #     'Museum - Zarosian I': 25,
    #     'Museum - Zarosian II': 81,
    #     'Museum - Zarosian III': 107,
    #     'Museum - Zarosian IV': 118,
    #     'Radiant Renaissance': 105,
    #     'Red Rum Relics I': 94,
    #     'Red Rum Relics II': 110,
    #     'Red Rum Relics III': 119,
    #     'Saradominist I': 56,
    #     'Saradominist II': 72,
    #     'Saradominist III': 100,
    #     'Saradominist IV': 117,
    #     'Showy Fings': 92,
    #     'Smoky Fings': 81,
    #     'Wise Am the Music Man': 81,
    #     'Zamorakian I': 36,
    #     'Zamorakian II': 81,
    #     'Zamorakian III': 104,
    #     'Zamorakian IV': 116,
    #     'Zarosian I': 25,
    #     'Zarosian II': 81,
    #     'Zarosian III': 107,
    #     'Zarosian IV': 118
    # }

# artefacts
if True:
    ARTEFACTS = [
        "Venator dagger",
        "Venator light crossbow",
        "Legionary gladius",
        "Legionary square shield",
        "Primis Elementis standard",
        "Zaros effigy",
        "Zarosian training dummy",
        "Hookah pipe",
        "Opulent wine goblet",
        "Crest of Dagon",
        "'Disorder' painting",
        "Legatus Maximus figurine",
        "'Solem in Umbra' painting",
        "Imp mask",
        "Lesser demon mask",
        "Greater demon mask",
        "Order of Dis robes",
        "Ritual dagger",
        "'Frying pan'",
        "Hallowed lantern",
        "Branding iron",
        "Manacles",
        "Ancient timepiece",
        "Legatus pendant",
        "Ceremonial unicorn ornament",
        "Ceremonial unicorn saddle",
        "Everlight harp",
        "Everlight trumpet",
        "Everlight violin",
        "Folded-arm figurine (female)",
        "Folded-arm figurine (male)",
        "Pontifex signet ring",
        "'Incite Fear' spell scroll",
        "Dominion discus",
        "Dominion javelin",
        "Dominion pelte shield",
        "'The Lake of Fire' painting",
        "'Lust' metal sculpture",
        "Chaos star",
        "Spiked dog collar",
        "Bronze Dominion medal",
        "Silver Dominion medal",
        "Dominion torch",
        "Ikovian gerege",
        "Toy glider",
        "Toy war golem",
        "Decorative vase",
        "Patera bowl",
        "Kantharos cup",
        "Ceremonial mace",
        "'Consensus ad Idem' painting",
        "Pontifex Maximus figurine",
        "Avian song-egg player",
        "Keshik drum",
        "Morin khuur",
        "Ekeleshuun blinder mask",
        "Narogoshuun 'Hob-da-Gob' ball",
        "Rekeshuun war tether",
        "Aviansie dreamcoat",
        "Ceremonial plume",
        "Peacocking parasol",
        "Ogre Kyzaj axe",
        "Ork cleaver sword",
        "Larupia trophy",
        "Lion trophy",
        "She-wolf trophy",
        "Pontifex censer",
        "Pontifex crozier",
        "Pontifex mitre",
        "Thorobshuun battle standard",
        "Yurkolgokh stink grenade",
        "Dominarian device",
        "Fishing trident",
        "Hawkeye lens multi-vision scope",
        "Talon-3 razor wing",
        "Necromantic focus",
        "'Exsanguinate' spell scroll",
        "High priest crozier",
        "High priest mitre",
        "High priest orb",
        "'Pandemonium' tapestry",
        "'Torment' metal sculpture",
        "Ceremonial dragonkin tablet",
        "Pasaha",
        "Ritual bell",
        "Prototype gravimeter",
        "Songbird recorder",
        "Amphora",
        "Rod of Asclepius",
        "Zarosian ewer",
        "Zarosian stein",
        "Beastkeeper helm",
        "Idithuun horn ring",
        "'Nosorog!' sculpture",
        "Stormguard gerege",
        "Dayguard shield",
        "Kilaya",
        "Vazara",
        "Garagorshuun anchor",
        "Ourg megahitter",
        "Ourg tower/goblin cower shield",
        "Golem heart",
        "Golem instruction",
        "Hellfire haladie",
        "Hellfire katar",
        "Hellfire zaghnal",
        "Death mask",
        "Dragonkin calendar",
        "Dragonkin staff",
        "Dorgeshuun spear",
        "'Forged in War' sculpture",
        "Kopis dagger",
        "Xiphos short sword",
        "'Smoke Cloud' spell scroll",
        "Vigorem vial",
        "Dragon scalpel",
        "Protective goggles",
        "Dragon burner",
        "Orthenglass flask",
        "Blackfire lance",
        "Nightguard shield",
        "Huzamogaarb chaos crown",
        "Saragorgak star crown",
        "'Possession' metal sculpture",
        "Trishula",
        "Tsutsaroth piercing",
        "'The Pride of Padosan' painting",
        "'Hallowed Be the Everlight' painting",
        "'The Lord of Light' painting",
        "Meditation pipe",
        "Personal totem",
        "Singing bowl",
        "Ancient magic tablet",
        "Portable phylactery",
        "'Animate Dead' spell scroll",
        "Lingam stone",
        "Master control",
        "'The Enlightened Soul' scroll",
        "'The Eudoxian Elements' tablet",
        "Drogokishuun hook sword",
        "Hobgoblin mansticker",
        "Chaos Elemental trophy",
        "Virius trophy",
        "Flat cap",
        "Night owl flight goggles",
        "Prototype godbow",
        "Prototype godstaff",
        "Prototype godsword",
        "Xolo hard hat",
        "Xolo pickaxe",
        "Praetorian hood",
        "Praetorian robes",
        "Praetorian staff",
        "Kal-i-kra chieftain crown",
        "Kal-i-kra mace",
        "Kal-i-kra warhorn",
        "Spear of Annihilation",
        "Tsutsaroth helm",
        "Tsutsaroth pauldron",
        "Tsutsaroth urumi",
        "Kontos lance",
        "Doru spear",
        "Chuluu stone",
        "Quintessence counter",
        "Spherical astrolabe",
        "Ancient globe",
        "Battle plans",
        "'Prima Legio' painting",
        "Horogothgar cooking pot",
        "'Da Boss Man' sculpture",
        "Xolo shield",
        "Xolo spear",
        "Gold dish",
        "'Raksha' idol",
        "Tetracompass (unpowered)",
        "Apex cap",
        "Curse tablet",
        "Funerary urn of shadow",
        "Infula robes",
        "Funerary urn of smoke",
        "Hand of the Ancients",
        "Decorative amphora",
        "Funerary urn of ice",
        "Loarnab rod",
        "Inquisitor's seal",
        "Inquisitor's ceremonial mask",
        "Inquisitor's ceremonial armour",
        "Gladiator sword",
        "Gladiator helmet",
        "Funerary urn of blood",
        "'The Serpent's Fall' carving",
        "Model Chariot",
        "Funerary urn of miasma"
    ]


if __name__ == '__main__':
    session = Session()
    # session.add_all(materials)
    # session.add_all(collectors)
    # session.add_all(collections)
    session.commit()
