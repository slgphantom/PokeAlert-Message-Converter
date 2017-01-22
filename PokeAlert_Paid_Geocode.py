# -*- coding: utf-8 -*-
import json
import requests
import re
import time
from time import strftime




# Dictionary for converting Pokemon_English_Name into Pokemon_id
pkm = {'Oddish': '43', 'Weezing': '110', 'Graveler': '75', 'Jynx': '124', 'Paras': '46', 'Kadabra': '64', 'Sandslash': '28', 'Kangaskhan': '115', 'Hitmonlee': '106', 'Poliwrath': '62', 'Machamp': '68', 'Butterfree': '12', 'Raichu': '26', 'Omanyte': '138', 'Tangela': '114', 'Slowpoke': '79', 'Chansey': '113', 'Diglett': '50', 'Rhydon': '112', 'Poliwhirl': '61', "Farfetch'd": '83', 'Parasect': '47', 'Tentacool': '72', 'Magnemite': '81', 'Ditto': '132', 'Aerodactyl': '142', 'Koffing': '109', 'Shellder': '90', 'Magmar': '126', 'Mankey': '56', 'Dratini': '147', 'Raticate': '20', 'Charmeleon': '5', 'Psyduck': '54', 'Slowbro': '80', 'Snorlax': '143', 'Arcanine': '59', 'Omastar': '139', 'Growlithe': '58', 'Articuno': '144', 'Blastoise': '9', 'Golem': '76', 'Pinsir': '127', 'Cloyster': '91', 'Beedrill': '15', 'Tauros': '128', 'Fearow': '22', 'Bulbasaur': '1', 'Kabutops': '141', 'Abra': '63', 'Arbok': '24', 'Doduo': '84', 'Muk': '89', 'Marowak': '105', 'Wartortle': '8', 'Wigglytuff': '40', 'Vulpix': '37', 'Magikarp': '129', 'Starmie': '121', 'Mew': '151', 'Geodude': '74', 'Pidgeotto': '17', 'Rattata': '19', 'Primeape': '57', 'Squirtle': '7', 'Exeggutor': '103', 'Bellsprout': '69', 'Nidoran_female': '29', 'Jolteon': '135', 'Venusaur': '3', 'Meowth': '52', 'Nidoran_male': '32', 'Spearow': '21', 'Scyther': '123', 'Ekans': '23', 'Alakazam': '65', 'Nidoqueen': '31', 'Mr. Mime': '122', 'Voltorb': '100', 'Dragonite': '149', 'Gyarados': '130', 'Vaporeon': '134', 'Metapod': '11', 'Jigglypuff': '39', 'Dragonair': '148', 'Hypno': '97', 'Lickitung': '108', 'Haunter': '93', 'Ivysaur': '2', 'Vileplume': '45', 'Gastly': '92', 'Drowzee': '96', 'Goldeen': '118', 'Pidgey': '16', 'Mewtwo': '150', 'Machoke': '67', 'Porygon': '137', 'Poliwag': '60', 'Eevee': '133', 'Sandshrew': '27', 'Venomoth': '49', 'Gloom': '44', 'Nidorino': '33', 'Nidorina': '30', 'Pidgeot': '18', 'Golduck': '55', 'Kingler': '99', 'Exeggcute': '102', 'Weepinbell': '70', 'Golbat': '42', 'Gengar': '94', 'Dodrio': '85', 'Rapidash': '78', 'Dugtrio': '51', 'Krabby': '98', 'Seadra': '117', 'Persian': '53', 'Nidoking': '34', 'Zapdos': '145', 'Zubat': '41', 'Charmander': '4', 'Electrode': '101', 'Moltres': '146', 'Victreebel': '71', 'Flareon': '136', 'Kabuto': '140', 'Electabuzz': '125', 'Weedle': '13', 'Charizard': '6', 'Pikachu': '25', 'Machop': '66', 'Caterpie': '10', 'Kakuna': '14', 'Horsea': '116', 'Seaking': '119', 'Dewgong': '87', 'Hitmonchan': '107', 'Clefable': '36', 'Ponyta': '77', 'Rhyhorn': '111', 'Tentacruel': '73', 'Ninetales': '38', 'Cubone': '104', 'Venonat': '48', 'Onix': '95', 'Clefairy': '35', 'Grimer': '88', 'Magneton': '82', 'Seel': '86', 'Lapras': '131', 'Staryu': '120'}

# Dictionary for converting Pokemon_Chinese_Name into Pokemon_id}
pkm_hk = {u'\u5c3c\u591a\u738b': '34', u'\u9b3c\u65af\u901a': '93', u'\u98db\u5929\u87b3\u8782': '123', u'\u50ac\u7720\u7378': '97', u'\u5361\u7f8e\u9f9c': '8', u'\u6bd4\u6bd4\u9ce5': '17', u'\u5949\u795e\u72ac': '59', u'\u842c\u5e74\u87f2': '140', u'\u868a\u9999\u874c\u86aa': '60', u'\u76ae\u76ae': '35', u'\u80a5\u6ce2\u7403': '40', u'\u5927\u529b': '67', u'\u5c0f\u78c1\u602a': '81', u'\u516d\u5c3e': '37', u'\u9ad8\u7ac7\u8c93': '53', u'\u9b54\u96c0': '22', u'\u591a\u8173\u6c34\u6bcd': '73', u'\u5927\u820c\u982d': '108', u'\u7a7f\u5c71\u9f20': '27', u'\u5c24\u57fa\u7d0d': '64', u'\u5361\u62c9\u5361\u62c9': '104', u'\u591a\u591a\u5229': '85', u'\u5947\u7570\u7a2e\u5b50': '1', u'\u50bb\u9d28': '54', u'\u6efe\u52d5\u5ca9': '76', u'\u8c9d\u6bbc\u602a': '90', u'\u6bdb\u6bdb\u87f2': '48', u'\u721b\u6ce5\u602a': '88', u'\u9435\u7532\u87f2': '11', u'\u5de8\u9257\u87f9': '99', u'\u8ff7\u4f60\u9f8d': '147', u'\u5927\u6bd4\u9ce5': '18', u'\u9435\u7532\u7280\u725b': '111', u'\u9bc9\u9b5a\u738b': '129', u'\u9bc9\u9b5a\u9f8d': '130', u'\u9435\u6bbc\u86f9': '14', u'\u5438\u76e4\u5c0f\u4e11': '122', u'\u9435\u7532\u8c9d': '91', u'\u942e\u5200\u87f2': '141', u'\u96f7\u8d85': '26', u'\u98df\u5922\u7378': '96', u'\u6c99\u53e4\u62c9': '106', u'\u5730\u9f20': '50', u'\u7334\u602a': '56', u'\u5361\u6bd4\u7378': '143', u'\u98db\u523a\u6d77\u99ac': '117', u'\u555f\u66b4\u9f8d': '149', u'\u6025\u51cd\u9ce5': '144', u'\u803f\u9b3c': '94', u'\u9b3c\u96c0': '21', u'\u6ce2\u6ce2': '16', u'\u96fb\u64ca\u7378': '125', u'\u5de8\u83c7\u87f2': '47', u'\u5c0f\u54e5\u9054': '19', u'\u5927\u529b\u86d9': '62', u'\u96f7\u4f0a\u8c9d': '135', u'\u5927\u9257\u87f9': '98', u'\u5947\u7570\u82b1': '3', u'\u5927\u53e3\u8760': '42', u'\u5927\u5446\u7378': '80', u'\u9d28\u5634\u706b\u9f8d': '126', u'\u6bd2\u6c23\u96d9\u5b50': '110', u'\u4e5d\u5c3e': '38', u'\u7a7f\u5c71\u738b': '28', u'\u9b54\u9b6f\u98a8': '49', u'\u91d1\u9b5a\u738b': '119', u'\u8b77\u4e3b\u72ac': '58', u'\u706b\u4f0a\u8c9d': '136', u'\u5c3c\u7f8e\u862d': '29', u'\u9257\u5200\u7532\u87f2': '127', u'\u9435\u8155': '66', u'\u5927\u98df\u82b1': '71', u'\u6bd4\u5361\u8d85': '25', u'\u5c3c\u7f8e\u863f': '30', u'\u5587\u53ed\u82bd': '69', u'\u9b3c\u65af': '92', u'\u5c0f\u706b\u9f8d': '4', u'\u5c3c\u591a\u90ce': '32', u'\u5c3c\u7f8e\u540e': '31', u'\u5947\u7570\u8349': '2', u'\u721b\u6ce5\u7378': '89', u'\u6ce2\u97f3\u8760': '41', u'\u7acb\u65b9\u7378': '137', u'\u9577\u7c50\u602a': '114', u'\u54e5\u9054': '20', u'\u5c0f\u5446\u7378': '79', u'\u5c0f\u706b\u99ac': '77', u'\u963f\u67cf\u602a': '24', u'\u5927\u773c\u6c34\u6bcd': '72', u'\u7368\u89d2\u91d1\u9b5a': '118', u'\u9ad8\u8d85\u9d28': '55', u'\u5361\u65af': '63', u'\u4e09\u982d\u5730\u9f20': '51', u'\u602a\u5473\u82b1': '44', u'\u5927\u91dd\u8702': '15', u'\u7d05\u5507\u5a03': '124', u'\u706b\u7206\u7334': '57', u'\u706b\u9ce5': '146', u'\u602a\u529b': '68', u'\u86cb\u86cb': '102', u'\u5674\u58a8\u6d77\u99ac': '116', u'\u8611\u83c7\u87f2': '46', u'\u706b\u6050\u9f8d': '5', u'\u9739\u9742\u86cb': '100', u'\u76ae\u53ef\u65af': '36', u'\u767e\u8b8a\u602a': '132', u'\u53e3\u5446\u82b1': '70', u'\u7da0\u6bdb\u87f2': '10', u'\u6930\u6a39\u7378': '103', u'\u5674\u706b\u9f8d': '6', u'\u6bd2\u6c23\u4e38': '109', u'\u767d\u6d77\u7345': '87', u'\u5c0f\u6d77\u7345': '86', u'\u70c8\u7130\u99ac': '78', u'\u5bcc\u8fea': '65', u'\u868a\u9999\u86d9': '61', u'\u5927\u5ca9\u86c7': '95', u'\u5316\u77f3\u98db\u9f8d': '142', u'\u6efe\u52d5\u77f3': '75', u'\u55b5\u55b5\u602a': '52', u'\u888b\u7378': '115', u'\u5409\u5229\u86cb': '113', u'\u5c3c\u591a\u5229': '33', u'\u9738\u738b\u82b1': '45', u'\u8d85\u5922\u5922': '150', u'\u5c0f\u62f3\u77f3': '74', u'\u884c\u8def\u8349': '43', u'\u683c\u62c9\u683c\u62c9': '105', u'\u591a\u523a\u83ca\u77f3\u7378': '139', u'\u6d77\u661f\u661f': '120', u'\u6bd4\u83ef\u62c9': '107', u'\u80cc\u80cc\u9f8d': '131', u'\u54c8\u53e4\u9f8d': '148', u'\u83ca\u77f3\u7378': '138', u'\u96f7\u9ce5': '145', u'\u5922\u5922': '151', u'\u706b\u8525\u9d28': '83', u'\u6c34\u7bad\u9f9c': '9', u'\u8eca\u5398\u9f9c': '7', u'\u7368\u89d2\u87f2': '13', u'\u9435\u7532\u66b4\u9f8d': '112', u'\u4e09\u5408\u4e00\u78c1\u602a': '82', u'\u963f\u67cf\u86c7': '23', u'\u591a\u591a': '84', u'\u6c34\u4f0a\u8c9d': '134', u'\u96f7\u9706\u86cb': '101', u'\u6ce2\u6ce2\u7403': '39', u'\u5df4\u4ed6\u8776': '12', u'\u5bf6\u77f3\u6d77\u661f': '121', u'\u5927\u96bb\u725b': '128', u'\u4f0a\u8c9d': '133'}

# Dictionary for converting Moves_English_name into Moves_id
mv = {'dragon pulse': '82', 'x scissor': '100', 'scratch': '220', 'gunk shot': '92', 'rest': '132', 'brine': '104', 'wrap pink': '137', 'flame charge': '101', 'poison fang': '50', 'cut': '223', 'flame burst': '102', 'bug buzz': '49', 'giga drain': '114', 'brick break': '123', 'fury cutter': '200', 'mud shot': '216', 'ice punch': '33', 'body slam': '131', 'thunder punch': '77', 'water gun (blastoise)': '232', 'fire punch': '115', 'air slash': '41', 'wing attack': '23', 'vine whip': '5', 'submission': '54', 'disarming voice': '84', 'heart stamp': '34', 'dig': '26', 'hydro pump': '107', 'dark pulse': '16', 'ice shard': '110', 'water gun': '9', 'bubble beam': '53', 'icy wind': '111', 'night slash': '51', 'solar beam': '116', 'air cutter': '121', 'hyper fang': '129', 'acid': '225', 'twineedle': '43', 'aerial ace': '45', 'scald': '106', 'bulldoze': '95', 'psychic': '108', 'hurricane': '122', 'sucker punch': '203', 'psyshock': '60', 'water pulse': '105', 'smog': '17', 'confusion': '235', 'mud slap': '233', 'shadow ball': '70', 'struggle': '133', 'stone edge': '32', 'spark': '76', 'play rough': '88', 'swift': '125', 'earthquake': '31', 'ice beam': '39', 'aqua tail': '58', 'rock smash': '241', 'mega drain': '48', 'petal blizzard': '47', 'headbutt': '128', 'razor leaf': '7', 'hydro pump (blastoise)': '135', 'hyper beam': '14', 'steel wing': '73', 'poison jab': '44', 'magnet bomb': '72', 'blizzard': '40', 'wrap green': '136', 'thunder shock': '78', 'mud bomb': '96', 'sludge bomb': '18', 'slash': '52', 'metal claw': '19', 'dragon claw': '83', 'lick': '15', 'karate chop': '208', 'wrap': '13', 'rock tomb': '63', 'iron head': '74', 'fire blast': '103', 'horn attack': '126', 'leaf blade': '117', 'bite': '202', 'heat wave': '42', 'flash cannon': '36', 'splash': '119', 'shadow punch': '67', 'seed bomb': '59', 'twister': '80', 'bubble': '237', 'flamethrower': '24', 'bullet punch': '71', 'parabolic charge': '75', 'cross poison': '89', 'low kick': '207', 'peck': '211', 'power whip': '118', 'psycho cut': '226', 'shadow sneak': '66', 'psystrike': '109', 'ember': '209', 'low sweep': '56', 'power gem': '65', 'poison sting': '236', 'pound': '11', 'shadow claw': '213', 'frost breath': '112', 'megahorn': '22', 'ancient power': '62', 'slam': '130', 'bug bite': '201', 'moonblast': '87', 'drill peck': '38', 'drill run': '46', 'double slap': '12', 'dragon breath': '204', 'rock slide': '64', 'quick attack': '2', 'aqua jet': '57', 'sludge wave': '91', 'draining kiss': '85', 'stomp': '127', 'feint attack': '238', 'signal beam': '99', 'thunderbolt': '79', 'rock throw': '227', 'cross chop': '28', 'scald (blastoise)': '134', 'vice grip': '20', 'absorb': '113', 'dazzling gleam': '86', 'zen headbutt': '234', 'flame wheel': '21', 'tackle': '221', 'discharge': '35', 'take down': '8', 'bone club': '94', 'psybeam': '30', 'ominous wind': '69', 'fire fang': '240'}

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
