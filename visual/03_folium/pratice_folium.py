import folium

my_loc = folium.Map(location=[36.3659806300997, 127.436127730684],zoom_start=6)
folium.Marker([36.3659806300997, 127.436127730684],popup=folium.Popup('송촌장로교회',max_width=100)).add_to(my_loc)

# zoom_start min == 6 max == 18 ?
my_loc.save('pratice.html')