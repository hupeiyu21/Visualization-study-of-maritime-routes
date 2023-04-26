import os

dir = "../BohaiData/result/xml" # Replace with desired directory
filename = "bohai_{}.xml".format("test")

file_path = os.path.join(dir, filename)

with open(file_path,"w") as f:
    f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
    f.write("<graphml xmlns=\"http://graphml.graphdrawing.org/xmlns\"")
    f.write("         xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"")
    f.write("         xsi:schemaLocation=\"http://graphml.graphdrawing.org/xmlns")
    f.write("  http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd\">")
    f.write('\r\n')
    f.write("    <key id=\"x\" for=\"node\" attr.name=\"x\" attr.type=\"double\"/>")
    f.write("    <key id=\"tooltip\" for=\"node\" attr.name=\"tooltip\" attr.type=\"string\"/>")
    f.write("    <key id=\"y\" for=\"node\" attr.name=\"y\" attr.type=\"double\"/>")
    f.write('\r\n')
    f.write("    <graph edgedefault=\"undirected\">")
    f.write('\r\n')
    f.write('\r\n')

    for count in range(0,120):
        dir = "../BohaiData/result"
        file_node = "file_node{}.txt".format(count)
        file_path_node = os.path.join(dir, file_node)

        with open(file_path_node, "r") as node:
            content = node.read()
        f.write(content)

    for count in range(0,76):
        dir = "../BohaiData/result"
        file_edge = "file_edge{}.txt".format(count)
        file_path_edge = os.path.join(dir, file_edge)
        with open(file_path_edge,"r") as edge:
            content = edge.read()
        f.write(content)

    f.write('\r\n')
    f.write('\r\n')

    f.write("    </graph>")
    f.write('\r\n')
    f.write("</graphml>")