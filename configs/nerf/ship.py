_base_ = '../default.py'

expname = 'dvgo_ship'
basedir = './logs/nerf_synthetic'

data = dict(
    datadir='/share/data/pals/jjahn/data/blender/ship',
    dataset_type='blender',
    white_bkgd=True,
)
