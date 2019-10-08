import arcade as ar
#import os

ar.open_window(600,600,"My Emoji")
ar.set_background_color(ar.color.WHITE)
ar.start_render()

ar.draw_circle_filled(300, 300,90,ar.color.YELLOW)
ar.finish_render()
ar.run()
#ar.draw_circle_filled(300,3)
