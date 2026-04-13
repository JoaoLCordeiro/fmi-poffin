from pymongo import MongoClient
from pymongo.collection import Collection as MongoCollection

# TODO: use the real database
ALL_CARDS_LIST = [
    "Scyther", "Pineco", "Seedot", "Nuzleaf", "Shiftry", "Shroomish",
    "Breloom", "Roselia", "Roserade", "Turtwig", "Grotle", "Torterra ex",
    "Shaymin", "Cottonee", "Whimsicott", "Deerling", "Sawsbuck", "Grubbin",
    "Dhelmise", "Bramblin", "Brambleghast", "Scovillain ex", "Rellor",
    "Rabsca", "Iron Leaves ex", "Ponyta", "Rapidash", "Slugma", "Magcargo",
    "Victini", "Heatmor", "Litten", "Torracat", "Incineroar ex", "Turtonator",
    "Sizzlipede", "Centiskorch", "Gouging Fire ex", "Totodile", "Croconaw",
    "Feraligatr", "Carvanha", "Sharpedo", "Keldeo", "Snom", "Frosmoth",
    "Wiglett", "Finizen", "Palafin", "Walking Wake ex", "Pikachu", "Raichu",
    "Electabuzz", "Electivire", "Charjabug", "Vikavolt", "Zeraora", "Yamper",
    "Boltund", "Wugtrio ex", "Iron Hands", "Iron Thorns", "Mr. Mime", "Marill",
    "Azumarill", "Girafarig", "Latias", "Bronzor", "Bronzong", "Solosis",
    "Duosion", "Reuniclus", "Elgyem", "Beheeyem", "Cutiefly", "Ribombee",
    "Scream Tail", "Flutter Mane", "Iron Valiant", "Iron Valiant",
    "Iron Crown ex", "Meditite", "Medicham", "Relicanth", "Drilbur",
    "Excadrill", "Golett", "Golurk", "Rockruff", "Lycanroc", "Mudbray",
    "Mudsdale", "Rolycoly", "Carkol", "Coalossal", "Great Tusk", "Great Tusk",
    "Sandy Shocks", "Iron Boulder ex", "Ekans", "Arbok", "Gastly", "Haunter",
    "Gengar ex", "Poochyena", "Mightyena", "Sableye", "Farigiraf ex",
    "Roaring Moon", "Forretress", "Scizor ex", "Mawile", "Beldum", "Metang",
    "Metagross", "Meltan", "Melmetal", "Iron Treads", "Koraidon",
    "Koraidon ex", "Miraidon", "Miraidon ex", "Raging Bolt ex", "Lickitung",
    "Lickilicky", "Hoothoot", "Noctowl", "Dunsparce", "Dudunsparce", "Skitty",
    "Delcatty", "Chatot", "Pidove", "Tranquill", "Unfezant", "Minccino",
    "Cinccino", "Drampa", "Iron Jugulis", "Ancient Booster Energy Capsule",
    "Awakening Drum", "Bianca's Devotion", "Boxed Order", "Buddy-Buddy Poffin",
    "Ciphermaniac's Codebreaking", "Eri", "Explorer's Guidance",
    "Full Metal Lab", "Future Booster Energy Capsule", "Hand Trimmer",
    "Heavy Baton", "Hero's Cape", "Master Ball", "Maximum Belt",
    "Morty's Conviction", "Perilous Jungle", "Prime Catcher", "Reboot Pod",
    "Rescue Board", "Salvatore", "Mist Energy", "Neo Upper Energy", "Tangela",
    "Tangrowth", "Pinsir", "Spinarak", "Ariados", "Sunkern", "Sunflora",
    "Heracross", "Volbeat", "Illumise", "Leafeon", "Phantump", "Trevenant",
    "Grookey", "Thwackey", "Rillaboom", "Applin", "Dipplin", "Iron Leaves",
    "Poltchageist", "Poltchageist", "Sinistcha", "Sinistcha ex",
    "Teal Mask Ogerpon", "Teal Mask Ogerpon ex", "Vulpix", "Ninetales",
    "Slugma", "Magcargo ex", "Torkoal", "Chimchar", "Monferno", "Infernape",
    "Darumaka", "Darmanitan", "Litwick", "Lampent", "Chandelure", "Chi-Yu",
    "Hearthflame Mask Ogerpon ex", "Poliwag", "Poliwhirl", "Poliwrath",
    "Goldeen", "Seaking", "Jynx", "Corphish", "Crawdaunt", "Feebas", "Milotic",
    "Snorunt", "Glalie", "Froslass", "Glaceon", "Phione", "Froakie",
    "Frogadier", "Cramorant", "Finizen", "Palafin", "Palafin ex",
    "Iron Bundle", "Walking Wake", "Wellspring Mask Ogerpon ex", "Zapdos",
    "Shinx", "Luxio", "Luxray ex", "Emolga", "Helioptile", "Heliolisk",
    "Morpeko", "Tadbulb", "Bellibolt", "Wattrel", "Kilowattrel",
    "Iron Thorns ex", "Clefairy", "Clefable", "Abra", "Kadabra", "Alakazam",
    "Girafarig", "Farigiraf", "Chimecho", "Flabébé", "Floette", "Florges",
    "Swirlix", "Slurpuff", "Sandygast", "Palossand", "Enamorus",
    "Scream Tail ex", "Munkidori", "Fezandipiti", "Sandshrew", "Sandslash",
    "Hisuian Growlithe", "Hisuian Arcanine", "Nosepass", "Probopass",
    "Timburr", "Gurdurr", "Conkeldurr", "Greninja ex", "Hawlucha", "Glimmet",
    "Glimmora", "Ting-Lu", "Okidogi", "Cornerstone Mask Ogerpon ex",
    "Poochyena", "Mightyena", "Venipede", "Whirlipede", "Scolipede",
    "Brute Bonnet", "Skarmory", "Aron", "Lairon", "Aggron", "Heatran",
    "Varoom", "Revavroom", "Applin", "Dipplin", "Dreepy", "Drakloak",
    "Dragapult ex", "Tatsugiri", "Farfetch'd", "Chansey", "Blissey ex",
    "Eevee", "Snorlax", "Aipom", "Ambipom", "Ducklett", "Swanna",
    "Bloodmoon Ursaluna ex", "Accompanying Flute", "Bug Catching Set",
    "Caretaker", "Carmine", "Community Center", "Cook",
    "Enhanced Hammer", "Festival Grounds", "Handheld Fan", "Hassel",
    "Hyper Aroma", "Jamming Tower", "Kieran", "Lana's Aid", "Love Ball",
    "Lucian", "Lucky Helmet", "Ogre's Mask", "Perrin", "Raifort",
    "Scoop Up Cyclone", "Secret Box", "Survival Brace", "Unfair Stamp",
    "Boomerang Energy", "Legacy Energy", "Joltik", "Galvantula", "Rowlet",
    "Dartrix", "Decidueye", "Tapu Bulu", "Houndour", "Houndoom", "Iron Moth",
    "Horsea", "Seadra", "Kingdra ex", "Sneasel", "Weavile", "Revavroom ex",
    "Drowzee", "Hypno", "Duskull", "Dusclops", "Dusknoir", "Cresselia",
    "Sylveon", "Croagunk", "Toxicroak", "Bloodmoon Ursaluna", "Slither Wing",
    "Zubat", "Golbat", "Crobat", "Absol", "Zorua", "Zoroark", "Inkay",
    "Malamar", "Yveltal", "Okidogi ex", "Munkidori ex", "Fezandipiti ex",
    "Pecharunt ex", "Genesect", "Cufant", "Copperajah", "Varoom", "Axew",
    "Fraxure", "Haxorus", "Kyurem", "Meowth", "Persian", "Eevee", "Furfrou",
    "Stufful", "Bewear", "Academy at Night", "Binding Mochi", "Cassiopeia",
    "Colress's Tenacity", "Dangerous Laser", "Janine's Secret Art",
    "Neutralization Zone", "Night Stretcher", "Poké Vital A", "Powerglass",
    "Xerosic's Machinations", "Venusaur ex", "Ledyba", "Ledian", "Celebi",
    "Lileep", "Cradily", "Carnivine", "Mow Rotom", "Grubbin", "Gossifleur",
    "Eldegoss", "Applin", "Dipplin", "Hydrapple ex", "Nymble", "Lokix",
    "Toedscool", "Toedscruel", "Ponyta", "Rapidash", "Pansear", "Reshiram",
    "Salandit", "Salazzle", "Turtonator", "Scorbunny", "Raboot",
    "Cinderace ex", "Charcadet", "Blastoise ex", "Lapras", "Lapras ex",
    "Marill", "Azumarill", "Finneon", "Lumineon", "Tirtouga", "Carracosta",
    "Froakie", "Frogadier", "Greninja ex", "Crabominable", "Chewtle",
    "Drednaw", "Veluza", "Electabuzz", "Electivire", "Chinchou", "Lanturn",
    "Joltik", "Galvantula ex", "Charjabug", "Vikavolt", "Togedemaru",
    "Zeraora", "Pawmi", "Slowpoke", "Slowking", "Mewtwo", "Drifloon",
    "Drifblim", "Yamask", "Comfey", "Milcery", "Alcremie", "Fidough",
    "Dachsbun ex", "Flittle", "Espathra", "Greavard", "Iron Boulder",
    "Cubone", "Marowak", "Rhyhorn", "Rhydon", "Rhyperior", "Meditite",
    "Meditite", "Medicham", "Medicham ex", "Riolu", "Lucario ex", "Mienfoo",
    "Mienshao", "Pancham", "Diancie", "Crabrawler", "Falinks", "Garganacl ex",
    "Koraidon", "Gulpin", "Swalot", "Pangoro", "Impidimp", "Morgrem",
    "Grimmsnarl", "Bombirdier", "Jirachi", "Klink", "Klang", "Klinklang",
    "Meltan", "Meltan", "Melmetal", "Melmetal ex", "Duraludon", "Archaludon",
    "Varoom", "Revavroom", "Orthworm ex", "Raging Bolt", "Tauros", "Eevee",
    "Hoothoot", "Noctowl", "Glameow", "Purugly", "Fan Rotom", "Bouffalant",
    "Tornadus", "Fletchling", "Fletchinder", "Talonflame", "Wooloo", "Dubwool",
    "Lechonk", "Cyclizar", "Terapagos ex", "Antique Cover Fossil",
    "Antique Root Fossil", "Area Zero Underdepths", "Briar", "Crispin",
    "Deluxe Bomb", "Glass Trumpet", "Grand Tree", "Gravity Gemstone", "Kofu",
    "Lacey", "Occa Berry", "Payapa Berry", "Sparkling Crystal", "Exeggcute",
    "Exeggcute", "Exeggutor", "Durant ex", "Scatterbug", "Spewpa", "Vivillon",
    "Morelull", "Shiinotic", "Dhelmise", "Zarude", "Capsakid", "Rellor",
    "Rabsca", "Wo-Chien", "Vulpix", "Ninetales", "Paldean Tauros", "Ho-Oh",
    "Castform Sunny Form", "Victini", "Pansear", "Simisear", "Larvesta",
    "Volcarona", "Oricorio", "Sizzlipede", "Centiskorch", "Fuecoco",
    "Crocalor", "Skeledirge", "Charcadet", "Charcadet", "Armarouge",
    "Ceruledge", "Ceruledge ex", "Scovillain ex", "Gouging Fire",
    "Paldean Tauros", "Mantine", "Feebas", "Milotic ex", "Spheal", "Sealeo",
    "Walrein", "Shellos", "Cryogonal", "Black Kyurem ex", "Bruxish", "Quaxly",
    "Quaxwell", "Quaquaval", "Cetoddle", "Cetitan", "Iron Bundle", "Chien-Pao",
    "Pikachu ex", "Magnemite", "Magneton", "Magnezone", "Rotom", "Blitzle",
    "Zebstrika", "Stunfisk", "Tapu Koko", "Wattrel", "Kilowattrel",
    "Kilowattrel ex", "Miraidon", "Togepi", "Togetic", "Togekiss", "Marill",
    "Azumarill", "Smoochum", "Latias ex", "Latios", "Uxie", "Mesprit", "Azelf",
    "Sigilyph", "Yamask", "Cofagrigus", "Espurr", "Meowstic", "Sylveon ex",
    "Dedenne", "Xerneas", "Oricorio", "Sandygast", "Palossand ex", "Tapu Lele",
    "Indeedee", "Flittle", "Espathra", "Flutter Mane", "Gimmighoul", "Mankey",
    "Primeape", "Annihilape", "Paldean Tauros", "Phanpy", "Donphan",
    "Trapinch", "Vibrava", "Flygon ex", "Gastrodon", "Drilbur", "Excadrill",
    "Landorus", "Passimian", "Clobbopus", "Grapploct", "Glimmet", "Glimmora",
    "Koraidon", "Deino", "Zweilous", "Hydreigon ex", "Shroodle", "Grafaiai",
    "Alolan Diglett", "Alolan Dugtrio", "Skarmory", "Registeel", "Bronzor",
    "Bronzong", "Klefki", "Duraludon", "Archaludon ex", "Gholdengo",
    "Iron Crown", "Alolan Exeggutor ex", "Altaria", "Dialga", "Palkia",
    "Turtonator", "Applin", "Flapple", "Appletun", "Eternatus", "Tatsugiri ex",
    "Eevee", "Snorlax", "Slakoth", "Vigoroth", "Slaking ex", "Swablu",
    "Zangoose", "Kecleon", "Bouffalant", "Rufflet", "Braviary", "Helioptile",
    "Heliolisk", "Oranguru", "Tandemaus", "Maushold", "Cyclizar ex",
    "Flamigo ex", "Terapagos", "Amulet of Hope", "Babiri Berry",
    "Brilliant Blender", "Call Bell", "Chill Teaser Toy",
    "Clemont's Quick Wit", "Colbur Berry", "Counter Gain", "Cyrano",
    "Deduction Kit", "Dragon Elixir", "Drasna", "Drayton", "Dusk Ball",
    "Energy Search Pro", "Gravity Mountain", "Jasmine's Gaze",
    "Lisia's Appeal", "Lively Stadium", "Meddling Memo", "Megaton Blower",
    "Miracle Headset", "Passho Berry", "Precious Trolley", "Scramble Switch",
    "Surfer", "Technical Machine: Fluorite", "Tera Orb", "Tyme",
    "Enriching Energy", "Exeggcute", "Exeggutor", "Pinsir", "Budew", "Leafeon",
    "Leafeon ex", "Cottonee", "Whimsicott", "Applin", "Dipplin",
    "Hydrapple ex", "Teal Mask Ogerpon ex", "Flareon", "Flareon ex", "Litleo",
    "Pyroar", "Hearthflame Mask Ogerpon ex", "Slowpoke", "Slowking", "Goldeen",
    "Seaking", "Vaporeon", "Vaporeon ex", "Suicune", "Glaceon", "Glaceon ex",
    "Wellspring Mask Ogerpon ex", "Pikachu ex", "Jolteon", "Jolteon ex",
    "Iron Hands ex", "Iron Thorns ex", "Espeon", "Espeon ex", "Duskull",
    "Dusclops", "Dusknoir", "Spritzee", "Aromatisse", "Sylveon", "Sylveon ex",
    "Scream Tail", "Flutter Mane", "Munkidori", "Fezandipiti", "Iron Boulder",
    "Larvitar", "Pupitar", "Groudon", "Riolu", "Lucario ex", "Hippopotas",
    "Hippowdon", "Bloodmoon Ursaluna", "Great Tusk", "Sandy Shocks ex",
    "Okidogi", "Cornerstone Mask Ogerpon ex", "Umbreon", "Umbreon ex",
    "Sneasel", "Houndour", "Houndoom", "Tyranitar ex", "Roaring Moon",
    "Bronzor", "Bronzong", "Heatran", "Duraludon", "Archaludon", "Dreepy",
    "Drakloak", "Dragapult ex", "Eevee", "Eevee ex", "Snorlax ex", "Hoothoot",
    "Noctowl", "Dunsparce", "Dudunsparce", "Miltank", "Lugia ex", "Buneary",
    "Lopunny", "Fan Rotom", "Regigigas", "Shaymin", "Furfrou", "Hawlucha",
    "Noibat", "Noivern ex", "Terapagos ex", "Amarys", "Area Zero Underdepths",
    "Binding Mochi", "Black Belt's Training", "Black Belt's Training",
    "Black Belt's Training", "Black Belt's Training", "Briar",
    "Buddy-Buddy Poffin", "Bug Catching Set", "Carmine",
    "Ciphermaniac's Codebreaking", "Crispin", "Earthen Vessel",
    "Explorer's Guidance", "Festival Grounds", "Friends in Paldea",
    "Glass Trumpet", "Haban Berry", "Janine's Secret Art", "Kieran", "Lacey",
    "Larry's Skill", "Max Rod", "Maximum Belt", "Ogre's Mask", "Prime Catcher",
    "Professor Sada's Vitality", "Professor Turo's Scenario",
    "Professor's Research", "Professor's Research", "Professor's Research",
    "Professor's Research", "Rescue Board", "Roto-Stick", "Scoop Up Cyclone",
    "Sparkling Crystal", "Techno Radar", "Treasure Tracker", "Caterpie",
    "Metapod", "Butterfree", "Paras", "Parasect", "Petilil", "Lilligant",
    "Maractus", "Karrablast", "Foongus", "Amoonguss ex", "Shelmet", "Accelgor",
    "Durant", "Virizion", "Sprigatito", "Floragato", "Meowscarada", "Nymble",
    "Magmar", "Magmortar", "Torchic", "Combusken", "Blaziken ex", "Torkoal",
    "N's Darumaka", "N's Darmanitan", "Larvesta", "Volcarona", "Reshiram ex",
    "Volcanion ex", "Articuno", "Remoraid", "Octillery", "Lotad", "Lombre",
    "Ludicolo", "Wingull", "Pelipper", "Wailmer", "Wailord", "Regice",
    "Veluza ex", "Alolan Geodude", "Alolan Graveler", "Alolan Golem",
    "Iono's Voltorb", "Iono's Electrode", "N's Joltik", "Togedemaru",
    "Tapu Koko ex", "Iono's Tadbulb", "Iono's Bellibolt ex", "Iono's Wattrel",
    "Iono's Kilowattrel", "Lillie's Clefairy ex", "Alolan Marowak", "Mr. Mime",
    "Shuppet", "Banette", "Beldum", "Metang", "Metagross", "N's Sigilyph",
    "Oricorio", "Lillie's Cutiefly", "Lillie's Ribombee", "Lillie's Comfey",
    "Mimikyu ex", "Dhelmise", "Impidimp", "Morgrem", "Grimmsnarl", "Milcery",
    "Alcremie ex", "Cubone", "Swinub", "Piloswine", "Mamoswine ex", "Larvitar",
    "Pupitar", "Regirock", "Pancham", "Rockruff", "Lycanroc",
    "Hop's Silicobra", "Hop's Sandaconda", "Toedscool", "Toedscruel", "Klawf",
    "Koffing", "Weezing", "Paldean Wooper", "Paldean Clodsire ex", "Tyranitar",
    "N's Purrloin", "N's Zorua", "N's Zoroark ex", "Pangoro", "Lokix",
    "Bombirdier", "Escavalier", "N's Klink", "N's Klang", "N's Klinklang",
    "Galarian Stunfisk", "Magearna", "Hop's Corviknight", "Cufant",
    "Copperajah", "Hop's Zacian ex", "Bagon", "Shelgon", "Salamence ex",
    "Druddigon", "N's Reshiram", "Hop's Snorlax", "Sentret", "Furret",
    "Dunsparce", "Dudunsparce ex", "Kecleon", "Tropius", "Audino", "Minccino",
    "Cinccino", "Noibat", "Noivern", "Komala", "Drampa", "Skwovet", "Greedent",
    "Hop's Rookidee", "Hop's Corvisquire", "Hop's Wooloo", "Hop's Dubwool",
    "Cramorant", "Hop's Cramorant", "Lechonk", "Oinkologne", "Squawkabilly",
    "Billy & O'Nare", "Black Belt's Training", "Black Belt's Training",
    "Black Belt's Training", "Brock's Scouting", "Hop's Bag",
    "Hop's Choice Band", "Iris's Fighting Spirit", "Levincia",
    "Lillie's Pearl", "N's Castle", "N's PP Up", "Postwick",
    "Professor's Research", "Redeemable Ticket", "Ruffian", "Super Potion",
    "Spiky Energy", "Ethan's Pinsir", "Yanma", "Yanmega ex", "Pineco",
    "Shroomish", "Breloom", "Cynthia's Roselia", "Cynthia's Roserade",
    "Mow Rotom", "Shaymin", "Dwebble", "Crustle", "Fomantis", "Lurantis",
    "Team Rocket's Blipbug", "Applin", "Dipplin", "Hydrapple",
    "Team Rocket's Tarountula", "Team Rocket's Spidops", "Smoliv", "Dolliv",
    "Arboliva ex", "Rellor", "Rabsca ex", "Teal Mask Ogerpon", "Growlithe",
    "Arcanine", "Ponyta", "Rapidash", "Team Rocket's Moltres ex",
    "Ethan's Cyndaquil", "Ethan's Quilava", "Ethan's Typhlosion",
    "Ethan's Slugma", "Ethan's Magcargo", "Team Rocket's Houndour",
    "Team Rocket's Houndoom", "Ethan's Ho-Oh ex", "Torchic", "Combusken",
    "Blaziken", "Heat Rotom", "Hearthflame Mask Ogerpon", "Misty's Psyduck",
    "Misty's Staryu", "Misty's Starmie", "Misty's Magikarp",
    "Misty's Gyarados", "Misty's Lapras", "Team Rocket's Articuno",
    "Cynthia's Feebas", "Cynthia's Milotic", "Clamperl", "Huntail", "Gorebyss",
    "Buizel", "Floatzel", "Snover", "Abomasnow", "Wash Rotom", "Arrokuda",
    "Barraskewda", "Cetoddle", "Cetitan ex", "Dondozo ex",
    "Wellspring Mask Ogerpon", "Electabuzz", "Electivire ex",
    "Team Rocket's Zapdos", "Ethan's Pichu", "Team Rocket's Mareep",
    "Team Rocket's Flaaffy", "Team Rocket's Ampharos", "Electrike",
    "Manectric", "Rotom", "Zeraora", "Team Rocket's Drowzee",
    "Team Rocket's Hypno", "Team Rocket's Mewtwo ex",
    "Team Rocket's Wobbuffet", "Steven's Baltoy", "Steven's Claydol",
    "Team Rocket's Chingling", "Steven's Carbink", "Team Rocket's Mimikyu",
    "Team Rocket's Dottler", "Team Rocket's Orbeetle", "Mankey", "Primeape",
    "Annihilape", "Ethan's Sudowoodo", "Team Rocket's Larvitar",
    "Team Rocket's Pupitar", "Team Rocket's Tyranitar", "Nosepass",
    "Probopass", "Meditite", "Medicham", "Regirock ex", "Cynthia's Gible",
    "Cynthia's Gabite", "Cynthia's Garchomp ex", "Hippopotas", "Hippowdon",
    "Mudbray", "Mudsdale", "Arven's Toedscool", "Arven's Toedscruel",
    "Cornerstone Mask Ogerpon", "Team Rocket's Ekans", "Team Rocket's Arbok",
    "Team Rocket's Nidoran♀", "Team Rocket's Nidorina",
    "Team Rocket's Nidoqueen", "Team Rocket's Nidoran♂",
    "Team Rocket's Nidorino", "Team Rocket's Nidoking ex",
    "Team Rocket's Zubat", "Team Rocket's Golbat", "Team Rocket's Crobat ex",
    "Team Rocket's Grimer", "Team Rocket's Muk", "Team Rocket's Koffing",
    "Team Rocket's Weezing", "Team Rocket's Murkrow", "Team Rocket's Sneasel",
    "Cynthia's Spiritomb", "Marnie's Purrloin", "Marnie's Liepard",
    "Marnie's Scraggy", "Marnie's Scrafty", "Marnie's Impidimp",
    "Marnie's Morgrem", "Marnie's Grimmsnarl ex", "Marnie's Morpeko",
    "Arven's Maschiff", "Arven's Mabosstiff ex", "Forretress", "Skarmory",
    "Steven's Skarmory", "Steven's Beldum", "Steven's Metang",
    "Steven's Metagross ex", "Zamazenta", "Team Rocket's Rattata",
    "Team Rocket's Raticate", "Team Rocket's Meowth",
    "Team Rocket's Persian ex", "Kangaskhan", "Tauros",
    "Team Rocket's Porygon", "Team Rocket's Porygon2",
    "Team Rocket's Porygon-Z", "Taillow", "Swellow", "Arven's Skwovet",
    "Arven's Greedent", "Squawkabilly", "Arven's Sandwich",
    "Cynthia's Power Weight", "Emcee's Hype", "Energy Recycler",
    "Ethan's Adventure", "Granite Cave", "Judge", "Sacred Ash",
    "Spikemuth Gym", "Team Rocket's Archer", "Team Rocket's Ariana",
    "Team Rocket's Bother-Bot", "Team Rocket's Factory",
    "Team Rocket's Giovanni", "Team Rocket's Great Ball",
    "Team Rocket's Petrel", "Team Rocket's Proton",
    "Team Rocket's Transceiver", "Team Rocket's Venture Bomb",
    "Team Rocket's Watchtower", "TM Machine", "Team Rocket's Energy", "Snivy",
    "Servine", "Serperior ex", "Pansage", "Simisage", "Petilil", "Lilligant",
    "Maractus", "Karrablast", "Foongus", "Amoonguss", "Victini", "Darumaka",
    "Darmanitan", "Larvesta", "Volcarona", "Panpour", "Simipour", "Tympole",
    "Palpitoad", "Seismitoad", "Tirtouga", "Carracosta", "Alomomola",
    "Cubchoo", "Beartic", "Cryogonal", "Kyurem ex", "Emolga", "Tynamo",
    "Eelektrik", "Eelektross", "Thundurus", "Zekrom ex", "Munna", "Musharna",
    "Solosis", "Duosion", "Reuniclus", "Elgyem", "Beheeyem", "Golett",
    "Golurk", "Meloetta ex", "Drilbur", "Excadrill ex", "Timburr", "Gurdurr",
    "Conkeldurr", "Throh", "Dwebble", "Crustle", "Landorus", "Venipede",
    "Whirlipede", "Scolipede", "Sandile", "Krokorok", "Krookodile",
    "Escavalier", "Klink", "Klang", "Klinklang", "Pawniard", "Bisharp",
    "Cobalion", "Genesect ex", "Axew", "Fraxure", "Haxorus", "Pidove",
    "Tranquill", "Unfezant", "Audino", "Minccino", "Cinccino", "Rufflet",
    "Braviary", "Air Balloon", "Antique Cover Fossil", "Energy Coin", "Fennel",
    "N's Plan", "Pokégear 3.0", "Professor's Research", "Prism Energy",
    "Sewaddle", "Swadloon", "Leavanny", "Cottonee", "Whimsicott ex",
    "Deerling", "Sawsbuck", "Shelmet", "Accelgor", "Virizion", "Tepig",
    "Pignite", "Emboar", "Pansear", "Simisear", "Litwick", "Lampent",
    "Chandelure", "Heatmor", "Reshiram ex", "Oshawott", "Dewott", "Samurott",
    "Basculin", "Ducklett", "Swanna", "Vanillite", "Vanillish", "Vanilluxe",
    "Keldeo ex", "Blitzle", "Zebstrika", "Joltik", "Galvantula", "Stunfisk",
    "Woobat", "Swoobat", "Sigilyph", "Yamask", "Cofagrigus", "Gothita",
    "Gothorita", "Gothitelle", "Frillish", "Jellicent ex", "Roggenrola",
    "Boldore", "Gigalith", "Sawk", "Archen", "Archeops", "Mienfoo", "Mienshao",
    "Terrakion", "Purrloin", "Liepard", "Scraggy", "Scrafty", "Trubbish",
    "Garbodor", "Zorua", "Zoroark", "Vullaby", "Mandibuzz", "Deino",
    "Zweilous", "Hydreigon ex", "Ferroseed", "Ferrothorn", "Durant",
    "Druddigon", "Patrat", "Watchog", "Lillipup", "Herdier", "Stoutland",
    "Bouffalant ex", "Tornadus", "Antique Plume Fossil", "Brave Bangle",
    "Cheren", "Energy Retrieval", "Harlequin", "Hilda", "Tool Scrapper",
    "Ignition Energy", "Meganium", "Inteleon", "Alakazam", "Lunatone",
    "Drifloon", "Drifblim", "Psyduck", "Golduck", "Alakazam", "Riolu",
    "Mega Latias ex", "Mega Lucario ex", "Mega Venusaur ex", "Ceruledge",
    "Zacian", "Flygon", "Toxtricity", "Cottonee", "Whimsicott", "Sneasel",
    "Weavile", "Charcadet", "Mega Charizard X ex", "Oricorio ex",
    "Mega Kangaskhan ex", "Meloetta", "Haunter", "Celebratory Fanfare",
    "Mega Charizard X ex", "Mega Charizard Y ex", "N's Zekrom",
    "Mega Gardevoir ex", "Mega Lucario ex", "Bulbasaur", "Ivysaur",
    "Mega Venusaur ex", "Exeggcute", "Exeggutor", "Tangela", "Tangrowth",
    "Chikorita", "Bayleef", "Meganium", "Shuckle", "Celebi", "Seedot",
    "Nuzleaf", "Shiftry", "Nincada", "Ninjask", "Dhelmise", "Vulpix",
    "Ninetales", "Numel", "Mega Camerupt ex", "Litleo", "Pyroar", "Volcanion",
    "Scorbunny", "Raboot", "Cinderace", "Sizzlipede", "Centiskorch", "Chi-Yu",
    "Mantine", "Corphish", "Kyogre", "Snover", "Mega Abomasnow ex",
    "Clauncher", "Clawitzer", "Sobble", "Drizzile", "Inteleon", "Snom",
    "Frosmoth", "Eiscue", "Magnemite", "Magneton", "Magnezone", "Raikou",
    "Electrike", "Mega Manectric ex", "Pachirisu", "Helioptile", "Heliolisk",
    "Abra", "Kadabra", "Alakazam", "Jynx", "Ralts", "Kirlia",
    "Mega Gardevoir ex", "Shedinja", "Spoink", "Grumpig", "Xerneas",
    "Greavard", "Houndstone", "Gimmighoul", "Sandshrew", "Sandslash", "Onix",
    "Tyrogue", "Makuhita", "Hariyama", "Lunatone", "Solrock", "Riolu",
    "Mega Lucario ex", "Croagunk", "Toxicroak", "Marshadow", "Stonjourner",
    "Nacli", "Naclstack", "Garganacl", "Crawdaunt", "Mega Absol ex",
    "Spiritomb", "Yveltal", "Nickit", "Thievul", "Shroodle", "Grafaiai",
    "Steelix", "Mega Mawile ex", "Dialga", "Tinkatink", "Tinkatuff",
    "Tinkaton", "Gholdengo", "Mega Latias ex", "Latios", "Spearow", "Fearow",
    "Mega Kangaskhan ex", "Delibird", "Miltank", "Buneary", "Lopunny",
    "Yungoos", "Gumshoos", "Stufful", "Bewear", "Acerola's Mischief",
    "Boss's Orders", "Energy Switch", "Fighting Gong", "Forest of Vitality",
    "Iron Defender", "Lillie's Determination", "Lt. Surge's Bargain",
    "Mega Signal", "Mystery Garden", "Pokémon Center Lady",
    "Premium Power Pro", "Rare Candy", "Repel", "Risky Ruins",
    "Strange Timepiece", "Surfing Beach", "Switch", "Ultra Ball",
    "Wally's Compassion", "Oddish", "Gloom", "Vileplume", "Mega Heracross ex",
    "Lotad", "Lombre", "Ludicolo", "Genesect", "Nymble", "Lokix", "Charmander",
    "Charmeleon", "Mega Charizard X ex", "Moltres", "Darumaka", "Darmanitan",
    "Reshiram", "Oricorio ex", "Charcadet", "Ceruledge", "Seel", "Dewgong",
    "Swinub", "Piloswine", "Mamoswine", "Suicune", "Piplup", "Prinplup",
    "Rotom ex", "Yamper", "Boltund", "Pawmi", "Pawmo", "Pawmot", "Misdreavus",
    "Mismagius ex", "Snubbull", "Granbull", "Cresselia", "Meloetta",
    "Mega Diancie ex", "Mimikyu", "Milcery", "Alcremie", "Zacian", "Bramblin",
    "Brambleghast", "Paldean Tauros", "Gligar", "Gliscor", "Trapinch",
    "Vibrava", "Flygon", "Gastly", "Haunter", "Mega Gengar ex", "Murkrow",
    "Honchkrow", "Sableye", "Carvanha", "Mega Sharpedo ex", "Seviper", "Absol",
    "Sandile", "Krokorok", "Krookodile", "Toxel", "Toxtricity", "Eternatus",
    "Empoleon ex", "Bronzor", "Bronzong", "Togedemaru", "Duraludon",
    "Archaludon", "Jigglypuff", "Wigglytuff", "Aipom", "Ambipom", "Smeargle",
    "Zigzagoon", "Linoone", "Buneary", "Mega Lopunny ex", "Battle Cage",
    "Blowtorch", "Dawn", "Dizzying Valley", "Firebreather", "Grimsley's Move",
    "Jumbo Ice Cream", "Punk Helmet", "Sacred Charm", "Wondrous Patch",
    "Erika's Oddish", "Erika's Gloom", "Erika's Vileplume ex",
    "Erika's Bellsprout", "Erika's Weepinbell", "Erika's Victreebel",
    "Erika's Tangela", "Chikorita", "Bayleef", "Mega Meganium ex", "Wurmple",
    "Silcoon", "Beautifly", "Cascoon", "Dustox", "Budew", "Grubbin",
    "Team Rocket's Tarountula", "Team Rocket's Spidops", "Charmander",
    "Charmeleon", "Mega Charizard Y ex", "Ethan's Slugma", "Ethan's Magcargo",
    "Entei", "Ethan's Ho-Oh ex", "Numel", "Camerupt", "Tepig", "Pignite",
    "Mega Emboar ex", "N's Darumaka", "N's Darmanitan", "Salandit", "Salazzle",
    "Scorbunny", "Raboot", "Cinderace ex", "Psyduck", "Golduck", "Totodile",
    "Croconaw", "Mega Feraligatr ex", "Sneasel", "Weavile", "Snorunt",
    "Mega Froslass ex", "Regice ex", "N's Vanillite", "N's Vanillish",
    "N's Vanilluxe", "Snom", "Frosmoth", "Glastrier", "Pikachu", "Raichu",
    "Pikachu ex", "Voltorb ex", "Tynamo", "Eelektrik", "Mega Eelektross ex",
    "Stunfisk", "Helioptile", "Heliolisk", "Charjabug", "Vikavolt",
    "Tapu Koko", "Hop's Pincurchin ex", "Iono's Tadbulb",
    "Iono's Bellibolt ex", "Iono's Wattrel", "Iono's Kilowattrel",
    "Miraidon ex", "Clefairy", "Clefable", "Lillie's Clefairy ex",
    "Team Rocket's Exeggcute", "Team Rocket's Exeggutor",
    "Team Rocket's Mewtwo ex", "Togepi", "Togetic", "Togekiss", "Marill",
    "Azumarill ex", "Misdreavus", "Mismagius", "Ralts", "Kirlia",
    "Mega Gardevoir ex", "Shuppet", "Banette", "Rotom", "Swirlix", "Slurpuff",
    "Hop's Phantump", "Hop's Trevenant", "Team Rocket's Mimikyu", "Spectrier",
    "Munkidori", "Team Rocket's Diglett", "Team Rocket's Dugtrio", "Hitmontop",
    "Meditite", "Medicham", "Lunatone", "Solrock", "Regirock ex", "Groudon",
    "Cynthia's Gible", "Cynthia's Gabite", "Cynthia's Garchomp ex", "Riolu",
    "Mega Lucario ex", "Stunfisk ex", "Pancham", "Mega Hawlucha ex", "Carbink",
    "Rolycoly", "Carkol", "Coalossal", "Koraidon ex", "Okidogi", "Gastly",
    "Haunter", "Mega Gengar ex", "Team Rocket's Murkrow",
    "Team Rocket's Honchkrow", "Poochyena", "Mightyena", "Galarian Zigzagoon",
    "Galarian Linoone", "Galarian Obstagoon", "Cynthia's Spiritomb", "Scraggy",
    "Mega Scrafty ex", "N's Zorua", "N's Zoroark ex", "Vullaby",
    "Mandibuzz ex", "Pangoro", "Hoopa", "Fezandipiti ex", "Pecharunt",
    "Mawile", "Registeel ex", "Pawniard", "Bisharp", "Kingambit",
    "Togedemaru ex", "Dratini", "Dragonair", "Mega Dragonite ex", "Rayquaza",
    "N's Reshiram", "N's Zekrom", "Noibat", "Noivern", "Dreepy", "Drakloak",
    "Dragapult ex", "Team Rocket's Meowth", "Team Rocket's Kangaskhan ex",
    "Larry's Dunsparce", "Larry's Dudunsparce ex", "Skitty", "Delcatty",
    "Zangoose ex", "Larry's Starly", "Larry's Staravia", "Larry's Staraptor",
    "Fan Rotom", "Mega Audino ex", "Larry's Rufflet", "Larry's Braviary",
    "Larry's Komala", "Drampa", "Hop's Cramorant", "Terapagos", "Terapagos ex",
    "Acerola's Mischief", "Air Balloon", "Anthea & Concordia", "Boss's Orders",
    "Buddy-Buddy Poffin", "Canari", "Counter Gain", "Fighting Gong",
    "Forest of Vitality", "Glass Trumpet", "Iris's Fighting Spirit",
    "Light Ball", "Lillie's Determination", "Mega Signal", "Mystery Garden",
    "N's PP Up", "Night Stretcher", "Nighttime Mine", "Poké Pad",
    "Premium Power Pro", "Surfer", "Team Rocket's Archer",
    "Team Rocket's Ariana", "Team Rocket's Factory", "Team Rocket's Giovanni",
    "Team Rocket's Great Ball", "Team Rocket's Hypnotizer",
    "Team Rocket's Petrel", "Team Rocket's Proton",
    "Team Rocket's Transceiver", "Team Rocket's Watchtower", "Thick Scale",
    "Tool Scrapper", "Ultra Ball", "Urbain", "Waitress", "Prism Energy",
    "Team Rocket's Energy", "Spinarak", "Ariados", "Shaymin", "Snivy",
    "Servine", "Serperior", "Scatterbug", "Spewpa", "Vivillon", "Rowlet",
    "Dartrix", "Decidueye ex", "Fletchinder", "Talonflame", "Salandit",
    "Salazzle ex", "Turtonator", "Seel", "Dewgong", "Staryu",
    "Mega Starmie ex", "Lapras ex", "Amaura", "Aurorus", "Volcanion", "Shinx",
    "Luxio", "Luxray", "Dedenne", "Clefairy", "Mega Clefable ex", "Mawile",
    "Espurr", "Meowstic", "Spritzee", "Aromatisse", "Nosepass", "Probopass",
    "Hippopotas", "Hippowdon", "Landorus", "Binacle", "Barbaracle", "Tyrunt",
    "Tyrantrum", "Hawlucha", "Mega Zygarde ex", "Gastly", "Haunter", "Gengar",
    "Skorupi", "Drapion", "Yveltal ex", "Chien-Pao", "Mega Skarmory ex",
    "Honedge", "Doublade", "Aegislash", "Klefki", "Rattata", "Raticate",
    "Meowth ex", "Snorlax", "Bunnelby", "Diggersby", "Fletchling", "Furfrou",
    "Antique Jaw Fossil", "Antique Sail Fossil", "Core Memory",
    "Crushing Hammer", "Energy Search", "Energy Swatter",
    "Hole-Digging Shovel", "Jacinthe", "Judge", "Lumiose City",
    "Lumiose Galette", "Naveen", "Poké Ball", "Poké Pad", "Pokémon Catcher",
    "Potion", "Rosa's Encouragement", "Tarragon", "Growing Grass Energy",
    "Rocky Fighting Energy", "Telepathic Psychic Energy", "Weedle", "Kakuna",
    "Beedrill ex", "Carnivine", "Chespin", "Quilladin", "Chesnaught", "Vulpix",
    "Ninetales", "Ho-Oh", "Fennekin", "Braixen", "Delphox", "Litleo",
    "Mega Pyroar ex", "Remoraid", "Octillery", "Delibird", "Keldeo", "Froakie",
    "Frogadier", "Mega Greninja ex", "Bergmite", "Avalugg", "Wimpod",
    "Golisopod", "Mareep", "Flaaffy", "Ampharos", "Emolga", "Deoxys", "Deoxys",
    "Deoxys", "Deoxys", "Mega Floette ex", "Espurr", "Meowstic", "Phantump",
    "Trevenant", "Pumpkaboo", "Gourgeist ex", "Xerneas", "Sudowoodo", "Phanpy",
    "Donphan", "Baltoy", "Claydol", "Zubat", "Golbat", "Crobat", "Qwilfish",
    "Stunky", "Skuntank", "Trubbish", "Garbodor", "Skrelp", "Beldum", "Metang",
    "Metagross", "Ferroseed", "Ferrothorn", "Cobalion ex", "Mega Dragalge ex",
    "Goomy", "Sliggoo", "Goodra", "Tauros", "Patrat", "Watchog", "Minccino",
    "Cinccino ex", "Special Red Card", "Big Catch Net",
    "Book of Transformation", "AZ's Tranquility", "Philippe",
    "Roxie's Performance", "Emma", "Ange Floette", "Prism Tower",
    "Nitro Fire Energy", "Bubble Water Energy", "Magnet Steel Energy",
]


class PoffinDatabase():
    def __init__(self, host="mongodb://localhost:27017/",
                 db_name="poffindb"):
        self.client = MongoClient(host)
        self.db = self.client[db_name]

        self._oc_tournaments_cname = "oc_tournaments"
        self._oc_decklists_cname = "oc_decklists"
        self._or_tournaments_cname = "or_tournaments"
        self._or_decklists_cname = "or_decklists"
        self._cards_cname = "cards"

        self._init_collections()

    def _init_collections(self):
        collections_name = [
            self._oc_tournaments_cname,
            self._oc_decklists_cname,
            self._or_tournaments_cname,
            self._or_decklists_cname,
            self._cards_cname
        ]

        existing_c = self.db.list_collection_names()

        for c_name in collections_name:
            if c_name not in existing_c:
                self.db.create_collection(c_name)

        self._oc_tournaments: MongoCollection = \
            self.db[self._oc_tournaments_cname]
        self._oc_decklists: MongoCollection = \
            self.db[self._oc_decklists_cname]
        self._or_tournaments: MongoCollection = \
            self.db[self._or_tournaments_cname]
        self._or_decklists: MongoCollection = \
            self.db[self._or_decklists_cname]
        self._cards: MongoCollection = \
            self.db[self._cards_cname]

    def store_tournaments(self, oc_or, tournament_data):
        if oc_or == "oc":
            curr_db = self._oc_tournaments
        elif oc_or == "or":
            curr_db = self._or_tournaments
        else:
            raise ValueError

        for tournament in tournament_data:
            id = tournament["_id"]
            updt_filter = {"_id": id}
            updt = {"$set": tournament}

            result = curr_db.update_one(
                filter=updt_filter,
                update=updt,
                upsert=True
            )

            if result.acknowledged is False:
                raise RuntimeError

    def store_decklists(self, oc_or, decklists_data):
        if oc_or == "oc":
            curr_db = self._oc_decklists
        elif oc_or == "or":
            curr_db = self._or_decklists
        else:
            raise ValueError

        for decklist in decklists_data:
            id = decklist["_id"]
            updt_filter = {"_id": id}
            updt = {"$set": decklist}

            result = curr_db.update_one(
                filter=updt_filter,
                update=updt,
                upsert=True
            )

            if result.acknowledged is False:
                raise RuntimeError

    def read_all_tournaments(self, oc_or):
        if oc_or == "oc":
            collection = self._oc_tournaments
        elif oc_or == "or":
            collection = self._or_tournaments
        else:
            raise ValueError

        doc_list_aux = []

        cursor = collection.find({})
        for doc in cursor:
            doc_list_aux += [doc]

        return doc_list_aux

    def read_all_decklists(self, oc_or):
        if oc_or == "oc":
            collection = self._oc_decklists
        elif oc_or == "or":
            collection = self._or_decklists
        else:
            raise ValueError

        doc_list_aux = []

        cursor = collection.find({})
        for doc in cursor:
            doc_list_aux += [doc]

        return doc_list_aux

    def get_all_cards(self):
        return ALL_CARDS_LIST
