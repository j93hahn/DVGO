_base_ = '../default.py'

expname = 'dvgo_ficus'
basedir = './logs/nerf_synthetic'

data = dict(
    datadir='/share/data/pals/jjahn/data/blender/ficus',
    dataset_type='blender',
    white_bkgd=True,
)
