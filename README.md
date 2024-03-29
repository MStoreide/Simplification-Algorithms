# Simplification-Algorithms
Collection of Simplification Algorithms for testing.
Purpose is to see how the different algorithms interact with primitive geometric shapes like spheres, angles, and different curvatures. Objective is to see if these can be charted in some way, in order to select the most appropriate one for different 3D objects.

Algorithms are picked from Open Source environments, and selected based on their common use as well as differences in approaches.  

Currently the implementation has a brute-force-esque approach with individual files for each object. No loops or iterations which would speed things up. Future plans include implementing this for ease of use. 

Python Version
> Python 3.10

Required Modules
> open3d, pymeshlab, bpy, matplotlib, pandas, numpy, polyscope

## Naming Conventions
Files are named with abbreviations to limit the length. Full names are listed below.
Names are listed as : (ObjectName)(Manifold/NonManifold)(SimplificationAlgorithm)(Simplification Step)

Example: NonUniformManifoldVertexClustering16.obj = NUMVC16.obj

### Object Names:

U = Uniform

NU = NonUniform

S = Sphere

A = Angled

R = Rugged

M = Manifold
Manifold geometry in this context means that the mesh is watertight. Meshes with this characteristic is denoted M after the object name.

NM = NonManifold 
For some algorithms it was not necessary to have manifold geometry, meaning that some geometries are surface meshes rather than watertight meshes. So the repository contains both manifold and nonmanifold versions of some geometry. They are denoted with NM after the object name.
UPDATE: This is not used in the final version. 

B = Baseline
This is the HiPoly mesh used in comparisons. 


### Algorithm Names:
Specficiation of which simplification approach has been used is at the end of each object-name. They are denoted as follows:

D = Decimation

VC = Vertex Clustering

QEM = Quadric Error Metrics

CFM = Coplanar Facets Merging

EC = Edge Collapse

## Algorithms

**Decimation**
*Done in Open3D*

**Vertex Clustering**
*Done in Open3D*

**Quadric Error Metrics**
*Done in Meshlab*

**Coplanar Facets Merging**

**Edge Collapse**
*Done in Blender*

## Citations and Licenses

This projects makes use of a lot of great open-source software, so please make sure to check these out. 


**Open3D License**
> // ----------------------------------------------------------------------------
// -                        Open3D: www.open3d.org                            -
// ----------------------------------------------------------------------------
// The MIT License (MIT)
//
// Copyright (c) 2018-2021 www.open3d.org
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
// FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
// IN THE SOFTWARE.
// ----------------------------------------------------------------------------

**Open3D Citation**
>@article{Zhou2018,
    author    = {Qian-Yi Zhou and Jaesik Park and Vladlen Koltun},
    title     = {{Open3D}: {A} Modern Library for {3D} Data Processing},
    journal   = {arXiv:1801.09847},
    year      = {2018},
}

**Meshlab License**
> /****************************************************************************
  MeshLab                                                           o o     *
  A versatile mesh processing toolbox                             o     o   *
                                                                 _   O  _   *
  Copyright(C) 2005 - 2021                                         \/)\/    *
  Visual Computing Lab                                            /\/|      *
  ISTI - Italian National Research Council                           |      *
                                                                     \      *
  All rights reserved.																											 *
  This program is free software; you can redistribute it and/or modify      *
  it under the terms of the GNU General Public License as published by      *
  the Free Software Foundation; either version 2 of the License, or         *
  (at your option) any later version.                                       *
                                                                            *
  This program is distributed in the hope that it will be useful,           *
  but WITHOUT ANY WARRANTY; without even the implied warranty of            *
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             *
  GNU General Public License (http://www.gnu.org/licenses/gpl.txt)          *
  for more details.                                                         *
                                                                            *
 ****************************************************************************/
 
 **Meshlab Citation**
 >@software{meshlab,
  author       = {Paolo Cignoni, Alessandro Muntoni, Guido Ranzuglia, Marco Callieri},
  title        = {{MeshLab}},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.5114037}
}

@inproceedings {LocalChapterEvents:ItalChap:ItalianChapConf2008:129-136,
  booktitle = {Eurographics Italian Chapter Conference},
  editor    = {Vittorio Scarano and Rosario De Chiara and Ugo Erra},
  title     = {{MeshLab: an Open-Source Mesh Processing Tool}},
  author    = {Cignoni, Paolo and Callieri, Marco and Corsini, Massimiliano and Dellepiane, Matteo and Ganovelli, Fabio and Ranzuglia, Guido},
  year      = {2008},
  publisher = {The Eurographics Association},
  ISBN      = {978-3-905673-68-5},
  DOI       = {10.2312/LocalChapterEvents/ItalChap/ItalianChapConf2008/129-136}
}

**Blender License**
> The source code we develop at blender.org is default being licensed as GNU GPL Version 2 or later. 
  Some modules we make are using more permissive licenses, though, for example, the Blender Cycles rendering engine is available as Apache 2.0.
  Blender also uses many modules or libraries from other projects. For example, Python uses the Python License; Bullet uses the Zlib License; Libmv uses the MIT License; and OSL, a BSD License. 
  All the components that together make Blender are compatible under the newer GNU GPL Version 3 or later. That is also the license to use for any distribution of Blender binaries. 

**Polyscope Citation**
 >@misc{polyscope,
  title = {Polyscope},
  author = {Nicholas Sharp and others},
  note = {www.polyscope.run},
  year = {2019}
}
  # Contact

  Markus Sebastian Bakken Storeide (markus.s.b.storeide@ntnu.no)