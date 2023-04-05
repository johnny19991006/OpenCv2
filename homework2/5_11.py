import numpy as np

def calc_histo(image, channels, bsize, ranges):
     shape = bsize if len(channels) > 1 else (bsize[0], 1)
     hist = np.zeros(shape, dtype=np.float32)

     gap = np.divide(ranges[1::2], bsize)

     for row in image:
          for val in row:
               idx = np.divide(val[channels], gap).astype('uint')
               hist[tuple(idx)] += 1

     return hist
