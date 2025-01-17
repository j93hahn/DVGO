_base_ = './nerf_unbounded_default.py'

expname = 'dvgo_kitchen_unbounded'

data = dict(
    datadir='/share/data/pals/jjahn/data/real_360/kitchen',
    factor=2, # 1558x1039
    movie_render_kwargs=dict(
        shift_y=-0.0,
        scale_r=0.9,
        pitch_deg=-40,
    ),
)
