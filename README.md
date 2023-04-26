# Visualization-study-of-maritime-routes

### Provide a way of processing the visualization of maritime routes: aggregation of routes by means of edge bundling to optimize the route layout map.

The first step is to reduce the number of points in the sample.csv file and retain the key points, using the RDP algorithm.

[rdp.pdf](https://github.com/hupeiyu21/Visualization-study-of-maritime-routes/files/11329237/rdp.pdf)

Convert_to_xml will convert the sample.csv file into an xml file, and when the dataset is a group, you can use concate.py to stitch the different datasets together to generate a whole undirected graph xml file, which also represents a route.

After that, you can use the edge binding algorithm of d3.js to implement edge binding for maritime routes.

<img width="1224" alt="image" src="https://user-images.githubusercontent.com/102003754/234477013-d3a3319e-4e85-4e90-9c6f-10ebd7f422d3.png">
