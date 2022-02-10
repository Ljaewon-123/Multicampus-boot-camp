import folium


my_loc = folium.Map(location=[37.50400583893831, 127.049690169316],zoom_start=18)
folium.Marker([37.50400583893831, 127.049690169316],popup=folium.Popup('멀티캠퍼스 선릉',max_width=100)).add_to(my_loc)

my_loc.save('visual02.html')
