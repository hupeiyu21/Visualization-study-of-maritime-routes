# Visualization-study-of-maritime-routes

### Abstract

In this paper, we propose a data visualization method for ship trajectories using the RDP and FDEB bundling algorithms. The RDP algorithm reduces the number of data points in the trajectories while retaining key features. The FDEB bundling algorithm simplifies the visualization by grouping similar trajectories together. An East China Sea shipping case study is reported using the proposed approach. The results show that our method can effectively reduce the complexity of the visualization while retaining key features of the data. The bundled visualization also clearly represents the main shipping routes and allows for a comparison of the frequency of routes. Our approach demonstrates a good balance between reducing data points and retraining key features while adjusting the parameters of the RDP algorithm and considering the trade-off between the data size and the visualization quality. Our approach can also be seen as a fruitful and effective tool for visualizing and analyzing ship trajectory data.

### Provide a way of processing the visualization of maritime routes: aggregation of routes by means of edge bundling to optimize the route layout map.

The first step is to reduce the number of points in the sample.csv file and retain the key points, using the RDP algorithm.

<img width="1260" alt="image" src="https://user-images.githubusercontent.com/102003754/234477120-735be6fa-b695-4ade-81a5-eb90d09d97ab.png">

Convert_to_xml will convert the sample.csv file into an xml file, and when the dataset is a group, you can use concate.py to stitch the different datasets together to generate a whole undirected graph xml file, which also represents a route.

After that, you can use the edge binding algorithm of d3.js to implement edge binding for maritime routes.

<img width="1224" alt="image" src="https://user-images.githubusercontent.com/102003754/234477013-d3a3319e-4e85-4e90-9c6f-10ebd7f422d3.png">
