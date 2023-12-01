import laspy as lp
import numpy as np

if __name__ == '__main__':
    file = r"C:\Users\Lenovo\Desktop\Suffering_is_our_prayer\worse\N-34-63-C-c-1-4-4.las"
    las_pcd = lp.file.File(file, header=None, mode="rw")
    X = las_pcd.x
    Y = las_pcd.y
    Z = las_pcd.z
    # Store x,y,z coordinates into the NumPy array
    las_points = np.vstack((las_pcd.x, las_pcd.y, las_pcd.z)).transpose()
    # print(las_points)

    # Get and print elements in header
    headerformat = las_pcd.header.header_format
    '''
    for spec in headerformat:
        print(spec.name)
    

    x_max = las_pcd.header.max
    print(x_max)

    las_pcd.header.max = [1.0, 1.0, 1.0]
    x_max = las_pcd.header.max
    print(x_max)

    offset = las_pcd.header.offset
    print(offset)
    
    # Get access to the point values
    pointformat = las_pcd.point_format
    for spec in pointformat:
        print(spec.name)
    '''
    # RGB values normalization
    r = las_pcd.red / max(las_pcd.red)
    g = las_pcd.green / max(las_pcd.green)
    b = las_pcd.blue / max(las_pcd.blue)