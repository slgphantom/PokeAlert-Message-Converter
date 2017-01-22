# -*- coding: utf-8 -*-
import json
import requests
import re
import time
from time import strftime


# Dictionary for converting Pokemon_English_Name into Pokemon_id
pkm = {'Bulbasaur' :'1' , 'Ivysaur' :'2' , 'Venusaur' :'3' , 'Charmander' :'4' , 'Charmeleon' :'5' , 'Charizard' :'6' , 'Squirtle' :'7' , 'Wartortle' :'8' , 'Blastoise' :'9' , 'Caterpie' :'10' , 'Metapod' :'11' , 'Butterfree' :'12' , 'Weedle' :'13' , 'Kakuna' :'14' , 'Beedrill' :'15' , 'Pidgey' :'16' , 'Pidgeotto' :'17' , 'Pidgeot' :'18' , 'Rattata' :'19' , 'Raticate' :'20' , 'Spearow' :'21' , 'Fearow' :'22' , 'Ekans' :'23' , 'Arbok' :'24' , 'Pikachu' :'25' , 'Raichu' :'26' , 'Sandshrew' :'27' , 'Sandslash' :'28' , 'Nidoran_female' :'29' , 'Nidorina' :'30' , 'Nidoqueen' :'31' , 'Nidoran_male' :'32' , 'Nidorino' :'33' , 'Nidoking' :'34' , 'Clefairy' :'35' , 'Clefable' :'36' , 'Vulpix' :'37' , 'Ninetales' :'38' , 'Jigglypuff' :'39' , 'Wigglytuff' :'40' , 'Zubat' :'41' , 'Golbat' :'42' , ' Oddish' :'43' , 'Gloom' :'44' , 'Vileplume' :'45' , 'Paras' :'46' , 'Parasect' :'47' , 'Venonat' :'48' , 'Venomoth' :'49' , 'Diglett' :'50' , 'Dugtrio' :'51' , 'Meowth' :'52' , 'Persian' :'53' , 'Psyduck' :'54' , 'Golduck' :'55' , 'Mankey' :'56' , 'Primeape' :'57' , 'Growlithe' :'58' , 'Arcanine' :'59' , 'Poliwag' :'60' , 'Poliwhirl' :'61' , 'Poliwrath' :'62' , 'Abra' :'63' , 'Kadabra' :'64' , 'Alakazam' :'65' , 'Machop' :'66' , 'Machoke' :'67' , 'Machamp' :'68' , 'Bellsprout' :'69' , 'Weepinbell' :'70' , 'Victreebel' :'71' , 'Tentacool' :'72' , 'Tentacruel' :'73' , 'Geodude' :'74' , 'Graveler' :'75' , 'Golem' :'76' , 'Ponyta' :'77' , 'Rapidash' :'78' , 'Slowpoke' :'79' , 'Slowbro' :'80' , 'Magnemite' :'81' , 'Magneton' :'82' , ' "Farfetch d"' :'83' , 'Doduo' :'84' , 'Dodrio' :'85' , 'Seel' :'86' , 'Dewgong' :'87' , 'Grimer' :'88' , 'Muk' :'89' , 'Shellder' :'90' , 'Cloyster' :'91' , 'Gastly' :'92' , 'Haunter' :'93' , 'Gengar' :'94' , 'Onix' :'95' , 'Drowzee' :'96' , 'Hypno' :'97' , 'Krabby' :'98' , 'Kingler' :'99' , 'Voltorb' :'100' , 'Electrode' :'101' , 'Exeggcute' :'102' , 'Exeggutor' :'103' , 'Cubone' :'104' , 'Marowak' :'105' , 'Hitmonlee' :'106' , 'Hitmonchan' :'107' , 'Lickitung' :'108' , 'Koffing' :'109' , 'Weezing' :'110' , 'Rhyhorn' :'111' , 'Rhydon' :'112' , 'Chansey' :'113' , 'Tangela' :'114' , 'Kangaskhan' :'115' , 'Horsea' :'116' , 'Seadra' :'117' , 'Goldeen' :'118' , 'Seaking' :'119' , 'Staryu' :'120' , 'Starmie' :'121' , 'Mr. Mime' :'122' , 'Scyther' :'123' , 'Jynx' :'124' , 'Electabuzz' :'125' , 'Magmar' :'126' , 'Pinsir' :'127' , 'Tauros' :'128' , 'Magikarp' :'129' , 'Gyarados' :'130' , 'Lapras' :'131' , 'Ditto' :'132' , 'Eevee' :'133' , 'Vaporeon' :'134' , 'Jolteon' :'135' , 'Flareon' :'136' , 'Porygon' :'137' , 'Omanyte' :'138' , 'Omastar' :'139' , 'Kabuto' :'140' , 'Kabutops' :'141' , 'Aerodactyl' :'142' , 'Snorlax' :'143' , 'Articuno' :'144' , 'Zapdos' :'145' , 'Moltres' :'146' , 'Dratini' :'147' , 'Dragonair' :'148' , 'Dragonite' :'149' , 'Mewtwo' :'150' , 'Mew' :'151'}

# Dictionary for converting Pokemon_Chinese_Name into Pokemon_id
pkm_hk = {u'\u5c3c\u591a\u738b': '34', u'\u9b3c\u65af\u901a': '93', u'\u98db\u5929\u87b3\u8782': '123', u'\u50ac\u7720\u7378': '97', u'\u5361\u7f8e\u9f9c': '8', u'\u6bd4\u6bd4\u9ce5': '17', u'\u5949\u795e\u72ac': '59', u'\u842c\u5e74\u87f2': '140', u'\u868a\u9999\u874c\u86aa': '60', u'\u76ae\u76ae': '35', u'\u80a5\u6ce2\u7403': '40', u'\u5927\u529b': '67', u'\u5c0f\u78c1\u602a': '81', u'\u516d\u5c3e': '37', u'\u9ad8\u7ac7\u8c93': '53', u'\u9b54\u96c0': '22', u'\u591a\u8173\u6c34\u6bcd': '73', u'\u5927\u820c\u982d': '108', u'\u7a7f\u5c71\u9f20': '27', u'\u5c24\u57fa\u7d0d': '64', u'\u5361\u62c9\u5361\u62c9': '104', u'\u591a\u591a\u5229': '85', u'\u5947\u7570\u7a2e\u5b50': '1', u'\u50bb\u9d28': '54', u'\u6efe\u52d5\u5ca9': '76', u'\u8c9d\u6bbc\u602a': '90', u'\u6bdb\u6bdb\u87f2': '48', u'\u721b\u6ce5\u602a': '88', u'\u9435\u7532\u87f2': '11', u'\u5de8\u9257\u87f9': '99', u'\u8ff7\u4f60\u9f8d': '147', u'\u5927\u6bd4\u9ce5': '18', u'\u9435\u7532\u7280\u725b': '111', u'\u9bc9\u9b5a\u738b': '129', u'\u9bc9\u9b5a\u9f8d': '130', u'\u9435\u6bbc\u86f9': '14', u'\u5438\u76e4\u5c0f\u4e11': '122', u'\u9435\u7532\u8c9d': '91', u'\u942e\u5200\u87f2': '141', u'\u96f7\u8d85': '26', u'\u98df\u5922\u7378': '96', u'\u6c99\u53e4\u62c9': '106', u'\u5730\u9f20': '50', u'\u7334\u602a': '56', u'\u5361\u6bd4\u7378': '143', u'\u98db\u523a\u6d77\u99ac': '117', u'\u555f\u66b4\u9f8d': '149', u'\u6025\u51cd\u9ce5': '144', u'\u803f\u9b3c': '94', u'\u9b3c\u96c0': '21', u'\u6ce2\u6ce2': '16', u'\u96fb\u64ca\u7378': '125', u'\u5de8\u83c7\u87f2': '47', u'\u5c0f\u54e5\u9054': '19', u'\u5927\u529b\u86d9': '62', u'\u96f7\u4f0a\u8c9d': '135', u'\u5927\u9257\u87f9': '98', u'\u5947\u7570\u82b1': '3', u'\u5927\u53e3\u8760': '42', u'\u5927\u5446\u7378': '80', u'\u9d28\u5634\u706b\u9f8d': '126', u'\u6bd2\u6c23\u96d9\u5b50': '110', u'\u4e5d\u5c3e': '38', u'\u7a7f\u5c71\u738b': '28', u'\u9b54\u9b6f\u98a8': '49', u'\u91d1\u9b5a\u738b': '119', u'\u8b77\u4e3b\u72ac': '58', u'\u706b\u4f0a\u8c9d': '136', u'\u5c3c\u7f8e\u862d': '29', u'\u9257\u5200\u7532\u87f2': '127', u'\u9435\u8155': '66', u'\u5927\u98df\u82b1': '71', u'\u6bd4\u5361\u8d85': '25', u'\u5c3c\u7f8e\u863f': '30', u'\u5587\u53ed\u82bd': '69', u'\u9b3c\u65af': '92', u'\u5c0f\u706b\u9f8d': '4', u'\u5c3c\u591a\u90ce': '32', u'\u5c3c\u7f8e\u540e': '31', u'\u5947\u7570\u8349': '2', u'\u721b\u6ce5\u7378': '89', u'\u6ce2\u97f3\u8760': '41', u'\u7acb\u65b9\u7378': '137', u'\u9577\u7c50\u602a': '114', u'\u54e5\u9054': '20', u'\u5c0f\u5446\u7378': '79', u'\u5c0f\u706b\u99ac': '77', u'\u963f\u67cf\u602a': '24', u'\u5927\u773c\u6c34\u6bcd': '72', u'\u7368\u89d2\u91d1\u9b5a': '118', u'\u9ad8\u8d85\u9d28': '55', u'\u5361\u65af': '63', u'\u4e09\u982d\u5730\u9f20': '51', u'\u602a\u5473\u82b1': '44', u'\u5927\u91dd\u8702': '15', u'\u7d05\u5507\u5a03': '124', u'\u706b\u7206\u7334': '57', u'\u706b\u9ce5': '146', u'\u602a\u529b': '68', u'\u86cb\u86cb': '102', u'\u5674\u58a8\u6d77\u99ac': '116', u'\u8611\u83c7\u87f2': '46', u'\u706b\u6050\u9f8d': '5', u'\u9739\u9742\u86cb': '100', u'\u76ae\u53ef\u65af': '36', u'\u767e\u8b8a\u602a': '132', u'\u53e3\u5446\u82b1': '70', u'\u7da0\u6bdb\u87f2': '10', u'\u6930\u6a39\u7378': '103', u'\u5674\u706b\u9f8d': '6', u'\u6bd2\u6c23\u4e38': '109', u'\u767d\u6d77\u7345': '87', u'\u5c0f\u6d77\u7345': '86', u'\u70c8\u7130\u99ac': '78', u'\u5bcc\u8fea': '65', u'\u868a\u9999\u86d9': '61', u'\u5927\u5ca9\u86c7': '95', u'\u5316\u77f3\u98db\u9f8d': '142', u'\u6efe\u52d5\u77f3': '75', u'\u55b5\u55b5\u602a': '52', u'\u888b\u7378': '115', u'\u5409\u5229\u86cb': '113', u'\u5c3c\u591a\u5229': '33', u'\u9738\u738b\u82b1': '45', u'\u8d85\u5922\u5922': '150', u'\u5c0f\u62f3\u77f3': '74', u'\u884c\u8def\u8349': '43', u'\u683c\u62c9\u683c\u62c9': '105', u'\u591a\u523a\u83ca\u77f3\u7378': '139', u'\u6d77\u661f\u661f': '120', u'\u6bd4\u83ef\u62c9': '107', u'\u80cc\u80cc\u9f8d': '131', u'\u54c8\u53e4\u9f8d': '148', u'\u83ca\u77f3\u7378': '138', u'\u96f7\u9ce5': '145', u'\u5922\u5922': '151', u'\u706b\u8525\u9d28': '83', u'\u6c34\u7bad\u9f9c': '9', u'\u8eca\u5398\u9f9c': '7', u'\u7368\u89d2\u87f2': '13', u'\u9435\u7532\u66b4\u9f8d': '112', u'\u4e09\u5408\u4e00\u78c1\u602a': '82', u'\u963f\u67cf\u86c7': '23', u'\u591a\u591a': '84', u'\u6c34\u4f0a\u8c9d': '134', u'\u96f7\u9706\u86cb': '101', u'\u6ce2\u6ce2\u7403': '39', u'\u5df4\u4ed6\u8776': '12', u'\u5bf6\u77f3\u6d77\u661f': '121', u'\u5927\u96bb\u725b': '128', u'\u4f0a\u8c9d': '133'}

# Dictionary for converting Moves_English_name into Moves_id
mv = {"Thunder Shock" : "1" , "Quick Attack" : "2" , "Scratch" : "3" , "Ember" : "4" , "Vine Whip" : "5" , "Tackle" : "6" , "Razor Leaf" : "7" , "Take Down" : "8" , "Water Gun" : "9" , "Bite" : "10" , "Pound" : "11" , "Double Slap" : "12" , "Wrap" : "13" , "Hyper Beam" : "14" , "Lick" : "15" , "Dark Pulse" : "16" , "Smog" : "17" , "Sludge Bomb" : "18" , "Metal Claw" : "19" , "Vice Grip" : "20" , "Flame Wheel" : "21" , "Megahorn" : "22" , "Wing Attack" : "23" , "Flamethrower" : "24" , "Sucker Punch" : "25" , "Dig" : "26" , "Low Kick" : "27" , "Cross Chop" : "28" , "Psycho Cut" : "29" , "Psybeam" : "30" , "Earthquake" : "31" , "Stone Edge" : "32" , "Ice Punch" : "33" , "Heart Stamp" : "34" , "Discharge" : "35" , "Flash Cannon" : "36" , "Peck" : "37" , "Drill Peck" : "38" , "Ice Beam" : "39" , "Blizzard" : "40" , "Air Slash" : "41" , "Heat Wave" : "42" , "Twineedle" : "43" , "Poison Jab" : "44" , "Aerial Ace" : "45" , "Drill Run" : "46" , "Petal Blizzard" : "47" , "Mega Drain" : "48" , "Bug Buzz" : "49" , "Poison Fang" : "50" , "Night Slash" : "51" , "Slash" : "52" , "Bubble Beam" : "53" , "Submission" : "54" , "Karate Chop" : "55" , "Low Sweep" : "56" , "Aqua Jet" : "57" , "Aqua Tail" : "58" , "Seed Bomb" : "59" , "Psyshock" : "60" , "Rock Throw" : "61" , "Ancient Power" : "62" , "Rock Tomb" : "63" , "Rock Slide" : "64" , "Power Gem" : "65" , "Shadow Sneak" : "66" , "Shadow Punch" : "67" , "Shadow Claw" : "68" , "Ominous Wind" : "69" , "Shadow Ball" : "70" , "Bullet Punch" : "71" , "Magnet Bomb" : "72" , "Steel Wing" : "73" , "Iron Head" : "74" , "Parabolic Charge" : "75" , "Spark" : "76" , "Thunder Punch" : "77" , "Thunder Shock" : "78" , "Thunderbolt" : "79" , "Twister" : "80" , "Dragon Breath" : "81" , "Dragon Pulse" : "82" , "Dragon Claw" : "83" , "Disarming Voice" : "84" , "Draining Kiss" : "85" , "Dazzling Gleam" : "86" , "Moonblast" : "87" , "Play Rough" : "88" , "Cross Poison" : "89" , "Sludge Bomb" : "90" , "Sludge Wave" : "91" , "Gunk Shot" : "92" , "Mud Shot" : "93" , "Bone Club" : "94" , "Bulldoze" : "95" , "Mud Bomb" : "96" , "Fury Cutter" : "97" , "Bug Bite" : "98" , "Signal Beam" : "99" , "X Scissor" : "100" , "Flame Charge" : "101" , "Flame Burst" : "102" , "Fire Blast" : "103" , "Brine" : "104" , "Water Pulse" : "105" , "Scald" : "106" , "Hydro Pump" : "107" , "Psychic" : "108" , "Psystrike" : "109" , "Ice Shard" : "110" , "Icy Wind" : "111" , "Frost Breath" : "112" , "Absorb" : "113" , "Giga Drain" : "114" , "Fire Punch" : "115" , "Solar Beam" : "116" , "Leaf Blade" : "117" , "Power Whip" : "118" , "Splash" : "119" , "Acid" : "120" , "Air Cutter" : "121" , "Hurricane" : "122" , "Brick Break" : "123" , "Cut" : "124" , "Swift" : "125" , "Horn Attack" : "126" , "Stomp" : "127" , "Headbutt" : "128" , "Hyper Fang" : "129" , "Slam" : "130" , "Body Slam" : "131" , "Rest" : "132" , "Struggle" : "133" , "Scald (Blastoise)" : "134" , "Hydro Pump (Blastoise)" : "135" , "Wrap Green" : "136" , "Wrap Pink" : "137" , "Fury Cutter" : "200" , "Bug Bite" : "201" , "Bite" : "202" , "Sucker Punch" : "203" , "Dragon Breath" : "204" , "Thunder Shock" : "205" , "Spark" : "206" , "Low Kick" : "207" , "Karate Chop" : "208" , "Ember" : "209" , "Wing Attack" : "210" , "Peck" : "211" , "Lick" : "212" , "Shadow Claw" : "213" , "Vine Whip" : "214" , "Razor Leaf" : "215" , "Mud Shot" : "216" , "Ice Shard" : "217" , "Frost Breath" : "218" , "Quick Attack" : "219" , "Scratch" : "220" , "Tackle" : "221" , "Pound" : "222" , "Cut" : "223" , "Poison Jab" : "224" , "Acid" : "225" , "Psycho Cut" : "226" , "Rock Throw" : "227" , "Metal Claw" : "228" , "Bullet Punch" : "229" , "Water Gun" : "230" , "Splash" : "231" , "Water Gun (Blastoise)" : "232" , "Mud Slap" : "233" , "Zen Headbutt" : "234" , "Confusion" : "235" , "Poison Sting" : "236" , "Bubble" : "237" , "Feint Attack" : "238" , "Steel Wing" : "239" , "Fire Fang" : "240" , "Rock Smash" : "241"} 



# Main function
def main():
    while True:

        data = []
        url = 'https://api.telegram.org/bot' + TOKEN +'/getUpdates?'

        # Using getUpdates method to check the lateset updates
        try:
            r = requests.get(url)
            r = r.text
            rx = json.loads(r)

            log_time = '==[' + strftime("%Y-%m-%d  %H:%M:%S") + ']=='
            print log_time

            update_no = int(len(rx['result']))
            update_status = int(update_no - 1)
            if update_status == 0:
                print 'Update Number: null'
            else:
                print 'Update Number: ' + str(update_status)

            number = int(update_no-1)
            update_id = rx['result'][number]['update_id']
            print 'Update ID:     ' + str(update_id)
            r2 = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', r)
            n = int(len(r2))

        except:
            print 'Cannot decode json, skipping items......'
            time.sleep(30)
            pass

       # Parameter to check is there any valid PokeAlert message or not
        log_x = "null"

        # Handling updates (messages sent by PokeAlert bot)
        sum = 1
        for i in range(0,n-1):
        
            # Use update_id as the encounter_id
            try:
                update_id = rx['result'][sum]['update_id']
                encounter_id = rx['result'][sum]['update_id']
            except:
                print 'Cannot decode json, skipping items......'
                pass

            try:
                if rx['result'][sum]['channel_post']['chat']['id'] == CHANNEL_ID:
                    ts = rx['result'][sum]['channel_post']['date']
                    ts_plus = ts + int(150)

                    try:
                        pkm_info = rx['result'][sum]['channel_post']['text']
                        pkm_info = pkm_info.encode("utf-8")
                    except:
                        pass

                    try:

                        pkm_info = pkm_info.replace('Nidoran♀','Nidoran_female').replace('Nidoran♂','Nidoran_male')
                        pkm_info = pkm_info.replace('fast/','XXX ').replace(') till',' YYY')                    
                        pkm_info = pkm_info.replace('(','').replace(')','').replace('https://maps.google.com/maps?q=','')
                        pkm_info = pkm_info.replace(',',' ').replace('/',' ').replace('  ','')

                        pkm_list = pkm_info.split(' ') 


    
                        # Find the Pokemon_name
                        pkm_n = str(pkm_list[1]).decode('utf-8')

                        # Pokemon_Chinese_Name-to-Pokemon_id convertion based on the dictionary
                        for k, v in pkm_hk.items():
                            pkm_n = pkm_n.replace(k, v)

                        # Pokemon_English_Name-to-Pokemon_id convertion based on the dictionary
                        for k, v in pkm.items():
                            pkm_n = pkm_n.replace(k, v)



                        # Define the values of each key (name, attack, defence, stamina, latitude, longitude)
                        pkm_iva = str(pkm_list[3])
                        pkm_ivd = str(pkm_list[4])
                        pkm_ivs = str(pkm_list[5])
                        pkm_lat = str(pkm_list[-2])
                        pkm_lng = str(pkm_list[-1])
                

                        # Define the value of move_1
                        XXX = pkm_list.index("XXX")
                        if XXX == 7:
                            pkm_mv1 = str(pkm_list[6])
                        else:
                            pkm_mv1 = str(pkm_list[6] + " " + pkm_list[7])

                    
                        # Define the value of move_2
                        YYY = pkm_list.index("YYY")
                        if XXX == 7 and YYY == 9:
                            pkm_mv2 = str(pkm_list[8])
                        elif XXX == 8 and YYY == 10:
                            pkm_mv2 = str(pkm_list[9])
                        elif XXX == 7 and YYY == 10:
                            pkm_mv2 = str(pkm_list[8] + " " + pkm_list[9])
                        else:
                            pkm_mv2 = str(pkm_list[9] + " " + pkm_list[10])

                        # Moves_English_Name-to-Moves_id convertion based on the dictionary  
                        for k, v in mv.items():
                            pkm_mv1 = pkm_mv1.replace(k, v)
                            pkm_mv2 = pkm_mv2.replace(k, v)

                        # Define the disappear_time, an additional 10 seconds are deducted for the delay time. If no time data recieved, default time_till_hidden set to 3 minutes
                        if pkm_list[-3] == "YYY":
                            pkm_time = str(ts_plus)
                            fake_time = "True"
                            print 'Fake time:     True'

                        elif 'm'in pkm_list[-3] and pkm_list[-5] == "YYY":
                            time_m = int(pkm_list[-3].replace("m","")) * 60
                            pkm_time = str(ts + time_m - 10)
                            fake_time = "False"
                            print 'Fake time:     False'

                        elif 'm' not in pkm_list[-4] and pkm_list[-3] != "YYY":
                            time_s = int(pkm_list[-3].replace("s",""))
                            pkm_time = str(ts + time_s - 10)
                            fake_time = "False"
                            print 'Fake time:     False'

                        else:
                            time_m = pkm_list[-4].replace("m","")
                            time_s = pkm_list[-3].replace("s","")
                            time_left = int(time_m)*60 + int(time_s)
                            pkm_time = str(ts + time_left - 10)
                            fake_time = "False"
                            print 'Fake time:     False'


                        x = '{"type": "pokemon","message":{"individual_attack":' + pkm_iva + ',"individual_defense":' + pkm_ivd + ',"latitude":' + pkm_lat + ',"longitude":' + pkm_lng +',"move_1":' + pkm_mv1 + ',"move_2":' + pkm_mv2 + ',"pokemon_id":' + pkm_n + ',"individual_stamina":' + pkm_ivs + ',"disappear_time":' + pkm_time + ',"encounter_id":"' + str(int(encounter_id)) + '"}}'
                        log_x = x

                        if log_x == "null":
                            print 'Update:        null'
                        else:
                            print 'Update:        ' + log_x

                        # Send webhook to PokeAlarm, assuming using port WH1 for handling fake disappear time, port WH2 for valid disappeaer time
                        if fake_time == "True":
                            try:
                                p = requests.post(WH1, data=x)
                                print 'Webhook:       Success!'
                            except:
                                print 'Webhook:       Failed'
                                pass
                        else:
                            try:
                                p = requests.post(WH2, data=x)
                                print 'Webhook:       Success!'
                            except:
                                print 'Webhook:       Failed'
                                pass

                    except:
                        pass
                else:
                    print "Recieving updates somewhere else, passing item......"
                    pass
            except:
                pass
            sum = sum + 1

            # Using getUpdates (with offset) method to confirm data recieved
            try:
                url2 = url + 'offset=' + str(int(update_id))
                r = requests.get(url2)
            except: 
                pass

            time.sleep(0)
 
        print '==========[Done]==========\n\n'
        time.sleep(0)

# Say thank you before you start
def run():   
    while True:
        run = raw_input('Type "thank you" to continue:  ')
        if run != 'thank you':
            continue
        else:
            break
        

# Start the script
print '\n\nThis is a script written by @slgphantom / @lord_ss to convert PokeAlert external notification to telegram (paid mode) into a json string which fits the webhook standand for PokeAlarm, via the getUpdates method. Please read the README.md before you start!'
TOKEN = str(raw_input('Enter your bot token:          '))
CHANNEL_ID = int(raw_input('Enter your channel_id:         '))
WH1 = str(raw_input('Enter your webhook address 1:  '))
WH2 = str(raw_input('Enter your webhook address 2:  '))
run()
main()
