from src.homework8.task4.Shape3D import Shape3D

def find_dominant_shapes(*shapes: Shape3D) -> list[Shape3D]:
    total_volume = sum(shape.get_volume() for shape in shapes)

    dominant_shapes = []
    for shape in shapes:
        volume = shape.get_volume()
        if volume >= total_volume - volume:
            dominant_shapes.append(shape)
    
    return dominant_shapes