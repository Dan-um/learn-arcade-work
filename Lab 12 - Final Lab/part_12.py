import random
import arcade


SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_ENEMY = 0.7
SPRITE_SCALING_LASER = 0.8
SPRITE_SCALING_MISSILE = 0.9
ENEMY_COUNT = 10

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Lab 12"

LASER_SPEED = 10
MISSILE_SPEED = 7
MISSILE_COUNT = 5
MOVEMENT_SPEED = 5



class Bullet(arcade.Sprite):
    def __init__(self, image, scale, health):
        super().__init__(image, scale)
        self.health = health



class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Variables that will hold sprite lists
        self.player_list = None
        self.enemy_list = None
        self.laser_list = None
        self.missile_list = None
        self.pickups_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0
        self.new_missiles = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # Load sounds. Sounds from kenney.nl
        self.gun_sound = arcade.load_sound("laserSmall_001.ogg")
        self.hit_sound = arcade.load_sound("explosionCrunch_000.ogg")
        self.missile_sound = arcade.load_sound("impactMetal_000.ogg")

        arcade.set_background_color(arcade.color.BLUE)

    def setup(self):

        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.laser_list = arcade.SpriteList()
        self.missile_list = arcade.SpriteList()
        self.pickups_list = arcade.SpriteList()

        # Set up the player
        self.score = 0

        # Sprite image from kenney.nl
        self.player_sprite = arcade.Sprite("character_femalePerson_run0.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.player_list.append(self.player_sprite)

        # Create the enemies
        for i in range(ENEMY_COUNT):

            # Create enemies
            # Enemy sprite from Kenny.nl
            enemy = arcade.Sprite("character_robot_attack0.png", SPRITE_SCALING_ENEMY)

            # Position the enemies
            enemy.center_x = random.randrange(SCREEN_WIDTH)
            enemy.center_y = random.randrange(120, SCREEN_HEIGHT)

            # Add the enemies to the lists
            self.enemy_list.append(enemy)

        # Set the background color
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.enemy_list.draw()
        self.laser_list.draw()
        self.player_list.draw()
        self.missile_list.draw()

        # Render the text
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)
        arcade.draw_text(f"Missiles: {MISSILE_COUNT - len(self.missile_list)}", 100, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """
        Called whenever the mouse moves.
        """
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_key_press(self, key, modifiers):
        if key == arcade.key.A and len(self.missile_list) < MISSILE_COUNT + self.new_missiles:

            # Play missile sound
            arcade.play_sound(self.missile_sound)
            # Create missile
            # Missile sprite from kenny.nl

            missile = Bullet("spaceMissiles_014.png", SPRITE_SCALING_MISSILE, 2)

            missile.angle = 270

            missile.change_x = MISSILE_SPEED

            missile.center_x = self.player_sprite.center_x + 5
            missile.bottom = self.player_sprite.top - 25

            self.missile_list.append(missile)

        if key == arcade.key.S:
            # Gunshot sound
            arcade.play_sound(self.gun_sound)
            # Create a laser
            # Laser sprite from Kenny.nl
            laser = arcade.Sprite("laserBlue03.png", SPRITE_SCALING_LASER)

            # The image points to the right, and we want it to point up. So
            # rotate it.
            laser.angle = 90

            # Give the bullet a speed
            laser.change_x = LASER_SPEED

            # Position the bullet
            laser.center_x = self.player_sprite.center_x
            laser.bottom = self.player_sprite.top - 25

            # Add the bullet to the appropriate lists
            self.laser_list.append(laser)

    #def on_key_release(self, key, modifiers):


    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on bullet sprites
        self.laser_list.update()
        self.missile_list.update()

        # Loop through each bullet
        for laser in self.laser_list:

            # Check this bullet to see if it hit a coin
            hit_list = arcade.check_for_collision_with_list(laser, self.enemy_list)

            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                laser.remove_from_sprite_lists()

            # For every enemy we hit, add to the score and remove the enemy
            for enemy in hit_list:
                enemy.remove_from_sprite_lists()
                self.score += 1
                # if random.randrange(1, 4) == 2:



                # Hit Sound
                arcade.play_sound(self.hit_sound)

            # If the bullet flies off-screen, remove it.
            if laser.bottom > SCREEN_HEIGHT:
                laser.remove_from_sprite_lists()

        for missile in self.missile_list:

            hit_list = arcade.check_for_collision_with_list(missile, self.enemy_list)

            for enemy in hit_list:
                enemy.remove_from_sprite_lists()
                missile.health -= 1
                if missile.health == 0:
                    missile.remove_from_sprite_lists()
                self.score += 1

                arcade.play_sound(self.hit_sound)
            if missile.bottom > SCREEN_HEIGHT:
                missile.remove_from_sprite_lists()




def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()