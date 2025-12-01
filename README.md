# ohdh
Old habits die hard, my own osmnx playground

# introduction
Recently [robvandort](https://github.com/robvandort) pointed me to this interesting LinkedIn post https://www.linkedin.com/posts/alindnbrg_geoai-urbandatascience-networkanalysis-activity-7400605781282279424-gCzn

[OSMnx](https://github.com/gboeing/osmnx) or: easy peasy OSM to full fleged walking, biking, driving routing networks in minutes!

It brought back geospatial memories of my time at [Speer IT](https://speerit.nl/) when I did a similar exercise, at that time with MapBasic for MapInfo Professional.

So need to try OSMnx myself too.

> **Boeing, G. (2025).** *Modeling and Analyzing Urban Networks and Amenities with OSMnx.*  
> Geographical Analysis, 57(4), 567–577.  
> https://doi.org/10.1111/gean.70009

# purpose
Check how accurate the data is for Nijmegen, the city where I live.

# inspiration

https://towardsdatascience.com/visualizing-road-networks-c4664182e6c1/

https://towardsdatascience.com/geospatial-data-analysis-with-osmnx-8a300d77b592-2/

# prep

```sh
source .env && mkdir -p ~/.venv && python3 -m venv ~/.venv && source ~/.venv/bin/activate
```

To unload the `venv` run `deactivate`.

In the terminal install Python modules (optional: update `pip`) and source the environment variables.

NOTE: pip <=25.2 had issue GHSA-4xh5-x5gv-qwph.

```sh
python3 -m pip install --upgrade pip
python3 -m pip install osmnx folium contextily
```

`python3 -m pip show osmnx`

# steps

`python3 play.py`

`open graph_map.html`
