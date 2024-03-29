from kivymd.app import MDApp
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.config import Config
from kivymd.theming import ThemeManager
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.camera import Camera
from kivymd.uix.boxlayout import MDBoxLayout
import cv2
import mediapipe as mp
mp_pose = mp.solutions.pose
import time
from kivy.clock import Clock
from glawnyy import osnownoy
from kivy.graphics.texture import Texture
from kivymd.uix.button import MDRaisedButton
from kivy.uix.switch import Switch
from kivy.uix.video import Video
from threading import Thread, currentThread, Lock
# import json
from sqlite_file import sqlite_add, statistika_zanyatiy_plus, statistika_posle_zanyatiy, obnuleniye_statistiki_uprajneniy, wremya_plus, obnuleniye_wremeni, return_time
from datetime import datetime, timedelta
from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine

# data = json.load(open('my.json'))
# print(data['response'])

Builder.load_file('kvfiles/first_profile_window.kv')


Builder.load_file('kvfiles/first_window_home.kv')
Builder.load_file('kvfiles/second_window_home.kv')
Builder.load_file('kvfiles/third_window_home.kv')
Builder.load_file('kvfiles/fourth_window_home.kv')
Builder.load_file('kvfiles/fifth_window_home.kv')
Builder.load_file('kvfiles/second_profile_window.kv')

Builder.load_file('kvfiles/first_window_activity.kv')
Builder.load_file('kvfiles/filter_home_window.kv')


# class Ex(MDExpansionPanel):
#     panel_cls = MDExpansionPanelThreeLine(text="Text")
class Con(BoxLayout):
    pass


class MdBotNav(MDBottomNavigation):
    pass


class HomeScreenManager(ScreenManager):
    pass
class ActivityScreenManager(ScreenManager):
    pass
class ProfileScreenManager(ScreenManager):
    pass

class FilterHome(Screen):
    pass

class SecondProfileWindow(Screen):
    pass

class FirstMainWindow(Screen):
    pass

class FirstWindowHome(Screen):
    pass

class SecondWindowHome(Screen):
    pass



class ThirdWindowHome(Screen):
    pass



class FourthWindowHome(Screen):
    def build(self):
        obnuleniye_statistiki_uprajneniy()
        obnuleniye_wremeni()
        self.slide_1_bool = False
        self.slide_3_bool = False

        # eti peremenny nujny ctoby delat perehody mejdu uprajneniyami
        # self.a = True
        # self.b = True
        # self.c = True
        self.total_time = 0

        print('sola')
        # ctoby zakrywat potok
        self._lock = Lock()

        self.start_threads = True

        # sozdayu potok
        self.ct = Thread(target=self.countdown, name='name', args=(30, lambda: self.start_threads))

        # zapuskayu potok
        self.ct.start()

        # delayem web-cameru ctoby byla widna
        self.ids.imagee.opacity = 1

        self.udali = True
        self.image = self.ids.imagee

        # zapuskayem cameru
        self.capture = cv2.VideoCapture(0)

        # citayem iz video frame
        _, self.frame = self.capture.read()

        #opredelyayem pozy celoweka s pomoshu mediapipe
        self.pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

        # zapuskayem ne pryrywnuyu funskiyu (self.load_video)

        # while self.ids.cur.previous_slide != None:
        #     print(self.ids.cur.previous_slide)
        self.ids.cur.load_slide(self.ids.cur.slides[0])
        # print(self.ids.cur.slides)
        if self.ids.cur.index == 0:
            self.ids.cur.current_slide.vid.state = 'play'
        self.slide1 = self.ids.cur.current_slide.vid
        Clock.schedule_interval(self.playy, 0)
        Clock.schedule_interval(self.load_video, 0)



    def playy(self, *args):
        self.slide2 = self.ids.cur.current_slide.vid
        if self.slide1 != self.slide2:
            print('slide1 != slide2')
            self.start_threads = True
            self.slide1 = self.slide2
            self.t = 30
            self.ct = Thread(target=self.countdown, name='name', args=(10, lambda: self.start_threads))
            self.ct.start()
            try:
                self.ids.cur.previous_slide.vid.state = 'stop'
            except:
                pass

            self.ids.cur.current_slide.vid.state = 'play'
            try:

                self.ids.cur.next_slide.vid.state = 'stop'
            except:
                pass
    def on_touch_up(self, touch):
        if self.ids.cur.current_slide.vid.state == 'play':
            self.ids.cur.current_slide.vid.state = 'pause'
            self.bez_mediapipe = True
            self.start_threads = False
            self.ts = self.t



        else:
            self.t = self.ts
            self.start_threads = True
            self.ct = Thread(target=self.countdown, name='name', args=(int(self.t), lambda: self.start_threads))
            self.ct.start()
            self.ids.cur.current_slide.vid.state = 'play'

            self.bez_mediapipe = False



    def countdown(self, t, start):

        # otshitywayem wremya nazad

        # self.ct = currentThread()
        # while t and getattr(self.ct, 'do_run', True):

        self.t = t
        while t and start():
            with self._lock:
                print('a')
                mins, secs = divmod(self.t, 60)
                self.timer = '{:02d}:{:02d}'.format(mins, secs)
                # self.t = t - 1
                if start():
                    time.sleep(1)
                    self.t -= 1
                    wremya_plus()
                    if self.slide_1_bool:
                        # wremya_plus()
                        wremya_plus(time_1=True)
                    elif self.slide_3_bool:
                        # wremya_plus()
                        wremya_plus(time_2=True)
                else:
                    break



        print('salam')
        return 0
    def udalit(self):
        self.bez_mediapipe = False
        self.start_threads = False
        self.jumpi_bool = False
        self.prisi_bool = False
        self.counter = 0
        self.stage = None
        self.udali = False
        print('nazhali')

        # delayem web-cameru prazraznoy
        self.ids.imagee.opacity = 0

        return 'ostanowili'


    def jum(self):
        self.jumpi_bool = True
        self.prisi_bool = False
        self.counter = 0
        self.stage = None

    def pris(self):
        # self.wremya = time.time()
        self.prisi_bool = True
        self.jumpi_bool = False
        self.counter = 0
        self.stage = None

    def pause(self):
        self.bez_mediapipe = True
        self.udali = False
        self.start_threads = False
    def play(self):
        self.bez_mediapipe = False
        self.udali = True
        self.start_threads = True


    def load_video(self, *args):
        # print('a')
        # _, self.frame = self.capture.read()
        if self.udali:
            # wsyo uprajneniye
            if self.ids.cur.current_slide.vid == self.ids.vid_1:
                self.slide_1_bool = True
                print('good')
                self.ids.tren_1.text = 'Prisidaniye\n \n '
                self.ids.reps_num_1.text = '10\n \n '
                counter = self.counter
                print('delayem prisidaniye')
                self.frame, self.counter, self.stage = osnownoy(self.capture, self.pose, pris_bool=True,
                                                                counter=self.counter, stage=self.stage)
                self.ids.repss_1.text = str(self.counter)
                self.ids.wremya_1.text = self.timer
                if counter != self.counter:
                    # data['response']['prisidaniye'] = data['response']['prisidaniye'] + 1
                    # with open('my.json', 'w') as file:
                    #     json.dump(data, file, indent=4)
                    data = datetime.now().strftime('%d-%m-%Y')
                    sqlite_add(data, prisi_bool=True)
                    statistika_zanyatiy_plus(urj_1=True)
                if self.t == 0:
                    print('self.t == 0')
                    self.ids.cur.load_slide(self.ids.cur.next_slide)
                    self.ct = Thread(target=self.countdown, name='name', args=(30, lambda: self.start_threads))
                    self.ct.start()

            elif self.ids.cur.current_slide.vid == self.ids.vid_2:
                self.slide_1_bool = False
                self.slide_3_bool = False

                self.ids.tren_2.text = 'Otdyhayem\n \n '
                self.ids.reps_num_2.text = '10\n \n '
                self.ids.wremya_2.text = self.timer
                self.ids.repss_2.text = '0'

                print('otdyhayem')
                _, self.frame = self.capture.read()
                self.counter = 0
                self.stage = None
                if self.t == 0:
                    self.ids.cur.load_slide(self.ids.cur.next_slide)
                    self.ct = Thread(target=self.countdown, name='name', args=(20, lambda: self.start_threads))
                    self.ct.start()

            elif self.ids.cur.current_slide.vid == self.ids.vid_3:
                self.slide_3_bool = True
                self.ids.tren_3.text = 'Prygayem\n \n '
                self.ids.reps_num_3.text = '10\n \n '
                print('prygayem')
                counter = self.counter
                self.frame, self.counter, self.stage = osnownoy(self.capture, self.pose, jump_bool=True,
                                                                counter=self.counter, stage=self.stage)
                self.ids.repss_3.text = str(self.counter)
                self.ids.wremya_3.text = self.timer
                if counter != self.counter:
                    # data['response']['jump'] = data['response']['jump'] + 1
                    # with open('my.json', 'w') as file:
                    #     json.dump(data, file, indent=4)
                    data = datetime.now().strftime('%d-%m-%Y')
                    sqlite_add(data, jump_bool=True)
                    statistika_zanyatiy_plus(urj_2=True)
                if self.t == 0:
                    self.ids.cur.load_slide(self.ids.cur.next_slide)
                    self.ct = Thread(target=self.countdown, name='name', args=(30, lambda: self.start_threads))
                    self.ct.start()

            elif self.ids.cur.current_slide.vid == self.ids.vid_4:
                self.slide_1_bool = False
                self.slide_3_bool = False
                self.ids.tren_4.text = 'Otdyhayem\n \n '
                self.ids.reps_num_4.text = '10\n \n '
                self.ids.wremya_4.text = self.timer
                self.ids.repss_4.text = '0'
                print('otdyhayem')
                _, self.frame = self.capture.read()
                self.counter = 0
                self.stage = None
                if self.t == 0:
                    # self.ct = Thread(target=self.countdown, name='name', args=(20, lambda: self.start_threads))
                    # self.ct.start()
                    # if self.a:
                    self.parent.ids.fifth_window_home.build()
                    self.start_threads = False
                    self.udali = False
                    self.ids.cur.current_slide.vid.state = 'stop'
                    Clock.unschedule(self.playy)
                    Clock.unschedule(self.load_video)

                    print('help')
                    # print(self.parent.current)
                    self.parent.current = 'fifth_home'

                    # print(self.parent.current)

            elif self.jumpi_bool:
                # tolko jump
                self.frame, self.counter, self.stage = osnownoy(self.capture, self.pose, jump_bool=True, counter=self.counter,
                                                                stage=self.stage)
            buffer = cv2.flip(self.frame, 0).tostring()
            texture = Texture.create(size=(self.frame.shape[1], self.frame.shape[0]), colorfmt='bgr')
            texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')


            self.image.texture = texture
            # self.ids.repss.text = str(self.counter)
        elif self.bez_mediapipe:
            _, self.frame = self.capture.read()
            buffer = cv2.flip(self.frame, 0).tostring()
            texture = Texture.create(size=(self.frame.shape[1], self.frame.shape[0]), colorfmt='bgr')
            texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
            self.image.texture = texture
        else:
            # ostanawliwayem wes process
            Clock.unschedule(self.load_video)



    def back(self):

        # knopka kotoraya idyot nazad po uprajneniyem
        self.start_threads = False
        # self.ct.join()
        self.ids.videoo.state = 'play'
        if self.a:

            # self.ct.do_run = False
            self.start_threads = True

            self.ct = Thread(target=self.countdown, name='name', args=(int(30), lambda: self.start_threads))
            self.ct.start()

            # self.ct.do_run = True

        elif self.b:
            self.a = True
            # self.ct.do_run = False

            self.start_threads = True

            self.ct = Thread(target=self.countdown, name='name', args=(int(30), lambda: self.start_threads))
            self.ct.start()

            # self.ct.do_run = True

        elif self.c:
            self.b = True
            # self.ct.do_run = False

            self.start_threads = True

            self.ct = Thread(target=self.countdown, name='name', args=(int(30), lambda: self.start_threads))
            self.ct.start()

            # self.ct.do_run = True


            # self.ct.do_run = True



    def forward(self):

        # knopka kotoraya idyot wperyod po uprajneniyem
        self.start_threads = False
        # self.ct.join()
        self.ids.videoo.state = 'play'
        if self.a:
            self.a = False
            self.b = True
            # self.ct.do_run = False

            self.start_threads = True

            self.ct = Thread(target=self.countdown, name='name', args=(int(30), lambda: self.start_threads))
            self.ct.start()

            # self.ct.do_run = True

        elif self.b:
            self.b = False
            self.c = True
            # self.ct.do_run = False

            self.start_threads = True

            self.ct = Thread(target=self.countdown, name='name', args=(int(30), lambda: self.start_threads))
            self.ct.start()

            # self.ct.do_run = True

        elif self.c:
            self.c = False
            self.a = True
            # self.ct.do_run = False


            self.start_threads = True

            self.ct = Thread(target=self.countdown, name='name', args=(int(30), lambda: self.start_threads))
            self.ct.start()
            # self.ct.do_run = True

    def plays(self):
        # knopka playa i pauzy
        if self.ids.videoo.state == 'play':
            # self.ct.do_run = False
            self.start_threads = False
            print('self.ct.join(): ', self.ct.is_alive())
            # self.ct.join()
            print('self.ct.join(): ', self.ct.is_alive())
            # self._lock.acquire()
            # self._lock.release()
            self.start_threads = True

            self.ts = self.t
            self.ids.videoo.state = 'pause'
            self.pause()

        else:
            self.t = self.ts
            # if self.ct.join() == None:
            # if self.ct.is_alive() == False:
            self.start_threads = True
            self.ct = Thread(target=self.countdown, name='name', args=(int(self.t), lambda: self.start_threads))
            self.ct.start()
            # self.ct.do_run = True

            self.ids.videoo.state = 'play'
            self.play()

class FifthWindowHome(Screen):
    def build(self):
        self.ids.upr_1.text = statistika_posle_zanyatiy(urj_1=True)[1]
        self.ids.upr_2.text = statistika_posle_zanyatiy(urj_2=True)[1]
        self.ids.total_reps.text = statistika_posle_zanyatiy()[0]
        self.ids.total_time.text = return_time() + 's'
        self.ids.time_1.text = return_time(time_1=True)[1]
        self.ids.time_2.text = return_time(time_2=True)[1]


class FirstWindowActivity(Screen):
    def build(self, **kwargs):
        print('activity')
        today = datetime.today()
        self.ids.day_1_num.text = str((today - timedelta(days=5)).day)
        self.ids.day_2_num.text = str((today - timedelta(days=4)).day)
        self.ids.day_3_num.text = str((today - timedelta(days=3)).day)
        self.ids.day_4_num.text = str((today - timedelta(days=2)).day)
        self.ids.day_5_num.text = str((today - timedelta(days=1)).day)
        self.ids.day_6_num.text = str((today + timedelta(days=1)).day)

        self.ids.day_1_str.text = str((today - timedelta(days=5)).strftime('%A')[:3])
        self.ids.day_2_str.text = str((today - timedelta(days=4)).strftime('%A')[:3])
        self.ids.day_3_str.text = str((today - timedelta(days=3)).strftime('%A')[:3])
        self.ids.day_4_str.text = str((today - timedelta(days=2)).strftime('%A')[:3])
        self.ids.day_5_str.text = str((today - timedelta(days=1)).strftime('%A')[:3])
        self.ids.day_today_str.text = str(today.strftime('%A')[:3])
        self.ids.day_6_str.text = str((today + timedelta(days=1)).strftime('%A')[:3])
class FirstWindowProfile(Screen):
    pass
#Window.size = (720, 1280)
Window.size = (360, 620)

class StackLayoutExample(StackLayout):
    pass

class ImageButton(ButtonBehavior, Image):
    pass



class GridLayoutExample(GridLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass

class MainWidget(Widget):
    pass

class TheLabApp(MDApp):
    def build(self):
        # Builder.load_file('TheLab.kv')
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = "BlueGray"






TheLabApp(kv_file='TheLab.kv').run()