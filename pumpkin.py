clear()
worldSize = get_world_size()
while True:
	for col in range(worldSize):
		for row in range (worldSize):
			if can_harvest():
				harvest()
			if (col + row) % 2 != 0 and col <= 2:
				plant(Entities.Tree)
			elif col > 0 and col <= 2:
				plantItem(Entities.Carrots, Items.Carrot_Seed, True)
			elif col > 2:
				plantItem(Entities.Pumpkin, Items.Pumpkin_Seed, True)
				
			move(North)
		move(East)
				
