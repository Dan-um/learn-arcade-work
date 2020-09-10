import arcade

# Set window dimensions
arcade.open_window(800, 600, "Drawing Example")

# Set background color
arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

arcade.start_render()

# Draw a sun on the horizon
arcade.draw_circle_filled(600, 175, 150, arcade.color.GOLD)
arcade.draw_line(600, 175, 500, 385, arcade.color.GOLD)
arcade.draw_line(600, 175, 550, 385, arcade.color.GOLD)
arcade.draw_line(600, 175, 600, 385, arcade.color.GOLD)
arcade.draw_line(600, 175, 650, 385, arcade.color.GOLD)
arcade.draw_line(600, 175, 700, 385, arcade.color.GOLD)

# Draw water to show contrast with sky
arcade.draw_lrtb_rectangle_filled(0, 800, 300, 0, arcade.color.SEA_BLUE)

# Draw lighthouse base
arcade.draw_ellipse_filled(400, 300, 200, 600, arcade.color.LIGHT_GRAY)

# Draw the island
arcade.draw_lrtb_rectangle_filled(200, 600, 100, 0, arcade.color.SLATE_GRAY)

# Draw a door to the lighthouse
arcade.draw_lrtb_rectangle_filled(376, 424, 153, 100, arcade.color.DARK_BROWN)
arcade.draw_lrtb_rectangle_filled(380, 420, 150, 100, arcade.color.BLACK)

# Draw a window
arcade.draw_lrtb_rectangle_filled(385, 413, 302, 248, arcade.color.DARK_BROWN)
arcade.draw_lrtb_rectangle_filled(389, 409, 299, 249, arcade.color.BLACK)

# Draw a higher window
arcade.draw_lrtb_rectangle_filled(385, 413, 402, 348, arcade.color.DARK_BROWN)
arcade.draw_lrtb_rectangle_filled(389, 409, 399, 349, arcade.color.BLACK)

# Draw the light of the lighthouse
arcade.draw_ellipse_filled(400, 500, 148, 75, arcade.color.GOLD)

# Draw the finishing touch with a bird(low detail like an abstract painting)
arcade.draw_ellipse_filled(200, 450, 50, 3, arcade.color.WHITE)

# Finish drawing
arcade.finish_render()

# Keep window open until closed
arcade.run()