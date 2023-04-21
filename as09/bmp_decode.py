#!/usr/bin/env python3

""" BMP image decoding. """

__author__ = 'Anthony Torres for CS 20P, altorresmoran@jeff.cis.cabrillo.edu'


class BmpImage:
  """A BMP Image Decoder!"""

  def __init__(self, path: str):
    """
    Constructs a BmpImage from a file path.

    >>> demo = BmpImage('/srv/datasets/cabrillo-logo.bmp')
    >>> demo.dimensions()
    (300, 151)
    """
    self.path = path
    with open(path, 'rb') as bmp_file:
      bmp_header = bmp_file.read(14)
      pixel_data_offset = int.from_bytes(bmp_header[10:14], 'little')
      dib_header = bmp_file.read(40)

      width = int.from_bytes(dib_header[4:8], 'little', signed=True)
      height = int.from_bytes(dib_header[8:12], 'little', signed=True)
      self.width = width
      self.height = height

      bmp_file.seek(pixel_data_offset)
      self.pixel_data = bmp_file.read()

  def __getitem__(self,
                  coord: int | tuple[int, int]) -> tuple[int, int, int] | tuple[int, int, int, int]:
    """
    Returns a 3-tuple or 4-tuple of integers in [0, 255] representing the RGB or RGBA values,
    respectively, of a pixel in this image. The pixel coordinate is either specified as a
    tuple[int, int] specifying the x and y pixel coordinates, or as a single integer specifying
    an index into the array of pixels, where index 0 is the upper-left corner of the image, and
    index len() - 1 is the lower-right corner.

    >>> demo = BmpImage('/srv/datasets/cabrillo-logo.bmp')
    >>> demo[0]
    (255, 255, 255)
    >>> demo[(224, 24)]
    (120, 188, 233)
    >>> demo[(82, 121)]
    (57, 97, 226)
    >>> demo[len(demo) - 1]
    (255, 255, 255)
    >>> demo = BmpImage('/srv/datasets/pelota.bmp')
    >>> demo[(9, 4)]
    (0, 0, 0, 0)
    >>> demo[(10, 4)]
    (15, 16, 17, 82)
    >>> demo[(11, 4)]
    (33, 34, 35, 252)
    """
    if isinstance(coord, int):
      x = coord % self.width
      y = coord // self.width
    else:
      x, y = coord

    pixel_index = (self.height - y - 1) * self.width * 3 + x * 3
    r = self.pixel_data[pixel_index]
    g = self.pixel_data[pixel_index + 1]
    b = self.pixel_data[pixel_index + 2]

    return r, g, b

  def __len__(self):
    """
    Returns the total number of pixels in the image.

    >>> len(BmpImage('/srv/datasets/cabrillo-logo.bmp'))
    45300
    """
    return self.width * self.height

  def __iter__(self):
    """
    Yields all pixels in the same format as __getitem__(), from the upper-left corner (0, 0)
    to the lower-right corner (width - 1, height - 1).

    >>> list(BmpImage('/srv/datasets/simple.bmp'))
    [(0, 0, 255), (0, 255, 0), (255, 0, 0), (255, 255, 255)]
    >>> len(list(BmpImage('/srv/datasets/cabrillo-logo.bmp')))
    45300
    >>> len(set(BmpImage('/srv/datasets/cabrillo-logo.bmp')))
    520
    """
    for index in range(len(self)):
      yield self[index]

  def dimensions(self):
    """
    Returns a tuple consisting of the width and height of this image, in pixels.

    >>> BmpImage('/srv/datasets/simple.bmp').dimensions()
    (2, 2)
    >>> BmpImage('/srv/datasets/cabrillo-logo.bmp').dimensions()
    (300, 151)
    """
    return self.width, self.height
