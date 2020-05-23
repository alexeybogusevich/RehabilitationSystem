#  !/usr/bin/env python
#
#  Created by Dmytro Kotsur on 9/19/19, 11:03 PM.
#  Copyright (c) 2019 Dmytro Kotsur. All rights reserved.

import trimesh
import numpy as np


def load3d_obj(filename):
    mesh = trimesh.load(filename)
    mesh.fix_normals()
    points = mesh.vertices.astype(np.float32)
    triangles = mesh.faces.astype(np.uint32)
    normals = mesh.vertex_normals.astype(np.float32)
    return points, triangles, normals


