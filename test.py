# import altair as alt
# from vega_datasets import data
# source = alt.topo_feature(data.world_110m.url, 'countries')
# base = alt.Chart(source).mark_geoshape(
# fill='#666666',
# stroke='white'
# ).properties(
# width=300,
# height=180
# )
# projections = ['equirectangular', 'mercator', 'orthographic', 'gnomonic']
# charts = [base.project(proj).properties(title=proj)
# for proj in projections]
# alt.concat(*charts, columns=2)

#matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

# 在底层参数的基础上进行三角剖分
from matplotlib.tri import Triangulation
tri = Triangulation(np.ravel(w), np.ravel(theta))

ax = plt.axes(projection='3d')
ax.plot_trisurf(x, y, z, triangles=tri.triangles,
                cmap='viridis', linewidths=0.2);

ax.set_xlim(-1, 1); ax.set_ylim(-1, 1); ax.set_zlim(-1, 1);