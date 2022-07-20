import random
Monster = ['Rathian', 'Rathalos', 'Basrios', 'Gravios', 'Khezu', 'Nargacuga', 'Tigrex', 'Diablos', 'Monoblos', 'Barioth', 'Bazelgeuse', 'Legiana', 'Paolumu', 'Espinas', 'Astalos', 'Tobi-Kadachi', 'Great Jagras', 'Great Girros', 'Dodogama', 'Zinogre', 'Magnamalo', 'Lunagaron', 'Odogaron', 'Barroth', 'Anjanath', 'Radobaan', 'Uragaan', 'Glavenus', 'Brachydios', 'Deviljho', 'Narajala', 'Velocidrome', 'Gendrome', 'Iodrome', 'Great Maccao', 'Great Izuchi', 'Great Jaggi', 'Great Baggi', 'Great Wroggi', 'Kulu-Ya-Ku', 'Yian-Kut-Ku', 'Gyperios', 'Aknosom', 'Qurupeco', 'Tzitzi-Ya-Ku', 'Pukei-Pukei', 'Malfestio', 'Yian Garuga', 'Plesioth', 'Beodotus', 'Lavasioth', 'Jyuratodus', 'Mizutsune', 'Somnacanth', 'Royal Ludroth', 'Lagiacrus', 'Agnaktor', 'Almudron', 'Bulldrome', 'Rajang', 'Congalala', 'Bishaten', 'Gammoth', 'Arzuros', 'Lagombi', 'Volvidon', 'Goss Harag', 'Garangolm', 'Tetradon', 'Tetscubra', 'Daimyo Hermitaur', 'Shogun Ceanataur', 'Shen Gaoren', 'Seltas', 'Seltas Queen', 'Ahtal-Ka', 'Rakna-Kadaki', 'Nerscylla', 'Chameleos', 'Kushala Daora', 'Teostra', 'Lunastra', 'Kirin', 'Vaal Hazak', 'Namielle', 'Velkhana', 'Nergigante', 'Ibushi', 'Narwa', 'Valstrax', 'Shaguru Magala', 'Malzeno', 'Nakarkos', 'Lao-Shan Lung', 'Zorah Magdaros', 'Dalamadur', 'Xeno`jiiva', 'Safi`jiiva', 'Gogmazios', 'Kulve Taroth', 'Gaismagorm', 'Dire Miralis', 'Alatreon', 'Fatalis']
Elements = ['Fire', 'Ice', 'Water', 'Thunder', 'Dragon', 'Fire/Ice' , 'Fire/Water', 'Fire/Thunder', 'Fire/', 'Ice/Water' , 'Ice/Thunder' , 'Ice/', 'Water/Thunder', 'Water/Dragon', 'Thunder/Dragon','None']
Aliments = ['Poison', 'Paralysis', 'Sleep', 'Blastblight', 'Poison/Paralysis', 'Poison/Sleep', 'Poison/Blastblight', 'Poison/Bleed', 'Paralysis/Sleep', 'Paralysis/Blastblight', 'Paralysis/Bleed', 'Sleep/Blastblight', 'Sleep/Bleed', 'Blastblight/Bleed', 'Stench/Poison', 'Stench/Paralysis', 'Stench/Sleep', 'Stench/Blastblight', 'Stench/Bleed', 'Frenzy', 'Bleed', 'Stench', 'Fire-Blastblight', 'None']
print('The New Species is a ' + random.choice(Monster) + ' with ' + random.choice(Elements) + ' and ' + random.choice(Aliments) + '.')
