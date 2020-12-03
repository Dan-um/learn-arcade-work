"""
Lab 12
"""
import random
import arcade

SPRITE_SCALING = 0.6
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_ENEMY = 0.7
SPRITE_SCALING_LASER = 0.8
SPRITE_SCALING_MISSILE = 0.9
ENEMY_COUNT = 20

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Lab 12"

LASER_SPEED = 10
MISSILE_SPEED = 7
MISSILE_COUNT = 5
MOVEMENT_SPEED = 5
MOVEMENT_SPEED_ENEMY = 1
GRAVITY = 1
JUMP_HEIGHT = 20

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
LEFT_VIEWPORT_MARGIN = 250
RIGHT_VIEWPORT_MARGIN = 250
BOTTOM_VIEWPORT_MARGIN = 50
TOP_VIEWPORT_MARGIN = 100
# Constants for keeping track of if the player sprite is facing right or left
RIGHT_FACING = 0
LEFT_FACING = 1


# def load_texture_pair(filename):
#     """
#     Load a texture pair, with the second being a mirror image.
#     """
#     return [
#         arcade.load_texture(filename),
#         arcade.load_texture(filename, flipped_horizontally=True)]


class Bullet(arcade.Sprite):
    def __init__(self, image, scale, health):
        super().__init__(image, scale)
        self.health = health


class Enemy(arcade.Sprite):
    # def __init__(self, image, scale, walls):
    #     super().__init__(image, scale)
    #     self.walls = walls

    def reset_pos(self):
        self.center_y = 500
        self.center_x = random.randrange(SCREEN_WIDTH)
        self.change_x = 1

    def update(self):
        # if self.center_x >= 500:
        #     self.reset_pos()
        # self.change_x = MOVEMENT_SPEED_ENEMY
        self.physics_engine.update()
        self.center_x += self.change_x
        hit_list = arcade.check_for_collision_with_list(self, self.physics_engine.platforms)
        if len(hit_list) > 0:
            self.change_x *= -1
        self.center_x -= self.change_x



# class PlayerCharacter(arcade.Sprite):
#     """ Player Sprite"""
#     def __init__(self):
#
#         # Set up parent class
#         super().__init__()
#
#         # Default to face-right
#         self.character_face_direction = RIGHT_FACING


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
        self.wall_list = None
        self.dont_touch_list = None
        self.weapon_list = None
        # self.pillar_list = None
        # Variable to hold the player sprite
        self.player_sprite = None

        # Set up physics engine
        self.physics_engine = None

        # Number holdings
        self.score = 0
        self.new_missiles = 0
        self.current_missiles = 5
        self.lives = 3

        self.view_bottom = 0
        self.view_left = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # Load sounds. Sounds from kenney.nl
        self.gun_sound = arcade.load_sound("laserSmall_001.ogg")
        self.hit_sound = arcade.load_sound("explosionCrunch_000.ogg")
        self.missile_sound = arcade.load_sound("impactMetal_000.ogg")

        arcade.set_background_color(arcade.color.BLUE)

    def setup(self):

        """ Set up the game and initialize the variables. """
        self.score = 0
        self.lives = 3
        self.view_bottom = 0
        self.view_left = 0

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.laser_list = arcade.SpriteList()
        self.missile_list = arcade.SpriteList()
        self.pickups_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.weapon_list = arcade.SpriteList()

        # Set up the player
        # Sprite image from kenney.nl
        self.player_sprite = arcade.Sprite("character_femalePerson_run0.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 800
        self.player_sprite.center_y = 500
        self.player_list.append(self.player_sprite)

        # Create the weapon
        # Gun sprite from kenney.nl
        gun = arcade.Sprite("raygunBig.png", .75)
        gun.center_x = self.player_sprite.center_x + self.view_left + 50
        gun.center_y = self.player_sprite.center_y + self.view_bottom
        self.weapon_list.append(gun)

        # Load map from Tiled
        # Name of map file to load
        map_name = "map.tmx"
        # Name of the layer in the file that has our platforms/walls
        platform_layer_name = 'Platforms'
        dont_touch_layer_name = 'Do Not Touch'
        # pillar_layer_name = 'Walls'

        # Read in the tiled map
        my_map = arcade.tilemap.read_tmx(map_name)

        # -- Platforms
        self.wall_list = arcade.tilemap.process_layer(map_object=my_map,
                                                      layer_name=platform_layer_name,
                                                      scaling=1,
                                                      use_spatial_hash=True)

        self.dont_touch_list = arcade.tilemap.process_layer(my_map,
                                                            dont_touch_layer_name,
                                                            scaling=1,
                                                            use_spatial_hash=True)
        # self.pillar_list = arcade.tilemap.process_layer(my_map, pillar_layer_name, scaling=1, use_spatial_hash=True)

        # Create the enemies
        for i in range(ENEMY_COUNT):

            # Create enemies
            # Enemy sprite from Kenny.nl
            enemy = Enemy("character_robot_attack0.png", SPRITE_SCALING_ENEMY)

            # Position the enemies
            success = False
            while not success:
                enemy.center_x = random.randrange(100, 1800)
                distance = abs(enemy.center_x - self.player_sprite.center_x)
                if distance > 200:
                    success = True
            enemy.center_y = 700
            enemy.change_x = MOVEMENT_SPEED_ENEMY
            enemy.physics_engine = arcade.PhysicsEnginePlatformer(enemy, self.wall_list, GRAVITY)
            # Add the enemies to the lists
            self.enemy_list.append(enemy)

        # Set the background color
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        # Set up physics engine
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list, GRAVITY)
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list, GRAVITY)

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
        self.wall_list.draw()
        self.dont_touch_list.draw()
        self.weapon_list.draw()
        # self.pillar_list.draw()

        # Render the text
        arcade.draw_text(f"Score: {self.score}", 10 + self.view_left, 20 + self.view_bottom, arcade.color.WHITE, 14)
        arcade.draw_text(f"Missiles: {self.current_missiles}", 100 + self.view_left, 20 + self.view_bottom, arcade.color.WHITE, 14)
        if self.lives > 0:
            arcade.draw_text(f"Health: {self.lives}", 200 + self.view_left, 20 + self.view_bottom, arcade.color.WHITE, 14)
        if self.lives <= 0:
            arcade.draw_text("GAME OVER!", 400 + self.view_left, 300 + self.view_bottom, arcade.color.WHITE,
                             14)
        if self.score >= 20:
            arcade.draw_text("YOU WIN!", 400 + self.view_left, 300 + self.view_bottom, arcade.color.WHITE,
                             14)

    # Set up user control
    def on_key_press(self, key, modifiers):
        # Only allows bullets and movement if the user has not died or the objective is not completed
        if self.score < 20 and self.lives <= 3 and self.lives != 0:
            # Shoot missiles only if we have missiles
            if key == arcade.key.A and len(self.missile_list) < MISSILE_COUNT + self.new_missiles:
                if self.current_missiles <= 0:
                    return
                self.current_missiles -= 1
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

            if key == arcade.key.UP:
                if self.physics_engine.can_jump():
                    self.player_sprite.change_y = JUMP_HEIGHT
            elif key == arcade.key.LEFT:
                self.player_sprite.change_x = -MOVEMENT_SPEED
            elif key == arcade.key.RIGHT:
                self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def update(self, delta_time):
        """ Movement and game logic """
        # Only move sprites if the objective is not completed or the user has not lost
        if self.lives > 0 or self.score >= 20:
            self.physics_engine.update()

            # Call update on sprites
            self.laser_list.update()
            self.missile_list.update()
            self.enemy_list.update()
            self.weapon_list[0].center_x = self.player_sprite.center_x + 50
            self.weapon_list[0].center_y = self.player_sprite.center_y

        # See if the player has touched an enemy, if they have, remove health
        health_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.enemy_list)
        for enemy in health_hit_list:
            enemy.remove_from_sprite_lists()
            self.lives -= 1

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

        if arcade.check_for_collision_with_list(self.player_sprite,
                                                self.dont_touch_list):
            self.lives -= 3

        for enemy in self.enemy_list:
            hit_list = arcade.check_for_collision_with_list(enemy, self.dont_touch_list)
            if len(hit_list) > 0:
                enemy.remove_from_sprite_lists()
                self.score += 1

        # --- Manage Scrolling --- #

        # Track if we need to change the viewport

        changed = False

        # Scroll left
        left_boundary = self.view_left + LEFT_VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - TOP_VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + BOTTOM_VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        if changed:
            # Only scroll to integers. Otherwise we end up with pixels that
            # don't line up on the screen
            self.view_bottom = int(self.view_bottom)
            self.view_left = int(self.view_left)

            # Do the scrolling
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
