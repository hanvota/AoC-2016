import numpy

pos = numpy.matrix((10, 15, 17, 1, 0, 1, 0))
number_of_pos = numpy.matrix((13, 17, 19, 7, 5, 3, 11))
discs = numpy.matrix((1, 2, 3, 4, 5, 6, 7))
done = False
time = 0

while not done:
    output = ((pos + discs + time) % number_of_pos).sum()
    if output == 0:
        done = True
        print(time)
    time += 1
