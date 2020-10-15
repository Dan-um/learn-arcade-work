import arcade
import random

# Constant variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPRITE_SCALING_PLAYER = 0.5
GOOD_SPRITE_SCALE = 0.2
BAD_SPRITE_SCALE = 0.2
GOOD_SPRITE_COUNT = 50
BAD_SPRITE_COUNT = 40


# Create window class
class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 08")
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.DEEP_SPACE_SPARKLE)
        # Load Sounds
        # Kenny.nl sci-fi-sounds.zip
        self.good_sound = arcade.load_sound("good_sound.ogg")
        self.bad_sound = arcade.load_sound("bad_sound.ogg")
        # Sprite variable lists
        self.good_sprite_list = None
        self.player_sprite_list = None
        self.bad_sprite_list = None
        self.player_sprite = None
        # Score
        self.score = 0

    def setup(self):

        # Sprite Lists
        self.good_sprite_list = arcade.SpriteList()
        self.player_sprite_list = arcade.SpriteList()
        self.bad_sprite_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Kenny.nl kenny_tooncharacters1.zip
        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING_PLAYER)

        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50

        self.player_sprite_list.append(self.player_sprite)

        # Create Coins
        # Kenny.nl puzzle-pack-ii.zip
        for i in range(GOOD_SPRITE_COUNT):
            good_sprite = Coin("good_sprite.png", GOOD_SPRITE_SCALE)

            good_sprite.center_x = random.randrange(SCREEN_WIDTH)
            good_sprite.center_y = random.randrange(SCREEN_HEIGHT)

            self.good_sprite_list.append(good_sprite)

        # Create Ships
        # Kenny.nl kenney_spaceshooter.zip
        for i in range(BAD_SPRITE_COUNT):
            bad_sprite = Ship("bad_sprite.png", BAD_SPRITE_SCALE)

            bad_sprite.center_x = random.randrange(SCREEN_WIDTH)
            bad_sprite.center_y = random.randrange(SCREEN_HEIGHT)

            self.bad_sprite_list.append(bad_sprite)

    def on_draw(self):

        # Draws all sprites
        arcade.start_render()
        self.good_sprite_list.draw()
        self.bad_sprite_list.draw()
        self.player_sprite_list.draw()

        # Draws score on screen
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
        if len(self.good_sprite_list) == 0:
            arcade.draw_text("Game Over", 400, 300, arcade.color.WHITE, 14)

    # Enables user control with a mouse
    def on_mouse_motion(self, x, y, dx, dy):
        if len(self.good_sprite_list) > 0:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def update(self, delta_time):
        if len(self.good_sprite_list) > 0:
            self.good_sprite_list.update()
            self.bad_sprite_list.update()

        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.good_sprite_list)
        for good_sprite in hit_list:
            good_sprite.remove_from_sprite_lists()
            arcade.play_sound(self.good_sound, volume=0.5)
            self.score += 1

        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bad_sprite_list)
        for bad_sprite in hit_list:
            bad_sprite.remove_from_sprite_lists()
            arcade.play_sound(self.bad_sound, volume=0.5)
            self.score -= 1


# Create good sprite object
class Coin(arcade.Sprite):
    def reset_pos(self):
        self.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        self.center_y -= 1
        if self.top < 0:
            self.reset_pos()


# Create bad sprite object
class Ship(arcade.Sprite):
    def reset_pos(self):
        self.center_y = random.randrange(-20, -5)
        self.center_x = random.randrange(200, 1500)

    def update(self):
        self.center_y += 1
        self.center_x -= 1
        if self.center_y > 620:
            self.reset_pos()


# Set up main function
def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()