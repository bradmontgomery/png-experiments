import sys
from pprint import pformat
from PIL import Image


def img_data(filename):

    img = Image.open(filename)

    print("\nFile name: {}".format(filename))
    print("Size: {}".format(img.size))
    print("Mode: {}".format(img.mode))
    print("Format: {}".format(img.format))
    print("Image Data: {:,} bytes".format(len(img.tobytes())))
    print("Info\n{}".format(pformat(img.info)))
    print("\n\n")


def duplicate(filename):
    result_filename = "opt-{}".format(filename)

    print("Duplicating {} as {}".format(filename, result_filename))
    img = Image.open(filename)
    img = img.copy()

    # Try setting the compression level:
    # 0 - no compression
    # 9 - max compression
    #img.save(result_filename, compress_level=9)

    # Let PIL figure out how to optimize this thing.
    #
    # > If present, instructs the PNG writer to make the output file as small
    # > as possible. This includes extra processing in order to find optimal
    # > encoder settings.
    img.save(result_filename, optimize=True)

    img_data(result_filename)


if __name__ == "__main__":

    filename = sys.argv[1] if len(sys.argv) == 2 else None
    if filename:
        print("Opening {}".format(filename))
        img_data(filename)
        duplicate(filename)
