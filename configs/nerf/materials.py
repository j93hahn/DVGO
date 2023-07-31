_base_ = '../default.py'

expname = 'dvgo_materials'
basedir = './logs/nerf_synthetic'

data = dict(
    datadir='/share/data/pals/jjahn/data/blender/materials',
    dataset_type='blender',
    white_bkgd=True,
)
