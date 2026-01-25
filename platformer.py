import arcade
import arcade.key
import random

class Spieler(arcade.Sprite):

    def update(self):

        self.center_x += self.change_x
        self.center_y += self.change_y
        

class Gegner_nahkampf(arcade.Sprite):
    def __init__(self, dateiname, pos_min, pos_max, laufrichtung, spieler):
        super().__init__(dateiname)

        self.dateiname = dateiname
        self.pos_min = pos_min
        self.pos_max = pos_max
        self.laufrichtung = laufrichtung
        self.spieler = spieler


    def update(self):
        if self.center_x > self.pos_max:
            self.change_x = -0.7
            self.texture = arcade.load_texture(self.dateiname)

        if self.center_x < self.pos_min:
            self.change_x = 0.7
            self.texture = arcade.load_texture(self.dateiname, flipped_horizontally=True)

        if self.center_x - self.spieler.center_x < 400 and self.center_x - self.spieler.center_x > -400 and self.center_y - self.spieler.center_y < 100 and self.center_y - self.spieler.center_y > -100:
            if self.spieler.center_x < self.center_x:
                self.change_x = -2
                self.texture = arcade.load_texture(self.dateiname)
            
            if self.spieler.center_x > self.center_x:
                self.change_x = 2
                self.texture = arcade.load_texture(self.dateiname, flipped_horizontally=True)               


        self.center_x += self.change_x


class Gegner_sniper(arcade.Sprite):
    def __init__(self, dateiname, pos_min, pos_max, laufrichtung, spieler):
        super().__init__(dateiname)

        self.dateiname = dateiname
        self.pos_min = pos_min
        self.pos_max = pos_max
        self.laufrichtung = laufrichtung
        self.spieler = spieler


    def update(self):
        if self.center_x > self.pos_max:
            self.change_x = -0.7
            self.texture = arcade.load_texture(self.dateiname)

        if self.center_x < self.pos_min:
            self.change_x = 0.7
            self.texture = arcade.load_texture(self.dateiname, flipped_horizontally=True)


        if self.center_x - self.spieler.center_x < 450 and self.center_x - self.spieler.center_x > -450 and self.center_y - self.spieler.center_y < 100 and self.center_y - self.spieler.center_y > -100:
            if self.spieler.center_x < self.center_x:
                self.change_x = -0.9
                self.texture = arcade.load_texture(self.dateiname)
            
            if self.spieler.center_x > self.center_x:
                self.change_x = 0.9
                self.texture = arcade.load_texture(self.dateiname, flipped_horizontally=True)

    def aktion(self):

        if self.center_x - self.spieler.center_x < 500 and self.center_x - self.spieler.center_x > -500:
            if self.spieler.center_x < self.center_x:

                kugel = arcade.Sprite("energie_ball.png", flipped_diagonally=True)

                kugel.center_x = self.center_x - 30
                kugel.center_y = self.center_y
    
                kugel.change_x = -5
                kugel.change_y = 0

                return (kugel)
            
            if self.spieler.center_x > self.center_x:

                kugel = arcade.Sprite("energie_ball.png")

                kugel.center_x = self.center_x + 30
                kugel.center_y = self.center_y
    
                kugel.change_x = -7
                kugel.change_y = 0

                return (kugel)
            



                
class Gegner_fernkampf(arcade.Sprite):
    def __init__(self, dateiname, pos_min, pos_max, laufrichtung, spieler):
        super().__init__(dateiname)

        self.dateiname = dateiname
        self.pos_min = pos_min
        self.pos_max = pos_max
        self.laufrichtung = laufrichtung
        self.spieler = spieler


    def update(self):
        if self.center_x > self.pos_max:
            self.change_x = -0.7
            self.texture = arcade.load_texture(self.dateiname)

        if self.center_x < self.pos_min:
            self.change_x = 0.7
            self.texture = arcade.load_texture(self.dateiname, flipped_horizontally=True)


        if self.center_x - self.spieler.center_x < 200 and self.center_x - self.spieler.center_x > -200 and self.center_y - self.spieler.center_y < 100 and self.center_y - self.spieler.center_y > -100:
            if self.spieler.center_x < self.center_x:
                self.change_x = -1.3
                self.texture = arcade.load_texture(self.dateiname)
            
            if self.spieler.center_x > self.center_x:
                self.change_x = 1.3
                self.texture = arcade.load_texture(self.dateiname, flipped_horizontally=True)

    def aktion(self):

        if self.center_x - self.spieler.center_x < 350 and self.center_x - self.spieler.center_x > -350:
            if self.spieler.center_x < self.center_x:

                kugel = arcade.Sprite("energie_ball.png", flipped_diagonally=True)

                kugel.center_x = self.center_x - 30
                kugel.center_y = self.center_y
    
                kugel.change_x = -5
                kugel.change_y = 0

                return (kugel)
            
            if self.spieler.center_x > self.center_x:

                kugel = arcade.Sprite("energie_ball.png")

                kugel.center_x = self.center_x + 30
                kugel.center_y = self.center_y
    
                kugel.change_x = -5
                kugel.change_y = 0

                return (kugel)
            



class Gegner_heavy(arcade.Sprite):
    def __init__(self, dateiname, pos_min, pos_max, laufrichtung, spieler):
        super().__init__(dateiname)

        self.dateiname = dateiname
        self.pos_min = pos_min
        self.pos_max = pos_max
        self.laufrichtung = laufrichtung
        self.spieler = spieler


    def update(self):
        if self.center_x > self.pos_max:
            self.change_x = -0.3
            self.texture = arcade.load_texture(self.dateiname)
        
        if self.center_x < self.pos_min:
            self.change_x = 0.3
            self.texture = arcade.load_texture(self.dateiname, flipped_horizontally=True)


        if self.center_x - self.spieler.center_x < 200 and self.center_x - self.spieler.center_x > -200 and self.center_y - self.spieler.center_y < 100 and self.center_y - self.spieler.center_y > -100:
            if self.spieler.center_x < self.center_x:
                self.change_x = -0.7
                self.texture = arcade.load_texture(self.dateiname)
            else:
                self.change_x = 0.7
                self.texture = arcade.load_texture(self.dateiname, flipped_horizontally=True)

    def aktion(self):

        if self.center_x - self.spieler.center_x < 700 and self.center_x - self.spieler.center_x > -700:
            if self.spieler.center_x < self.center_x:

                rocket = arcade.Sprite("rocket_pod.png")

                rocket.center_x = self.center_x - 30
                rocket.center_y = self.center_y
    
                rocket.change_x = -10
                rocket.change_y = 0

                return (rocket)
            
            else:

                rocket = arcade.Sprite("rocket_pod.png", flipped_diagonally=True)

                rocket.center_x = self.center_x + 30
                rocket.center_y = self.center_y
    
                rocket.change_x = 10
                rocket.change_y = 0

                return (rocket)



 
class Spiel(arcade.Window): 
    def __init__(self, breite, höhe, titel):
        super().__init__(700, 300, titel)
        arcade.set_background_color(arcade.color.WHITE)
        self.kamera = arcade.Camera(700, 300)

        arcade.enable_timings()
        self.x_alt = 0

        self.setup()

    def setup(self):
        
        tm = arcade.load_tilemap("Karte.tmx")
        self.szene = arcade.Scene.from_tilemap(tm)
         
        self.dash_verzögerung = 0

        self.level_zahl = 1

        self.facing_direction = 0

        self.herzen = 1

        self.herzen_leer = 0
        
        self.h = 2

        self.szene.add_sprite_list("spielerliste")

        self.szene.add_sprite_list("sprite_list")

        self.szene.add_sprite_list("herzen")

        self.szene.add_sprite_list("schlüssel")

        self.herz = arcade.Sprite("herz.png")
        self.herz.center_x = 660
        self.herz.center_y = 300
        self.szene.get_sprite_list("herzen").append(self.herz)

        self.herz2 = arcade.Sprite("herz2.png")
        self.herz2.center_x = 450
        self.herz2.center_y = 170
        self.szene.get_sprite_list("herzen").append(self.herz2)

        self.herz3 = arcade.Sprite("herz.png")
        self.herz3.center_x = 10000
        self.herz3.center_y = 10000
        self.szene.get_sprite_list("herzen").append(self.herz3)
        
        self.herz4 = arcade.Sprite("herz2.png")
        self.herz4.center_x = 448
        self.herz4.center_y = 530
        self.szene.get_sprite_list("herzen").append(self.herz4)

        self.herz5 = arcade.Sprite("herz.png")
        self.herz5.center_x = 100000
        self.herz5.center_y = 100000
        self.szene.get_sprite_list("herzen").append(self.herz5)

        self.Spieler1 = Spieler("Sprite-0001.png")
        self.Spieler1.center_x = 70
        self.Spieler1.center_y = 200
        self.szene.get_sprite_list("spielerliste").append(self.Spieler1)


        self.schlüssel = arcade.Sprite("Schlüssel.png")
        self.schlüssel.center_x = 449
        self.schlüssel.center_y = 80
        self.szene.get_sprite_list("schlüssel").append(self.schlüssel)
            
        self.physik_engine = arcade.PhysicsEnginePlatformer(self.Spieler1, [self.szene.get_sprite_list("Tile Layer 1"), self.szene.get_sprite_list("Tueren"), self.szene.get_sprite_list("herzen"), self.szene.get_sprite_list("schlüssel")], ladders=self.szene["Leitern"], gravity_constant = 0.3)

    def setup2(self):

        self.dash_verzögerung = 0

        self.arrows = 20

        self.runen = 1

        self.level_zahl = 2

        self.gp2 = 0

        self.gp = 0

        self.b = 0

        self.facing_direction = 0

        self.h = self.h

        self.tm2 = arcade.load_tilemap("Level_2.tmx") 
        self.szene2 = arcade.Scene.from_tilemap(self.tm2)

        self.szene2.add_sprite_list("gegnerliste")

        self.szene2.add_sprite_list("spielerliste")

        self.szene2.add_sprite_list("sprite_list")

        self.szene2.add_sprite_list("herzen")

        self.szene2.add_sprite_list("bow")

        self.szene2.add_sprite_list("bullets")

        self.bow = arcade.Sprite("bow1-removebg-preview.png")
        self.bow.center_x = 970
        self.bow.center_y = 55
        self.szene2.get_sprite_list("bow").append(self.bow)

        self.herz = arcade.Sprite("herz.png")
        self.herz.center_x = 660
        self.herz.center_y = 300
        self.szene2.get_sprite_list("herzen").append(self.herz)

        self.herz3 = arcade.Sprite("herz.png")
        self.herz3.center_x = 10000
        self.herz3.center_y = 10000
        self.szene2.get_sprite_list("herzen").append(self.herz3)

        self.herz5 = arcade.Sprite("herz.png")
        self.herz5.center_x = 100000
        self.herz5.center_y = 100000
        self.szene2.get_sprite_list("herzen").append(self.herz5)

        self.Spieler1 = arcade.Sprite("Sprite-0001.png")
        self.Spieler1.center_x = 48
        self.Spieler1.center_y = 944
        self.szene2.get_sprite_list("spielerliste").append(self.Spieler1)
        
        self.gegner = Gegner_nahkampf("skel.png", 176, 304, "x", self.Spieler1)
        self.gegner.center_x = 192
        self.gegner.center_y = 880
        self.gegner.change_x = 1
        self.szene2.get_sprite_list("gegnerliste").append(self.gegner)
        self.gegner.texture = arcade.load_texture("skel.png", flipped_horizontally=True)

        self.gegner2 = Gegner_nahkampf("skel.png", 950, 1216, "x", self.Spieler1)
        self.gegner2.center_x = 1152
        self.gegner2.center_y = 48
        self.gegner2.change_x = 1
        self.szene2.get_sprite_list("gegnerliste").append(self.gegner2)
        self.gegner2.texture = arcade.load_texture("skel.png", flipped_horizontally=True)

        self.physik_engine = arcade.PhysicsEnginePlatformer(self.Spieler1, self.szene2.get_sprite_list("herzen"), walls=[self.szene2.get_sprite_list("Tile Layer 1"), self.szene2.get_sprite_list("Tueren"),], ladders=self.szene2["Leitern"], gravity_constant = 0.3)

        self.physik_engine_2 = arcade.PhysicsEnginePlatformer(self.gegner, walls=[self.szene2.get_sprite_list("Tile Layer 1"),], gravity_constant=0.3)
        self.physik_engine_3 = arcade.PhysicsEnginePlatformer(self.gegner2, walls=[self.szene2.get_sprite_list("Tile Layer 1"),], gravity_constant=0.3)

    def setup3(self):

        self.delta_help = 0

        self.dash_verzögerung = 0

        self.shield_time = 0

        self.shield_verzögerung = 0

        self.gp2 = 0

        self.gp = 0

        self.b = 1

        self.arrows = 20

        self.level_zahl = 3

        self.h = self.h

        self.facing_direction = 0

        self.kugel_verzögerung = 0

        self.door = 1

        self.tm3 = arcade.load_tilemap("Level_3.tmx") 
        self.szene3 = arcade.Scene.from_tilemap(self.tm3)

        self.szene3.add_sprite_list("gegnerliste")

        self.szene3.add_sprite_list("spielerliste")

        self.szene3.add_sprite_list("sprite_list")

        self.szene3.add_sprite_list("herzen")

        self.szene3.add_sprite_list("bow")

        self.szene3.add_sprite_list("bullets")

        self.szene3.add_sprite_list("props") 

        self.herz = arcade.Sprite("herz.png")
        self.herz.center_x = 660
        self.herz.center_y = 300
        self.szene3.get_sprite_list("herzen").append(self.herz)

        self.herz3 = arcade.Sprite("herz.png")
        self.herz3.center_x = 10000
        self.herz3.center_y = 10000
        self.szene3.get_sprite_list("herzen").append(self.herz3)

        self.herz5 = arcade.Sprite("herz.png")
        self.herz5.center_x = 100000
        self.herz5.center_y = 100000
        self.szene3.get_sprite_list("herzen").append(self.herz5)

        self.Spieler1 = Spieler("Sprite-0001.png")
        self.Spieler1.center_x = 4704
        self.Spieler1.center_y = 384
        self.szene3.get_sprite_list("spielerliste").append(self.Spieler1)

        self.gegner = Gegner_nahkampf("slushy.png", 362, 694, "x", self.Spieler1)
        self.gegner.center_x = 538
        self.gegner.center_y = 112
        self.gegner.change_x = 1
        self.szene3.get_sprite_list("gegnerliste").append(self.gegner)
        self.gegner.texture = arcade.load_texture("slushy.png", flipped_horizontally=True)

        self.gegner2 = Gegner_nahkampf("slushy.png", 362, 694, "x", self.Spieler1)
        self.gegner2.center_x = 538
        self.gegner2.center_y = 112
        self.gegner2.change_x = -1
        self.szene3.get_sprite_list("gegnerliste").append(self.gegner2)
        self.gegner2.texture = arcade.load_texture("slushy.png")

        self.gegner3 = Gegner_fernkampf("android_gegner.png", 1290, 1718, "x", self.Spieler1)
        self.gegner3.center_x = 1380
        self.gegner3.center_y = 140
        self.gegner3.change_x = -1
        self.szene3.get_sprite_list("gegnerliste").append(self.gegner3)
        self.gegner3.texture = arcade.load_texture("android_gegner.png")        

        self.gegner4 = Gegner_fernkampf("android_gegner.png", 1898, 2454, "x", self.Spieler1)
        self.gegner4.center_x = 2016
        self.gegner4.center_y = 140
        self.gegner4.change_x = -1
        self.szene3.get_sprite_list("gegnerliste").append(self.gegner4)
        self.gegner4.texture = arcade.load_texture("android_gegner.png")    

        self.gegner5 = Gegner_fernkampf("test.png", 1898, 2454, "x", self.Spieler1)
        self.gegner5.center_x = 2156
        self.gegner5.center_y = 140
        self.gegner5.change_x = 1
        self.szene3.get_sprite_list("gegnerliste").append(self.gegner5)
        self.gegner5.texture = arcade.load_texture("android_gegner.png")

            

        self.gegner6 = Gegner_fernkampf("android_gegner.png", 1898, 2454, "x", self.Spieler1)
        self.gegner6.center_x = 2186
        self.gegner6.center_y = 140
        self.gegner6.change_x = -1
        self.szene3.get_sprite_list("gegnerliste").append(self.gegner6)
        self.gegner6.texture = arcade.load_texture("android_gegner.png")

        self.bubble = arcade.Sprite("bubble_game.png")
        self.bubble.center_x = 10000
        self.bubble.center_y = 10000
        self.szene3.get_sprite_list("props").append(self.bubble)

        self.physik_engine = arcade.PhysicsEnginePlatformer(self.Spieler1, self.szene3.get_sprite_list("herzen"), walls=[self.szene3.get_sprite_list("Tile Layer 1"),], gravity_constant = 0.3)

        self.physik_engine_1 = arcade.PhysicsEnginePlatformer(self.gegner, walls=[self.szene3.get_sprite_list("Tile Layer 1"),], gravity_constant = 0.3)
        self.physik_engine_2 = arcade.PhysicsEnginePlatformer(self.gegner2, walls=[self.szene3.get_sprite_list("Tile Layer 1"),], gravity_constant=0.3)
        self.physik_engine_3 = arcade.PhysicsEnginePlatformer(self.gegner3, walls=[self.szene3.get_sprite_list("Tile Layer 1"),], gravity_constant=0.3)
        self.physik_engine_4 = arcade.PhysicsEnginePlatformer(self.gegner4, walls=[self.szene3.get_sprite_list("Tile Layer 1"),], gravity_constant=0.3)
        self.physik_engine_5 = arcade.PhysicsEnginePlatformer(self.gegner5, walls=[self.szene3.get_sprite_list("Tile Layer 1"),], gravity_constant=0.3)
        self.physik_engine_6 = arcade.PhysicsEnginePlatformer(self.gegner6, walls=[self.szene3.get_sprite_list("Tile Layer 1"),], gravity_constant=0.3)

    def setup4(self):

        self.delta_help = 0

        self.dash_verzögerung = 0

        self.shield_time = 0

        self.shield_verzögerung = 0

        self.gp2 = 0

        self.gp = 0

        self.b = 1

        self.arrows = 20

        self.level_zahl = 4

        self.h = self.h

        self.facing_direction = 0

        self.kugel_verzögerung = 0

        self.rocket_verzögerung = 0


        self.tm4 = arcade.load_tilemap("Level_4.tmx") 
        self.szene4 = arcade.Scene.from_tilemap(self.tm4)

        self.szene4.add_sprite_list("gegnerliste")

        self.szene4.add_sprite_list("spielerliste")

        self.szene4.add_sprite_list("sprite_list")

        self.szene4.add_sprite_list("herzen")

        self.szene4.add_sprite_list("bow")

        self.szene4.add_sprite_list("bullets")



        self.szene4.add_sprite_list("props") 

        self.szene4.add_sprite_list("entrance doors")

        self.szene4.add_sprite_list("exit doors")


        self.herz = arcade.Sprite("herz.png")
        self.herz.center_x = 660
        self.herz.center_y = 300
        self.szene4.get_sprite_list("herzen").append(self.herz)

        self.herz3 = arcade.Sprite("herz.png")
        self.herz3.center_x = 10000
        self.herz3.center_y = 10000
        self.szene4.get_sprite_list("herzen").append(self.herz3)

        self.herz5 = arcade.Sprite("herz.png")
        self.herz5.center_x = 100000
        self.herz5.center_y = 100000
        self.szene4.get_sprite_list("herzen").append(self.herz5)

        self.Spieler1 = Spieler("Sprite-0001.png")
        self.Spieler1.center_x = 48
        self.Spieler1.center_y = 48
        self.szene4.get_sprite_list("spielerliste").append(self.Spieler1)


        self.en_door1 = arcade.Sprite("factorie_door.jpg")
        self.en_door1.center_x = 2064
        self.en_door1.center_y = 183
        self.szene4.get_sprite_list("entrance doors").append( self.en_door1)

        self.en_door2 = arcade.Sprite("factorie_door.jpg")
        self.en_door2.center_x = 3760
        self.en_door2.center_y = 87
        self.szene4.get_sprite_list("entrance doors").append( self.en_door2)

        self.en_door3 = arcade.Sprite("factorie_door.jpg")
        self.en_door3.center_x = 4432
        self.en_door3.center_y = 87
        self.szene4.get_sprite_list("entrance doors").append( self.en_door3)

        self.en_door4 = arcade.Sprite("factorie_door.jpg")
        self.en_door4.center_x = 4592
        self.en_door4.center_y = 279
        self.szene4.get_sprite_list("entrance doors").append( self.en_door4)

        self.en_door5 = arcade.Sprite("factorie_door.jpg")
        self.en_door5.center_x = 4208
        self.en_door5.center_y = 567
        self.szene4.get_sprite_list("entrance doors").append( self.en_door5)
        self.en_door5.texture = arcade.load_texture("factorie_door.jpg", flipped_horizontally=True)    

        self.en_door6 = arcade.Sprite("factorie_door.jpg")
        self.en_door6.center_x = 176
        self.en_door6.center_y = 535
        self.szene4.get_sprite_list("entrance doors").append( self.en_door6)
        self.en_door6.texture = arcade.load_texture("factorie_door.jpg", flipped_horizontally=True)    

        self.en_door7 = arcade.Sprite("factorie_door.jpg")
        self.en_door7.center_x = 4720
        self.en_door7.center_y = 887
        self.szene4.get_sprite_list("entrance doors").append( self.en_door7)

        self.en_door8 = arcade.Sprite("factorie_door.jpg")
        self.en_door8.center_x = 4752
        self.en_door8.center_y = 1463
        self.szene4.get_sprite_list("entrance doors").append( self.en_door8)



        self.ex_door1 = arcade.Sprite("factorie_door.jpg")
        self.ex_door1.center_x = 2128
        self.ex_door1.center_y = 183
        self.szene4.get_sprite_list("exit doors").append( self.ex_door1)
        self.ex_door1.texture = arcade.load_texture("factorie_door.jpg", flipped_horizontally=True)    

        self.ex_door2 = arcade.Sprite("factorie_door.jpg")
        self.ex_door2.center_x = 3056
        self.ex_door2.center_y = 119
        self.szene4.get_sprite_list("exit doors").append( self.ex_door2)
        self.ex_door2.texture = arcade.load_texture("factorie_door.jpg", flipped_horizontally=True)    

        self.ex_door3 = arcade.Sprite("factorie_door.jpg")
        self.ex_door3.center_x = 4496
        self.ex_door3.center_y = 87
        self.szene4.get_sprite_list("exit doors").append( self.ex_door3)
        self.ex_door3.texture = arcade.load_texture("factorie_door.jpg", flipped_horizontally=True)

        self.ex_door4 = arcade.Sprite("factorie_door.jpg")
        self.ex_door4.center_x = 4656
        self.ex_door4.center_y = 279
        self.szene4.get_sprite_list("exit doors").append( self.ex_door4)
        self.ex_door4.texture = arcade.load_texture("factorie_door.jpg", flipped_horizontally=True)    

        self.ex_door5 = arcade.Sprite("factorie_door.jpg")
        self.ex_door5.center_x = 4143
        self.ex_door5.center_y = 567
        self.szene4.get_sprite_list("exit doors").append( self.ex_door5)
        self.ex_door5.texture = arcade.load_texture("factorie_door.jpg")    

        self.ex_door6 = arcade.Sprite("factorie_door.jpg")
        self.ex_door6.center_x = 784
        self.ex_door6.center_y = 311
        self.szene4.get_sprite_list("exit doors").append( self.ex_door6)
        self.ex_door6.texture = arcade.load_texture("factorie_door.jpg")    

        self.ex_door7 = arcade.Sprite("factorie_door.jpg")
        self.ex_door7.center_x = 4175
        self.ex_door7.center_y = 791
        self.szene4.get_sprite_list("exit doors").append( self.ex_door7)
        self.ex_door7.texture = arcade.load_texture("factorie_door.jpg", flipped_horizontally=True)    

        self.ex_door8 = arcade.Sprite("factorie_door.jpg")
        self.ex_door8.center_x = 48
        self.ex_door8.center_y = 1463
        self.szene4.get_sprite_list("exit doors").append( self.ex_door8)
        self.ex_door8.texture = arcade.load_texture("factorie_door.jpg", flipped_horizontally=True)   

        self.ex_door9 = arcade.Sprite("factorie_door.jpg")
        self.ex_door9.center_x = 16
        self.ex_door9.center_y = 55
        self.szene4.get_sprite_list("exit doors").append( self.ex_door9)
        self.ex_door9.texture = arcade.load_texture("factorie_door.jpg", flipped_horizontally=True)       

        self.gegner1 = Gegner_heavy("Rocket_Cyborg.png", 1856, 1984, "x", self.Spieler1)
        self.gegner1.center_x = 1920
        self.gegner1.center_y = 1280
        self.gegner1.change_x = -1
        self.szene4.get_sprite_list("gegnerliste").append(self.gegner1)
        self.gegner1.texture = arcade.load_texture("Rocket_Cyborg.png", flipped_horizontally=True)

        self.gegner2 = Gegner_nahkampf("rt1.png", 832, 1664, "x", self.Spieler1)
        self.gegner2.center_x = 1280
        self.gegner2.center_y = 80
        self.gegner2.change_x = 0
        self.szene4.get_sprite_list("gegnerliste").append(self.gegner2)    

        self.gegner3 = Gegner_sniper("th.png", 1792, 2016, "x", self.Spieler1)
        self.gegner3.center_x = 1920
        self.gegner3.center_y = 192
        self.gegner3.change_x = 1
        self.szene4.get_sprite_list("gegnerliste").append(self.gegner3)

        self.gegner4 = Gegner_nahkampf("rt1.png", 192, 736, "x", self.Spieler1)
        self.gegner4.center_x = 448
        self.gegner4.center_y = 320
        self.gegner4.change_x = -1
        self.szene4.get_sprite_list("gegnerliste").append(self.gegner4)
        self.gegner4.texture = arcade.load_texture("rt1.png", flipped_horizontally=True)

        self.gegner5 = Gegner_sniper("th.png", 2944, 3616, "x", self.Spieler1)
        self.gegner5.center_x = 3584
        self.gegner5.center_y = 320
        self.gegner5.change_x = 0
        self.szene4.get_sprite_list("gegnerliste").append(self.gegner5)

        self.gegner6 = Gegner_nahkampf("rt1.png", 2112, 3808, "x", self.Spieler1)
        self.gegner6.center_x = 3008
        self.gegner6.center_y = 320
        self.gegner6.change_x = 0
        self.szene4.get_sprite_list("gegnerliste").append(self.gegner6)

        self.gegner7 = Gegner_nahkampf("rt1.png", 2112, 3808, "x", self.Spieler1)
        self.gegner7.center_x = 3296
        self.gegner7.center_y = 320
        self.gegner7.change_x = 0
        self.szene4.get_sprite_list("gegnerliste").append(self.gegner7)

        self.gegner8 = Gegner_sniper("th.png", 4448, 4576, "x", self.Spieler1)
        self.gegner8.center_x = 4544
        self.gegner8.center_y = 288
        self.gegner8.change_x = -1
        self.szene4.get_sprite_list("gegnerliste").append(self.gegner8)




        self.physik_engine = arcade.PhysicsEnginePlatformer(self.Spieler1, self.szene4.get_sprite_list("herzen"), walls=[self.szene4.get_sprite_list("Tile Layer 1"),], ladders=self.szene4.get_sprite_list("leitern"), gravity_constant = 0.3)

        self.physik_engine_1 = arcade.PhysicsEnginePlatformer(self.gegner1, walls=[self.szene4.get_sprite_list("Tile Layer 1"),], gravity_constant = 0.3)
        self.physik_engine_2 = arcade.PhysicsEnginePlatformer(self.gegner2, walls=[self.szene4.get_sprite_list("Tile Layer 1"),], gravity_constant = 0.3)
        self.physik_engine_3 = arcade.PhysicsEnginePlatformer(self.gegner3, walls=[self.szene4.get_sprite_list("Tile Layer 1"),], gravity_constant = 0.3)
        self.physik_engine_4 = arcade.PhysicsEnginePlatformer(self.gegner4, walls=[self.szene4.get_sprite_list("Tile Layer 1"),], gravity_constant = 0.3)  
        self.physik_engine_5 = arcade.PhysicsEnginePlatformer(self.gegner5, walls=[self.szene4.get_sprite_list("Tile Layer 1"),], gravity_constant = 0.3)
        self.physik_engine_6 = arcade.PhysicsEnginePlatformer(self.gegner6, walls=[self.szene4.get_sprite_list("Tile Layer 1"),], gravity_constant = 0.3)
        self.physik_engine_7 = arcade.PhysicsEnginePlatformer(self.gegner7, walls=[self.szene4.get_sprite_list("Tile Layer 1"),], gravity_constant = 0.3)       
        self.physik_engine_8 = arcade.PhysicsEnginePlatformer(self.gegner8, walls=[self.szene4.get_sprite_list("Tile Layer 1"),], gravity_constant = 0.3)    

    def on_update(self, delta_time):
        unten_links = self.unten_links()

        
        if self.level_zahl == 4:
            self.szene4.update()
            self.physik_engine_1.update()
            self.physik_engine_2.update()
            self.physik_engine_3.update()
            self.physik_engine_4.update()
            self.physik_engine_5.update()
            self.physik_engine_6.update()
            self.physik_engine_7.update()
            self.physik_engine_8.update()
            print(self.gegner3.position)

            if self.h == 1:
                self.herz3.position = (unten_links[0] + 595, unten_links[1] + 260)

            if self.h == 0:
                self.herz5.position = (unten_links[0] + 530, unten_links[1] + 260)
                self.herz3.position = (unten_links[0] + 595, unten_links[1] + 260)


            pve = arcade.check_for_collision_with_list(self.Spieler1, self.szene4["gegnerliste"])

            for gegner in pve:
                gegner.remove_from_sprite_lists()
                self.herzen = self.herzen - 1

                self.herzen_leer = self.herzen_leer + 1
                    

            self.szene4["bullets"].update()


            for bullet in self.szene4["bullets"]:     

                if bullet.center_x > self.tm4.width*self.tm4.tile_width or bullet.center_x < 0:
                    bullet.remove_from_sprite_lists()

                hit_list = arcade.check_for_collision_with_list(bullet, self.szene4["gegnerliste"])

                if len(hit_list) > 0:
                    bullet.remove_from_sprite_lists()

                for gegner in hit_list:
                    gegner.remove_from_sprite_lists()
            
                col = arcade.check_for_collision_with_list(bullet, self.szene4.get_sprite_list("Tile Layer 1"))

                if len(col) > 0:
                    bullet.remove_from_sprite_lists()





            for kugel in self.szene4["bullets"]:

                if kugel.center_x > self.tm4.width*self.tm4.tile_width or kugel.center_x < 0:
                    kugel.remove_from_sprite_lists()

                if self.shield_time > 0:
                    ...
                else:

                    hit_list = arcade.check_for_collision_with_list(kugel , self.szene4["spielerliste"])

                    if len(hit_list) > 0:
                        kugel.remove_from_sprite_lists()
                        self.herzen = self.herzen - 1

                        self.herzen_leer = self.herzen_leer + 1




            for rocket in self.szene4["bullets"]:

                if rocket.center_x > self.tm4.width*self.tm4.tile_width or rocket.center_x < 0:
                    rocket.remove_from_sprite_lists()

                if self.shield_time > 0:
                    ...
                else:

                    hit_list = arcade.check_for_collision_with_list(rocket , self.szene4["spielerliste"])

                    if len(hit_list) > 0:
                        rocket.remove_from_sprite_lists()
                        self.herzen = self.herzen - 2

                        self.herzen_leer = self.herzen_leer + 2


            if self.dash_verzögerung > 0:

                self.delta_help = self.delta_help + 1
                if self.delta_help > 100:
                    self.dash_verzögerung = self.dash_verzögerung - 1
                    self.delta_help = self.delta_help - self.delta_help

            if self.rocket_verzögerung > 0:

                self.delta_help = self.delta_help + 1
                if self.delta_help > 100:
                    self.rocket_verzögerung = self.rocket_verzögerung - 1
                    self.delta_help = self.delta_help - self.delta_help


            if self.kugel_verzögerung > 0:

                self.delta_help = self.delta_help + 1
                if self.delta_help > 100:
                    self.kugel_verzögerung = self.kugel_verzögerung - 1
                    self.delta_help = self.delta_help - self.delta_help

                

            if self.shield_time > 0:

                self.bubble.center_x = self.Spieler1.center_x
                self.bubble.center_y = self.Spieler1.center_y
                self.delta_help = self.delta_help + 1
                if self.delta_help > 100:
                    self.delta_help = self.delta_help - self.delta_help
                    self.shield_time = self.shield_time - self.shield_time
                    self.shield_verzögerung = self.shield_verzögerung + 1
                    self.bubble.center_x = 10000
                    self.bubble.center_y = 10000
                    

            if self.shield_verzögerung > 0:

                self.delta_help = self.delta_help + 1
                if self.delta_help > 21:
                    self.shield_verzögerung = self.shield_verzögerung - 1
                    self.delta_help = self.delta_help - self.delta_help



            if self.rocket_verzögerung == 0 and self.gegner1 in self.szene4.get_sprite_list("gegnerliste"):

                if self.gegner1.aktion():

                    rocket = self.gegner1.aktion()

                    self.szene4.get_sprite_list("bullets").append(rocket)
                
                self.rocket_verzögerung = self.rocket_verzögerung + 1



            if self.kugel_verzögerung == 0 and self.gegner3 in self.szene4.get_sprite_list("gegnerliste"):
                
                if self.gegner3.aktion():

                    kugel = self.gegner3.aktion()

                    self.szene4.get_sprite_list("bullets").append(kugel)
                
                self.kugel_verzögerung = self.kugel_verzögerung + 1




            if self.kugel_verzögerung == 0 and self.gegner5 in self.szene4.get_sprite_list("gegnerliste"):
                
                if self.gegner5.aktion():

                    kugel = self.gegner5.aktion()

                    self.szene4.get_sprite_list("bullets").append(kugel)
                
                self.kugel_verzögerung = self.kugel_verzögerung + 1



            if self.kugel_verzögerung == 0 and self.gegner8 in self.szene4.get_sprite_list("gegnerliste"):
                
                if self.gegner8.aktion():

                    kugel = self.gegner8.aktion()

                    self.szene4.get_sprite_list("bullets").append(kugel)
                
                self.kugel_verzögerung = self.kugel_verzögerung + 1

            ed = arcade.check_for_collision_with_list(self.Spieler1, self.szene4.get_sprite_list("entrance doors"))

            for spieler in ed:
                

                if random.randrange(10) == 1:

                    self.Spieler1.center_x = self.ex_door1.center_x
                    self.Spieler1.center_y = self.ex_door1.center_y

                if random.randrange(10) == 2:

                    self.Spieler1.center_x = self.ex_door2.center_x
                    self.Spieler1.center_y = self.ex_door2.center_y

                if random.randrange(10) == 3:

                    self.Spieler1.center_x = self.ex_door3.center_x
                    self.Spieler1.center_y = self.ex_door3.center_y

                if random.randrange(10) == 4:

                    self.Spieler1.center_x = self.ex_door4.center_x
                    self.Spieler1.center_y = self.ex_door4.center_y

                if random.randrange(10) == 5:

                    self.Spieler1.center_x = self.ex_door5.center_x
                    self.Spieler1.center_y = self.ex_door5.center_y

                if random.randrange(10) == 6:

                    self.Spieler1.center_x = self.ex_door6.center_x
                    self.Spieler1.center_y = self.ex_door6.center_y

                if random.randrange(10) == 7:

                    self.Spieler1.center_x = self.ex_door7.center_x
                    self.Spieler1.center_y = self.ex_door7.center_y

                if random.randrange(10) == 8:

                    self.Spieler1.center_x = self.ex_door8.center_x
                    self.Spieler1.center_y = self.ex_door8.center_y

                if random.randrange(10) == 9:

                    self.Spieler1.center_x = self.ex_door9.center_x
                    self.Spieler1.center_y = self.ex_door9.center_y
                

                
            self.herz.position = (unten_links[0] + 660, unten_links[1] + 260)



        if self.level_zahl == 3:
            self.szene3.update()
            self.physik_engine_1.update()
            self.physik_engine_2.update()
            self.physik_engine_3.update()
            self.physik_engine_4.update()
            self.physik_engine_5.update()
            self.physik_engine_6.update()

            if self.h == 1:
                self.herz3.position = (unten_links[0] + 595, unten_links[1] + 260)

            if self.h == 0:
                self.herz5.position = (unten_links[0] + 530, unten_links[1] + 260)
                self.herz3.position = (unten_links[0] + 595, unten_links[1] + 260)

            tt = arcade.check_for_collision_with_list(self.Spieler1, self.szene3.get_sprite_list("Door"))
            for Door in tt:
                Door.remove_from_sprite_lists()
                self.door = self.door - 1

                if self.door == 0:
                    self.setup4()

            pve = arcade.check_for_collision_with_list(self.Spieler1, self.szene3["gegnerliste"])

            for gegner in pve:
                gegner.remove_from_sprite_lists()
                self.herzen = self.herzen - 1

                self.herzen_leer = self.herzen_leer + 1
                    

            self.szene3["bullets"].update()

            for kugel in self.szene3["bullets"]:

                if kugel.center_x > self.tm3.width*self.tm3.tile_width or kugel.center_x < 0:
                    kugel.remove_from_sprite_lists()

                if self.shield_time > 0:
                    ...
                else:

                    hit_list = arcade.check_for_collision_with_list(kugel , self.szene3["spielerliste"])

                    if len(hit_list) > 0:
                        kugel.remove_from_sprite_lists()
                        self.herzen = self.herzen - 1

                        self.herzen_leer = self.herzen_leer + 1


            for bullet in self.szene3["bullets"]:     

                if bullet.center_x > self.tm3.width*self.tm3.tile_width or bullet.center_x < 0:
                    bullet.remove_from_sprite_lists()

                hit_list = arcade.check_for_collision_with_list(bullet, self.szene3["gegnerliste"])

                if len(hit_list) > 0:
                    bullet.remove_from_sprite_lists()

                for gegner in hit_list:
                    gegner.remove_from_sprite_lists()
            
                col = arcade.check_for_collision_with_list(bullet, self.szene3.get_sprite_list("Tile Layer 1"))

                if len(col) > 0:
                    bullet.remove_from_sprite_lists()

            if self.dash_verzögerung > 0:

                self.delta_help = self.delta_help + 1
                if self.delta_help > 100:
                    self.dash_verzögerung = self.dash_verzögerung - 1
                    self.delta_help = self.delta_help - self.delta_help


            if self.kugel_verzögerung > 0:

                self.delta_help = self.delta_help + 1
                if self.delta_help > 100:
                    self.kugel_verzögerung = self.kugel_verzögerung - 1
                    self.delta_help = self.delta_help - self.delta_help

            if self.shield_time > 0:

                self.bubble.center_x = self.Spieler1.center_x
                self.bubble.center_y = self.Spieler1.center_y
                self.delta_help = self.delta_help + 1
                if self.delta_help > 100:
                    self.delta_help = self.delta_help - self.delta_help
                    self.shield_time = self.shield_time - self.shield_time
                    self.shield_verzögerung = self.shield_verzögerung + 1
                    self.bubble.center_x = 10000
                    self.bubble.center_y = 10000
                    

            if self.shield_verzögerung > 0:

                self.delta_help = self.delta_help + 1
                if self.delta_help > 21:
                    self.shield_verzögerung = self.shield_verzögerung - 1
                    self.delta_help = self.delta_help - self.delta_help

            if self.kugel_verzögerung == 0 and self.gegner3 in self.szene3.get_sprite_list("gegnerliste"):
                
                if self.gegner3.aktion():

                    kugel = self.gegner3.aktion()

                    self.szene3.get_sprite_list("bullets").append(kugel)
                
                self.kugel_verzögerung = self.kugel_verzögerung + 1


            if self.kugel_verzögerung == 0 and self.gegner4 in self.szene3.get_sprite_list("gegnerliste"):
                
                if self.gegner4.aktion():

                    kugel = self.gegner4.aktion()

                    self.szene3.get_sprite_list("bullets").append(kugel)
                
                self.kugel_verzögerung = self.kugel_verzögerung + 1


            if self.kugel_verzögerung == 0 and self.gegner5 in self.szene3.get_sprite_list("gegnerliste"):
                
                if self.gegner5.aktion():

                    kugel = self.gegner5.aktion()

                    self.szene3.get_sprite_list("bullets").append(kugel)
                
                self.kugel_verzögerung = self.kugel_verzögerung + 1


            if self.kugel_verzögerung == 0 and self.gegner6 in self.szene3.get_sprite_list("gegnerliste"):
                
                if self.gegner6.aktion():

                    kugel = self.gegner6.aktion()

                    self.szene3.get_sprite_list("bullets").append(kugel)
                
                self.kugel_verzögerung = self.kugel_verzögerung + 1


            self.herz.position = (unten_links[0] + 660, unten_links[1] + 260)





        if self.level_zahl == 2:
            self.szene2.update()
            self.physik_engine_2.update()
            self.physik_engine_3.update()
            

            ll = arcade.check_for_collision_with_list(self.Spieler1, self.szene2.get_sprite_list("Rune"))
            for Rune in ll:
                Rune.remove_from_sprite_lists()
                self.runen = self.runen - 1

                if self.runen == 0:
                    self.setup3()


            pve = arcade.check_for_collision_with_list(self.Spieler1, self.szene2["gegnerliste"])

            for gegner in pve:
                gegner.remove_from_sprite_lists()
                self.herzen = self.herzen - 1

                self.herzen_leer = self.herzen_leer + 1


            if self.h == 1:
                self.herz3.position = (unten_links[0] + 595, unten_links[1] + 260)

            if self.h == 0:
                self.herz5.position = (unten_links[0] + 530, unten_links[1] + 260)
                self.herz3.position = (unten_links[0] + 595, unten_links[1] + 260)


            pvb = arcade.check_for_collision_with_list(self.Spieler1, self.szene2["bow"])

            for bow in pvb:
                bow.remove_from_sprite_lists()
                self.b = self.b + 1

            self.szene2["bullets"].update()

            for bullet in self.szene2["bullets"]:     

                if bullet.center_x > self.tm2.width*self.tm2.tile_width or bullet.center_x < 0:
                    bullet.remove_from_sprite_lists()

                hit_list = arcade.check_for_collision_with_list(bullet, self.szene2["gegnerliste"])

                if len(hit_list) > 0:
                    bullet.remove_from_sprite_lists()

                for gegner in hit_list:
                    gegner.remove_from_sprite_lists()

            self.herz.position = (unten_links[0] + 660, unten_links[1] + 260)
            



        if self.level_zahl == 1:

            self.szene.update()

            shl = arcade.check_for_collision_with_list( self.Spieler1, self.szene["schlüssel"])
            
            for self.schlüssel in shl:
                self.schlüssel.remove_from_sprite_lists()
                self.physik_engine.platforms.pop()

            if self.Spieler1.center_x >= 915 and self.schlüssel not in self.szene["schlüssel"]:
                self.setup2()


            hkc = arcade.check_for_collision_with_list( self.Spieler1, self.szene["herzen"])
            
            for herz in hkc:
                herz.remove_from_sprite_lists()
                self.herzen = self.herzen + 1
                self.h = self.h - 1
                
            if self.h == 1:
                self.herz3.position = (unten_links[0] + 595, unten_links[1] + 260)

            if self.h == 0:
                self.herz5.position = (unten_links[0] + 530, unten_links[1] + 260)
                self.herz3.position = (unten_links[0] + 595, unten_links[1] + 260)

            self.herz.position = (unten_links[0] + 660, unten_links[1] + 260)
            
        if self.Spieler1.center_y < 0:
            self.herzen = self.herzen - 3

        self.tx = (unten_links[0])

        self.ty = (unten_links[1])

        self.physik_engine.update()

        self.kamera.move_to(unten_links)

        self.x_alt = self.Spieler1.center_x
            
    def unten_links(self):



        if self.level_zahl == 2:

            if self.Spieler1.center_x - self.kamera.viewport_width/2 < 0:
                            vpx = 0
            else:
                    vpx = self.Spieler1.center_x - self.kamera.viewport_width/2

            if self.Spieler1.center_y - self.kamera.viewport_height/2 < 0:
                    vpy = 0
            else:
                    vpy = self.Spieler1.center_y - self.kamera.viewport_height/2
                    
            if self.Spieler1.center_x + self.kamera.viewport_width/2 > 1920:
                    vpx = 1920 - self.kamera.viewport_width

            if self.Spieler1.center_y + self.kamera.viewport_height/2 > 1280:
                    vpy = 1280 - self.kamera.viewport_height



        if self.level_zahl == 1:

            if self.Spieler1.center_x - self.kamera.viewport_width/2 < 0:
                vpx = 0
            elif self.Spieler1.center_x + self.kamera.viewport_width/2 > 960:
                vpx = 960 - self.kamera.viewport_width
            else:
                vpx = self.Spieler1.center_x - self.kamera.viewport_width/2

            if self.Spieler1.center_y - self.kamera.viewport_height/2 < 0:
                vpy = 0
            elif self.Spieler1.center_y + self.kamera.viewport_height/2 > 640:
                vpy = 640 - self.kamera.viewport_height
            else:
                vpy = self.Spieler1.center_y - self.kamera.viewport_height/2



        if self.level_zahl == 3:

            if self.Spieler1.center_x - self.kamera.viewport_width/2 < 0:
                vpx = 0
            elif self.Spieler1.center_x + self.kamera.viewport_width/2 > 4800:
                vpx = 4800 - self.kamera.viewport_width
            else:
                vpx = self.Spieler1.center_x - self.kamera.viewport_width/2

            if self.Spieler1.center_y - self.kamera.viewport_height/2 < 0:
                vpy = 0
            elif self.Spieler1.center_y + self.kamera.viewport_height/2 > 640:
                vpy = 640 - self.kamera.viewport_height
            else:
                vpy = self.Spieler1.center_y - self.kamera.viewport_height/2



        if self.level_zahl == 4:

            if self.Spieler1.center_x - self.kamera.viewport_width/2 < 0:
                vpx = 0
            elif self.Spieler1.center_x + self.kamera.viewport_width/2 > 4800:
                vpx = 4800 - self.kamera.viewport_width
            else:
                vpx = self.Spieler1.center_x - self.kamera.viewport_width/2

            if self.Spieler1.center_y - self.kamera.viewport_height/2 < 0:
                vpy = 0
            elif self.Spieler1.center_y + self.kamera.viewport_height/2 > 1600:
                vpy = 1600 - self.kamera.viewport_height
            else:
                vpy = self.Spieler1.center_y - self.kamera.viewport_height/2



        return (vpx,vpy)


    def on_key_press(self, symbol: int, modifiers: int):


        if modifiers & arcade.key.MOD_ALT:

            if self.shield_verzögerung == 0:
                self.shield_time = self.shield_time + 1
        
            else:
                ...

        if modifiers & arcade.key.MOD_SHIFT:

            if self.dash_verzögerung == 0:

                if self.facing_direction == 1:
                    self.Spieler1.center_x = self.Spieler1.center_x - 50
                
                else:
                    self.Spieler1.center_x = self.Spieler1.center_x + 50

                self.dash_verzögerung = self.dash_verzögerung + 1


        if symbol == arcade.key.E:
            self.setup()

        if symbol == arcade.key.R:
            self.setup2()

        if symbol == arcade.key.T:
            self.setup3()

        if symbol == arcade.key.Z:
            self.setup4()

        if symbol == arcade.key.N:
            self.herzen = self.herzen + 1
            self.setup()

        if symbol == arcade.key.V and self.b > 0:

            if self.level_zahl == 4:
                if self.arrows > 0:

                    if self.facing_direction == 1:
                        bullet = arcade.Sprite("arrow-Photoroom.png", flipped_horizontally=True)
                        self.szene4["bullets"].append(bullet)
                    
                        start_x = self.Spieler1.center_x - 30
                        start_y = self.Spieler1.center_y
                        bullet.center_x = start_x
                        bullet.center_y = start_y

                        bullet.change_x = -10
                        bullet.change_y = 0

                        self.arrows = self.arrows - 1

                    else:
                    
                        bullet = arcade.Sprite("arrow-Photoroom.png", flipped_horizontally=False)
                        self.szene4["bullets"].append(bullet)

                        start_x = self.Spieler1.center_x + 30
                        start_y = self.Spieler1.center_y
                        bullet.center_x = start_x
                        bullet.center_y = start_y

                        bullet.change_x = 10
                        bullet.change_y = 0

                        self.arrows = self.arrows - 1

                else:
                    ...




            if self.level_zahl == 3:
                if self.arrows > 0:

                    if self.facing_direction == 1:
                        bullet = arcade.Sprite("arrow-Photoroom.png", flipped_horizontally=True)
                        self.szene3["bullets"].append(bullet)
                    
                        start_x = self.Spieler1.center_x - 30
                        start_y = self.Spieler1.center_y
                        bullet.center_x = start_x
                        bullet.center_y = start_y

                        bullet.change_x = -10
                        bullet.change_y = 0

                        self.arrows = self.arrows - 1

                    else:
                    
                        bullet = arcade.Sprite("arrow-Photoroom.png", flipped_horizontally=False)
                        self.szene3["bullets"].append(bullet)

                        start_x = self.Spieler1.center_x + 30
                        start_y = self.Spieler1.center_y
                        bullet.center_x = start_x
                        bullet.center_y = start_y

                        bullet.change_x = 10
                        bullet.change_y = 0

                        self.arrows = self.arrows - 1

                else:
                    ...

            if self.level_zahl == 2:
                    
                if self.arrows > 0:

                    if self.facing_direction == 1:
                        bullet = arcade.Sprite("arrow-Photoroom.png", flipped_horizontally=True)
                        self.szene2["bullets"].append(bullet)
                    
                        start_x = self.Spieler1.center_x - 30
                        start_y = self.Spieler1.center_y
                        bullet.center_x = start_x
                        bullet.center_y = start_y

                        bullet.change_x = -10
                        bullet.change_y = 0

                        self.arrows = self.arrows - 1

                    else:
                    
                        bullet = arcade.Sprite("arrow-Photoroom.png", flipped_horizontally=False)
                        self.szene2["bullets"].append(bullet)

                        start_x = self.Spieler1.center_x + 30
                        start_y = self.Spieler1.center_y
                        bullet.center_x = start_x
                        bullet.center_y = start_y

                        bullet.change_x = 10
                        bullet.change_y = 0

                        self.arrows = self.arrows - 1

                else:
                    ...

        if symbol == arcade.key.D:
            self.Spieler1.change_x = 1
            self.Spieler1.texture = arcade.load_texture("Sprite-0001.png")
            self.facing_direction = 0

        if symbol == arcade.key.A:
            self.Spieler1.change_x = -1
            self.Spieler1.texture = arcade.load_texture("Sprite-0001.png", flipped_horizontally=True)
            self.facing_direction = 1

        if symbol == arcade.key.W:
            if self.physik_engine.is_on_ladder:
                self.Spieler1.change_y = 1

        if symbol == arcade.key.S:
            if self.physik_engine.is_on_ladder:
                self.Spieler1.change_y = -1

        if symbol == arcade.key.SPACE and self.physik_engine.can_jump():
            self.Spieler1.change_y = 5
            
    def on_key_release(self, symbol: int, modifiers: int):

        if symbol == arcade.key.D:
            self.Spieler1.change_x = 0

        if symbol == arcade.key.A:
            self.Spieler1.change_x = 0

        if symbol == arcade.key.SPACE:
            self.Spieler1.change_y = 0

        if symbol == arcade.key.UP or symbol == arcade.key.W:
            if self.physik_engine.is_on_ladder():
                self.Spieler1.change_y = 0
        elif symbol == arcade.key.DOWN or symbol == arcade.key.S:
            if self.physik_engine.is_on_ladder():
                self.Spieler1.change_y = 0
        elif symbol == arcade.key.LEFT or symbol == arcade.key.A:
            self.Spieler1.change_x = 0
        elif symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            self.Spieler1.change_x = 0

    def on_draw(self):
        self.clear()
        
        self.kamera.use()

        if self.level_zahl == 2:
            self.szene2.draw()
            self.szene2["bullets"].draw()

        if self.level_zahl == 1:
            self.szene.draw()

        if self.level_zahl == 3:
            self.szene3.draw()
            self.szene3["bullets"].draw()

        if self.level_zahl == 4:
            self.szene4.draw()
            self.szene4["bullets"].draw()
                           

        if self.herzen_leer == 1 and self.herzen == 1:
            self.herz3.texture = arcade.load_texture("herz_tot.png")

        if self.herzen_leer == 1 and self.herzen == 2:
            self.herz5.texture = arcade.load_texture("herz_tot.png")

        if self.herzen_leer == 2:
            self.herz3.texture = arcade.load_texture("herz_tot.png")
            self.herz5.texture = arcade.load_texture("herz_tot.png")

        if self.herzen < 1:
            arcade.draw_lrwh_rectangle_textured(self.tx, self.ty, 700, 300, arcade.load_texture("lose-screen.webp"))

Spiel(1000, 1000, "Plattformer")
arcade.run()


# TODO auf 10.4.: Rocket Classe neu schreiben (Innovativ sein)

#log: Freitag 11.10. 15:00-15:15.: Ich habe es geshcafft das wenn man dasht es eine verzögerung gibt und man eine bestimmte zeit warten muss bisman ihn wieder benutzen kann.
#     Samstag 19:00-19:15: Bugs mit Zeit Dash gefixt 
#     Sonntag 19:10-19:25: Köcher mit bestimmter anzahl von pfeilen geaddet sowei an der Map von level 3 weiter gearbeitet
#     montag 17:10-17:34: Bugs gefixt und map 3 fertiggestellt.
#     donnerstag 16:05-16:20: Spieler class erstellt und angefangen das game für diese class umzuschreiben.
#       sonntag 12:30-12:45: Spieler Class fertiggestellt und bewegung für diese fertiggestellt.

#Ideen: Für Dash im Hud ein Symbol einbauen das zeigt ob man ihn schon wieder benutzen kann und wenn nicht einem die zeit anzeigt die man noch warten muss.
#       Wie wäre es mit einer Fähigkeit die alle gegner in einem bestimmten umfeld einfriert.
#       Gegner könnenen dich ab einer gewissen Nähe sehen und versuchen dich anzugreifen(Das muss ich umbedingt einbauen um das kampf gameplay spannend zu machen).
#       teleport fähigkeit bei der du Türen werfen kannst durch die du dich teleportieren kannst.
#
#       Fähigkeit einbauen die einen schild um dich herum herbeiruft der dich für 5sekunden vor allen schüßen beschützt der aber eine lange abklingzeit hat. 
#
#       gegner stufen system mit verscheidenen stats.
#
#       4.Level: Eine futuristische brücke die über einen Lavasee führt und auf der man androids bekämpfen muss.
#
#       Melee Angriffe und Kämpfe mit gegnern.


#Merken: Um change_x zu ändern muss ich immer gp benutzen.
#   	pos_min muss immer um 10 von der Blockposition erhört werden.
#       pos_max muss immer um 10 von der Blockposition verringert werden.

# Todos: 1. Mapränder unzugänglich machen /Done
#        2. Gegner in Physik einbauen /Done
#        3. Bug testing /Done
#        4. Pfeile Richtung anpassen / Dash in beide Richtungen möglich machen, dash zeit verkürzen /Done
#        5. Wenn außerhalb von Map = Tot /Done
#        6. Herzen Texturen bei Level-Wechsel anpassen /Done
#        7. Überflüssigen code löschen/zu nutzvollem überarbeiten /Done
#        8. Variablen Namen überarbeiten(für leichtere erkennung) /Done
#        9. Gegner in level 2 fixen /Done
#        10. Neue gegner in Level 3 hinzufügen, die schießen können. /Done
#        11. Neue Fähigkeit hinzufügen. /Done
#        12. Menu hinzufügen. /
#        13. Dash funktioniert nicht (Fixen). /Done
#        14. Neue gegner hinzufügen um level 3 fertigstellen /Done
#        15. Leicht, Mittel und Schwere gegner Kathegorie erstellen. /
#        16. Template für Level Erstellung erstellen. /Done
#        17. Gegner Spieler Erkenneungs Höhen Limit einbauen /
#        18. Rocket Gegner class fixen /


# Templates: 

        # Door templates:
            
            #notes:
                #you have to add the lists for both types in a level first.
                #you have to change the szene and depending on the position on the mape you have to load the texture reversed if needed.
                # you always have to subtract 9 from the y coordinate to get the right position.

            #entrance door:

                #       self.en_door = arcade.Sprite("factorie_door.jpg")
                #       self.en_door.center_x = ... # x center
                #       self.en_door.center_y = ... # y center
                #       self.szene4.get_sprite_list("entrance doors").append( self.en_door)

            #exit door:

                #       self.ex_door = arcade.Sprite("factorie_door.jpg")
                #       self.ex_door.center_x = ... # x center
                #       self.ex_door.center_y = ... # y center
                #       self.szene4.get_sprite_list("exit doors").append( self.ex_door)     


