import imageio.v3 as iio

pictures = ['one.jpg', 'two.jpg','three.jpg','four.jpg','five.jpg']
images = [ ]

for picture in pictures:
  images.append(iio.imread(picture))

iio.imwrite('mrrobot.gif', images, duration = 250, loop = 0)