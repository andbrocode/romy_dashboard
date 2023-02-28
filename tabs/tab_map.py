def __tab_map(config):
    
    import folium

    from obspy import UTCDateTime
    from numpy import array
    from bokeh.models import TabPanel
    from bokeh.plotting import figure, show
    from bokeh.plotting import figure, output_file, show
    from bokeh.tile_providers import CARTODBPOSITRON, get_provider
    
    
#     base_map = folium.Map(location=[config['BSPF_lat'], config['BSPF_lon']], zoom_start=14)
#     base_map
     

    def __makeplot():
        
        p = figure(width=300, height=300)

        tile_provider = get_provider(CARTODBPOSITRON)

        # range bounds supplied in web mercator coordinates
        p = figure(x_range=(-2000000, 6000000), y_range=(-1000000, 7000000),
                   x_axis_type="mercator", y_axis_type="mercator")
        p.add_tile(tile_provider)
        
        return p

#     def update(attr, old, new):
#         new_src = make_dataset(airline_list)
#         src.data.update(new_src.data)
#         controls = ...   
        
    p = __makeplot()
    
#     show(p)
    
    tab = TabPanel(child=p, title = 'Seismicity Map')

    return tab