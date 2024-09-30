clear()
while True:
	for i in range(get_world_size()):
		move(East)
		for i in range(get_world_size()):
			harvest()
			move(North)
