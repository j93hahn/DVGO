_base_ = '../default.py'

expname = 'dvgo_mic'
basedir = './logs/nerf_synthetic'

data = dict(
    datadir='/share/data/pals/jjahn/data/blender/mic',
    dataset_type='blender',
    white_bkgd=True,
)
