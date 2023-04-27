import folium
a = 37.5752205086784
b = 127.010502773568

my_loc = folium.Map(location=[37.5752205086784,127.010502773568],zoom_start=18)
folium.Marker([37.5752205086784,127.010402773568],popup=folium.Popup('이쁜아이 공원면적:가능?',max_width=100),icon=folium.Icon(color="green",icon='cloud'),).add_to(my_loc)
# folium.Marker(
#     location=[37.5752205086784, 127.010502773568],
#     popup="Timberline Lodge",
#     icon=folium.Icon(color="green"),
# ).add_to(my_loc)

# zoom_start min == 6 max == 18 ?
my_loc.save('pratice.html')
print(type(my_loc))