from __future__ import division, print_function

import click
from skimage.external import tifffile
import pickle

@click.command()
@click.argument('fn_exp')
@click.argument('fn_img')
@click.option('')
def analysis(fn_exp, fn_img):
    """

    :param fn_exp:
    :param fn_img:
    :return:
    """
    click.echo('Input names: %s, %s' % (fn_exp, fn_img))
    exp = pickle.load(open(fn_exp))
    #img = tifffile.imread(fn_img)


if __name__ == '__main__':
    analysis()