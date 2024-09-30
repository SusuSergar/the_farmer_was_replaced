while True:
	
	plant_all_tiles(Entities.Cactus, Items.Cactus_Seed, True)
	for col in range(get_world_size()):
		sort_col()
		move(North)
	for col in range(get_world_size()):
		sort_row()
		move(East)#
	go_home()
	harvest()
