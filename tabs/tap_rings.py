def __tab_rings(config):

    from bokeh.plotting import figure, show
    from bokeh.models import TabPanel
    from bokeh.layouts import column, row
    
    import obspy as obs
    
    def __makeplot(st, component="Z"):

        tr = st.select(channel=f"*{component}")[0]
        title = f"{tr.stats.network}.{tr.stats.station}.{tr.stats.location}.{tr.stats.channel}"

        p = figure(width=1000, height=150, 
                   title=title,
                   tools='save',
                   y_axis_label='Y Label',
                   y_axis_type='linear',
                  )

        p.line(tr.times(), tr.data , line_width=2)

#         p.legend.location = 'top_left'
        
        return p
    try:
        st = obs.read(config['workdir']+"/data/ROMY_BJZ_2023-01-31.mseed")
        st.trim(config['tbeg'], config['tend'])
    except:
        print("Failed to load data!")
        
    p1 = __makeplot(st, component="Z")
    p2 = __makeplot(st, component="Z")
    p3 = __makeplot(st, component="Z")
    p4 = __makeplot(st, component="Z")
    p5 = __makeplot(st, component="Z")

    
    r1 = column(p1, p2, p3, p4, p5)
    # r1 = column(children=[p1, p2], sizing_mode='stretch_both')

    tab = TabPanel(child=r1, title = 'Rings')
    
    return tab

