linh_file = open("linh_fav_foods.txt")
linh_favs = linh_file.readlines()
linh_file.close()

with open("daniel_fav_foods.txt") as daniel_file:
	daniel_favs = daniel_file.readlines()


def compare_favs(linh_favs, daniel_favs):
	if linh_favs[0] == daniel_favs[0]:
		return "Our favorite foods are the same!"
	else:
		return "Ours favorite foods are different"
print compare_favs(linh_favs, daniel_favs)