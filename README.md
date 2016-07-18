Bloated PNG files, oh my!
=========================

Exploring PNG file size and image data with (a very small amount) of python.

# Background

A coworker pointed out this article: [Hidden data in your image files](https://medium.com/@duhroach/hidden-data-in-your-image-files-a68ad61081b8#.30yusyna1)

It got me thinking, can we see and/or fix this with some simple python? So,
here's the experiment:

1. Create a simple image of a black circle with a transparent background
2. Use various methods to export it in Photoshop.
3. Do the same in pixelmator.
4. See what we get, and then explore the image files with python (using PIL).


## The sample PNG file details

- Size: 512 x 512, 72 pixels/in
- Black circle w/ a transparent background.

Resulting filesizes:

- Pixelmator `img-pixelmator.png`: ~16KB
- Photoshop (quick export as png) `img-photoshopcc2015.png`: ~10KB
- Photoshop (save as, png "compressed") `img-photoshopcc2015-saveas.png` ~ 26K
- Photoshop (legacy save for web, png-24) `img-photoshopcc2015-saveforweb-png-24.png` ~ 10K
- Photoshop (legacy save for web, png-8) `img-photoshopcc2015-saveforweb-png-8.png` ~ 4.8K

Running any of these through [tinypng](https://tinypng.com/) gives a file size of ~ 4K


## Exploring

Check out one of the image's in a HEX editor:

- Open an image in vim
- Run `:% ! xxd`
- explore!

Open the image with PIL, and find the length of the image data (in bytes).

    >>> from PIL import Image
    >>>
    >>> img = Image.open(filename)
    >>> len(img.tobytes())

See what sort of extra data we have in the image (an image has an `info` dict
that may contain arbitrary data).

    >>> img.info

Make a copy of the original image data, and save an optimized result. Note: PIL's
[PNG encoder](https://pillow.readthedocs.io/en/3.3.x/handbook/image-file-formats.html#png)
has a handfull of options for saving images.

    >>> new_image = img.copy()
    >>> new_image = image.save("newfile.png", optimize=True)

You can also explicitly set a ZLIB compression level (0 = none, 9 = maximum)

    >>> new_image = img.copy()
    >>> new_image = image.save("newfile.png", compression_level=9)

See the `main.py` file in this repo for (a litte bit) more.


# Also really cool:

- [Reducing PNG file size](https://medium.com/@duhroach/reducing-png-file-size-8473480d0476#.1679mqm7r)
- [How PNG works](https://medium.com/@duhroach/how-png-works-f1174e3cc7b7#.m2slfpldp)


