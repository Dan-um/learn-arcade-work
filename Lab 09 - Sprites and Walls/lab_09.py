import random
import arcade


SPRITE_SCALING = 0.5
SPRITE_SCALING_PLAYER = 0.4
SPRITE_SCALING_COIN = 0.2

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Lab 09"

VIEWPORT_MARGIN = 40

MOVEMENT_SPEED = 5

COIN_COUNT = 75


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Sprite lists
        self.player_list = None

        # Set up the player
        self.player_sprite = None
        self.coin_list = None
        self.wall_list = None
        self.physics_engine = None

        # Score
        self.score = 0

        # Collect coin sound effect
        self.collect_coin = arcade.load_sound("coin_collect.ogg")

        # Used in scrolling
        self.view_bottom = 0
        self.view_left = 0

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        self.player_sprite = arcade.Sprite("character_malePerson_idle.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 270
        self.player_list.append(self.player_sprite)

        # Set up walls
        # Walls from Kenney.nl
        # Create border

        for x in range(-100, 1200, 64):
            border = arcade.Sprite("brickGrey.png", SPRITE_SCALING)
            border.center_x = x
            border.center_y = 0
            self.wall_list.append(border)
        for x in range(-100, 1200, 64):
            border = arcade.Sprite("brickGrey.png", SPRITE_SCALING)
            border.center_x = x
            border.center_y = 800
            self.wall_list.append(border)
        for y in range(0, 800, 64):
            border = arcade.Sprite("brickGrey.png", SPRITE_SCALING)
            border.center_x = 0
            border.center_y = y
            self.wall_list.append(border)
        for y in range(0, 800, 64):
            border = arcade.Sprite("brickGrey.png", SPRITE_SCALING)
            border.center_x = 1200
            border.center_y = y
            self.wall_list.append(border)

        # Create individual Cacti to block path
        cactus = arcade.Sprite("cactus.png", SPRITE_SCALING)
        cactus.center_x = 200
        cactus.center_y = 264
        self.wall_list.append(cactus)

        cactus = arcade.Sprite("cactus.png", SPRITE_SCALING)
        cactus.center_x = 400
        cactus.center_y = 415
        self.wall_list.append(cactus)

        cactus = arcade.Sprite("cactus.png", SPRITE_SCALING)
        cactus.center_x = 500
        cactus.center_y = 128
        self.wall_list.append(cactus)

        cactus = arcade.Sprite("cactus.png", SPRITE_SCALING)
        cactus.center_x = 600
        cactus.center_y = 610
        self.wall_list.append(cactus)

        cactus = arcade.Sprite("cactus.png", SPRITE_SCALING)
        cactus.center_x = 1000
        cactus.center_y = 700
        self.wall_list.append(cactus)

        wall = arcade.Sprite("boxCrate_single.png", SPRITE_SCALING)
        wall.center_x = 500
        wall.center_y = 64
        self.wall_list.append(wall)

        # Create boxes for main walls in game

        for x in range(200, 600, 64):
            if random.randrange(5) > 0:
                wall = arcade.Sprite("boxCrate_single.png", SPRITE_SCALING)
                wall.center_x = x
                wall.center_y = 200
                self.wall_list.append(wall)

        for x in range(300, 500, 64):
            if random.randrange(4) > 0:
                wall = arcade.Sprite("boxCrate_single.png", SPRITE_SCALING)
                wall.center_x = x
                wall.center_y = 350
                self.wall_list.append(wall)

        for x in range(200, 800, 64):
            if random.randrange(4) > 0:
                wall = arcade.Sprite("boxCrate_single.png", SPRITE_SCALING)
                wall.center_x = x
                wall.center_y = 550
                self.wall_list.append(wall)

        for y in range(64, 400, 64):
            if random.randrange(5) > 0:
                wall = arcade.Sprite("boxCrate_single.png", SPRITE_SCALING)
                wall.center_x = 700
                wall.center_y = y
                self.wall_list.append(wall)

        for y in range(64, 700, 64):
            if random.randrange(5) > 0:
                wall = arcade.Sprite("boxCrate_single.png", SPRITE_SCALING)
                wall.center_x = 1000
                wall.center_y = y
                self.wall_list.append(wall)

        # Set up coins
        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = arcade.Sprite("coinSilver.png", SPRITE_SCALING_COIN)

            # Boolean variable if we successfully placed the coin
            coin_placed_successfully = False

            # Keep trying until success
            while not coin_placed_successfully:
                # Position the coin
                coin.center_x = random.randrange(SCREEN_WIDTH)
                coin.center_y = random.randrange(SCREEN_HEIGHT)

                # See if the coin is hitting a wall
                wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)

                # See if the coin is hitting another coin
                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    # It is!
                    coin_placed_successfully = True

            # Add the coin to the lists
            self.coin_list.append(coin)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.ASH_GREY)

        # Set the viewport boundaries
        self.view_left = 0
        self.view_bottom = 0

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()

        output = f"Coins Collected: {self.score}"
        arcade.draw_text(output, 40 + self.view_left, 40 + self.view_left, arcade.color.WHITE, 14)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
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
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in hit_list:
            coin.remove_from_sprite_lists()
            arcade.play_sound(self.collect_coin, volume=0.1)
            self.score += 1

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.physics_engine.update()

        # --- Manage Scrolling ---

        changed = False

        # Scroll left
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        # Make sure our boundaries are integer values. While the view port does
        # support floating point numbers, for this application we want every pixel
        # in the view port to map directly onto a pixel on the screen. We don't want
        # any rounding errors.
        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        # If we changed the boundary values, update the view port to match
        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()