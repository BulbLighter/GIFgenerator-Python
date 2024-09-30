import imageio.v3 as iio

filenames = ['one.jpg', 'two.jpg','three.jpg','four.jpg','five.jpg']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('mrrobot.gif', images, duration = 250, loop = 0)