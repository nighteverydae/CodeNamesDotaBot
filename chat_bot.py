import telebot
import random
from glob import glob

from telebot import types

bot = telebot.TeleBot('6312214732:AAEasFhBOtem_rzmR5OJiYw3eFp12ZaMIYM')
pull = []
answer = []

@bot.message_handler(commands=['start'])

def welcome(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    item1 = types.KeyboardButton('show')
    item2 = types.KeyboardButton('answer')
    markup.add(item1, item2)
    
    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup = markup)

    
@bot.message_handler(content_types=['text'])

def valhalla(message):
    if message.chat.type == 'private':
        
        heroes = ['Ogre Magi','Alchemist','Axe','Bristleback','Centaur Warrunner','Chaos Knight','Dawnbreaker','Doom','Dragon Knight','Earth Spirit','Earthshaker','Elder Titan','Huskar','Kunkka','Legion Commander','Lifestealer','Mars','Night Stalker','Omniknight','Primal Beast','Pudge','Slardar','Spirit Breaker','Sven','Tidehunter','Tiny','Treant Protector','Tusk','Underlord','Undying','Wraith King','Anti-Mage','Arc Warden','Bloodseeker','Bounty Hunter','Clinkz','Drow Ranger','Ember Spirit','Faceless Void','Gyrocopter','Hoodwink','Juggernaut','Luna','Medusa','Meepo','Monkey King','Morphling','Naga Siren','Phantom Assassin','Phantom Lancer','Razor','Riki','Shadow Fiend','Slark','Sniper','Spectre','Templar Assassin','Terrorblade','Troll Warlord','Ursa','Viper',
        'Weaver','Ancient Apparition','Crystal Maiden','Death Prophet','Disruptor','Enchantress','Grimstroke','Invoker','Jakiro','Keeper of the Light','Leshrac','Lich','Lina','Lion','Muerta','Nature’s Prophet','Necrophos','Oracle','Outworld Devourer','Puck','Pugna','Queen of Pain','Rubick','Shadow Demon','Shadow Shaman','Silencer','Skywrath Mage','Storm Spirit','Tinker','Warlock','Witch Doctor','Zeus','Abaddon','Bane','Batrider','Chen','Beastmaster','Brewmaster','Broodmother','Clockwerk','Dark Seer','Dark Willow','Dazzle','Enigma','Io','Lone Druid','Lycan','Magnus','Marci','Mirana','Nyx Assassin','Pangolier','Phoenix','Sand King','Snapfire','Techies','Timbersaw','Vengeful Spirit','Venomancer','Visage','Void Spirit','Windranger','Winter Wyvern']        
        
        
        
            
        if message.text.lower() == 'generate':
            markup = types.InlineKeyboardMarkup(row_width = 3)
            for i in range (16):
                hero = heroes.pop(random.randint(0,len(heroes)-1))
                pull.append(hero)
                item1 = types.InlineKeyboardButton(hero, callback_data = hero)
                markup.add(item1)            
            
            bot.send_message(message.chat.id, 'Новая игра создана!', reply_markup = markup)        
            for i in range(len(pull)-6):
                if i%2 == 0:
                    answer.append('🔵')
                else:
                    answer.append('🔴')
            answer.append('⚪')
            answer.append('⚪')
            answer.append('⚪')
            answer.append('⚪')
            answer.append('🟡')
            answer.append('⚫')
            
            random.shuffle(answer)
            for i in range(len(pull)):
                answer[i] += pull[i]
            print('generation succes!' + str(message.chat.id))    
        
        if message.text.lower() == 'show':
            red = 0
            blue = 0
            for i in range(len(pull)):
                if pull[i] == '🔴':
                    red += 1
                elif pull[i] == '🔵':
                    blue += 1
            print(str(message.chat.id) + 'посмотрел список')
            bot.send_message(message.chat.id, 'Текущий игровой список:\n' + str(pull) + '\nТекущий счет:' + ' 🔴'+str(red) + ' 🔵'+str(blue))        
            
        if message.text.lower() == 'answer':
            text = ''
            for i in range(len(answer)):
                text += '\n' + answer[i]
            print(str(message.chat.id) + 'получил ответ')
            bot.send_message(message.chat.id, 'Для чела, который объясняет:' + text)      
            
            
            
        else:
            pass
            

@bot.callback_query_handler(func = lambda call: True)
def callback_Inline(call):
    try:
        if call.message:
            
            for i in range(len(pull)):
                if call.data == pull[i]:
                    bot.send_message(call.message.chat.id, answer[i])
                    pull[i] = answer[i][0]
                
       
    except Exception as e:
        print(repr(e))
# RUN

bot.polling(none_stop=True, interval=0)
