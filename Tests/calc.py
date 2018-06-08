fx = 1.0
fy = 1.0
focal_length = 1.0
lower_res = 1024.0
native_res = 1111.0
object_1 = 5.0
object_2 = 5.0


m = ((fx+fy)/2)/focal_length
object_img_sensor_1 = (native_res/m)*lower_res
object_img_sensor_2 = (native_res/m)*lower_res

distance_to_1 = ((object_1*focal_length)/object_img_sensor_1)**2
distance_to_2 = ((object_1*focal_length)/object_img_sensor_2)**2

distance = (distance_to_1-distance_to_2) ** .5
