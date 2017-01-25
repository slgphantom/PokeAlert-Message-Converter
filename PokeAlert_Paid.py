# -*- coding: utf-8 -*-
import json
import requests
import re
import time
from time import strftime


# Dictionary for converting Pokemon_English_Name into Pokemon_id
pkm_1 = {"Bulbasaur" :"1" , "Ivysaur" :"2" , "Venusaur" :"3" , "Charmander" :"4" , "Charmeleon" :"5" , "Charizard" :"6" , "Squirtle" :"7" , "Wartortle" :"8" , "Blastoise" :"9" , "Caterpie" :"10" , "Metapod" :"11" , "Butterfree" :"12" , "Weedle" :"13" , "Kakuna" :"14" , "Beedrill" :"15" , "Pidgey" :"16" , "Pidgeotto" :"17" , "Pidgeot" :"18" , "Rattata" :"19" , "Raticate" :"20" , "Spearow" :"21" , "Fearow" :"22" , "Ekans" :"23" , "Arbok" :"24" , "Pikachu" :"25" , "Raichu" :"26" , "Sandshrew" :"27" , "Sandslash" :"28" , "Nidoran_female" :"29" , "Nidorina" :"30" , "Nidoqueen" :"31" , "Nidoran_male" :"32" , "Nidorino" :"33" , "Nidoking" :"34" , "Clefairy" :"35" , "Clefable" :"36" , "Vulpix" :"37" , "Ninetales" :"38" , "Jigglypuff" :"39" , "Wigglytuff" :"40" , "Zubat" :"41" , "Golbat" :"42" , " Oddish" :"43" , "Gloom" :"44" , "Vileplume" :"45" , "Parasect" :"47" , "Venonat" :"48" , "Venomoth" :"49" , "Diglett" :"50" , "Dugtrio" :"51" , "Meowth" :"52" , "Persian" :"53" , "Psyduck" :"54" , "Golduck" :"55" , "Mankey" :"56" , "Primeape" :"57" , "Growlithe" :"58" , "Arcanine" :"59" , "Poliwag" :"60" , "Poliwhirl" :"61" , "Poliwrath" :"62" , "Abra" :"63" , "Kadabra" :"64" , "Alakazam" :"65" , "Machop" :"66" , "Machoke" :"67" , "Machamp" :"68" , "Bellsprout" :"69" , "Weepinbell" :"70" , "Victreebel" :"71" , "Tentacool" :"72" , "Tentacruel" :"73" , "Geodude" :"74" , "Graveler" :"75" , "Golem" :"76" , "Ponyta" :"77" , "Rapidash" :"78" , "Slowpoke" :"79" , "Slowbro" :"80" , "Magnemite" :"81" , "Magneton" :"82" , " Farfetch\'d" :"83" , "Doduo" :"84" , "Dodrio" :"85" , "Seel" :"86" , "Dewgong" :"87" , "Grimer" :"88" , "Muk" :"89" , "Shellder" :"90" , "Cloyster" :"91" , "Gastly" :"92" , "Haunter" :"93" , "Gengar" :"94" , "Onix" :"95" , "Drowzee" :"96" , "Hypno" :"97" , "Krabby" :"98" , "Kingler" :"99" , "Voltorb" :"100" , "Electrode" :"101" , "Exeggcute" :"102" , "Exeggutor" :"103" , "Cubone" :"104" , "Marowak" :"105" , "Hitmonlee" :"106" , "Hitmonchan" :"107" , "Lickitung" :"108" , "Koffing" :"109" , "Weezing" :"110" , "Rhyhorn" :"111" , "Rhydon" :"112" , "Chansey" :"113" , "Tangela" :"114" , "Kangaskhan" :"115" , "Horsea" :"116" , "Seadra" :"117" , "Goldeen" :"118" , "Seaking" :"119" , "Staryu" :"120" , "Starmie" :"121" , "Mr. Mime" :"122" , "Scyther" :"123" , "Jynx" :"124" , "Electabuzz" :"125" , "Magmar" :"126" , "Pinsir" :"127" , "Tauros" :"128" , "Magikarp" :"129" , "Gyarados" :"130" , "Lapras" :"131" , "Ditto" :"132" , "Eevee" :"133" , "Vaporeon" :"134" , "Jolteon" :"135" , "Flareon" :"136" , "Porygon" :"137" , "Omanyte" :"138" , "Omastar" :"139" , "Kabutops" :"141" , "Aerodactyl" :"142" , "Snorlax" :"143" , "Articuno" :"144" , "Zapdos" :"145" , "Moltres" :"146" , "Dratini" :"147" , "Dragonair" :"148" , "Dragonite" :"149" , "Mewtwo" :"150"}
pkm_2 = {"Paras" :"46" , "Kabuto" :"140" , "Mew" :"151"}

# Dictionary for converting Pokemon_Chinese_Name into Pokemon_id
pkm_hk_1 = {u"奇異種子" : "1" , u"奇異草" : "2" , u"奇異花" : "3" , u"小火龍" : "4" , u"火恐龍" : "5" , u"噴火龍" : "6" , u"車厘龜" : "7" , u"卡美龜" : "8" , u"水箭龜" : "9" , u"綠毛蟲" : "10" , u"鐵甲蟲" : "11" , u"巴他蝶" : "12" , u"獨角蟲" : "13" , u"鐵殼蛹" : "14" , u"大針蜂" : "15" , u"比比鳥" : "17" , u"大比鳥" : "18" , u"小哥達" : "19" , u"鬼雀" : "21" , u"魔雀" : "22" , u"阿柏蛇" : "23" , u"阿柏怪" : "24" , u"比卡超" : "25" , u"雷超" : "26" , u"穿山鼠" : "27" , u"穿山王" : "28" , u"尼美蘭" : "29" , u"尼美蘿" : "30" , u"尼美后" : "31" , u"尼多郎" : "32" , u"尼多利" : "33" , u"尼多王" : "34" , u"皮皮" : "35" , u"皮可斯" : "36" , u"六尾" : "37" , u"九尾" : "38" , u"波波球" : "39" , u"肥波球" : "40" , u"波音蝠" : "41" , u"大口蝠" : "42" , u"行路草" : "43" , u"怪味花" : "44" , u"霸王花" : "45" , u"蘑菇蟲" : "46" , u"巨菇蟲" : "47" , u"毛毛蟲" : "48" , u"魔魯風" : "49" , u"三頭地鼠" : "51" , u"喵喵怪" : "52" , u"高竇貓" : "53" , u"傻鴨" : "54" , u"高超鴨" : "55" , u"猴怪" : "56" , u"火爆猴" : "57" , u"護主犬" : "58" , u"奉神犬" : "59" , u"蚊香蝌蚪" : "60" , u"蚊香蛙" : "61" , u"大力蛙" : "62" , u"卡斯" : "63" , u"尤基納" : "64" , u"富迪" : "65" , u"鐵腕" : "66" , u"大力" : "67" , u"怪力" : "68" , u"喇叭芽" : "69" , u"口呆花" : "70" , u"大食花" : "71" , u"大眼水母" : "72" , u"多腳水母" : "73" , u"小拳石" : "74" , u"滾動石" : "75" , u"滾動岩" : "76" , u"小火馬" : "77" , u"烈焰馬" : "78" , u"小呆獸" : "79" , u"大呆獸" : "80" , u"小磁怪" : "81" , u"三合一磁怪" : "82" , u"火蔥鴨" : "83" , u"多多利" : "85" , u"小海獅" : "86" , u"白海獅" : "87" , u"爛泥怪" : "88" , u"爛泥獸" : "89" , u"貝殼怪" : "90" , u"鐵甲貝" : "91" , u"鬼斯通" : "93" , u"耿鬼" : "94" , u"大岩蛇" : "95" , u"食夢獸" : "96" , u"催眠獸" : "97" , u"大鉗蟹" : "98" , u"巨鉗蟹" : "99" , u"霹靂蛋" : "100" , u"雷霆蛋" : "101" , u"蛋蛋" : "102" , u"椰樹獸" : "103" , u"卡拉卡拉" : "104" , u"格拉格拉" : "105" , u"沙古拉" : "106" , u"比華拉" : "107" , u"大舌頭" : "108" , u"毒氣丸" : "109" , u"毒氣雙子" : "110" , u"鐵甲犀牛" : "111" , u"鐵甲暴龍" : "112" , u"吉利蛋" : "113" , u"長籐怪" : "114" , u"袋獸" : "115" , u"噴墨海馬" : "116" , u"飛刺海馬" : "117" , u"獨角金魚" : "118" , u"金魚王" : "119" , u"海星星" : "120" , u"寶石海星" : "121" , u"吸盤小丑" : "122" , u"飛天螳螂" : "123" , u"紅唇娃" : "124" , u"電擊獸" : "125" , u"鴨嘴火龍" : "126" , u"鉗刀甲蟲" : "127" , u"大隻牛" : "128" , u"鯉魚王" : "129" , u"鯉魚龍" : "130" , u"背背龍" : "131" , u"百變怪" : "132" , u"水伊貝" : "134" , u"雷伊貝" : "135" , u"火伊貝" : "136", u"立方獸" : "137" , u"多刺菊石獸" : "139" , u"萬年蟲" : "140" , u"鐮刀蟲" : "141" , u"化石飛龍" : "142" , u"卡比獸" : "143" , u"急凍鳥" : "144" , u"雷鳥" : "145" , u"火鳥" : "146" , u"迷你龍" : "147" , u"哈古龍" : "148" , u"啟暴龍" : "149" , u"超夢夢" : "150"}
pkm_hk_2 = {u"波波" : "16" , u"哥達" : "20" , u"地鼠" : "50" , u"多多" : "84" , u"鬼斯" : "92" , u"伊貝" : "133"  , u"菊石獸" : "138" , u"夢夢" : "151"}

# Dictionary for converting Moves_English_name into Moves_id
mv_1 = {"aerial ace" : "45" , "air cutter" : "121" , "air slash" : "41" , "ancient power" : "62" , "aqua jet" : "57" , "aqua tail" : "58" , "body slam" : "131" , "bone club" : "94" , "brick break" : "123" , "bubble beam" : "53" , "bug bite" : "201" , "bug bite" : "98" , "bug buzz" : "49" , "bullet punch" : "229" , "bullet punch" : "71" , "cross chop" : "28" , "cross poison" : "89" , "dark pulse" : "16" , "dazzling gleam" : "86" , "disarming voice" : "84" , "double slap" : "12" , "dragon breath" : "204" , "dragon breath" : "81" , "dragon claw" : "83" , "dragon pulse" : "82" , "draining kiss" : "85" , "drill peck" : "38" , "drill run" : "46" , "feint attack" : "238" , "fire blast" : "103" , "fire fang" : "240" , "fire punch" : "115" , "flame burst" : "102" , "flame charge" : "101" , "flame wheel" : "21" , "flash cannon" : "36" , "frost breath" : "112" , "frost breath" : "218" , "fury cutter" : "200" , "fury cutter" : "97" , "giga drain" : "114" , "gunk shot" : "92" , "heart stamp" : "34" , "heat wave" : "42" , "horn attack" : "126" , "hydro pump (blastoise)" : "135" , "hydro pump" : "107" , "hyper beam" : "14" , "hyper fang" : "129" , "ice beam" : "39" , "ice punch" : "33" , "ice shard" : "110" , "ice shard" : "217" , "icy wind" : "111" , "iron head" : "74" , "karate chop" : "208" , "karate chop" : "55" , "leaf blade" : "117" , "low kick" : "207" , "low kick" : "27" , "low sweep" : "56" , "magnet bomb" : "72" , "mega drain" : "48" , "metal claw" : "19" , "metal claw" : "228" , "mud bomb" : "96" , "mud shot" : "216" , "mud shot" : "93" , "mud slap" : "233" , "night slash" : "51" , "ominous wind" : "69" , "parabolic charge" : "75" , "petal blizzard" : "47" , "play rough" : "88" , "poison fang" : "50" , "poison jab" : "224" , "poison jab" : "44" , "poison sting" : "236" , "power gem" : "65" , "power whip" : "118" , "psycho cut" : "226" , "psycho cut" : "29" , "quick attack" : "2" , "quick attack" : "219" , "razor leaf" : "215" , "razor leaf" : "7" , "rock slide" : "64" , "rock smash" : "241" , "rock throw" : "227" , "rock throw" : "61" , "rock tomb" : "63" , "scald (blastoise)" : "134" , "seed bomb" : "59" , "shadow ball" : "70" , "shadow claw" : "213" , "shadow claw" : "68" , "shadow punch" : "67" , "shadow sneak" : "66" , "signal beam" : "99" , "sludge bomb" : "18" , "sludge bomb" : "90" , "sludge wave" : "91" , "solar beam" : "116" , "steel wing" : "239" , "steel wing" : "73" , "stone edge" : "32" , "sucker punch" : "203" , "sucker punch" : "25" , "take down" : "8" , "thunder punch" : "77" , "thunder shock" : "1" , "thunder shock" : "205" , "thunder shock" : "78" , "vice grip" : "20" , "vine whip" : "214" , "vine whip" : "5" , "water gun (blastoise)" : "232" , "water gun" : "230" , "water gun" : "9" , "water pulse" : "105" , "wing attack" : "210" , "wing attack" : "23" , "wrap green" : "136" , "wrap pink" : "137" , "x scissor" : "100" , "zen headbutt" : "234"}
mv_2 = {"absorb" : "113" , "acid" : "120" , "acid" : "225" , "bite" : "10" , "bite" : "202" , "blizzard" : "40" , "brine" : "104" , "bubble" : "237" , "bulldoze" : "95" , "confusion" : "235" , "cut" : "124" , "cut" : "223" , "dig" : "26" , "discharge" : "35" , "earthquake" : "31" , "ember" : "209" , "ember" : "4" , "flamethrower" : "24" , "headbutt" : "128" , "hurricane" : "122" , "lick" : "15" , "lick" : "212" , "megahorn" : "22" , "moonblast" : "87" , "peck" : "211" , "peck" : "37" , "pound" : "11" , "pound" : "222" , "psybeam" : "30" , "psychic" : "108" , "psyshock" : "60" , "psystrike" : "109" , "rest" : "132" , "scald" : "106" , "scratch" : "220" , "scratch" : "3" , "slam" : "130" , "slash" : "52" , "smog" : "17" , "spark" : "206" , "spark" : "76" , "splash" : "119" , "splash" : "231" , "stomp" : "127" , "struggle" : "133" , "submission" : "54" , "swift" : "125" , "tackle" : "221" , "tackle" : "6" , "thunderbolt" : "79" , "twineedle" : "43" , "twister" : "80" , "wrap" : "13", "sludge" : "90"}


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
                        pkm_list = [x for x in pkm_list if not x.startswith('#')]

    
                        # Find the Pokemon_name
                        pkm_n = str(pkm_list[0]).decode('utf-8')

                        # Pokemon_Chinese_Name-to-Pokemon_id convertion based on the dictionary
                        for k, v in pkm_hk_1.items():
                            pkm_n = pkm_n.replace(k, v)
                        for k, v in pkm_hk_2.items():
                            pkm_n = pkm_n.replace(k, v)

                        # Pokemon_English_Name-to-Pokemon_id convertion based on the dictionary
                        for k, v in pkm_1.items():
                            pkm_n = pkm_n.replace(k, v)
                        for k, v in pkm_2.items():
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
                        for k, v in mv_1.items():
                            pkm_mv1 = pkm_mv1.replace(k, v)
                            pkm_mv2 = pkm_mv2.replace(k, v)
                            
                        for k, v in mv_2.items():
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
