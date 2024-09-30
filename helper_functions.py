def plantItem(item_type, item_seed, tiled):
	if num_items(item_seed) == 0:
		trade(item_seed)
	if  tiled and get_ground_type() != Grounds.Soil:
		till()
	plant(item_type)
		
def plant_all_tiles(item_type, item_seed, tiled):
	clear()
	world_size = get_world_size()
	for cool in range(world_size):
			for row in range (world_size):
				plantItem(item_type, item_seed, tiled)
				move(North)
			move(East)
			
def go_to(x_pos, y_pos):
	go_home()
	for x in range(x_pos):
		move(East)
	for y in range(y_pos):
		move(North)

def buy_use(item_type):
	trade(item_type)
	use_item(item_type)
	
def replant_fertelyze(item_type, item_seed, tiled, max_num1):
	harvest()
	plantItem(item_type, item_seed, tiled)
	if measure() >= max_num1:
		buy_use(Items.Fertilizer)

def go_home():
	while True:
		if get_pos_x() == 0: # starting to count at the 0th position 
			break
		move(East)
	while True:
		if get_pos_y() == 0: # starting to count at the 0th position 
			break
		move(South)
def plant_harvest_til_zero_v1():
	 
	plantItem(Entities.Sunflower, Items.Sunflower_Seed, True)
	while True:
		if get_entity_type() == Entities.Sunflower and measure() == 7:
			break
		
		if can_harvest():
			harvest()
			plantItem(Entities.Sunflower, Items.Sunflower_Seed, True)
		else:
			buy_use(Items.Fertilizer)
def harvest_sunflowers():
	clear()
	for row in range(get_world_size()):
		for col in range(get_world_size()):
			plant_harvest_til_zero_v1()
			move(North)
		move(East)
	while True:
		if can_harvest():
			harvest()
			plantItem(Entities.Sunflower, Items.Sunflower_Seed, True)
		else:
			buy_use(Items.Fertilizer)
def plant_col():
	for i in range(get_world_size()):
		plantItem(Entities.Cactus, Items.Cactus_Seed, True)
		move(East)
def sort_col():
	for coll in range(get_world_size() * (get_world_size() - 1)):
		if measure() > measure(East):
			swap(East)
		
		move(East)
def sort_row():
	for roww in range(get_world_size() * (get_world_size() - 1)):
		if measure() > measure(North):
			swap(North)
		
		move(North)
		
