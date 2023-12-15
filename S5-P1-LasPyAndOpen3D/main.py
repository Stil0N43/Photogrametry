import laspy as lp
import numpy as np

#Save LAS file with header copy
def save_points_after_processing(file, las, new_las):
    las_pcd = lp.file.File(file, header=las.header, mode = "w")
    las_pcd.points = new_las #i.e. ground_points
    las_pcd.close()

#Save LAS file with header generation
def save_points_with_header_generation(file, x,y,z):
    print('Header generation')
    header = lp.header.Header()
    las_pcd = lp.file.File(file, header=header, mode = "w")
    print('Compute max, min values')
    min_x = np.min(x)
    min_y = np.min(y)
    min_z = np.min(z)
    max_x = np.max(x)
    max_y = np.max(y)
    max_z = np.max(z)
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    mean_z = np.mean(z)
    las_pcd.header.offset = [mean_x, mean_y, mean_z]
    las_pcd.header.max = [max_x, max_y, max_z]
    las_pcd.header.min = [min_x, min_y, min_z]
    las_pcd.header.scale = [0.001,0.001,0.01]
    las_pcd.X = x
    las_pcd.Y = y
    las_pcd.Z = z
    las_pcd.close()

#Save LAS file with header copy
def save_points_to_ascii_file(file, las):
    X = las.x
    Y = las.y
    Z = las.z
    pcd = open(file,'w')
    pcd.write("%i\n" % len(X))
    for i in range(0, len(X)):
        pcd.write("%f %f %f\n" % (X[i], Y[i], Z[i]))
    pcd.close()

#Export points from classes
def point_extraction_based_on_the_class(las, classification):
    if classification == 'buildings':
        print('Buildings extraction')
        buildings_only = np.where(las.raw_classification == 6)
        buildings_points = las.points[buildings_only]
        return buildings_points
    elif classification == 'vegetation':
        print('Vegetation extraction')
        vegetation_low = np.where(las.raw_classification == 3)
        vegetation_medium = np.where(las.raw_classification == 4)
        vegetation_high = np.where(las.raw_classification == 5)
        vegetation = np.hstack((vegetation_low, vegetation_medium, vegetation_high),dtype="int64")
        vegetation = las.points(vegetation)
        return vegetation
    else:
        print('Ground extraction')
        ground_only = np.where(las.raw_classification == 2)
        ground_points = las.points[ground_only]
        return ground_points

if __name__ == '__main__':
    file = r"database\N-34-63-C-c-1-4-4.las"
    las_pcd = lp.file.File(file, header=None, mode="rw")
    las_points = np.vstack((las_pcd.x, las_pcd.y, las_pcd.z)).transpose()
    buld = point_extraction_based_on_the_class(las_pcd, "buildings")
    veg = point_extraction_based_on_the_class(las_pcd, "vegetation")
    # RGB values normalization
    # print(len(las_pcd.intensity))
    # r = las_pcd.red / max(las_pcd.red)
    # g = las_pcd.green / max(las_pcd.green)
    # b = las_pcd.blue / max(las_pcd.blue)