from homework8.task4.Cube import Cube
from homework8.task4.Cylinder import Cylinder
from homework8.task4.Ellipsoid import Ellipsoid
from homework8.task4.Parallelepiped import Parallelepiped
from homework8.task4.Sphere import Sphere

from homework8.task4.analyzer import find_dominant_shapes


def test_empty_shapes_list():
    assert find_dominant_shapes() == []

def test_one_huge_shape_among_others():
    huge_sphere = Sphere(10)
    small_cube = Cube(2)
    small_cylinder = Cylinder(2, 1)
    small_box = Parallelepiped(2, 3, 2)
    small_ellipsoid = Ellipsoid(1, 1, 1)

    result = find_dominant_shapes(huge_sphere, small_cube, small_cylinder, small_box, small_ellipsoid)
    assert result == [huge_sphere]

def test_no_dominant_shapes_diverse():
    cube = Cube(4)
    box = Parallelepiped(4, 4, 4)
    sphere = Sphere(2.5)
    
    result = find_dominant_shapes(cube, box, sphere)
    assert result == []

def test_two_equal_dominant_shapes_sphere_and_ellipsoid():
    sphere = Sphere(3)
    
    ellipsoid = Ellipsoid(3, 3, 3)
    
    result = find_dominant_shapes(sphere, ellipsoid)
    assert result == [sphere, ellipsoid]