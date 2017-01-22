# -*- coding: utf-8 -*-
import json
import requests
import re
import time
from time import strftime




# Dictionary for converting Pokemon_English_Name into Pokemon_id
pkm = {"1":"Bulbasaur","2":"Ivysaur","3":"Venusaur","4":"Charmander","5":"Charmeleon","6":"Charizard","7":"Squirtle","8":"Wartortle","9":"Blastoise","10":"Caterpie","11":"Metapod","12":"Butterfree","13":"Weedle","14":"Kakuna","15":"Beedrill","16":"Pidgey","17":"Pidgeotto","18":"Pidgeot","19":"Rattata","20":"Raticate","21":"Spearow","22":"Fearow","23":"Ekans","24":"Arbok","25":"Pikachu","26":"Raichu","27":"Sandshrew","28":"Sandslash","29":"Nidoran_female","30":"Nidorina","31":"Nidoqueen","32":"Nidoran_male","33":"Nidorino","34":"Nidoking","35":"Clefairy","36":"Clefable","37":"Vulpix","38":"Ninetales","39":"Jigglypuff","40":"Wigglytuff","41":"Zubat","42":"Golbat","43":"Oddish","44":"Gloom","45":"Vileplume","46":"Paras","47":"Parasect","48":"Venonat","49":"Venomoth","50":"Diglett","51":"Dugtrio","52":"Meowth","53":"Persian","54":"Psyduck","55":"Golduck","56":"Mankey","57":"Primeape","58":"Growlithe","59":"Arcanine","60":"Poliwag","61":"Poliwhirl","62":"Poliwrath","63":"Abra","64":"Kadabra","65":"Alakazam","66":"Machop","67":"Machoke","68":"Machamp","69":"Bellsprout","70":"Weepinbell","71":"Victreebel","72":"Tentacool","73":"Tentacruel","74":"Geodude","75":"Graveler","76":"Golem","77":"Ponyta","78":"Rapidash","79":"Slowpoke","80":"Slowbro","81":"Magnemite","82":"Magneton","83":"Farfetch'd","84":"Doduo","85":"Dodrio","86":"Seel","87":"Dewgong","88":"Grimer","89":"Muk","90":"Shellder","91":"Cloyster","92":"Gastly","93":"Haunter","94":"Gengar","95":"Onix","96":"Drowzee","97":"Hypno","98":"Krabby","99":"Kingler","100":"Voltorb","101":"Electrode","102":"Exeggcute","103":"Exeggutor","104":"Cubone","105":"Marowak","106":"Hitmonlee","107":"Hitmonchan","108":"Lickitung","109":"Koffing","110":"Weezing","111":"Rhyhorn","112":"Rhydon","113":"Chansey","114":"Tangela","115":"Kangaskhan","116":"Horsea","117":"Seadra","118":"Goldeen","119":"Seaking","120":"Staryu","121":"Starmie","122":"Mr. Mime","123":"Scyther","124":"Jynx","125":"Electabuzz","126":"Magmar","127":"Pinsir","128":"Tauros","129":"Magikarp","130":"Gyarados","131":"Lapras","132":"Ditto","133":"Eevee","134":"Vaporeon","135":"Jolteon","136":"Flareon","137":"Porygon","138":"Omanyte","139":"Omastar","140":"Kabuto","141":"Kabutops","142":"Aerodactyl","143":"Snorlax","144":"Articuno","145":"Zapdos","146":"Moltres","147":"Dratini","148":"Dragonair","149":"Dragonite","150":"Mewtwo","151":"Mew"}
pkm = {y:x for x,y in pkm.iteritems()}

# Dictionary for converting Pokemon_Chinese_Name into Pokemon_id
pkm_hk = {"1":u"奇異種子","2":u"奇異草","3":u"奇異花","4":u"小火龍","5":u"火恐龍","6":u"噴火龍","7":u"車厘龜","8":u"卡美龜","9":u"水箭龜","10":u"綠毛蟲","11":u"鐵甲蟲","12":u"巴他蝶","13":u"獨角蟲","14":u"鐵殼蛹","15":u"大針蜂","16":u"波波","17":u"比比鳥","18":u"大比鳥","19":u"小哥達","20":u"哥達","21":u"鬼雀","22":u"魔雀","23":u"阿柏蛇","24":u"阿柏怪","25":u"比卡超","26":u"雷超","27":u"穿山鼠","28":u"穿山王","29":u"尼美蘭","30":u"尼美蘿","31":u"尼美后","32":u"尼多郎","33":u"尼多利","34":u"尼多王","35":u"皮皮","36":u"皮可斯","37":u"六尾","38":u"九尾","39":u"波波球","40":u"肥波球","41":u"波音蝠","42":u"大口蝠","43":u"行路草","44":u"怪味花","45":u"霸王花","46":u"蘑菇蟲","47":u"巨菇蟲","48":u"毛毛蟲","49":u"魔魯風","50":u"地鼠","51":u"三頭地鼠","52":u"喵喵怪","53":u"高竇貓","54":u"傻鴨","55":u"高超鴨","56":u"猴怪","57":u"火爆猴","58":u"護主犬","59":u"奉神犬","60":u"蚊香蝌蚪","61":u"蚊香蛙","62":u"大力蛙","63":u"卡斯","64":u"尤基納","65":u"富迪","66":u"鐵腕","67":u"大力","68":u"怪力","69":u"喇叭芽","70":u"口呆花","71":u"大食花","72":u"大眼水母","73":u"多腳水母","74":u"小拳石","75":u"滾動石","76":u"滾動岩","77":u"小火馬","78":u"烈焰馬","79":u"小呆獸","80":u"大呆獸","81":u"小磁怪","82":u"三合一磁怪","83":u"火蔥鴨","84":u"多多","85":u"多多利","86":u"小海獅","87":u"白海獅","88":u"爛泥怪","89":u"爛泥獸","90":u"貝殼怪","91":u"鐵甲貝","92":u"鬼斯","93":u"鬼斯通","94":u"耿鬼","95":u"大岩蛇","96":u"食夢獸","97":u"催眠獸","98":u"大鉗蟹","99":u"巨鉗蟹","100":u"霹靂蛋","101":u"雷霆蛋","102":u"蛋蛋","103":u"椰樹獸","104":u"卡拉卡拉","105":u"格拉格拉","106":u"沙古拉","107":u"比華拉","108":u"大舌頭","109":u"毒氣丸","110":u"毒氣雙子","111":u"鐵甲犀牛","112":u"鐵甲暴龍","113":u"吉利蛋","114":u"長籐怪","115":u"袋獸","116":u"噴墨海馬","117":u"飛刺海馬","118":u"獨角金魚","119":u"金魚王","120":u"海星星","121":u"寶石海星","122":u"吸盤小丑","123":u"飛天螳螂","124":u"紅唇娃","125":u"電擊獸","126":u"鴨嘴火龍","127":u"鉗刀甲蟲","128":u"大隻牛","129":u"鯉魚王","130":u"鯉魚龍","131":u"背背龍","132":u"百變怪","133":u"伊貝","134":u"水伊貝","135":u"雷伊貝","136":u"火伊貝","137":u"立方獸","138":u"菊石獸","139":u"多刺菊石獸","140":u"萬年蟲","141":u"鐮刀蟲","142":u"化石飛龍","143":u"卡比獸","144":u"急凍鳥","145":u"雷鳥","146":u"火鳥","147":u"迷你龍","148":u"哈古龍","149":u"啟暴龍","150":u"超夢夢","151":u"夢夢"}
pkm_hk = {y:x for x,y in pkm_hk.iteritems()}

# Dictionary for converting Moves_English_name into Moves_id
mv = {"1":"Thunder Shock","2":"Quick Attack","3":"Scratch","4":"Ember","5":"Vine Whip","6":"Tackle","7":"Razor Leaf","8":"Take Down","9":"Water Gun","10":"Bite","11":"Pound","12":"Double Slap","13":"Wrap","14":"Hyper Beam","15":"Lick","16":"Dark Pulse","17":"Smog","18":"Sludge Bomb","19":"Metal Claw","20":"Vice Grip","21":"Flame Wheel","22":"Megahorn","23":"Wing Attack","24":"Flamethrower","25":"Sucker Punch","26":"Dig","27":"Low Kick","28":"Cross Chop","29":"Psycho Cut","30":"Psybeam","31":"Earthquake","32":"Stone Edge","33":"Ice Punch","34":"Heart Stamp","35":"Discharge","36":"Flash Cannon","37":"Peck","38":"Drill Peck","39":"Ice Beam","40":"Blizzard","41":"Air Slash","42":"Heat Wave","43":"Twineedle","44":"Poison Jab","45":"Aerial Ace","46":"Drill Run","47":"Petal Blizzard","48":"Mega Drain","49":"Bug Buzz","50":"Poison Fang","51":"Night Slash","52":"Slash","53":"Bubble Beam","54":"Submission","55":"Karate Chop","56":"Low Sweep","57":"Aqua Jet","58":"Aqua Tail","59":"Seed Bomb","60":"Psyshock","61":"Rock Throw","62":"Ancient Power","63":"Rock Tomb","64":"Rock Slide","65":"Power Gem","66":"Shadow Sneak","67":"Shadow Punch","68":"Shadow Claw","69":"Ominous Wind","70":"Shadow Ball","71":"Bullet Punch","72":"Magnet Bomb","73":"Steel Wing","74":"Iron Head","75":"Parabolic Charge","76":"Spark","77":"Thunder Punch","78":"Thunder Shock","79":"Thunderbolt","80":"Twister","81":"Dragon Breath","82":"Dragon Pulse","83":"Dragon Claw","84":"Disarming Voice","85":"Draining Kiss","86":"Dazzling Gleam","87":"Moonblast","88":"Play Rough","89":"Cross Poison","90":"Sludge Bomb","91":"Sludge Wave","92":"Gunk Shot","93":"Mud Shot","94":"Bone Club","95":"Bulldoze","96":"Mud Bomb","97":"Fury Cutter","98":"Bug Bite","99":"Signal Beam","100":"X Scissor","101":"Flame Charge","102":"Flame Burst","103":"Fire Blast","104":"Brine","105":"Water Pulse","106":"Scald","107":"Hydro Pump","108":"Psychic","109":"Psystrike","110":"Ice Shard","111":"Icy Wind","112":"Frost Breath","113":"Absorb","114":"Giga Drain","115":"Fire Punch","116":"Solar Beam","117":"Leaf Blade","118":"Power Whip","119":"Splash","120":"Acid","121":"Air Cutter","122":"Hurricane","123":"Brick Break","124":"Cut","125":"Swift","126":"Horn Attack","127":"Stomp","128":"Headbutt","129":"Hyper Fang","130":"Slam","131":"Body Slam","132":"Rest","133":"Struggle","134":"Scald (Blastoise)","135":"Hydro Pump (Blastoise)","136":"Wrap Green","137":"Wrap Pink","200":"Fury Cutter","201":"Bug Bite","202":"Bite","203":"Sucker Punch","204":"Dragon Breath","205":"Thunder Shock","206":"Spark","207":"Low Kick","208":"Karate Chop","209":"Ember","210":"Wing Attack","211":"Peck","212":"Lick","213":"Shadow Claw","214":"Vine Whip","215":"Razor Leaf","216":"Mud Shot","217":"Ice Shard","218":"Frost Breath","219":"Quick Attack","220":"Scratch","221":"Tackle","222":"Pound","223":"Cut","224":"Poison Jab","225":"Acid","226":"Psycho Cut","227":"Rock Throw","228":"Metal Claw","229":"Bullet Punch","230":"Water Gun","231":"Splash","232":"Water Gun (Blastoise)","233":"Mud Slap","234":"Zen Headbutt","235":"Confusion","236":"Poison Sting","237":"Bubble","238":"Feint Attack","239":"Steel Wing","240":"Fire Fang","241":"Rock Smash"}
mv = {y:x for x,y in mv.iteritems()}
mv = {k.lower(): v for k, v in mv.items()}
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
                        pkm_n = str(pkm_list[0]).decode('utf-8')

                        # Pokemon_Chinese_Name-to-Pokemon_id convertion based on the dictionary
                        for k, v in pkm_hk.items():
                            pkm_n = pkm_n.replace(k, v)

                        # Pokemon_English_Name-to-Pokemon_id convertion based on the dictionary
                        for k, v in pkm.items():
                            pkm_n = pkm_n.replace(k, v)



                        # Define the values of each key (name, attack, defence, stamina, latitude, longitude)
                        pkm_iva = str(pkm_list[2])
                        pkm_ivd = str(pkm_list[3])
                        pkm_ivs = str(pkm_list[4])
                        pkm_lat = str(pkm_list[-2])
                        pkm_lng = str(pkm_list[-1])
                

                        # Define the value of move_1
                        XXX = pkm_list.index("XXX")
                        if XXX == 6:
                            pkm_mv1 = str(pkm_list[5])
                        else:
                            pkm_mv1 = str(pkm_list[5] + " " + pkm_list[6])

                    
                        # Define the value of move_2
                        YYY = pkm_list.index("YYY")
                        if XXX == 6 and YYY == 8:
                            pkm_mv2 = str(pkm_list[7])
                        elif XXX == 7 and YYY == 9:
                            pkm_mv2 = str(pkm_list[8])
                        elif XXX == 6 and YYY == 9:
                            pkm_mv2 = str(pkm_list[7] + " " + pkm_list[8])
                        else:
                            pkm_mv2 = str(pkm_list[8] + " " + pkm_list[9])

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
