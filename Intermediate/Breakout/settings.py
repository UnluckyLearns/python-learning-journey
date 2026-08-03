from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ASSETS = BASE_DIR / "assets"
PADDLE_PATH = ASSETS/ "Paddle.png"
BACKGROUND_PATH = ASSETS /"Background"/"breakout_bg2.png"
BALL_PATH = ASSETS / "balls2.png"
HEART_PATH = ASSETS/"red_heart.png"
QUIT_PATH = ASSETS/"Quit.png"
OVER_PATH = ASSETS/"GameOver.png"
RETRY_PATH = ASSETS/"Retry.png"
FONT_PATH = ASSETS/"font"/"pixeloid_sans"/"PixeloidSans.ttf"
BLOCK1_PATH = ASSETS /  "1HP.png"
BLOCK2_PATH = ASSETS /  "2HP.png"


PLAYER_ACC = 0.5
BALL_ACC = 1
PLAYER_FRICTION = -0.05
PADDLE_HALF_WIDTH = 36
PADDLE_THIRD_WIDTH = 24
PLAYER_HP =3


EDGE_MAX = 790
EDGE_MIN = 3


BLOCK_PER_LEVEL = 15
LEVEL_STARTING_X = 175
LEVEL_STARTING_Y = 200



HEIGHT = 800
WIDTH = 800