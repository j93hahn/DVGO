_base_ = '../default.py'

expname = 'dvgo_lego'
basedir = './logs/nerf_synthetic'

data = dict(
    datadir='/share/data/pals/jjahn/data/blender/lego',
    dataset_type='blender',
    white_bkgd=True,
)
