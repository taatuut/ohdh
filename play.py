import osmnx as ox
import folium
import contextily as cx
import matplotlib.pyplot as plt

def plot_graph_folium(G):
    # Convert edges to a GeoDataFrame
    gdf_nodes, gdf_edges = ox.graph_to_gdfs(G)
    network_type = G.graph.get('network_type')
    # Get a reasonable center for the map
    center = [gdf_nodes.geometry.y.mean(), gdf_nodes.geometry.x.mean()]
    m = folium.Map(location=center, zoom_start=13)
    # Add edges as GeoJSON
    folium.GeoJson(
        gdf_edges[["geometry"]].to_json(),
        name="streets"
    ).add_to(m)
    # Optional: add layer control
    folium.LayerControl().add_to(m)
    # Save to HTML and open in browser manually
    filename = f"graph_map_{network_type}.html"
    m.save(filename)
    print(f"Saved map to {filename}")

PLACE_NAME = 'Nijmegen, Netherlands'

NETWORK_TYPE = 'drive'
G = ox.graph_from_place(PLACE_NAME, network_type=NETWORK_TYPE)
G.graph['network_type'] = NETWORK_TYPE
ox.plot_graph(G)
# Decprecated in OSMnx > 2.x
#ox.plot_graph_folium(G)
plot_graph_folium(G)

NETWORK_TYPE = 'bike'
G = ox.graph_from_place(PLACE_NAME, network_type=NETWORK_TYPE)
G.graph['network_type'] = NETWORK_TYPE
ox.plot_graph(G)
plot_graph_folium(G)

gdf_nodes,gdf_edges = ox.graph_to_gdfs(G)
print(gdf_nodes.head())
print(gdf_edges.head())
