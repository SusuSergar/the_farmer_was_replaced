clear()
while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			buy_use(Items.Egg)
			move(North)
		move(East)
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			harvest()	
			move(North)
		move(East)
