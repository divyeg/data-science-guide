import PIL
import PIL.Image
import PIL.ImageOps
import PIL.ImageEnhance
import PIL.ImageFilter
import requests
import io
import loguru as logger


class ImageHandler(object):
    def __init__(self):
        pass

    def read_image_from_file(self, path):
        """
        This function is used to read image from file stored in local repository
        Example path: 'Ex_Files_Programming_Efficiently/Exercise Files/Ch03/cached/20130903_002924_512_0171.jpg'

        Returns:
        -----------------------
        img: PIL.Image

        """

        img = PIL.Image.open(path)
        return img

    def read_image_from_url(self, url):
        """
        This function is used to read image from file stored in http url
        Example url: 'https://sdo.gsfc.nasa.gov/assets/img/browse/2013/09/03/20130903_082900_512_0171.jpg'

        Returns:
        -----------------------
        img: PIL.Image

        """

        req = requests.get(url)
        img = PIL.Image.open(io.BytesIO(req.content))
        return img

    def print_image_properties(self, img):
        """
        This function is used to print basic properties of an image

        """

        logger.debug(f"Size of the image = {img.size}")
        logger.debug(f"Mode of the image = {img.mode}")

    def resize_image(self, img, dim1, dim2):
        """
        This function is used to resize the image

        """

        resized_image = img.resize((dim1, dim2))
        return resized_image

    def convert_image_to_grayscale(self, img):
        """
        This function is used to convert image to grayscale

        """
        gray_img = img.convert("L").filter(PIL.ImageFilter.SHARPEN)
        return gray_img

    def colorize_image(self, img, r, g, b):
        """
        This function is used to change color of the image

        """

        img_new = PIL.ImageOps.colorize(img.convert("L"), (0, 0, 0), (r, g, b))
        return img_new

    def blend_images(self, img1, img2):
        """
        This function is used to blend two images

        """

        blend_img = PIL.Image.blend(img1, img2, 0.5)
        return blend_img

    def change_image_brightness(self, img):
        """
        This function is used to change the brightness of the image

        """

        img = PIL.ImageEnhance.Brightness(img).enhance(2.5)
        return img
