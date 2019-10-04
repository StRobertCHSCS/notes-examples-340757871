
import arcade as ar
import os

line1 = " Me: The user will love the simple and easy to use UI"
line2 = "USER: "
height = 600
width = 600

ar.open_window(height, width, "Meme Generator")
ar.set_background_color(ar.color.WHITE)
ar.start_render()

texture = ar.load_texture("images/Capture.PNG")
ar.draw_texture_rectangle(texture.width//2+50, texture.height //
                          2, texture.width,  texture.height, texture, 0)

ar.draw_text(line1, 0, height-20, ar.color.BLACK, 20)
ar.draw_text(line2, 0, height-70, ar.color.BLACK, 20)

ar.finish_render()
ar.run()
print(texture.width)
# TODO LIST
''' get it prints width of image, must center the image 
then move it to the working folder,
then check if it meets the requiremetn and format of the pep8
check how format of how it needs to be submitted
then do the emoji
'''
