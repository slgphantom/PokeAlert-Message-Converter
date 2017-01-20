## PokeAlert-Message-Converter
A python script converting PokeAlert external notification to Telegram (paid mode) into a json string which fits the webhook standand for PokeAlarm, via the getUpdates method.

Before using the script, I assume that you are already using [PokeAlert](https://github.com/PokeAlert/PokeAlert) and [PokeAlarm](https://github.com/kvangent/PokeAlarm) for scanning and pushing alert via Telegram.

Please feel free to imporve my code!

## Support
We currently support the following services:
* Paid Version 
[For example: Exeggcute 91% (14/12/15) confusion fast/psychic) till 21:38:00 (7m 24s) https://maps.google.com/maps?q=22.333501806422824,114.14156653862335 ]

We currently support the following languages:
* English
* Chinese

The free version script and the paid version (with reverse geocoding) will be uploaded once I have finish cleaning the code.

## Setup the Telegram
1. Set up two telegram channels (Channel A for public use, Channel B for updating the message)
2. Set up two bots (Bot A for PokeAlert external notification, Bot B for getUpdates and posting message in Channel A)
3. In Channel B, add Bot A as an administrator, then add Bot B as a member
4. In Channel A, add Bot B as an administrator

## Run the script
1. Run `python PokeAlert_Paid_Final.py`
2. Enter your BOT B TOKEN (should be something like `123456:asdfgh`)
3. Enter your CHANNEL_ID (Channel B) (should be something like `-1001081234123123`)
4. Enter WEBHOOK ADDRESS 1 (should be something like `http://127.0.0.1:4500`)
5. Enter WEBHOOK ADDRESS 2 (should be something like `http://127.0.0.1:4501`)
6. Type `thank you` (for my efforts XD)
7. Keep the script running

## FAQ

#### Why do I need to enter two webhook address?

* In some cases, PokeAlert external notification will not the show the time_till_hidden (XXm YYs), in order to keep the json string valid for PokeAlarm, the script will automatically set the tth for 3 minutes. Webhook Address 1 is for handling the fake time, while webhook address 2 is for handling the valid tth.

#### Will the getUpdates delay time affect the disappear time shown in PokeAlarm?

* In my own experience, there will have about 3 seconds delay time from recieving message from Channel B to posting message in Channel A, addition to the delay time from the PokeAlert app to Channel B, the script will automatically deduct 10s from the tth to minimize the affect of delay time.

#### How could you identify the tth?

* For the current version, we are using the (XXm YYs) to identify the tth, it should be fine for getUpdates in channel. In the coming versions, we will use the HH:MM:SS instead.

#### Anythings else I need to know?

* Remember to create two new bots, and use them **ONLY** in these two channel.

* After everything are setup, remeber to send a test notification from PokeAlert. In order to prevent duplicate messages, the first message recieved via getUpdates will be ignore, so if you don't sent the test notification, the first alert message sent by PokeAlert will be ignored. (Or you can manually send the message again by yourself in Channel B)

* A demostrating [Telegram Group](https://t.me/joinchat/AAAAAEDneTL7N4ys9T2Gmw) (in Chinese, and for testing only)
