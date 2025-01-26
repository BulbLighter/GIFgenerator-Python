import imageio.v3 as iio
#A very simple script that creates a gif from a list of images.
pictures = ['one.jpg', 'two.jpg','three.jpg','four.jpg','five.jpg']
images = [ ]

for picture in pictures:
  images.append(iio.imread(picture))

iio.imwrite('mrrobot.gif', images, duration = 250, loop = 0)