import arcade, random

class Spiel(arcade.Window):
    def __init__(self, breite, höhe, titel):
        super().__init__(breite, höhe, titel)

        arcade.set_background_color(arcade.color.AMAZON)

        self.setup()

    def setup(self):
        self.gegenstand_liste = arcade.SpriteList()
        self.total_time = 0.0
        self.punkte = 0
        self.bomb_list = arcade.SpriteList(0)

        schlüssel = arcade.Sprite("Schlüssel.png")
        schlüssel.center_x = random.randrange(800)
        schlüssel.center_y = random.randrange(600)
        self.gegenstand_liste.append(schlüssel)

        geld = arcade.Sprite("geld.png")
        geld.center_x = random.randrange(800)
        geld.center_y = random.randrange(600)
        self.gegenstand_liste.append(geld)

        handy = arcade.Sprite("Handy.png")
        handy.center_x = random.randrange(800)
        handy.center_y = random.randrange(600)
        self.gegenstand_liste.append(handy)

        brille = arcade.Sprite("Brille.png")
        brille.center_x = random.randrange(800)
        brille.center_y = random.randrange(600)
        self.gegenstand_liste.append(brille)

        kuchen = arcade.Sprite("kuchen.png")
        kuchen.center_x = random.randrange(800)
        kuchen.center_y = random.randrange(600)
        self.gegenstand_liste.append(kuchen)

        for i in range(0):
            Zeitung = arcade.Sprite("Zeitung.png")
            Zeitung.center_x = random.randrange(800)
            Zeitung.center_y = random.randrange(600)
            self.gegenstand_liste.append(Zeitung)

        for i in range(30):
            bombe = arcade.Sprite("bombe.png")
            bombe.center_x = random.randrange(800)
            bombe.center_y = random.randrange(600)
            self.bomb_list.append(bombe)
            self.bomben = bombe

    def on_mouse_press(self, x, y, button, modifiers):
        pseudosprite = arcade.Sprite()
        pseudosprite.center_x = x
        pseudosprite.center_y = y
        pseudosprite.set_hit_box([(1,1), (-1,1), (-1,-1), (1,-1)])

        gegenstand_hitliste = arcade.check_for_collision_with_list(pseudosprite, self.gegenstand_liste)

        for gegenstand in gegenstand_hitliste:
            gegenstand.kill()
            self.punkte = self.punkte + 1
        
        gegenstand_bomb_list = arcade.check_for_collision_with_list(pseudosprite, self.bomb_list)

        for gegenstand in gegenstand_bomb_list:
            gegenstand.kill()
            self.punkte = self.punkte - 1
    

    def on_draw(self):
        self.clear()

        hintergrund = arcade.load_texture("Easy.jpg")
        arcade.draw_lrwh_rectangle_textured(0, 0, 800, 600, hintergrund)

        self.gegenstand_liste.draw()

        self.bomb_list.draw()

        arcade.draw_text(self.punkte, 770, 580, arcade.color.BLACK )

        arcade.draw_text(self.timer_text, 15, 580, arcade.color.BLACK)
        
        if self.punkte < 0:
            lose_screen = arcade.load_texture("lose-screen.webp")
            arcade.draw_lrwh_rectangle_textured(0, 0, 800, 600, lose_screen)
        
        if len(self.gegenstand_liste) == 0:
            endscreen = arcade.load_texture("end_screen.png")
            arcade.draw_lrwh_rectangle_textured(0, 0, 800, 600, endscreen)


    def on_update(self, delta_time):
        self.total_time += delta_time   
        seconds = round(self.total_time)
        self.timer_text = f"{seconds:1}"
        
      
            
       

        

        




spiel = Spiel(800, 600, "Suchspiel")
arcade.run()