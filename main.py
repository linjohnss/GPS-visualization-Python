from gps_class import GPSVis
while(1):
    vis = GPSVis(data_path='FusionSolution-0817_0.005_V_R03_NEW.txt',
                map_path='map2.png',  # Path to map downloaded from the OSM.
                points=(25.04569, 121.55102, 25.03734, 121.56518)) # Two coordinates of the map (upper left, lower right)

    vis.create_image(color=(0, 0, 255), width=3)  # Set the color and the width of the GNSS tracks.

    vis.plot_map()
