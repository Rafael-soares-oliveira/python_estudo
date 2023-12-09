from pathlib import Path
import qdarktheme

ROOT_DIR = Path(__file__).parent
FILES_DIR = ROOT_DIR / 'files'
WINDOW_ICON_PATH = FILES_DIR / 'icon.png'

# Sizing
BIG_FONT_SIZE = 32
MEDIUM_FONT_SIZE = 16
SMALL_FONT_SIZE = 14
TEXT_MARGIN = 10
MINIMUM_WIDTH = 500

# Colors
LIGHT_PRIMARY_COLOR = "#67c0eb"
PRIMARY_COLOR = "#1e81b0"
DARK_PRIMARY_COLOR = "#16658a"
DARKEST_PRIMARY_COLOR = "#115270"

# Theme button
qss = f"""
    PushButton[cssClass="specialButton"],
    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
    }}
    PushButton[cssClass="specialButton"]:hover,
        QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARK_PRIMARY_COLOR};
    }}
    PushButton[cssClass="specialButton"]:pressed,
        QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""

# Theme


def setupTheme():
    qdarktheme.setup_theme(
        theme='dark',
        corner_shape='rounded',
        custom_colors={
            "[dark]": {
                "primary": f"{PRIMARY_COLOR}",
            },
            "[light]": {
                "primary": f"{PRIMARY_COLOR}"
            }
        },
        additional_qss=qss
    )
