_base_ = '../default.py'

expname = 'dvgo_hotdog'
basedir = './logs/nerf_synthetic'

data = dict(
    datadir='/share/data/pals/jjahn/data/blender/hotdog',
    dataset_type='blender',
    white_bkgd=True,
)
