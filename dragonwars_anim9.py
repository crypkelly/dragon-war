

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.image import AsyncImage
from kivy.properties import StringProperty
from kivy.uix.slider import Slider
from kivy.uix.behaviors import ButtonBehavior  
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.core.audio import SoundLoader
from functools import partial
import random
import datetime

__version__ = '1.10.1'

Builder.load_string('''
#: import ScreenManager kivy.uix.screenmanager.ScreenManager

<Screen_Manager>:
    id: screen_manager
    Screen1:
        id: screen1
        name: "screen1"
    new_game:
        id: new_game
        name: "new_game"
    Begin_Screen:
        id: begin_screen
        name: 'begin_screen'
    Fight_Screen:
        id: fight_screen
        name: 'fight_screen'
        
<Screen1>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: "dragon_back4.jpg"
    BoxLayout:
        orientation: 'vertical'
      
        Image:
            source: 'dragon_title.png'
        Image:
            size_hint: 1,.7
            source: 'dragon_logo.png'
        Image:
            source: 'wars.png'
        Label:
            text: "It's a game of dragons... that war!"
        NewGame_Image:
            source: 'newgame.png'
            on_press: app.root.current= "new_game"
        LoadGame_Image:
            source: 'loadgame.png'
                
<new_game>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: "fantasy.jpg"
    BoxLayout:
        orientation: 'vertical'
        Label:
            font_size: 70
            bold: True
            color: 0,.3,.5,1
            size_hint: 1,.3
            text: "Select Dragon"
        BoxLayout:
            ImageButton:
                source: 'red_dragon.png'
                #on_press: app.root.current= "screen1"
            ImageButton1:
                source: 'regal_dragon.png'
                #on_press: app.root.current= "screen1"
        BoxLayout:
            ImageButton2:
                source: 'bad_dragon.png'
                #on_press: app.root.current= "screen1"
            ImageButton3:
                source: 'baby_dragon.png'
                #on_press: app.root.current= "screen1"
                
<Begin_Screen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: "hell.jpg"
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            size_hint: 1,.5
            Arena_Image:
                size_hint: 1,1
                source: 'arena_button.png'
                on_press: app.root.current= 'fight_screen'
        Label:
            size_hint: 1,.1
            text: "Arena Battle"
        BoxLayout:
            BoxLayout:
                size_hint: 1,.6
                orientation: 'vertical'
                Image:
                    size_hint: 1,.6
                    source: 'armor_button.png'
                Label:
                    size_hint: 1,.2
                    text: 'Dragon Armory'
            Image:
                source: 'selection_screen.png'
            BoxLayout:
                size_hint: 1,.5
                orientation: 'vertical'
                Image:
                    size_hint: 1,.5
                    source: 'apothecary_button.png'
                Label:
                    size_hint: 1,.2
                    text: 'Apothecary'
        Image:
            size_hint: 1,.5
            source: 'daily_button.png'
        Label:
            size_hint: 1,.2
            text: "Daily Reward"
            
        BoxLayout:
            Label:
                id: game_lbl
            Image:
                id: main_icon
    
<Fight_Screen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: "arena2.jpg"
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            size_hint: 1,1
            Image:
                size_hint: .6,.8
                id: enemy_dragon_img
            BoxLayout:
                size_hint: 1,.8
                orientation: 'vertical'
                BoxLayout:
                    spacing: 10
                    padding: 10               
                    Image:
                        size_hint: .3,1
                        source: 'agility1.png'
                    ProgressBar:
                        id: enemy_agility_bar
                        max: 100
                BoxLayout:
                    spacing: 10
                    padding: 10
                    Image:
                        size_hint: .3,1
                        source: 'strength.png'
                    ProgressBar:
                        id: enemy_strength_bar
                        max: 100
                BoxLayout:
                    spacing: 10
                    padding: 10
                    Image:
                        id: enemy_intellect_button
                        size_hint: .3,1
                        source: 'brain.png'
                    ProgressBar:
                        id: enemy_intellect_bar
                        max: 100
        BoxLayout:
            id: enemy_health
            size_hint: 1,.3
            Label:
            Label:
                id: enemy_health_lbl
                color: 0,1,1,1
                size_hint: .3,1
                text: '100'
                font_size: 50
            Image:
                size_hint: .5,1
                source: 'heart.png'
            Label:
        BoxLayout:
            id: enemy_attacks
            size_hint: 1,.2
        BoxLayout:
            BoxLayout:
                size_hint: .3,1
                Image:
                    pos: self.pos
                    id: enemy_shield_pic
                    source: 'enemy_shield1.png'
            Label:
                size_hint_y: None
                text_size: self.width, None
                height: self.texture_size[1]
                size_hint: 1,1
                id: enemy_fight_lbl
                font_size: 60
            BoxLayout:
                size_hint: .3,1
                Image:
                    pos: self.pos
                    id: enemy_attack_pic
                    source: 'enemy_target.png'
        BoxLayout:
            BoxLayout:
                size_hint: .3,1
                Image:
                    pos: self.pos
                    id: player_shield_pic
                    source: 'shield.png'
            Label:
                size_hint_y: None
                text_size: self.width, None
                height: self.texture_size[1]
                size_hint: 1,1
                id: fight_lbl
                font_size: 60
            BoxLayout:
                size_hint: .3,1
                Image:
                    pos: self.pos
                    id: player_attack_pic
                    source: 'player_target.png'
                   
        BoxLayout:
            id: player_health
            size_hint: 1,.3
            Agility_Image:
                id: agility_button
                size_hint: .7,.8
                source: 'agility1.png'
                on_press: root.agility_stat()
            Strength_Image:
                id: strength_button
                size_hint: .7,.8
                source: 'strength.png'
                on_press: root.strength_dmg()
            Intellect_Image:
                id: intellect_button
                size_hint: .7,.8
                source: 'brain.png' 
                on_press: root.intellect_powerup_schedule()   
            Image:
                size_hint: .3,1
                source: 'heart.png'
            Label:
                id: player_health_lbl
                color: 0,1,1,1
                size_hint: .3,1
                text: '100'
                font_size: 50
        BoxLayout:
            padding: 10
            spacing: 10
            id: player_attacks
            size_hint: 1,.2
        BoxLayout: 
            size_hint: 1,.7
            BoxLayout:
                size_hint: 1,.9
                orientation: 'vertical'
                BoxLayout:
                    spacing: 10
                    padding: 10
                    ProgressBar:
                        id: agility_bar
                        max: 100
                    Image:
                        size_hint: .6,1
                        source: 'agility1.png'
                BoxLayout:
                    spacing: 10
                    padding: 10
                    ProgressBar:
                        id: strength_bar
                        max: 100
                    Image:
                        size_hint: .6,1
                        source: 'strength.png'
                BoxLayout:
                    spacing: 10
                    padding: 10
                    ProgressBar:
                        id: intellect_bar
                        max: 100
                    Image:
                        size_hint: .6,1
                        source: 'brain.png'
            BoxLayout:
                size_hint: .4,1
                Image:
                    id: main_icon
            
<DragonStats>:
    size_hint: .6,.6
    title: 'Dragon Stats'
    BoxLayout:
        orientation: 'vertical'
        Label:
            id: stats_lbl
        Button:
            id: begin_bttn
            size_hint: 1,.2
            text: "Select Dragon"
            on_press: root.load_dragon()

''')

dragon_num=0

class Dragon1:
    def __init__(self,health=100,strength=0, agility=0, intellect=0):
        self.health=health
        self.strength= strength
        self.agility=agility
        self.intellect=intellect
        self.icon_source= 'red_dragon.png'
        
    def dr1_stats(self):
        self.agility= 0
        self.agility_regen = random.randint(1,10)
        self.strength = random.randint(10,10)
        self.intellect = 0
        self.intellect_regen = random.randint(20,30)
        
class Dragon2:
    def __init__(self,health=100,strength=0, agility=0, intellect=0):
        self.health=health
        self.strength= strength
        self.agility=agility
        self.intellect=intellect
        self.icon_source= 'regal_dragon.png'
        
    def dr2_stats(self):
        self.agility= 0
        self.agility_regen = random.randint(1,10)
        self.strength = random.randint(20,30)
        self.intellect = 0
        self.intellect_regen = random.randint(1,10)
        
class Dragon3:
    def __init__(self,health=100,strength=0, agility=0, intellect=0):
        self.health=health
        self.strength= strength
        self.agility=agility
        self.intellect=intellect
        self.icon_source= 'bad_dragon.png'
        
    def dr3_stats(self):
        self.agility= 0
        self.agility_regen = random.randint(10,20)
        self.strength = random.randint(10,20)
        self.intellect = 0
        self.intellect_regen = random.randint(1,10)
        
class Dragon4:
    def __init__(self,health=100,strength=0, agility=0, intellect=0):
        self.health=health
        self.strength= strength
        self.agility=agility
        self.intellect=intellect
        self.icon_source= 'baby_dragon.png'
        
    def dr4_stats(self):
        self.agility= 0
        self.agility_regen = random.randint(1,10)
        self.strength = random.randint(20,30)
        self.intellect = 0
        self.intellect_regen = random.randint(1,10)
        
class Enemy_Dragon:
    def __init__(self,health=100,strength=0, agility=0, intellect=0, intellect_regen=0, agility_regen= 0):
        self.health= health
        self.strength= strength
        self.agility=agility
        self.agility_regen = agility_regen
        self.intellect=intellect
        self.intellect_regen= intellect_regen
        self.icon_source= 'enemy_dragon1.png'
        
    def enemy_stats(self):
        self.agility= 0
        self.agility_regen = random.randint(10,20)
        self.strength = random.randint(20,30)
        self.intellect = 0
        self.intellect_regen = random.randint(10,20)
               
        
class Selected_Dragon:
    def __init__(self, choice='0', agility=0, strength= 0, intellect=0, intellect_regen=0, agility_regen= 0):
        self.source=choice
        self.agility= agility
        self.agility_regen= agility_regen
        self.strength= strength
        self.intellect= intellect
        self.intellect_regen= intellect_regen
        


class Screen_Manager(ScreenManager):
    pass
    
class Screen1(Screen):
    pass
    
class new_game(Screen):
    def on_enter(self):       
        self.bttn_effect = SoundLoader.load('steelsword.wav')
        self.bttn_effect.play()
        new_game.unstoppable = SoundLoader.load('unstoppable.wav')
        new_game.unstoppable.volume= .4
        
class Begin_Screen(Screen):
  
    def on_enter(self):
        global dragon_num
        if dragon_num == 4:
            self.ids.main_icon.source='baby_dragon.png'
            self.ids.game_lbl.text= 'Agility Regeneration  '+str(Selected_Dragon.agility_regen)+'\n''\n'+'Strength  '+str(Selected_Dragon.strength)+'\n''\n'+'Intellect Regeneration  '+str(Selected_Dragon.intellect_regen)
        if dragon_num == 3:
            self.ids.main_icon.source='bad_dragon.png'
            self.ids.game_lbl.text= 'Agility  '+str(dr3.agility)+'\n''\n'+'Strength  '+str(dr3.strength)+'\n''\n'+'Intellect  '+str(dr3.intellect)
        if dragon_num == 2:
            self.ids.main_icon.source= 'regal_dragon.png'
            self.ids.game_lbl.text= 'Agility  '+str(dr2.agility)+'\n''\n'+'Strength  '+str(dr2.strength)+'\n''\n'+'Intellect  '+str(dr2.intellect)
        if dragon_num == 1:
            self.ids.main_icon.source='red_dragon.png'
            self.ids.game_lbl.text= 'Agility  '+str(dr1.agility)+'\n''\n'+'Strength  '+str(dr1.strength)+'\n''\n'+'Intellect  '+str(dr1.intellect)
            
class Fight_Screen(Screen):
    
    def screen_splash(self, dt):
        with self.canvas.before:
            self.rec= Rectangle(pos=(800,1500), size_hint=(0,0), source='enemy_dragon1.png')
        self.splash= Animation(pos=(self.pos), size=self.size, duration=3)
        self.splash.start(self.rec)
        Clock.schedule_once(self.screen_splash_close, 3.5)
        
    def screen_splash_close(self, dt):
        self.splash= Animation(pos=(0,1300), size= (0,0), duration=1)
        self.splash.start(self.rec)

    def play_music(self):
        new_game.unstoppable.play()
        self.player_fire_breath= SoundLoader.load('player_dragon_breath.wav')
        self.enemy_fire_breath= SoundLoader.load('enemy_dragon_breath.wav')

    def on_enter(self):
        D= DragonWars()
        D.stop_intro()
        self.play_music()
        self.enemy_label_timer1 = datetime.datetime.now()
        self.player_label_timer1 = datetime.datetime.now()
        self.future= datetime.timedelta(seconds=5)
        player_shield_pic= Animation(size_hint=(0,0))
        player_shield_pic.start(self.ids.player_shield_pic)
        enemy_shield_pic= Animation(size_hint=(0,0))
        enemy_shield_pic.start(self.ids.enemy_shield_pic)
        attack_pic= Animation(size_hint=(0,0))
        attack_pic.start(self.ids.enemy_attack_pic)
        player_attack_pic= Animation(size_hint=(0,0))
        player_attack_pic.start(self.ids.player_attack_pic)
        self.count= 4
        self.regen_num= 1
        self.enemy_regen_num= 1
        self.player_random= 10
        self.enemy_random= 10
        self.dodge_window=False
        self.prevent_double_attack= False
        self.prevent_double_boost= False
        self.player_dodge=0
        self.ids.main_icon.source = Selected_Dragon.source
        self.ids.enemy_dragon_img.source = E.icon_source
        E.enemy_stats()
        self.ids.agility_bar.value = 0
        Clock.schedule_interval(self.countdown, 1)
        
    def countdown(self, dt):
        self.count= self.count - 1
        self.ids.fight_lbl.text= str(self.count)
        self.ids.enemy_fight_lbl.text= str(self.count)
        if self.count == 0:
            self.ids.fight_lbl.text = 'FIGHT!'
            self.ids.enemy_fight_lbl.text = 'FIGHT!'
            Clock.unschedule(self.countdown)
            self.begin_fight()
    
    def begin_fight(self):
        Clock.schedule_interval(self.update_bar, .3)
        Clock.schedule_interval(self.enemy_update_bar, .3)
          
    def update_bar(self,dt):
        self.player_label_timer = datetime.datetime.now()
        self.delta= self.player_label_timer1 + self.future
        if self.player_label_timer > self.delta:
            self.fight_label_anim_close(.3)
        if self.ids.strength_bar.value >= 30:
            self.ids.strength_button.size_hint = .7,1
        else:
            self.ids.strength_button.size_hint = .7,.8
        if self.ids.agility_bar.value >= 30:
            self.ids.agility_button.size_hint = .7,1
        else:
            self.ids.agility_button.size_hint = .7,.8
        if Selected_Dragon.intellect > 80:
            self.ids.intellect_button.size_hint = .7,1
        else: 
            self.ids.intellect_button.size_hint = .7,.8
               
        Selected_Dragon.intellect= Selected_Dragon.intellect + (self.regen_num + (Selected_Dragon.intellect_regen / 10))
        self.ids.intellect_bar.value = Selected_Dragon.intellect
        Selected_Dragon.agility = Selected_Dragon.agility + (self.regen_num + (Selected_Dragon.agility_regen / 10))
        self.ids.agility_bar.value = Selected_Dragon.agility
        self.ids.strength_bar.value = self.ids.strength_bar.value + self.regen_num
        self.player_chance= random.randint(1, 15)
        if self.player_chance == self.player_random:
            Selected_Dragon.agility = random.randint(1,100)
            self.ids.strength_bar.value = random.randint(1,100)         
        
        if Selected_Dragon.intellect > 100:
            Selected_Dragon.intellect = 100
            
        if Selected_Dragon.intellect < 0:
            Selected_Dragon.intellect = 0
        
        if Selected_Dragon.agility > 100:
            Selected_Dragon.agility = 100
            
        if Selected_Dragon.agility < 0:
            Selected_Dragon.agility = 0
            
        if Selected_Dragon.intellect > 75:
            self.combo_dmg()
            
    def intellect_powerup_schedule(self):
        if Selected_Dragon.intellect > 80:
            self.ids.intellect_button.source = 'idea.png'
            self.update_fight_label("Intellect powerup!", .3)
            self.intellect_counter= 11
            Clock.schedule_interval(self.intellect_powerup_timer, 1)
        else:
            self.update_fight_label("Not focused enough!", .3)
        
    def intellect_powerup_timer(self, dt):
        Selected_Dragon.intellect = 0
        self.intellect_counter= self.intellect_counter - 1
        self.player_random = 0
        self.regen_num = 3
        if self.intellect_counter == 0:
            self.update_fight_label("Intellect powerup finished.. ", .3)
            Clock.unschedule(self.intellect_powerup_timer)
            self.player_random = 10
            self.regen_num= 1
            self.ids.intellect_button.source = 'brain.png'
#enemy
            
    def enemy_intellect_powerup_schedule(self):
        if E.intellect > 80:
            self.ids.enemy_intellect_button.source = 'idea.png'
            self.update_enemy_fight_label("Intellect powerup!", .3)
            self.enemy_intellect_counter= 11
            Clock.schedule_interval(self.enemy_intellect_powerup_timer, 1)
        else:
            self.update_enemy_fight_label("Not focused enough!", .3)
        
    def enemy_intellect_powerup_timer(self, dt):
        self.prevent_double_boost= True
        E.intellect = 0
        self.enemy_intellect_counter= self.enemy_intellect_counter - 1
        self.enemy_random = 0
        self.enemy_regen_num = 3
        if self.enemy_intellect_counter == 0:
            self.update_enemy_fight_label("Intellect powerup finished.. ", .3)
            Clock.unschedule(self.enemy_intellect_powerup_timer)
            self.enemy_random = 10
            self.enemy_regen_num= 1
            self.prevent_double_boost= False
            self.ids.enemy_intellect_button.source = 'brain.png'
            
            
    def clear_player_combo(self, dt):
        self.ids.player_attacks.clear_widgets()              
          
    def combo_dmg(self):
           
        if self.ids.strength_bar.value and self.ids.agility_bar.value > 60:
            self.bttn=Button(text='test', background_color= (.2,.7,.6,.9))
            bttncallback= partial(self.screen_splash)
            self.bttn.bind(on_press= bttncallback)
            self.bttn.bind(on_release= self.clear_player_combo)
            self.ids.player_attacks.add_widget(self.bttn)
        
        if Selected_Dragon.intellect < 75:
            try:
                self.ids.player_attacks.clear_widgets()
            except:
                pass
           
    def enemy_update_bar(self,dt):
        self.enemy_label_timer = datetime.datetime.now()
        self.enemy_delta= self.enemy_label_timer1 + self.future
        if self.enemy_label_timer > self.enemy_delta:
            self.enemy_fight_label_anim_close(.3)
        E.intellect= E.intellect + (self.enemy_regen_num + (E.intellect_regen / 10))
        self.ids.enemy_intellect_bar.value = E.intellect
        E.agility = E.agility + (self.enemy_regen_num + (E.agility_regen / 10))
        self.ids.enemy_agility_bar.value = E.agility
        self.ids.enemy_strength_bar.value = self.ids.enemy_strength_bar.value + self.enemy_regen_num
        self.enemy_chance= random.randint(1, 17)
        if self.enemy_chance == 10:
            E.agility = random.randint(1,100)
            self.ids.enemy_strength_bar.value = random.randint(1,100)         
        
        if E.intellect > 100:
            E.intellect = 100
            
        if E.intellect < 0:
            E.intellect = 0
        
        if E.agility > 100:
            E.agility = 100
            
        if E.agility < 0:
            E.agility = 0
            
        
        self.enemy_chance_attack = random.randint(1,25)
        if self.enemy_chance_attack == 5 and self.prevent_double_attack==False:
            self.attack_countdown_clock()    
        
        if E.intellect > 80:
            self.enemy_chance_intellect_boost = random.randint(1,3)
            if self.enemy_chance_intellect_boost == 3 and self.prevent_double_boost==False:
                self.enemy_intellect_powerup_schedule()   
                

    def attack_countdown_clock(self):
        attack_pic= Animation(size_hint=(1,1))
        attack_pic.start(self.ids.enemy_attack_pic)
        self.prevent_double_attack=True
        self.dodge_window= True
        self.player_dodge= 1
        self.enemy_count = 4
        Clock.schedule_interval(self.enemy_attack_countdown, 1)

    def enemy_attack_countdown(self, dt):
        self.enemy_count= self.enemy_count - 1
        self.update_enemy_fight_label('Enemy attack in {}'.format(self.enemy_count), .3)
        
        if self.enemy_count == 0:
            Clock.unschedule(self.enemy_attack_countdown)
            self.enemy_attack()

    def enemy_attack(self):
        if self.ids.enemy_strength_bar.value and E.agility > 30:
            self.enemy_fire_breath.play()
            if self.player_dodge > 1:
                enemy_dmg_amount_float = int((E.strength * (self.ids.enemy_strength_bar.value / 100)) * ((100 - self.player_dodge) / 100))
                enemy_dmg_amount = int(enemy_dmg_amount_float)
            else:
                enemy_dmg_amount_float = int((E.strength * (self.ids.enemy_strength_bar.value / 100)))
                enemy_dmg_amount = int(enemy_dmg_amount_float)
                self.player_dodge= 0
            self.ids.player_health_lbl.text  = str(int(self.ids.player_health_lbl.text) - enemy_dmg_amount)
            self.ids.enemy_strength_bar.value = 0
            E.agility= E.agility - 30
            E.intellect = E.intellect - 50
            self.update_enemy_fight_label("Enemy burns you for {}".format(enemy_dmg_amount), .3)
            self.update_fight_label("You barrel roll and dodge {}% damage!".format(self.player_dodge), .3)
            self.prevent_double_attack= False
            attack_pic= Animation(size_hint=(0,0))
            attack_pic.start(self.ids.enemy_attack_pic)
            self.screen_splash(.3)
            #vibrator.vibrate(time=2)
            
        else:
            self.update_enemy_fight_label("Misses! No juice..", .3)
            self.prevent_double_attack= False
            attack_pic= Animation(size_hint=(0,0))
            attack_pic.start(self.ids.enemy_attack_pic)
       
    def strength_dmg(self):
        if self.ids.strength_bar.value and Selected_Dragon.agility > 30:
            self.enemy_agility_chance = random.randint(1,3)
            if self.enemy_agility_chance == 2:
                self.dmg_amount = int(Selected_Dragon.strength * (self.ids.strength_bar.value / 100))
                self.enemy_agility_stat()
            else:
                self.player_fire_breath.play()
                player_attack_pic= Animation(size_hint=(1,1))
                player_attack_pic.start(self.ids.player_attack_pic)
                Clock.schedule_once(self.player_attack_anim_close, 3)                                
                self.dmg_amount = int(Selected_Dragon.strength * (self.ids.strength_bar.value / 100))
                self.ids.enemy_health_lbl.text  = str(int(self.ids.enemy_health_lbl.text) - self.dmg_amount)
                self.ids.strength_bar.value = 0
                Selected_Dragon.agility= Selected_Dragon.agility - 50
                Selected_Dragon.intellect = Selected_Dragon.intellect - 30
                self.update_fight_label("Nailed 'em for {}".format(self.dmg_amount), .3)
                #vibrator.vibrate(time=2)
        else: 
            self.update_fight_label("Not enough skillz!", .3)

    def player_attack_anim_close(self,dt):
        player_attack_pic= Animation(size_hint=(0,0))
        player_attack_pic.start(self.ids.player_attack_pic)

    def player_shield_anim_close(self,dt):
        player_shield_pic= Animation(size_hint=(0,0))
        player_shield_pic.start(self.ids.player_shield_pic)
        
    def enemy_shield_anim_close(self,dt):
        enemy_shield_pic= Animation(size_hint=(0,0))
        enemy_shield_pic.start(self.ids.enemy_shield_pic)
        
    def agility_stat(self):
        if self.dodge_window==True:
            if Selected_Dragon.agility and self.ids.strength_bar.value > 30:
                player_shield_pic= Animation(size_hint=(1,1))
                player_shield_pic.start(self.ids.player_shield_pic)
                self.player_dodge = int(Selected_Dragon.agility) 
                Selected_Dragon.agility = Selected_Dragon.agility - 50
                Selected_Dragon.intellect = Selected_Dragon.intellect - 30
                self.dodge_window=False
                self.update_fight_label("You plan for the attack..", .3)
                Clock.schedule_once(self.player_shield_anim_close, 3)
            else:
                self.update_fight_label("Too exhausted to defend!", .3)
        else:
            self.update_fight_label("There's no attack weiner!", .3)
            Clock.schedule_once(self.player_shield_anim_close, 3)
            
    def enemy_agility_stat(self):
      
        if E.agility and self.ids.enemy_strength_bar.value > 30:
            enemy_shield_pic= Animation(size_hint=(1,1))
            enemy_shield_pic.start(self.ids.enemy_shield_pic)
            self.enemy_dodge= int(E.agility)
            self.enemy_hit_dmg= int(self.dmg_amount * ((100 - self.enemy_dodge) / 100))
            E.agility = E.agility - 50
            E.intellect = E.intellect - 30
            self.update_enemy_fight_label("Enemy dodges {}% damage, taking {}! ".format(self.enemy_dodge, self.enemy_hit_dmg), .3)
            self.ids.enemy_health_lbl.text  = str(int(self.ids.enemy_health_lbl.text) - self.enemy_hit_dmg)
            Clock.schedule_once(self.enemy_shield_anim_close, 3)
           
    def update_fight_label(self, msg, dt):
        self.player_label_timer1 = datetime.datetime.now()
        self.fight_label_anim= Animation(font_size=50, duration= .5)
        self.fight_label_anim.start(self.ids.fight_lbl)
        self.ids.fight_lbl.text= msg
        #Clock.schedule_once(self.fight_label_anim_close, 2.5)
        
    def fight_label_anim_close(self,dt):
        self.fight_label_anim = Animation(font_size=0, duration= .5)
        self.fight_label_anim.start(self.ids.fight_lbl)
       
    def update_enemy_fight_label(self, msg, dt):
        self.enemy_label_timer1 = datetime.datetime.now()
        self.enemy_fight_label_anim= Animation(font_size=50, duration= .5)
        self.enemy_fight_label_anim.start(self.ids.enemy_fight_lbl)
        self.ids.enemy_fight_lbl.text= msg
        #Clock.schedule_once(self.enemy_fight_label_anim_close, 4)
        
    def enemy_fight_label_anim_close(self,dt):
        self.enemy_fight_label_anim = Animation(font_size=0, duration= .5)
        self.enemy_fight_label_anim.start(self.ids.enemy_fight_lbl)
         
class ImageButton(ButtonBehavior, Image):  
    def on_press(self):
        global dragon_num
        dr1.dr1_stats()
        dragon_num=1
        Selected_Dragon.source= 'red_dragon.png'
        Selected_Dragon.agility= dr3.agility
        Selected_Dragon.agility_regen= dr1.agility_regen
        Selected_Dragon.strength= dr1.strength
        Selected_Dragon.intellect= dr1.intellect
        Selected_Dragon.intellect_regen= dr1.intellect_regen
        z.ids.stats_lbl.text= 'Agility  '+str(dr1.agility_regen)+'\n''\n'+'Strength  '+str(dr1.strength)+'\n''\n'+'Intellect Regeneration  '+str(dr1.intellect_regen)
        z.open() 
class ImageButton1(ButtonBehavior, Image):  
    def on_press(self):
        global dragon_num
        dr2.dr2_stats()
        dragon_num=2
        Selected_Dragon.source= 'regal_dragon.png'
        Selected_Dragon.agility= dr2.agility
        Selected_Dragon.agility_regen= dr2.agility_regen
        Selected_Dragon.strength= dr2.strength
        Selected_Dragon.intellect= dr2.intellect
        Selected_Dragon.intellect_regen= dr2.intellect_regen
        z.ids.stats_lbl.text= 'Agility  '+str(dr2.agility_regen)+'\n''\n'+'Strength  '+str(dr2.strength)+'\n''\n'+'Intellect Regeneration  '+str(dr2.intellect_regen)
        z.open() 
class ImageButton2(ButtonBehavior, Image):  
    def on_press(self):
        global dragon_num
        dr3.dr3_stats()
        dragon_num=3
        Selected_Dragon.source= 'bad_dragon.png'
        Selected_Dragon.agility= dr3.agility
        Selected_Dragon.agility_regen= dr3.agility_regen
        Selected_Dragon.strength= dr3.strength
        Selected_Dragon.intellect= dr3.intellect
        Selected_Dragon.intellect_regen= dr3.intellect_regen
        z.ids.stats_lbl.text= 'Agility  '+str(dr3.agility_regen)+'\n''\n'+'Strength  '+str(dr3.strength)+'\n''\n'+'Intellect Regeneration  '+str(dr3.intellect_regen)
        z.open()                                                                                                      
 
class ImageButton3(ButtonBehavior, Image):  
    def on_press(self):
        global dragon_num
        dr4.dr4_stats()
        dragon_num=4
        Selected_Dragon.source= 'baby_dragon.png'
        Selected_Dragon.agility= dr4.agility
        Selected_Dragon.agility_regen= dr4.agility_regen
        Selected_Dragon.strength= dr4.strength
        Selected_Dragon.intellect= dr4.intellect
        Selected_Dragon.intellect_regen= dr4.intellect_regen
        z.ids.stats_lbl.text= 'Agility  '+str(dr4.agility_regen)+'\n''\n'+'Strength  '+str(dr4.strength)+'\n''\n'+'Intellect Regeneration  '+str(dr4.intellect_regen)
        z.open()   

class Intellect_Image(ButtonBehavior, Image):
    def on_press(self):
        pass
               
class Strength_Image(ButtonBehavior, Image):
    def on_press(self):
        pass
class Agility_Image(ButtonBehavior, Image):
    def on_press(self):
        pass   
class Arena_Image(ButtonBehavior, Image):
    def on_press(self):
        pass   
class Daily_Image(ButtonBehavior, Image):
    def on_press(self):
        pass  
class NewGame_Image(ButtonBehavior, Image):
    def on_press(self):
        pass  
class LoadGame_Image(ButtonBehavior, Image):
    def on_press(self):
        pass  
                                                                                                                                                                                                              

class DragonStats(Popup):
    
    def load_dragon(self):
        z.dismiss()
        App.get_running_app().root.current = 'begin_screen'

class DragonWars(App):
        def build(self):
            return Screen_Manager()

        def on_start(self):
            DragonWars.intro= SoundLoader.load('intro.wav')
            Clock.schedule_once(self.play_intro, 3)
            
        def play_intro(self,dt):
            DragonWars.intro.play()

        def stop_intro(self):
            DragonWars.intro.stop()
          
dr1=Dragon1()
dr2=Dragon2()
dr3=Dragon3()
dr4=Dragon4()
z=DragonStats()
f= Fight_Screen()
E= Enemy_Dragon()

                               
DragonWars().run()
