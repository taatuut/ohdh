import osmnx as ox
import folium
import contextily as cx
import matplotlib.pyplot as plt

PLACE_NAME = 'Nijmegen, Netherlands'
NETWORK_TYPE = 'drive'

G = ox.graph_from_place(PLACE_NAME, network_type=NETWORK_TYPE)
ox.plot_graph(G)

ox.plot_graph_folium(G)

NETWORK_TYPE = 'bike'

G = ox.graph_from_place(PLACE_NAME, network_type=NETWORK_TYPE)

area,edges = ox.graph_to_gdfs(G)
area.head()

edges.head()