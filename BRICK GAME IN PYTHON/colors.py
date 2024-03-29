class Colors:
	dark_grey = (170, 176, 188)
	dark_green = "#013220"
	green = (47, 230, 23)
	red = (232, 18, 18)
	orange = (226, 116, 17)
	yellow = (237, 234, 4)
	purple = (166, 0, 247)
	cyan = (21, 204, 209)
	blue = (13, 64, 216)
	white = (255, 255, 255)
	dark_blue = (44, 44, 127)
	light_blue = (59, 85, 162)
	light_orange = (250, 134, 2)

	@classmethod
	def get_cell_colors(cls):
		return [cls.dark_green, cls.green, cls.red, cls.dark_grey, cls.yellow, cls.purple, cls.cyan, cls.blue]
