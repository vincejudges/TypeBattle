from enum import Enum

class Game_status(Enum):
	NOT_START = 0
	READY = 1
	RUNNING = 2
	END = 3
	SOMEONE_WIN = 4