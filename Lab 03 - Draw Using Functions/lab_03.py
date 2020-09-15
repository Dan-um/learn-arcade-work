import arcade


# Set up window
def open_window():
    arcade.open_window(800, 600, "Drawing with functions")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)
    arcade.start_render()


# Draw the sun
def draw_sun():
    arcade.draw_circle_filled(600, 175, 150, arcade.color.GOLD)
    arcade.draw_line(600, 175, 500, 385, arcade.color.GOLD)
    arcade.draw_line(600, 175, 550, 385, arcade.color.GOLD)
    arcade.draw_line(600, 175, 600, 385, arcade.color.GOLD)
    arcade.draw_line(600, 175, 650, 385, arcade.color.GOLD)
    arcade.draw_line(600, 175, 700, 385, arcade.color.GOLD)


# Draw the water
def draw_water():
    arcade.draw_lrtb_rectangle_filled(0, 800, 300, 0, arcade.color.SEA_BLUE)


# Draw the structure of the lighthouse
def draw_lighthouse():
    arcade.draw_ellipse_filled(400, 300, 200, 600, arcade.color.LIGHT_GRAY)


# Draw the island
def draw_island():
    arcade.draw_lrtb_rectangle_filled(200, 600, 100, 0, arcade.color.SLATE_GRAY)


# Draw the door
def draw_door():
    # Frame
    arcade.draw_lrtb_rectangle_filled(376, 424, 153, 100, arcade.color.DARK_BROWN)
    # Inside door
    arcade.draw_lrtb_rectangle_filled(380, 420, 150, 100, arcade.color.BLACK)


# Draw a lower, fatter window
def draw_window(x, y):
    # Frame
    arcade.draw_lrtb_rectangle_filled(350 + x, 450 + x, 304 + y, 245 + y, arcade.color.DARK_BROWN)
    # Inside window
    arcade.draw_lrtb_rectangle_filled(355 + x, 445 + x, 299 + y, 249 + y, arcade.color.BLACK)


# Draw higher, skinnier window
def draw_higher_window(x, y):
    # Frame
    arcade.draw_lrtb_rectangle_filled(385 + x, 413 + x, 402 + y, 345 + y, arcade.color.DARK_BROWN)
    # Inside window
    arcade.draw_lrtb_rectangle_filled(389 + x, 409 + x, 399 + y, 349 + y, arcade.color.BLACK)


# Draw the light for the lighthouse
def draw_light_in_lighthouse():
    arcade.draw_ellipse_filled(400, 500, 148, 75, arcade.color.GOLD)


# Draw a cloud
def draw_cloud(x, y):
    # Cloud
    arcade.draw_ellipse_filled(200 + x, 450 + y, 200, 75, arcade.color.WHITE)


# Main function
def main():
    open_window()
    draw_sun()
    draw_water()
    draw_lighthouse()
    draw_island()
    draw_door()
    draw_window(0, 0)
    draw_window(0, 70)
    draw_higher_window(0, 40)
    draw_higher_window(0, -175)
    draw_light_in_lighthouse()
    draw_cloud(-30, 0)
    draw_cloud(400, 50)

    # Finish drawing
    arcade.finish_render()

    # Keep window open until closed
    arcade.run()


# Call the main function
main()