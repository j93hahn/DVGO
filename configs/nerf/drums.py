_base_ = '../default.py'

expname = 'dvgo_drums'
basedir = './logs/nerf_synthetic'

data = dict(
    datadir='/share/data/pals/jjahn/data/blender/drums',
    dataset_type='blender',
    white_bkgd=True,
)
