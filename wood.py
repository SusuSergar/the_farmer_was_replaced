clear()
world_size = get_world_size()
while True:
	for col in range(world_size):
		for row in range(world_size):
			if can_harvest():
				harvest()
			if (col + row) % 2 != 0:
				plant(Entities.Tree)
			else:
				plant(Entities.Bush)
			move(North)
		move(East)
