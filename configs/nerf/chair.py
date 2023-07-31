_base_ = '../default.py'

expname = 'dvgo_chair'
basedir = './logs/nerf_synthetic'

data = dict(
    datadir='/share/data/pals/jjahn/data/blender/chair',
    dataset_type='blender',
    white_bkgd=True,
)
