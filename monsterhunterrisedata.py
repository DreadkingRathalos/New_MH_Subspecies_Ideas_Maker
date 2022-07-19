#Monster Hunter Rise Sunbreak is owned by Capcom
print('Welcome, what monster class are you looking for?')
Monster_Class=input('Flying Wyvern, Fanged Wyvern, Brute Wyvern, Bird Wyvern, Piscine Wyvern, Levianths, Fanged Beasts, Amphians, Carapaceons, Elder Dragons, Other')

if(Monster_Class == 'Flying Wyvern'or Monster_Class in 'Flying'):
    Monster=input('Rathian, Rathalos, Basrios, Khezu, Nargacuga, Tigrex, Diablos, Barioth, Bazelgeuse, Espinas')
    if(Monster == 'Rathian'):
            Apex=input('Base, Apex')
            if(Apex == 'Base'):
                Monster_Name = 'Monster: Rathian'
                Elements = 'Elements: Fire' 
                Aliments = 'Aliments: Fireblight, Poison'
                Weaknesses ='Weaknesses: Dragon'
                Breakable_Parts = 'Breakable Parts: Head, Back, Wings, and tail'
                Rare_Materials = 'Rare Materials: Rathian Plate, Rathian Ruby, Rathian Mantle'
            if(Apex == 'Apex'):
                Monster_Name = 'Monster: Apex Rathian'
                Elements = 'Elements: Fire'
                Aliments = 'Aliments: Fireblight, Poison, Deadly Poison' 
                Weaknesses = 'Weaknesses: Dragon'
                Breakable_Parts = 'Breakable Parts: Head, Back, Wings, and tail'
                Rare_Materials = 'Rare Materials: Rathian Plate, Rathian Ruby' 
    if(Monster == 'Rathalos'):
            Apex=input('Base, Apex')
            if(Apex == 'Base'):
                Monster_Name = 'Monster: Rathalos'
                Elements = 'Elements: Fire'
                Aliments = 'Aliments: Fireblight, Poison' 
                Weaknesses = 'Weaknesses: Dragon' 
                Breakable_Parts = 'Breakable Parts: Head, Back, Wings, and tail'
                Rare_Materials = 'Rare Materials: Rathalos Plate, Rathalos Ruby, Rathalos Mantle'
            if(Apex == 'Apex'):
                Monster_Name = 'Monster: Apex Rathalos'
                Elements = 'Elements: Fire'
                Aliments = 'Aliments: Fireblight, Poison' 
                Weaknesses = 'Weaknesses: Dragon' 
                Breakable_Parts = 'Breakable Parts: Head, Back, Wings, and tail'
                Rare_Materials = 'Rare Materials: Rathalos Plate, Rathalos Ruby'
    if(Monster == 'Basrios'):
        Monster_Name = 'Monster: Basrios'
        Elements = 'Elements: Fire'
        Aliments = 'Aliments: Fireblight, Poison, Sleep' 
        Weaknesses = 'Weaknesses: Water' 
        Breakable_Parts = 'Breakable Parts: Head, Back, Wings, and tail'
        Rare_Materials = 'Rare Materials: Wyvern Gem, Large Wyvern Gem'
    if(Monster == 'Khezu'):
        Monster_Name = 'Monster: Khezu'
        Elements = 'Elements: Thunder'
        Aliments = 'Aliments: Thunderblight, Paralysis' 
        Weaknesses = 'Weaknesses: Fire' 
        Breakable_Parts = 'Breakable Parts: Head, Body, and Legs'
        Rare_Materials = 'Rare Materials: Wyvern Gem, Large Wyvern Gem'
    if(Monster == 'Nargacuga'):
        Variant=input('Nargacuga, Lucent')
        if(Variant == 'Nargacuga'):
            Monster_Name = 'Monster: Nargacuga'
            Elements = 'Elements: None'
            Aliments = 'Aliments: None' 
            Weaknesses = 'Weaknesses: Thunder' 
            Breakable_Parts = 'Breakable Parts: Head, Wings, and tail'
            Rare_Materials = 'Rare Materials: Wyvern Gem, Large Wyvern Gem, Nargacuga Mantle'
        if(Variant == 'Lucent Nargacuga' or Variant in 'Lucent'):
            Monster_Name = 'Monster: Lucent Nargacuga'
            Elements = 'Elements: None'
            Aliments = 'Aliments: Poison' 
            Weaknesses = 'Weaknesses: Thunder' 
            Breakable_Parts = 'Breakable Parts: Head, Wings, and tail'
            Rare_Materials = 'Rare Materials: Large Wyvern Gem, Nargacuga'
    if(Monster == 'Tigrex'):
        Monster_Name = 'Monster: Tigrex'
        Elements = 'Elements: None'
        Aliments = 'Aliments: None' 
        Weaknesses = 'Weaknesses: Thunder' 
        Breakable_Parts = 'Breakable Parts: Head, Back, Wings, and tail'
        Rare_Materials = 'Rare Materials: Wyvern Gem, Tigrex Jaw, Large Wyvern Gem, Tigrex Mantle'
    if(Monster == 'Diablos'):
            Apex=input('Base, Apex')
            if(Apex == 'Base'):
                Monster_Name = 'Monster: Diablos'
                Elements = 'Elements: None'
                Aliments = 'Aliments: None' 
                Weaknesses = 'Weaknesses: Ice' 
                Breakable_Parts = 'Breakable Parts: Head, Back, and tail'
                Rare_Materials = 'Rare Materials: Wyvern Gem, Large Wyvern Gem'
            if(Apex == 'Apex'):
                Monster_Name = 'Monster: Apex Diablos'
                Elements = 'Elements: None'
                Aliments = 'Aliments: None' 
                Weaknesses = 'Weaknesses: Ice' 
                Breakable_Parts = 'Breakable Parts: Head, Back, and tail'
                Rare_Materials = 'Rare Materials: Wyvern Gem'
    if(Monster == 'Barioth'):
        Monster_Name = 'Monster: Barioth'
        Elements = 'Elements: Ice'
        Aliments = 'Aliments: Iceblight' 
        Weaknesses = 'Weaknesses: Fire' 
        Breakable_Parts = 'Breakable Parts: Head, Wings, and tail'
        Rare_Materials = 'Rare Materials: Wyvern Gem, Large Wyvern Gem'
    if(Monster == 'Bazelgeuse'):
        Variant=input('Base, Seething')
        if(Variant == 'Base'):
            Monster_Name = 'Monster: Bazelgeuse'
            Elements = 'Elements: Fire'
            Aliments = 'Aliments: Fireblight' 
            Weaknesses = 'Weaknesses: Thunder' 
            Breakable_Parts = 'Breakable Parts: Head, Wings, and tail'
            Rare_Materials = 'Rare Materials: Bazelgeuse Gem, Bazelgeuse Mantle'
        if(Variant == 'Seething'):
            Monster_Name = 'Monster: Seething Bazelgeuse'
            Elements = 'Elements: Fire'
            Aliments = 'Aliments: Fireblight' 
            Weaknesses = 'Weaknesses: Ice' 
            Breakable_Parts = 'Breakable Parts: Head, Wings, and tail'
            Rare_Materials = 'Rare Materials: Bazelgeuse Mantle'
    if(Monster == 'Espinas'):
        Monster_Name = 'Monster: Espinas'
        Elements = 'Elements: Fire'
        Aliments = 'Aliments: Fireblight, Poison, Paralysis' 
        Weaknesses = 'Weaknesses: Ice' 
        Breakable_Parts = 'Breakable Parts: Head, Back, Belly, Wings, and tail'
    if(Monster == 'Seregios'):
        Monster_Name = 'Monster: Seregios'
        Elements = 'Elements: None'
        Aliments = 'Aliments: Bleeding' 
        Weaknesses = 'Weaknesses: Thunder' 
        Breakable_Parts = 'Breakable Parts: Head, Wings, and tail'
        Rare_Materials = 'Rare Materials: Seregios Lens'
    if(Monster == 'Astalos'):
        Monster_Name = 'Monster: Astalos'
        Elements = 'Elements: Thunder'
        Aliments = 'Aliments: Thunderblight, Paralysis' 
        Weaknesses = 'Weaknesses: Ice' 
        Breakable_Parts = 'Breakable Parts: Head, Back, Wings, and tail'
        Rare_Materials = 'Astalos Mantle'

if(Monster_Class == 'Fanged Wyvern'or Monster_Class in 'Fanged'):
    Monster=input('Tobi-Kadachi, Zinogre, Magnamalo, Lunagaron')
    if(Monster == 'Tobi-Kadachi'):
        Monster_Name = 'Monster: Tobi-Kadachi'
        Elements = 'Elements: Thunder'
        Aliments = 'Weaknesses: Water' 
        Weaknesses = 'Aliments: Thunderblight'
        Breakable_Parts = 'Breakable Parts: Head, Back, and tail'
    if(Monster == 'Zinogre'):
            Apex=input('Base, Apex')
            if(Apex == 'Base'):
                Monster_Name = 'Monster: Zinogre'
                Elements = 'Elements: Thunder'
                Aliments = 'Aliments: Thunderblight' 
                Weaknesses = 'Weaknesses: Ice' 
                Breakable_Parts = 'Breakable Parts: Head, Back, Legs, and tail'
                Rare_Materials = 'Rare Materials: Zinogre Plate, Zinogre Jasper, Zinogre Mantle'
            if(Apex == 'Apex'):
                Monster_Name = 'Monster: Apex Zinogre'
                Elements = 'Elements: Thunder'
                Aliments = 'Aliments: Thunderblight' 
                Weaknesses = 'Weaknesses: Ice' 
                Breakable_Parts = 'Breakable Parts: Head, Back, Legs, and tail'
                Rare_Materials = 'Rare Materials: Zinogre Plate, Zinogre Jasper'
    if(Monster == 'Magnamalo'):
        Variant=input('Magnamalo, Scorned')
        if(Variant == 'Magnamalo'):
            Monster_Name = 'Monster: Magnamalo'
            Elements = 'Elements: None'
            Aliments = 'Aliments: Blast-Fireblight' 
            Weaknesses = 'Weaknesses: Water' 
            Breakable_Parts = 'Breakable Parts: Head, Back, Scutes, and tail'
            Rare_Materials = 'Rare Materials: Magnamalo Plate, Purple Magna Orb, Magnamalo Orb'
        if(Variant == 'Scorned Magnamalo' or Variant in 'Scorned'):
            Monster_Name = 'Monster: Scorned Magnamalo'
            Elements = 'Elements: None'
            Aliments = 'Aliments: Blast-Fireblight' 
            Weaknesses = 'Weaknesses: Water' 
            Breakable_Parts = 'Breakable Parts: Head, Back, Scutes, and tail'
            Rare_Materials = 'Rare Materials: Mangamalo Orb'
    if(Monster == 'Lunagaron'):
        Monster_Name = 'Monster: Lunagaron'
        Elements = 'Elements: Ice'
        Aliments = 'Aliments: Iceblight' 
        Weaknesses = 'Weaknesses: Dragon' 
        Breakable_Parts = 'Breakable Parts: Head, Claws, Back, and tail'
        Rare_Materials = 'Rare Materials: Lunagaron Frostjewel'

if(Monster_Class == 'Brute Wyvern' or Monster_Class in 'Brute'):
    Monster=input('Barroth, Anjanath')
    if(Monster == 'Barroth'):
            print('Monster: Barroth, Elements: Water, Aliments: Waterblight, Muddy, Weaknesses: Water(Mud) Fire(No Mud), Breakable Parts: Head, Back, Arms, and tail')
            print('Rare Materials: Wyvern Gem, Large Wyvern Gem')
    if(Monster == 'Anjanath'):
            print('Monster: Anjanath, Elements: Fire, Aliments: Fireblight, Weaknesses: Water, Breakable Parts: Head, Legs, and tail')
            print('Rare Materials: Anjanath Plate, Anjanath Gem, Anjanath Mantle')

if(Monster_Class == 'Bird Wyvern' or Monster_Class in 'Bird'):
    Monster=input('Great Izuchi, Great Baggi, Great Wroggi, Kulu-Ya-Ku, Aknosom, Pukei-Pukei')
    if(Monster == 'Great Izuchi'):
        print('Monster: Great Izuchi, Elements: None, Aliments: None, Weaknesses: Thunder, Breakable Parts: Head and Tail')
        print('Rare Materials: Bird Wyvern Gem, Fey Wyvern Gem')
    if(Monster == 'Great Baggi'):
        print('Monster: Great Baggi, Elements: None, Aliments: Sleep, Weaknesses: Fire, Breakable Parts: Head')
        print('Rare Materials: Bird Wyvern Gem, Fey Wyvern Gem')
    if(Monster == 'Great Wroggi'):
        print('Monster: Great Wroggi, Elements: None, Aliments: Poison, Weaknesses: Ice, Breakable Parts: Head')
        print('Rare Materials: Bird Wyvern Gem, Fey Wyvern Gem')
    if(Monster == 'Kulu-Ya-Ku'):
            print('Monster: Kulu-Ya-Ku, Elements: None, Aliments: None, Weaknesses: Water, Breakable Parts: Head and Arms')
            print('Rare Materials: Bird Wyvern Gem, Fey Wyvern Gem')
    if(Monster == 'Aknosom'):
            print('Monster: Aknosom, Elements: Fire, Aliments: Fireblight, Weaknesses: Water, Breakable Parts: Head, Wings, and tail')
            print('Rare Materials: Bird Wyvern Gem, Fey Wyvern Gem')
    if(Monster == 'Pukei-Pukei'):
            print('Monster: Pukei-Pukei, Elements: None, Aliments: None, Weaknesses: Thunder, Breakable Parts: Head, Wings, and Tail')
            print('Rare Materials: Bird Wyvern Gem, Fey Wyvern Gem')

if(Monster_Class == 'Piscine Wyvern'or Monster_Class in 'Piscine'):
    Monster=input('Jyuratodus')
    if(Monster == 'Jyuratodus'):
        print('Monster: Jyuratodus, Elements: Water, Aliments: Waterblight, Muddy, Weaknesses: Water (Mud)/Thunder (No Mud), Breakable Parts: Head, Back, and tail')

if(Monster_Class == 'Levianths'):
    Monster=input('Mizutsune, Somnacanth, Royal Ludroth, Almudron')
    if(Monster == 'Mizutsune'):
        Apex=input('Base, Apex')
        if(Apex == 'Base'):
            print('Monster: Mizutsune, Elements: Water, Aliments: Waterblight, Bubble, Weaknesses: Thunder, Breakable Parts: Head, Front Legs, and tail')
            print('Rare Materials: Mizutsune Plate, Mizutsune Orb, Mizutsune Mantle')
        if(Apex == 'Apex'):
            print('Monster: Apex Mizutsune, Elements: Water, Aliments: Waterblight, Fire-Blastblight, Bubble, Weaknesses: Thunder, Breakable Parts: Head, Front Legs, and tail')
            print('Rare Materials: Mizutsune Plate, Mizutsune Ruby')
    if(Monster == 'Somnacanth'):
        Subspecies=input('Base or Aurora')
        if(Subspecies == 'Base'):
            print('Monster: Somnacanth, Elements: None, Aliments: Sleep, Weaknesses: Thunder, Breakable Parts: Head, Arms, and tail')
            print('Rare Materials: Wyvern Gem, Large Wyvern Gem')
        if(Subspecies == 'Aurora'):
            print('Monster: Aurora Somnacanth, Elements: Ice, Aliments: Iceblight, Weaknesses: Fire, Breakable Parts: Head, Arms, and tail')
            print('Rare Materials: Large Wyvern Gem')
    if(Monster == 'Royal Ludroth'):
        print('Monster: Royal Ludroth, Elements: Water, Aliments: Waterblight, Weaknesses: Fire, Breakable Parts: Head, Creat, and tail')
        print('Rare Materials: Wyvern Gem, Large Wyvern Gem')
    if(Monster == 'Almudron'):
        Subspecies=input('Base or Magma')
        if(Subspecies == 'Base'):
            print('Monster: Almudron, Elements: Water, Aliments: Waterblight, Muddy, Weaknesses: Fire, Breakable Parts: Head, Back, and tail')
            print('Rare Materials: Almudron Plate, Golden Almudron Orb, Almudron Mantle')
        if(Subspecies == 'Magma'):
            print('Monster: Magma Almudron, Elements: Fire, Aliments: Fireblight, Weaknesses: Water, Breakable Parts: Head, Back, and tail')
            print('Rare Materials: Almudron Plate, Golden Almudron Orb, Almudron Mantle')

if(Monster_Class == 'Fanged Beasts'or Monster_Class in 'Beasts'):
    Monster=input('Rajang, Bishaten, Arzuros, Lagombi, Volvidon, Goss Harag')
    if(Monster == 'Rajang'):
        Variant=input('Rajang, Furious')
        if(Variant == 'Rajang'):
            print('Monster: Rajang, Elements: Thunder, Aliments: Thunderblight, Weaknesses: Ice, Breakable Parts: Head, Arms, and tail')
            print('Rare Materials: Beast Gem, Large Beast Gem')
        if(Variant == 'Rajang' or Variant in 'Furious'):
            print('Monster: Furious Rajang, Elements: Thunder, Aliments: Thunderblight, Weaknesses: Ice, Breakable Parts: Head, and Arms')
            print('Rare Materials: Large Beast Gem')
    if(Monster == 'Bishaten'):
        Subspecies=input('Base or Blood Orange')
        if(Subspecies == 'Base'):
                print('Monster: Bishaten, Elements: None, Aliments: Paralysis, Poison, Weaknesses: Dragon, Breakable Parts: Head, Wings, and tail')
                print('Rare Materials: Beast Gem, Large Beast Gem')
        if(Subspecies == 'Blood Orange' or Subspecies in 'Blood Orange'):
                print('Monster: Blood Orange Bishaten, Elements: Fire, Aliments: Fireblight, Weaknesses: Water, Breakable Parts: Head, Wings, and tail')
                print('Rare Materials: Large Beast Gem')
    if(Monster == 'Arzuros'):
        Apex=input('Base, Apex')
        if(Apex == 'Base'):
            print('Monster: Arzuros, Elements: None, Aliments: None, Weaknesses: Fire, Breakable Parts: Arms')
            print('Rare Materials: Beast Gem, Large Beast Gem')
        if(Apex == 'Apex'):
            print('Monster: Apex Arzuros, Elements: None, Aliments: None, Weaknesses: Ice, Breakable Parts: Arms')
            print('Rare Materials: Beast Gem')
    if(Monster == 'Lagombi'):
        print('Monster: Lagombi, Elements: Ice, Aliments: Iceblight, Weaknesses: Fire, Breakable Parts: Head, and Belly')
        print('Rare Materials: Beast Gem, Large Beast Gem')
    if(Monster == 'Volvidon'):
            print('Monster: Volvidon, Elements: None, Aliments: Stench, Weaknesses: Water, Breakable Parts: Back')
            print('Rare Materials: Beast Gem, Large Beast Gem')
    if(Monster == 'Goss Harag'):
        print('Monster: Goss Harag, Elements: Ice, Aliments: Iceblight, Weaknesses: Fire, Breakable Parts: Head, and Arms')
        print('Rare Materials: Beast Gem, Large Beast Gem')
    if(Monster == 'Garangolm'):
        print('Monster: Garangolm, Elements: , Aliments: , Weaknesses: Thunder, Breakable Parts: Head, and Arms')
        print('Rare Materials: Large Beast Gem')

if(Monster_Class == 'Amphians'):
    Monster=input('Tetradon')
    if(Monster == 'Tetradon'):
        print('Monster: Tetradon, Elements: Water, Aliments: Waterblight, Weaknesses: Thunder, Breakable Parts: Head, and Arms')

if(Monster_Class == 'Carapaceons'):
    Monster=input('Daimyo Hermitaur, Shogun Ceanataur')
    if(Monster == 'Daimyo Hermitaur'):
        print('Monster: Daimyo Hermitaur, Elements: Water, Aliments: Waterblight, Weaknesses: Ice, Breakable Parts: Arms and Shell')
    if(Monster == 'Shogun Ceanataur'):
        print('Monster: Shogun Ceanataur, Elements: None, Aliments: Bleeding, Weaknesses: Ice, Breakable Parts: Arms, and Shell')

if(Monster_Class == 'Temnoceran'or Monster_Class in 'Temnoceran'):
    Monster=input('Rakna-Kadaki')
    if(Monster == 'Rakna-Kadaki'):
        Subspecies=input('Base or Pyre')
        if(Subspecies == 'Base'):
            Monster_Name = 'Monster: Rakna-Kadaki'
            Elements = 'Elements: Fire'
            Aliments = 'Aliments: Fireblight, Webbed' 
            Weaknesses = 'Weaknesses: Ice' 
            Breakable_Parts = 'Breakable Parts: Head, Claws Legs, and Abdomen'
            Rare_Materials = ''
        if(Subspecies == 'Pyre'):
            Monster_Name = 'Monster: Pyre Rakna-Kadaki'
            Elements = 'Elements: Fire'
            Aliments = 'Aliments: Fireblight, Blastblight, Webbed' 
            Weaknesses = 'Weaknesses: Water' 
            Breakable_Parts = 'Breakable Parts: Head, Claws, Legs, and Abdomen'
            Rare_Materials = ''

if(Monster_Class == 'Elder Dragons'):
    Monster=input('Chameleos, Kushala Doara, Teostra, Ibushi, Narwa, Crimson Glow Valstrax, Shaguru Magala, Malzeno')
    if(Monster == 'Chameleos'):
        Monster_Name = 'Monster: Chameleos'
        Elements = 'Elements: None'
        Aliments = 'Aliments: Poison, Severe Poison' 
        Weaknesses = 'Weaknesses: Fire' 
        Breakable_Parts = 'Breakable Parts: Head, Wings, and tail'
        Rare_Materials = 'Rare Materials: Chameleos Gem, Elder Dragon Gem'
    if(Monster == 'Kushala Doara' or Monster in 'Kushala'):
        Monster_Name = 'Monster: Kushala Doara'
        Elements = 'Elements: Ice, Dragon'
        Aliments = 'Aliments: Iceblight, Dragonblight' 
        Weaknesses = 'Weaknesses: Thunder/Dragon' 
        Breakable_Parts = 'Breakable Parts: Head, Wings, and tail'
        Rare_Materials = 'Rare Materials: Kushala Gem, Elder Dragon Gem'
    if(Monster == 'Teostra'):
        Monster_Name = 'Monster: Teostra'
        Elements = 'Elements: Fire'
        Aliments = 'Aliments: Fireblight, Blastblight' 
        Weaknesses = 'Weaknesses: Water/Ice' 
        Breakable_Parts = 'Breakable Parts: Head, Wings, and tail'
        Rare_Materials = 'Rare Materials: Teostra Gem, Elder Dragon Gem'
    if(Monster == 'Ibushi'):
        Monster_Name = 'Monster: Wind Serpent Ibushi'
        Elements = 'Elements: Dragon'
        Aliments = 'Aliments: Dragonblight' 
        Weaknesses = 'Weaknesses: Dragon' 
        Breakable_Parts = 'Breakable Parts: Head, Wings, and tail'
        Rare_Materials = 'Rare Materials: Wind Serpemt Orb, Wind Draonspire'
    if(Monster == 'Narwa'):
        Variant=input('Narwa, Allmother Narwa')
        if(Variant == 'Narwa'):
            Monster_Name = 'Monster: Thunder Serpent Narwa'
            Elements = 'Elements: Thunder'
            Aliments = 'Aliments: Thunderblight' 
            Weaknesses = 'Weaknesses: Dragon' 
            Breakable_Parts = 'Breakable Parts: Head, Wings, and tail'
            Rare_Materials = 'Rare Materials: Thunder Serpent Orb'  
        if(Variant == 'Allmother Narwa'):
            Monster_Name = 'Monster: Narwa the Allmother'
            Elements = 'Elements: Thunder, Dragon'
            Aliments = 'Aliments: Thunderblight, Dragonblight' 
            Weaknesses = 'Weaknesses: Dragon' 
            Breakable_Parts = 'Breakable Parts: Head, Wings, and tail'
            Rare_Materials = 'Rare Materials: Orb of Orgin, Mantle of Orgin'
    if(Monster == 'Crimson Glow Valstrax' or Monster in 'Valstrax'):
            Monster_Name = 'Monster: Crimson Glow Valstrax'
            Elements = 'Elements: Dragon'
            Aliments = 'Aliments: Dragonblight' 
            Weaknesses = 'Weaknesses: Fire/Water/Thunder/Ice' 
            Breakable_Parts = 'Breakable Parts: Head, Wings, Back and tail'
            Rare_Materials = 'Rare Materials: Valstrax Gem, Valstrax Mantle, Elder Dragon Gem'
    if(Monster == 'Shaguru Magala' or Monster in 'Shaguru'):
            Monster_Name = 'Monster: Shaguru Magala'
            Elements = 'Elements: None'
            Aliments = 'Aliments: Frenzy' 
            Weaknesses = 'Weaknesses: Dragon' 
            Breakable_Parts = 'Breakable Parts: Head, Wingarms, and tail'
            Rare_Materials = 'Rare Materials: Shaguru Mantle'
    if(Monster == 'Malzeno'):
            Monster_Name = 'Monster: Malzeno'
            Elements = 'Elements: Dragon'
            Aliments = 'Aliments: Dragonblight, Bloodblight' 
            Weaknesses = 'Weaknesses: Dragon' 
            Breakable_Parts = 'Breakable Parts: Head, Wings, and tail'
            Rare_Materials = 'Rare Materials: Malzeno Bloodstone'
    if(Monster == 'Gaismagorm'):
            Monster_Name = 'Monster: Gaismagorm'
            Elements = 'Elements: None'
            Aliments = 'Aliments: Bloodblight' 
            Weaknesses = 'Weaknesses: Dragon' 
            Breakable_Parts = 'Breakable Parts: Head, Wings, and tail'
            Rare_Materials = 'Rare Materials: Abyssal Dragonspire'

if(Monster_Class == 'Others'):
    Monster=input('Gore Magala')
    if(Monster == 'Gore Magala'):
            Monster_Name = 'Monster: Gore Magala'
            Elements = 'Elements: None'
            Aliments = 'Aliments: Frenzy' 
            Weaknesses = 'Weaknesses: Fire' 
            Breakable_Parts = 'Breakable Parts: Head, Feelers, Wingarms, and tail'
            Rare_Materials = 'Rare Materials: Gore Mantle'
print('{Monster_Name}')
print('{Elements}')
print('{Aliments}')
print('{Weaknesses}')
print('{Breakable_Parts}')
print('{Rare_Materials}')
